counts={}
while True:
    try:
        item=input("输入要买的商品").upper()
        counts[item] = counts.get(item, 0) + 1
    except EOFError:
        break
for item in sorted(counts):    
    print(f"{counts[item]} {item}")

