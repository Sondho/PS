from run_test import run_test
from solution import solution


def main():
    test_case = [
        # numbers	hand	result
        [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right", "LRLLLRLLRRL"],
        [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left", "LRLLRRLLLRR"],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right", "LLRLLRLLRL"],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
