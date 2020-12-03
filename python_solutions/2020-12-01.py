#!/usr/bin/env python3
from typing import List  # For type annotation


def two_sum(nums: List, target: int) -> List:
    values = set(nums)  # Faster lookup
    for i in nums:
        complement = target - i
        if complement in values and complement != i:
            return [i, complement]
    raise RuntimeError('No two sum solution!')


def three_sum(nums: List, target: int) -> List:
    values = set(nums)  # Faster lookup
    for i in nums:
        for j in nums[1:]:
            complement = target - (i + j)
            if complement in values:
                return [complement, i, j]
    raise RuntimeError('No three sum solution!')


if __name__ == "__main__":
    # Part One
    with open(file='2020-12-01-input-puzzle.txt', mode='r') as f:
        nums = f.read().split()
        nums = [int(i) for i in nums]
    pair = two_sum(nums=nums, target=2020)
    product = pair[0] * pair[1]
    print(f'Numbers whose sum is 2020: {pair}')
    print(f'Product of those numbers: {product}')
    # Part Two
    triplet = three_sum(nums=nums, target=2020)
    product = triplet[0] * triplet[1] * triplet[2]
    print(f'Numbers whose sum is 2020: {triplet}')
    print(f'Product of those numbers: {product}')
