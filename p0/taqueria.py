total=0
MENU={"Baja Taco":4.25,
       "Burrito":7.50,
       "Bowl":8.50,
       "Nachos":11.00,
       "Quesadilla":8.50,
       "Super Burrito":8.50,
       "Super Quesadilla":9.50,
       "Taco":3.00,
       "Tortilla Salad":8.00,}
while True:
    try:
        order=input("输入一个菜名").strip().title()
        if order in MENU:
            total=total+MENU[order]
        else:
            continue
    except EOFError:
        break
    else:
        print(f"Total: ${total:.2f}")       


