#!/usr/bin/python

import sys


def add_plays(plays):
    possible_plays = ["rock", "paper", "scissors"]

    if len(plays) <= 1:
        return plays
    one_third = len(plays) // 3
    first = plays[:one_third]
    second = plays[one_third:one_third * 2]
    third = plays[one_third * 2:]
    for item in first:
        item.append(possible_plays[0])
    for item in second:
        item.append(possible_plays[1])
    for item in third:
        item.append(possible_plays[2])

    first = add_plays(first)
    second = add_plays(second)
    third = add_plays(third)

    return first + second + third


def rock_paper_scissors(n):
    return add_plays([[] for play in range(3**n)])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
