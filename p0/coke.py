total=0
while total<50:
    coin=int(input("投入硬币"))
    if coin in (25,10,5):
        total=total+coin
    if total<50:
        print(f"Amount Due: {50-total}")

print(f"Change Owed: {total-50}")    
 