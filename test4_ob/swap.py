def main ():#line:1
    try :#line:3
        OOO0OOOO0OO0O0OO0 =input ('Enter value of x: ')#line:4
        O00O00O00OO000OOO =input ('Enter value of y: ')#line:5
        O00O0O00OOOO00O00 =OOO0OOOO0OO0O0OO0 #line:8
        OOO0OOOO0OO0O0OO0 =O00O00O00OO000OOO #line:9
        O00O00O00OO000OOO =O00O0O00OOOO00O00 #line:10
        print ('The value of x after swapping: {}'.format (OOO0OOOO0OO0O0OO0 ))#line:13
        print ('The value of y after swapping: {}'.format (O00O00O00OO000OOO ))#line:14
    except ValueError :#line:16
        print ("Invalid input! Please enter numeric values.")#line:17
if __name__ =="__main__":#line:19
    main ()
