def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
        except (ValueError, ZeroDivisionError):
            # convert 报告错误，交互层决定重新询问。
            continue
        print(gauge(percentage))
        break


def convert(fraction):
    numerator, denominator = fraction.split("/")
    numerator = int(numerator)
    denominator = int(denominator)

    # 检查零分母时要早于大小比较，例如 1/0 应抛出 ZeroDivisionError。
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if numerator < 0 or denominator < 0 or numerator > denominator:
        raise ValueError("Expected 0 <= numerator <= denominator")

    return round(numerator / denominator * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()
