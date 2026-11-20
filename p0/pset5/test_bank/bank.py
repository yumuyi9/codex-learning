def main():
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.lower()
    # hello 也以 h 开头，必须先判断更具体的条件。
    if greeting.startswith("hello"):
        return 0
    if greeting.startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()
