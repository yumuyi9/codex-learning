import emoji


def main():
    text = input("Input: ")
    # alias 模式同时识别标准代码和别名。
    print("Output:", emoji.emojize(text, language="alias"))


if __name__ == "__main__":
    main()
