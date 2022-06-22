#!/usr/bin/python3
import math
import sys


def is_prime(N):
    if N % 2 == 0:
        return False
    for i in range(3, round(math.sqrt(N)) + 1, 2):
        if N % i == 0:
            return False
    return True


def factor(N):

    if N % 2 == 0:
        print("{}={}*{}".format(N, N // 2, 2))
    else:
        for i in range(3, round(math.sqrt(N)) + 1, 2):
            if N % i == 0:
                print("{}={}*{}".format(N, N // i, i))
                break


with open(sys.argv[1]) as f:
    for line in f.readlines():
        factor(int(line))
