answer=(input("什么是生命、宇宙以及一切终极问题的答案"))
answer = answer.lower().strip()
if answer == "42":
    print("Yes") 
elif answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")