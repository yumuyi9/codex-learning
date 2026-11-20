import inflect


def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            # CS50 终端按 Ctrl+D，Windows 终端通常按 Ctrl+Z 再回车。
            break

    # join 会根据姓名数量决定使用逗号还是 and。
    print("Adieu, adieu, to " + inflect.engine().join(names))


if __name__ == "__main__":
    main()
