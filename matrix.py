# Author: Timothy Lu
# 8/29/2017
# 
# Run this to find the lowest determinant of paired rows in matrices

import sys
import numpy as np
from random import randint
import minimum

# reads in a .txt file as a numpy matrix
def read_matrix_file(filename):
    matrix = []
    # print("reading...")

    try:
        with open(filename) as file:
            for i, line in enumerate(file):
                temp = []
                temp = line.split()
                temp = [int(i) for i in temp]
                #print(temp)
                matrix.append(temp[:])
                temp[:] = []
        return_mat = np.matrix(np.array(matrix))
        # print(return_mat)
        # print("# of rows: " + str(return_mat.shape[0]))
        # print()
        return return_mat
    except:
    	print("ERROR: could not find " + filename)
    	sys.exit

# Returns a matrix with "num" number of rows picked randomly from "matrix"
def rand_rows(num, matrix):
    # print("randomizing to " + str(num)+ " rows...")
    idx = []
    rows = set()
    for i in range(0, num):
        current = randint(0, matrix.shape[0] - 1)
        while(current in rows):
            current = randint(0, matrix.shape[0] - 1)
        rows.add(current)
        idx.append(i)

    temp = []
    for row in rows:
        temp.append(matrix[row])
    return_mat = np.matrix(np.array(temp))
    # print (return_mat)
    # print("# of rows: " + str(return_mat.shape[0]))
    # print()
    return idx, return_mat

# Generates a paired matrix (adds every row in "matrix" with every other row)
def generate_paired_matrix(idx, matrix):
    #print("generating paired matrix...")
    temp = []
    idx_return = []
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[0]):
            if not np.array_equal(matrix[i], matrix[j]):
                #print("summing: " + str(matrix[i]) + str(matrix[j]) + "...")
                temp.append(np.sum([matrix[i], matrix[j]], 0))
                idx_return.append([idx[i], idx[j]])
            else:
                #print("row " + str(i) + " and row " + str(j) + " are equal." + str(matrix[i]) + str(matrix[j])) 
                pass
    return_mat = np.matrix(np.array(temp))
    #print(return_mat)
    #print("# of rows: " + str(return_mat.shape[0]))
    #print()
    return idx_return, return_mat

def min_determinant():
    inp = read_matrix_file("input.txt")
    idx, rand = rand_rows(128, inp)
    idx, mat = generate_paired_matrix(idx, rand)
    min_idx, min_mat = minimum.min_row(idx, mat)
    return min_idx, min_mat.sum()

def main():
    iterations = int(input("How many iterations? "))
    min_sum = -1
    min_idx = [-1,-1]
    for i in range(0, iterations):
        cur_idx, cur_sum = min_determinant()
        if min_sum < 0:
            min_sum = cur_sum
            min_idx = cur_idx
        else:
            if min_sum > cur_sum:
                min_sum = cur_sum
                min_idx = cur_idx
    print("minimum at " + str(min_sum))
    print(min_idx)

if __name__ == "__main__":
    main()