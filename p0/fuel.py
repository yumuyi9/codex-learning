while True:
    try:
        a=(input("油箱剩余油量"))
        b,c=a.split("/")
        B=int(b)
        C=int(c)
        if B<0 or C<=0 or B>C:
            raise ValueError
    except ValueError:
        print("请重新输入")
    else:
        D=round(B/C*100)
        if D<=1:
            print("E")
        elif D >= 99:
            print("F")
        else:
            print(f"{D}%")
        break        


    

   

