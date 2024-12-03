def main ():#line:1:def main():
    try :#line:2:try:
        OO0O00O0OO0OO0OO0 =float (input ("Enter temperature in Celsius: "))#line:3:celsius = float(input("Enter temperature in Celsius: "))
        O0OO00OOO0OOO0OO0 =(OO0O00O0OO0OO0OO0 *9 /5 )+32 #line:4:fahrenheit = (celsius * 9/5) + 32
        print (f"Temperature in Fahrenheit: {O0OO00OOO0OOO0OO0}")#line:5:print(f"Temperature in Fahrenheit: {fahrenheit}")
    except ValueError :#line:7:except ValueError:
        print ("Invalid input! Please enter a string.")#line:8:print("Invalid input! Please enter a string.")
if __name__ =="__main__":#line:10:if __name__ == "__main__":
    main ()
