#!/usr/bin/env python3
# https://adventofcode.com/2020/day/2
from collections import Counter


def valid(line: str) -> bool:
    policy_password = line.split(':')
    password = policy_password[1].split()[0]
    policy = policy_password[0].split()
    min_max = policy[0].split('-')
    minimum, maximum = int(min_max[0]), int(min_max[1])
    char = policy[1]
    counter = Counter(password)
    if counter[char] >= minimum and counter[char] <= maximum:
        return True
    else:
        return False


def truly_valid(line: str) -> bool:
    policy_password = line.split(':')
    password = policy_password[1].split()[0]
    policy = policy_password[0].split()
    first_last = policy[0].split('-')
    first, last = int(first_last[0]) - 1, int(first_last[1]) - 1
    char = policy[1]
    if password[first] != password[last]:
        if char in set([password[first], password[last]]):
            return True
    else:
        return False


if __name__ == "__main__":
    try:
        with open(file='2020-12-02-puzzle-input.txt', mode='r') as f:
            passwords = f.readlines()
            print(len(passwords))
    except FileNotFoundError as e:
        exit(f'Could not find {e.filename}')
    # Part One
    count_valid = 0
    for p in passwords:
        if valid(p):
            count_valid += 1
    print(f'The number of valid passwords is: {count_valid}')
    # Part Two
    count_valid = 0
    for p in passwords:
        if truly_valid(p):
            count_valid += 1
    print(f'The number of truly valid passwords is: {count_valid}')
