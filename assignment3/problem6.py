import MapReduce
import sys

"""
Problem 6
Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value.
 Design a MapReduce algorithm to compute the matrix multiplication A x B

Map Input
The input to the map function will be a row of a matrix represented as a list. Each list will be of the form
 [matrix, i, j, value] where matrix is a string and i, j, and value are integers.

The first item, matrix, is a string that identifies which matrix the record originates from. This field has two possible
 values: "a" indicates that the record is from matrix A and "b" indicates that the record is from matrix B

Reduce Output
The output from the reduce function will also be a row of the result matrix represented as a tuple. Each tuple
 will be of the form (i, j, value) where each element is an integer.

You can test your solution to this problem using matrix.json: $ python multiply.py matrix.json

You can verify your solution by comparing your result with the file multiply.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # matrix name, i coordinate (row), j coordinate(column), value. [string, int, int, int]
    # two matrices a, b. Input matrices [i, j] are 5x5
    matrix_length = 5
    matrix_name = record[0]
    row = record[1]
    column = record[2]
    value = record[3]

    if matrix_name == "a":
        for num in range(0, matrix_length):
            mr.emit_intermediate((row, num),[column, value])
    else:
        for num in range(0,matrix_length):
            mr.emit_intermediate((num, column), [row, value])

def reducer(key, value):
    # key is a tuple containing output matrix coordinates (represents a single cell in the output matrix)
    # value is a list
    matrix_length = 5
    total = 0

    for num in range(0, matrix_length):
        values = filter(lambda i: i[0] == num, value)
        if len(values) <= 1:
            i_val = 0
        else:
            i_val = reduce(lambda x, y: x[1] * y[1], values)
        total = total + i_val

    mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)