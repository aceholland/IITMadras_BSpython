#sum_until_0:  Continuously read integers from standard input until you receive a zero. Print the sum of these integers.

task=input()

if task.lower()=="sum_until_0":
    total=0
    n=int(input())
    while (n!=0):
        total+=n
        n=int(input())
    print(total)

#total_price:  Continuously read pairs of integers from standard input, representing the quantity and price of items, 
# until you receive the string "END".
#  Print the total price of all items.

if task.lower()=="total_price":
    total=0
    while True:
        line=input()
        if line.lower()=="end":
            break
        quanity, price=line.split()
        quantity, price=int(quantity), int(price)
        total+=quantity*price
    print(total)

#only_ed_or_ing:  Continuously read strings from standard input until you encounter the word 
# "STOP" (case insensitive and not included in the output). 
# Print only those strings that end with "ed" or "ing" (case insensitive).

if task.lower()=="only_ed_or_ing":
    while True:
        word=input()
        if word.lower=="stop":
            break
        if word.lower().endswith("ed") or word.lower().endswith("ing"):
            print(word)

#reverse_sum_palindrome: Continuously read positive integers from standard input until
#  you encounter a "-1"(not included in the output).
#  Print only those integers for which the sum of the number and its reverse is a palindrome.

if task.lower()=="reverse_sum_palindrome":
    while True:
        n=int(input())
        if n==-1:
            break
        n2=n+int(str(n)[::-1])
        if (n2==int(str(n2)[::-1])):
            print(n)

#double_string: Continuously read lines from standard input until an empty line is encountered. Print each line repeated twice.
if task.lower()=="double_string":
    while True:
        line=input()
        if line=="":
            break
        print(line*2)

#odd_char: Continuously read strings from standard input until you encounter a string ending with a "."
# (include that string with the "." in the output). Extract characters at odd positions (starting from 1) of each line, 
# and print the results in a single line separated by spaces.

if task.lower()=="odd_char":
    while True:
        line=input()
        if line.endswith("."):
            print(line[::2])
            break
        print(line[::2], end=" ")

#only_even_squares: Continuously read numbers from standard input until "NAN" is encountered. 
# Print the square of each number only if it is even.

if task.lower()=="only_even_squares":
    while True:
        number=input()
        if number.lower()=="nan":
            break
        if (int(number)%2==0):
            print((int(number))**2)

#only_odd_lines: Continuously read lines from standard input until "END"(not included in the output) is encountered. 
# Create a string by prepending only the odd lines (starting from 1) with a newline character in between, and print 
# the result which will be the odd lines in reverse order.

if task.lower()=="only_odd_lines":
    count=1
    result=""
    while True:

        line=input()
        if line.lower()=="end":
            break

        if count%2==1:
            result=line+"\n"+result
        count+=1

    print(result)
        
