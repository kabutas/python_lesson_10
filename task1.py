def all_equal(sum_list):
    return all(x == sum_list[0] for x in sum_list)


def puzzle_pieces(a: list[int], b: list[int]) -> bool:
    if len(a) == len(b):
        sum_list = [x + y for x, y in zip(a, b)]
        # print(sum_list)
        return all_equal(sum_list)
    else:
        return False


print(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]),
      puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]),
      puzzle_pieces([1, 2], [-1, -1]),
      puzzle_pieces([9, 8, 7], [7, 8, 9, 10]))
