name=input("输入一段文字:")
result=""
for i in name:
    if i.lower() not in ("aeiou"):
        result=result+i

print(result)

