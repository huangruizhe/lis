#include <iostream>
#include "lis.h"

int main() {
    // Test input array
    // int X[] = {3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10};
    // int X[] = {10, 9, 2, 5, 3, 7, 101, 18, 102};
    int X[] = {10, 9, 2, 5, 3, 7, 18, 101, 102};
    int N = sizeof(X) / sizeof(X[0]);

    // Call the longestIncreasingSubsequence function
    int L;
    int* result = longestIncreasingSubsequence(X, N, L);

    // Print the result
    std::cout << "Longest increasing subsequence (S): ";
    for (int i = 0; i < L; ++i) {
        std::cout << result[i] << " ";
    }
    std::cout << std::endl;

    // Free the memory allocated for the result array
    delete[] result;

    return 0;
}

// g++ -o test test.cpp lis.cpp -std=c++11
// ./test