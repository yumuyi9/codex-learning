import random
import sys

from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    # argv 的第一个元素是文件名，切片后才是用户提供的参数。
    arguments = sys.argv[1:]

    if not arguments:
        font = random.choice(fonts)
    elif len(arguments) == 2 and arguments[0] in ("-f", "--font"):
        font = arguments[1]
        if font not in fonts:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    figlet.setFont(font=font)
    text = input("Input: ")
    print("Output:")
    # renderText 已经在末尾换行，end="" 避免多打印一行。
    print(figlet.renderText(text), end="")


if __name__ == "__main__":
    main()
