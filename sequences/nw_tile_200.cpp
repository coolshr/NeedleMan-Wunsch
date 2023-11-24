#include <bits/stdc++.h>
#include "align.h"
using namespace std;

int main(int argc, char *argv[])
{
    string A, B;

    // take input of both sequences
    string file = argv[1];
    file += ".txt";
    ifstream inputFile(file);
    if (inputFile.is_open())
    {
        getline(inputFile, A);
        getline(inputFile, B);
        inputFile.close();
    }
    else
    {
        cout << "Unable to open file\n";
        return 0;
    }
    // cout << A << "\n" << B << "\n";
    Needleman_Wunsch_optimise_tile(A, B, A.size(), B.size(), 2, -1, -1, 200);
    return 0;
}