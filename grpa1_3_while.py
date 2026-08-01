#sum_until_0:  Continuously read integers from standard input until you receive a zero. Print the sum of these integers.
#total_price:  Continuously read pairs of integers from standard input, representing the quantity and price of items, 
# until you receive the string "END".
#  Print the total price of all items.
task=input()

if task.lower()=="sum_until_0":
    total=0
    n=int(input())
    while (n!=0):
        total+=n
        n=int(input())
    print(total)

if task.lower()=="total_price":
    total=0
    while True:
        line=input()
        if line.lower=="end":
            break
        quanity, price=line.split()
        quantity, price=int(quantity), int(price)
        total+=quantity*price
    print(total)
    