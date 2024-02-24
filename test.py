import lis

def test_lis():
    X = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]
    expected_result = [-1, 2, 3, 7, 9, 10]

    result = lis.longestIncreasingSubsequence(X)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"

    print("Test passed!")

if __name__ == "__main__":
    test_lis()