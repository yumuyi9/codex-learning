def length(s):
    return 2<=len(s)<=6
def starts_with_letters(s):
    return s[0:2].isalpha()
def only(s):
    return s.isalnum()
def first_digit_not_zero(s):
    for c in s:
        if c.isdigit():
            return c!="0"
    return True 
def digits_at_end(s):
    seen_digit=False
    for c in s:
        if c.isdigit():
            seen_digit=True
        elif seen_digit:
            return False
    return True 
def main():
    plate = input("Plate: ")
    if length(plate) and starts_with_letters(plate) and only(plate) and first_digit_not_zero(plate) and digits_at_end(plate): 
                                                                            
        print("Valid")
    else:
        print("Invalid")    

main()