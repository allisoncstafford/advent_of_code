# import necessary packages
from day2_pt1 import get_input, intcode


def main():
    input = get_input('day2_input.txt')
    for noun in range(0, 100):
        for verb in range(0, 100):
            test_input = input.copy()
            test_input[1] = noun
            test_input[2] = verb
            result = intcode(test_input)
            if result[0] == 19690720:
                print(f"noun: {noun}\nverb: {verb}\n100n + v: {100*noun+verb}")


if __name__ == "__main__":
    main()