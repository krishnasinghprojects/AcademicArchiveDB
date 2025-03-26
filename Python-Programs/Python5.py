def read_matrix(name):
    # Read matrix dimensions
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    
    print(f"Enter the elements of {name} row-wise (separate numbers with space):")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        # Ensure the row has the correct number of elements
        while len(row) != cols:
            print(f"Error: Expected {cols} numbers. Please re-enter row {i + 1}:")
            row = list(map(int, input().split()))
        matrix.append(row)
    return matrix, rows, cols

def multiply_matrices(A, B):
    # Multiply matrices A and B
    m = len(A)         # rows in A
    n = len(B[0])      # columns in B
    common = len(A[0]) # should be same as number of rows in B
    result = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            for k in range(common):
                result[i][j] += A[i][k] * B[k][j]
    return result

def print_matrix(M):
    for row in M:
        print(" ".join(map(str, row)))

def main():
    # Read the two matrices
    matrix1, r1, c1 = read_matrix("Matrix 1")
    matrix2, r2, c2 = read_matrix("Matrix 2")

    # Check if multiplication is possible
    if c1 != r2:
        print("Matrix multiplication is not possible because the number of columns in Matrix 1"
              " does not equal the number of rows in Matrix 2.")
    else:
        result = multiply_matrices(matrix1, matrix2)
        print("Resultant Matrix:")
        print_matrix(result)


main()
