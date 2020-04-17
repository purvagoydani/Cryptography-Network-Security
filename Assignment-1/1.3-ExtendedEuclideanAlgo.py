# CNS Assignment-1
# Written By PURVA GOYDANI
# BT17CSE072

#Extended Euclidean Algo to find GCD
def gcd(a,b,s1,s2,t1,t2):
    if b==0:
        print("GCD = ",a,"\ns = ",s1,"\nt = ",t1)
    else:
        r= a%b
        q=(a-r)/b
        return gcd(b,r,s2,s1-q*s2,t2,t1-q*t2)


a=int(input("First Number  : "))
b=int(input("Second Number : "))
if(a>b):
    gcd(a,b,1,0,0,1)
else:
    gcd(b,a,0,1,1,0)

