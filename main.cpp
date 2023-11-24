#include <bits/stdc++.h>
#include "align.h"
using namespace std;

int main(int argc, char *argv[])
{
    string A, B;

    // take input of both sequences
    string file = "10.txt";
    // file += string(argv[1]);
    // file += ".txt";
    // cout << file << "\n";
    // ifstream inputFile(file);
    // if (inputFile.is_open())
    // {
    //     cout<<"h";
    //     getline(inputFile, A);
    //     getline(inputFile, B);
    //     inputFile.close();
    // }
    // else
    // {
    //     cout << "Unable to open file\n";
    //     return 0;
    // }
    FILE *f = fopen("10.txt", "r");
    if (f == NULL)
    {
        cout << "Unable to open file\n";
        return 0;
    }
    fscanf(f, "%s", A.c_str());
    fscanf(f, "%s", B.c_str());
    cout << "here\n";
    // cout << A << "\n" << B << "\n";
    // Needleman_Wunsch_optimise(A, B, A.size(), B.size(), 2, -1, -1);
    Needleman_Wunsch_optimise_tile(A, B, A.size(), B.size(), 2, -1, -1,2);
    // Needleman_Wunsch_optimise_tile(A, B, A.size(), B.size(), 2, -1, -1, 100);
    // Needleman_Wunsch_optimise_tile(A, B, A.size(), B.size(), 2, -1, -1, 200);
    // Needleman_Wunsch_optimise_tile(A, B, A.size(), B.size(), 2, -1, -1, 500);
    // Needleman_Wunsch_optimise_tile(A, B, A.size(), B.size(), 2, -1, -1, 1000);
    // Needleman_Wunsch_optimise_tile(A, B, A.size(), B.size(), 2, -1, -1, 2000);
    // Needleman_Wunsch(A, B, A.size(), B.size(), 2, -1, -1);
    return 0;
}