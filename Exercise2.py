def count_islands(matrix):
    count = 0
    visited = set()

    def visit_island(row, col):
        visited.add((row, col))
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == 1 and (r, c) not in visited:
                visit_island(r, c)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1 and (row, col) not in visited:
                visit_island(row, col)
                count += 1
    return count