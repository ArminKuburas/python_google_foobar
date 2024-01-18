def solution(src, dest):
    # Convert source and destination to (row, column) coordinates
    src_row, src_col = divmod(src, 8)
    dest_row, dest_col = divmod(dest, 8)

    # Possible knight moves
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]

    # Initialize the queue with the source square and its distance
    queue = [(src_row, src_col, 0)]

    # Set to keep track of visited squares
    visited = set()

    while queue:
        current_row, current_col, distance = queue.pop(0)

        # Check if the destination is reached
        if (current_row, current_col) == (dest_row, dest_col):
            return distance

        # Explore possible moves
        for move in moves:
            new_row = current_row + move[0]
            new_col = current_col + move[1]

            # Check if the new move is within the chessboard
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                new_square = (new_row, new_col)

                # Check if the square has not been visited
                if new_square not in visited:
                    visited.add(new_square)
                    queue.append((new_row, new_col, distance + 1))

    # If no valid path is found (should not happen with a valid chessboard)
    return -1

# Example usage:
src_square = 0
dest_square = 63
result = solution(src_square, dest_square)
print(result)