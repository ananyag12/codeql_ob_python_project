def main ():#line:1:def main():
    try :#line:2:try:
        OO000O0O0OOO0OO0O =int (input ("Enter a number: "))#line:3:num = int(input("Enter a number: "))
        if OO000O0O0OOO0OO0O %2 ==0 :#line:4:if num % 2 == 0:
            print (f"{OO000O0O0OOO0OO0O} is even.")#line:5:print(f"{num} is even.")
        else :#line:6:else:
            print (f"{OO000O0O0OOO0OO0O} is odd.")#line:7:print(f"{num} is odd.")
    except ValueError :#line:9:except ValueError:
        print ("Invalid input! Please enter numeric values.")#line:10:print("Invalid input! Please enter numeric values.")
if __name__ =="__main__":#line:12:if __name__ == "__main__":
    main ()
