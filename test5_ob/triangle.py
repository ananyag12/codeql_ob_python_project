def main ():#line:1
    try :#line:2
        OOO0OOOO0O0O000O0 =float (input ('Enter first side: '))#line:3
        OOO0OO0O0OOOO0OOO =float (input ('Enter second side: '))#line:4
        O0OO0OOO0OOOO0OO0 =float (input ('Enter third side: '))#line:5
        OO00OOO0O00O00O0O =(OOO0OOOO0O0O000O0 +OOO0OO0O0OOOO0OOO +O0OO0OOO0OOOO0OO0 )/2 #line:8
        O000OOOOO00O000O0 =(OO00OOO0O00O00O0O *(OO00OOO0O00O00O0O -OOO0OOOO0O0O000O0 )*(OO00OOO0O00O00O0O -OOO0OO0O0OOOO0OOO )*(OO00OOO0O00O00O0O -O0OO0OOO0OOOO0OO0 ))**0.5 #line:11
        print ('The area of the triangle is %0.2f'%O000OOOOO00O000O0 )#line:12
    except ValueError :#line:14
        print ("Invalid input! Please enter numeric values.")#line:15
if __name__ =="__main__":#line:17
    main ()
