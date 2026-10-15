answer=input("输入一句问候语: ").lower().strip()
if answer.startswith("hello"):
    print("$0")
elif answer.startswith("h"):
    print("$20")
else:
    print("$100")
