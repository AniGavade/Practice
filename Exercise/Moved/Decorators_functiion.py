def abc(tt):#abc(vv) ,tt =vv
    def gg():
        tt() #vv() #"BB" 
        print("hi") #HI
        def rohit():
            tt()#VV()#bb

        rohit()

    return gg     
        
@abc
def vv():
    print('bb') 
 #vv = abc(vv)
vv() #vv() = abc(vv) = gg()