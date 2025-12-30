a=int(input("enteer a number"))
if(a>0):
    i=1
    while i**i<=a:
        if(i**i==a):
            print("square root of a is ",i)
            break
        i+=1
    else:
        print("entered number is not a perfect square",a)


else:
    print("enter number above 0")


