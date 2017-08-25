import sys
import numpy as np
from random import randint

def read_matrix_file(filename):
    matrix = []
    with open(filename) as file:
        for i, line in enumerate(file):
            temp = []
            temp = line.split()
            matrix.append(temp)
            temp[:] = []
    return np.matrix(np.array(matrix))

def rand_rows(num, matrix):
    rows = set()
    for i in range(0, num):
        current = randint(0, matrix.size)
        while(current in rows):
            current = randint(0, matrix.size)
        rows.add(current)

    temp = []
    for row in rows:
        temp.append(matrix[row])
    return np.matrix(np.array(temp))

def generate_paired_matrix(matrix):
    temp = []
    for row in matrix:
        for row1 in matrix:
            if row not in row1:
                temp.append(row + row1)
    return np.matrix(np.array(temp))

def main():
    generate_paired_matrix(rand_rows(read_matrix_file("input.txt")))
