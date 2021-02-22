"""Fizz buzz."""
import argparse


def fizz_buzz(start_num, end_num):
    """Print to stdout Fizz/Buzz/FizzBuzz or none based on loop number.

    === Args ===
    start_num: Start number of loop.
    end_num: End number of loop.

    Example)
        If start_num=3, end_num=5, loop for 3, 4, 5, 6, 7.

    === Returns ===
    None
    """
    print_width = len(str(end_num))
    format_type = "0{}".format(print_width)

    for i in range(start_num, end_num + 1):
        fizzbuzz_str = gen_fizzbuzz_str(i)

        # Print index and fizzbuzz str.
        # Ex)
        # 03 Fizz
        # 04
        # 05 Buzz
        # ...
        # 15 FizzBuz
        print(
            "{idx:{format_type}} {fizzbuzz_str}"
            .format(
                idx=i,
                format_type=format_type,
                fizzbuzz_str=fizzbuzz_str,
            )
        )


def gen_fizzbuzz_str(num):
    """Generate Fizz/Buzz/FizzBuzz or empty string for given number."""
    key = 5 * (num % 5 == 0) + 3 * (num % 3 == 0)
    fiz_buz_str_map = {
        0: "",
        3: "Fizz",
        5: "Buzz",
        8: "FizzBuzz",
    }

    return fiz_buz_str_map[key]


def main():
    """Execute fizzbuzz with given command line arguments."""
    parser = argparse.ArgumentParser(description='Enjoy FizzBuzz!')

    parser.add_argument(
        'start_num', type=int, help='Start number for FizzBuzz loop.'
    )
    parser.add_argument(
        'end_num', type=int, help='End number for FizzBuzz loop.'
    )

    args = parser.parse_args()
    start_num = args.start_num
    end_num = args.end_num

    fizz_buzz(start_num, end_num)


if __name__ == '__main__':
    main()
