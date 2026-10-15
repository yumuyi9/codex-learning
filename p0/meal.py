def main():
    time=input("输入一个时间: ")
    if 7<= convert(time) <= 8:
        print("breakfast time")
    elif 12<= convert(time) <= 13:
        print("lunch time")
    elif 18<= convert(time) <= 19:
        print("dinner time")
    

def convert(time):
    x,y=time.split(":")
    x = int(x)
    y = int(y)/60
    return x+y
if __name__ == "__main__":
    main()