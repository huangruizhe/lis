#include "lis.h"
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

int* longestIncreasingSubsequence(int* X, int N) {
    // Allocate memory for P array
    int* P = new int[N];

    // Allocate memory for M array
    int* M = new int[N + 1];
    M[0] = -1; // Undefined, can be any value

    int L = 0;
    for (int i = 0; i < N; ++i) {
        int lo = 1;
        int hi = L + 1;
        while (lo < hi) {
            int mid = lo + std::floor((hi - lo) / 2);
            if (X[M[mid]] >= X[i])
                hi = mid;
            else
                lo = mid + 1;
        }

        int newL = lo;
        P[i] = M[newL - 1];
        M[newL] = i;

        if (newL > L)
            L = newL;
    }

    // Reconstruct the longest increasing subsequence
    int* S = new int[L];
    int k = M[L];
    for (int j = L - 1; j >= 0; --j) {
        S[j] = X[k];
        k = P[k];
    }

    // Free memory allocated for P and M arrays
    delete[] P;
    delete[] M;

    // Return the longest increasing subsequence
    return S;
}