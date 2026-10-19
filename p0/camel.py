name=input("输入一个驼峰命名的变量名: ")
for i in name:
    if i.isupper():
        name=name.replace(i,"_"+i.lower())
print(name)
    

