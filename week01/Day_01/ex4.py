# Sum of digits (classic): given a non-negative integer like 98765, return the digit sum using % and // in a while loop, 
# without converting to a string.

num = input("Enter a non-negative integer: ")
n=int(num)
sum=0
while(n!=0):
    sum+= n%10
    n=n//10
print(f"sum: {sum}")