def main ():#line:1:def main():
    try :#line:2:try:
        OOO00O0OO0OOOO0OO =int (input ("Enter a year: "))#line:3:year = int(input("Enter a year: "))
        if (OOO00O0OO0OOOO0OO %4 ==0 and OOO00O0OO0OOOO0OO %100 !=0 )or (OOO00O0OO0OOOO0OO %400 ==0 ):#line:4:if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print (f"{OOO00O0OO0OOOO0OO} is a leap year.")#line:5:print(f"{year} is a leap year.")
        else :#line:6:else:
            print (f"{OOO00O0OO0OOOO0OO} is not a leap year.")#line:7:print(f"{year} is not a leap year.")
    except ValueError :#line:9:except ValueError:
        print ("Invalid input! Please enter a string.")#line:10:print("Invalid input! Please enter a string.")
if __name__ =="__main__":#line:12:if __name__ == "__main__":
    main ()
