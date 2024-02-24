# A python library for finding Longest Increasing Subsequence (LIS) in an integer array

This repository implements the efficient $O(NlogN)$ algorithm to find the "longest increasing subsequence" as outlined [here](https://en.wikipedia.org/wiki/Longest_increasing_subsequence) in the Wikepedia.

## Installation

To install it, run:
```
git clone https://github.com/huangruizhe/lis.git
cd lis
python setup.py install --record files.txt
```

If you want to remove the installed package, you can run:
```
cat files.txt | xargs sudo rm -rf
```

## Usage

```
import lis

def test_lis():
    X = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]

    result = lis.longestIncreasingSubsequence(X)
    print(f"X:      {X}")
    print(f"result: {result}")

    // X:     [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]
    //result: [-1, 2, 3, 7, 9, 10]

if __name__ == "__main__":
    test_lis()
```