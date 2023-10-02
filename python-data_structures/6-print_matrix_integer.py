#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for index0 in range(len(matrix)):
        for index1 in range(len(matrix[index0])):
            print("{:d}".format(matrix[index0][index1]), end="")
            if index1 != (len(matrix[index0]) - 1):
                print(" ", end="")
        print("")
