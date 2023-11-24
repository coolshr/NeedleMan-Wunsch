#include <stdlib.h>
#include <sys/time.h>
#include <stdlib.h>
#include <omp.h>
#include "align.h"
using namespace std;

void Needleman_Wunsch_Helper(std::string A, std::string B, size_t sizea, size_t sizeb,
                             int match, int mismatch, int gap, int lda, int DP_Matrix[],
                             int startrow, int startcol, int tileSize)
{
    // algorithm
    for (int i = startrow; i < startrow + tileSize; i++)
    {
        for (int j = startcol; j < startcol + tileSize; j++)
        {
            char nuc_a = A[j - 1];
            char nuc_b = B[i - 1];

            int diag_score;
            diag_score = (nuc_a == nuc_b) ? DP_Matrix[(i - 1) * lda + j - 1] + match : DP_Matrix[(i - 1) * lda + j - 1] + mismatch;

            pair<int, int> temp = max_score(DP_Matrix[i * lda + j - 1] + gap, diag_score, DP_Matrix[(i - 1) * lda + j] + gap);
            DP_Matrix[i * lda + j] = temp.first;
        }
    }
    return;
}

void Needleman_Wunsch_optimise_tile(std::string A, std::string B, size_t sizea, size_t sizeb,
                                    int match, int mismatch, int gap, int tile_size)
{
    int *DP_Matrix = new int[(sizeb + 1) * (sizea + 1)];
    int *TB_Matrix = new int[(sizeb + 1) * (sizea + 1)];
    size_t sum = 0;
    struct timeval t;
    tick(&t);
#pragma omp parallel for simd
    for (size_t j = 0; j <= sizea; j++)
    {
        DP_Matrix[j] = j * gap;
        TB_Matrix[j] = 2;
    }

#pragma omp parallel for simd
    for (size_t i = 0; i <= sizeb; i++)
    {
        DP_Matrix[i * (sizea + 1)] = i * gap;
        TB_Matrix[i * (sizea + 1)] = 1;
    }

    // int tile_size = 3;
    int num_tiles = (sizeb) * (sizea) / tile_size;

    for (sum = 2; sum <= (sizeb + 2) - tile_size; sum += tile_size)
    {
        #pragma omp parallel for simd
        for (int i = 1, j = sum - i; j >= 1; i += tile_size, j -= tile_size)
        {
            // cout << sum << " " << i << " " << j << "\n";
            Needleman_Wunsch_Helper(A, B, sizea, sizeb, match, mismatch, gap, sizea + 1, DP_Matrix, i, j, tile_size);
        }
    }
    for (sum = sizea + 2; sum <= 2 * sizea + 2 - 2 * tile_size; sum += tile_size)
    {
        #pragma omp parallel for simd
        for (int j = sizea - tile_size + 1, i = sum - j; i <= sizea - tile_size + 1; i += tile_size, j -= tile_size)
        {
            // cout << sum << " " << i << " " << j << "\n";
            Needleman_Wunsch_Helper(A, B, sizea, sizeb, match, mismatch, gap, sizea + 1, DP_Matrix, i, j, tile_size);
        }
    }

    // cout << DP_Matrix[(sizeb) * (sizea + 1) + sizea] << "\n";
    // double time = tock(&t);
    cout << time * 1000 << "\n";
    // cout << "DP MATRIX\n";
    // Print_Matrix(DP_Matrix, sizea, sizeb);
    // cout << "TB MATRIX\n";
    // Print_Matrix(TB_Matrix, sizea, sizeb);
    // cout << "\n\n";
    // Print_Alignment(TB_Matrix, A, B, sizea, sizeb);
    delete[] DP_Matrix;
    delete[] TB_Matrix;
}