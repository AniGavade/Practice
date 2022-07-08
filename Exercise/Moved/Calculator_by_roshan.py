print ("Hello,welcome\nchose the oprator that you want:-\n 1:-Addition\n2:-Substraction\n3:-Multiplication\n4:-Division")
a=int (input())
# for addition
if a in range (0,4+1)and a==1:
    s1=int(input("enter the first number:- "))
    s2=int(input("enter the sencond number:- "))
    if s1==56 and s2==9:
        print("sum:",s1,"+",s2,"=77")
    else:
        r1=s1+s2
        print("sum:",s1,"+",s2,"=",r1)

# for substraction
if a in range (1,4+1) and a==2:
    s3=int(input("enter the first number:- "))
    s4=int(input("enter the sencond number:- "))
    if s3==57 and s4==7:
        print("sub:",s3,"-",s4,"=77")
    else:
        r2=s3-s4
        print("sub:",s3,"-",s4,"=",r2)

# for multipication
if a in range (1,4+1)and a==3:
    s5=int(input("enter the first number:- "))
    s6=int(input("enter the sencond number:- "))
    if s5==43 and s6==3:
        print("mul:",s5,"*",s6,"=555")
    else:
        r3=s5*s6
        print("mul:",s5,"*",s6,"=",r3)

# for Division
if  a in range (1,4+1) and a==4:
    s7=int(input("enter the first number:- "))
    s8=int(input("enter the sencond number:- "))
    if s7==56 and s8==6:
        print("div:",s7,"%",s8,"=4")
    else:
        r4=s7/s8
        print("div:",s7,"%",s8,"=",r4)
else:
    print("Plz enter the valid input")