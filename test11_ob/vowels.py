def main ():#line:1:def main():
    try :#line:2:try:
        O00O0000O0000OO00 =input ("Enter a string: ").lower ()#line:3:text = input("Enter a string: ").lower()
        OOO00000OOO0000OO ="aeiou"#line:4:vowels = "aeiou"
        O0O00OO000O00O0O0 =sum (1 for O000O0O00OO0O0O0O in O00O0000O0000OO00 if O000O0O00OO0O0O0O in OOO00000OOO0000OO )#line:5:count = sum(1 for char in text if char in vowels)
        print ("Number of vowels:",O0O00OO000O00O0O0 )#line:6:print("Number of vowels:", count)
    except ValueError :#line:8:except ValueError:
        print ("Invalid input! Please enter a string.")#line:9:print("Invalid input! Please enter a string.")
if __name__ =="__main__":#line:11:if __name__ == "__main__":
    main ()
