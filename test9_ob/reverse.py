def main ():#line:1:def main():
    try :#line:2:try:
        O0O0O0OOOOOOOOO0O =input ("Enter a string: ")#line:3:text = input("Enter a string: ")
        OOO0O0000O0O000O0 =O0O0O0OOOOOOOOO0O [::-1 ]#line:4:reversed_text = text[::-1]
        print ("Reversed string:",OOO0O0000O0O000O0 )#line:5:print("Reversed string:", reversed_text)
    except ValueError :#line:7:except ValueError:
        print ("Invalid input! Please enter a string.")#line:8:print("Invalid input! Please enter a string.")
if __name__ =="__main__":#line:10:if __name__ == "__main__":
    main ()
