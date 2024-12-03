def main ():#line:1:def main():
    try :#line:2:try:
        if n ==0 or n ==1 :#line:3:if n == 0 or n == 1:
            return 1 #line:4:return 1
        else :#line:5:else:
            return n *factorial (n -1 )#line:6:return n * factorial(n - 1)
        O000O0OO00OOOO0OO =int (input ("Enter a number: "))#line:7:num = int(input("Enter a number: "))
        print (f"The factorial of {O000O0OO00OOOO0OO} is {factorial(O000O0OO00OOOO0OO)}")#line:8:print(f"The factorial of {num} is {factorial(num)}")
    except ValueError :#line:10:except ValueError:
        print ("Invalid input! Please enter numeric values.")#line:11:print("Invalid input! Please enter numeric values.")
if __name__ =="__main__":#line:13:if __name__ == "__main__":
    main ()
