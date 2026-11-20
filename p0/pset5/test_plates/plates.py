def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6 or not s[:2].isalpha() or not s.isalnum():
        return False

    seen_digit = False
    for character in s:
        if character.isdigit():
            # 只有首个数字不能是 0，例如 AB10 合法。
            if not seen_digit and character == "0":
                return False
            seen_digit = True
        elif seen_digit:
            # 数字部分开始后，不能再出现字母。
            return False

    return True


if __name__ == "__main__":
    main()
