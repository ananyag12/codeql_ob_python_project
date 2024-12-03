def main ():#line:1:def main():
    try :#line:2:try:
        O0O0OO00O000OO00O =int (input ("Enter a number: "))#line:3:num = int(input("Enter a number: "))
        if O0O0OO00O000OO00O >1 :#line:4:if num > 1:
            for OOOO000O00OO00O00 in range (2 ,O0O0OO00O000OO00O ):#line:5:for i in range(2, num):
                if O0O0OO00O000OO00O %OOOO000O00OO00O00 ==0 :#line:6:if num % i == 0:
                    print (f"{O0O0OO00O000OO00O} is not a prime number.")#line:7:print(f"{num} is not a prime number.")
                    break #line:8:break
            else :#line:9:else:
                print (f"{O0O0OO00O000OO00O} is a prime number.")#line:10:print(f"{num} is a prime number.")
        else :#line:11:else:
            print (f"{O0O0OO00O000OO00O} is not a prime number.")#line:12:print(f"{num} is not a prime number.")
    except ValueError :#line:13:except ValueError:
        print ("Invalid input! Please enter numeric values.")#line:14:print("Invalid input! Please enter numeric values.")
if __name__ =="__main__":#line:16:if __name__ == "__main__":
    main ()
