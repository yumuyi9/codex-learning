import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        # 一题一题地生成，每题先生成 x，再生成 y。
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y

        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                # 非整数也消耗一次作答机会。
                print("EEE")
                continue

            if answer == correct:
                score += 1
                break
            print("EEE")
        else:
            # for 的 else 只在循环没有被 break 提前结束时执行。
            print(f"{x} + {y} = {correct}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level in (1, 2, 3):
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)
    raise ValueError("Level must be 1, 2, or 3")


if __name__ == "__main__":
    main()
