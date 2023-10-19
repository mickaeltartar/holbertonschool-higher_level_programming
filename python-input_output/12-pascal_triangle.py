#!/usr/bin/python3
""" returns a list of lists of int representing the Pascal’s triangle of n """


def pascal_triangle(n):
    """ function that returns a representing the Pascal's triangle
        Args : n: size of triangle
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]

            for j in range(1, i):
                previous_row = triangle[i - 1]
                new_value = previous_row[j - 1] + previous_row[j]
                row.append(new_value)

            row.append(1)
            triangle.append(row)

    return triangle
