def main ():#line:1
    try :#line:3
        O0OOO000OO000O00O =float (input ("Enter value in kilometers: "))#line:5
        O00OO000OO00000OO =0.621371 #line:8
        O00O0O0OO0O000O00 =O0OOO000OO000O00O *O00OO000OO00000OO #line:11
        print ('%0.2f kilometers is equal to %0.2f miles'%(O0OOO000OO000O00O ,O00O0O0OO0O000O00 ))#line:14
    except ValueError :#line:16
        print ("Invalid input! Please enter numeric values.")#line:17
if __name__ =="__main__":#line:19
    main ()
