# Sum of digits (classic): given a non-negative integer like 98765, return the digit sum using % and // in a while loop,
# without converting to a string.

num_o = input("Enter a non-negative integer: ")
n=int(num_o)
if n<0:
    n=n*-1
sum_digits=0
while(n!=0):
    sum_digits+= n%10
    n=n//10
print(f"sum: {sum_digits}")