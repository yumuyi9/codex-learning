def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    result = ""
    for character in word:
        # 小写化只用于判断，保留下来的字符使用原来的大小写。
        if character.lower() not in "aeiou":
            result += character
    return result


# pytest 导入 shorten 时，跳过需要键盘输入的 main。
if __name__ == "__main__":
    main()
