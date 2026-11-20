import random


def main():
    level = read_positive_integer("Level: ")
    # 只生成一次，后续猜测都与同一个数字比较。
    target = random.randint(1, level)

    while True:
        guess = read_positive_integer("Guess: ")
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            return


def read_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            # 输入无法转成整数时，回到循环开头重新询问。
            continue
        if number > 0:
            return number


if __name__ == "__main__":
    main()
