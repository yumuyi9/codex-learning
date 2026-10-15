def convert (text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text
def main():
    text = input("请输入: ")
    print(convert(text))

main()



