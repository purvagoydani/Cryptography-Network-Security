# CNS Assignment-1
# Written By PURVA GOYDANI
# BT17CSE072

#additive inverse of a number
def additiveInverse(n):
    print("Additive inverses are: ")
    for i in range(n):
        for j in range(i,n):
            if((i+j)%n == 0):
                print(i,",",j)

#multiplicative inverse of a number
def multiplicativeInverse(n):
    print("\nMultiplicative inverses are: ")
    for i in range(n):
        for j in range(i,n):
            if((i*j)%n == 1):
                print(i,",",j)

n=int(input("Enter 'n' to find Additive and Multiplicative in set Zn: "))
additiveInverse(n)
multiplicativeInverse(n)