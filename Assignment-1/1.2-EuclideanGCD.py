# CNS Assignment-1
# Written By PURVA GOYDANI
# BT17CSE072

#Euclidean Algo to find GCD
def gcd(a,b):
    if b==0:
        return a
    else:
        r= a%b
        return gcd(b,r)


a=int(input("First Number : "))
b=int(input("Second Number: "))
if(a>b):
    print("GCD = ",gcd(a,b))
else:
    print("GCD = ",gcd(b,a))

