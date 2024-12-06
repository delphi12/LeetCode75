def funcHopSkipJump(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Directions for anti-clockwise movement: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0
    visited = set()

    # Start at the top-left corner
    x, y = 0, 0
    visited.add((x, y))
    total_cells = rows * cols
    steps = 1  # Count the first step
    skip = False

    while len(visited) < total_cells:
        # Determine the next cell to move to
        next_x = x + directions[direction_index][0]
        next_y = y + directions[direction_index][1]

        if 0 <= next_x < rows and 0 <= next_y < cols and (next_x, next_y) not in visited:
            if not skip:
                x, y = next_x, next_y
                visited.add((x, y))
            skip = not skip  # Toggle skipping
        else:
            # Change direction anti-clockwise
            direction_index = (direction_index + 1) % 4

        # If all possible moves are either out of bounds or visited, break the loop
        if all(0 > x + directions[d][0] or x + directions[d][0] >= rows or
               0 > y + directions[d][1] or y + directions[d][1] >= cols or
               (x + directions[d][0], y + directions[d][1]) in visited for d in range(4)):
            break

    return matrix[x][y]

def main():
    matrix = []
    matrix_rows, matrix_cols = map(int, input().split())
    for idx in range(matrix_rows):
        matrix.append(list(map(int, input().split())))
    result = funcHopSkipJump(matrix)
    print(result)

if __name__ == "__main__":
    main()