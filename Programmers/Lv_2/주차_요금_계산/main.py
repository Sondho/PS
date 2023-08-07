from run_test import run_test
from solution import solution


def main():
    test_case = [
        # fees	records	result
        [[180, 5000, 10, 600],
         ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
          "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"], [14600, 34400, 5000]],
        [[120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"],
         [0, 591]],
        [[1, 461, 1, 10], ["00:00 1234 IN"], [14841]],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
