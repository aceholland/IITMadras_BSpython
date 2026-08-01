#Accept a positive integer n>1, as input from the user and print all the prime factors of n in ascending order.

n=int(input())
factor=2
while n>1:
    if n%factor==0:
        print(factor)
        while n%factor==0:
         n//=factor
    else:
        factor+=1
        

    