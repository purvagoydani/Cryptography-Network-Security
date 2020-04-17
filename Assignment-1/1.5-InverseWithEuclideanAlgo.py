# CNS Assignment-1
# Written By PURVA GOYDANI
# BT17CSE072

#additive and multiplicative inverse using Extended Euclidean Algo
def gcd(a,b,t1,t2):
    if b==0:
        return t1
    else:
        r= a%b
        q=(a-r)/b
        return gcd(b,r,t2,t1-q*t2)

n=int(input("Enter value of n in set Zn:"))
b=int(input("Enter the number whose Inverse is to be calculated: "))
t=gcd(n,b,0,1)
print("\nAdditive inverse of ",b," = ",(n-b)%n)
print("\nMultiplicative inverse of ",b," = ",int(t%n),"\n")

