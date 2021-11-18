#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#

from copy import deepcopy


def crosswordPuzzle(crossword, words):
    # Write your code here
    coords = {}
    for row, line in enumerate(crossword):
        for col, char in enumerate(line):
            if char == "-":
                coords[(row, col)] = None
    lines = identify_lines(crossword)
    words = words.split(";")
    words_used = {}
    for w in words:
        words_used[w] = False
    print(coords)
    print(lines)
    global result
    logic(0, words_used, coords, lines)
    print(result)
    answer = [["+" for _ in range(10)] for _ in range(10)]
    for row, col in result.keys():
        answer[row][col] = result[(row, col)]
    for row, line in enumerate(answer):
        crossword[row] = "".join(line)
    return crossword


def logic(line_num, words_used, coords, lines):
    if line_num == len(words_used):
        global result
        print(coords)
        result = deepcopy(coords)
        return
    else:
        for w in words_used.keys():
            if words_used[w] == True or len(w) != len(lines[line_num]):
                continue
            c, overlap = check(line_num, w, coords, lines)
            if c:
                cand_coords = lines[line_num]
                for i, coord in enumerate(cand_coords):
                    coords[coord] = w[i]
                words_used[w] = True
                logic(line_num + 1, words_used, coords, lines)
                for i, coord in enumerate(cand_coords):
                    if coord not in overlap:
                        coords[coord] = None
                words_used[w] = False


def check(line_num, word, coords, lines):
    cand_coords = lines[line_num]
    overlap = []
    for i, coord in enumerate(cand_coords):
        if coords[coord] != None:
            if coords[coord] != word[i]:
                return False, overlap
            else:
                overlap.append(coord)
    return True, overlap


def identify_lines(crossword):
    line_num = 0
    lines = {}
    for row in range(10):
        for col in range(9):
            if crossword[row][col] == "-" and crossword[row][col + 1] == "-":
                trow, tcol = row, col
                lines[line_num] = []
                while tcol < 10 and crossword[trow][tcol] == "-":
                    lines[line_num].append((trow, tcol))
                    tcol += 1
                line_num += 1
                break
    for col in range(10):
        for row in range(9):
            if crossword[row][col] == "-" and crossword[row + 1][col] == "-":
                trow, tcol = row, col
                lines[line_num] = []
                while trow < 10 and crossword[trow][tcol] == "-":
                    lines[line_num].append((trow, tcol))
                    trow += 1
                line_num += 1
                break
    return lines


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)
    print(result)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
