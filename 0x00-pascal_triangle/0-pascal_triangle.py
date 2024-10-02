#!/usr/bin/python3
"""
0x00. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the
    Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Each number is the sum of the two numbers directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
