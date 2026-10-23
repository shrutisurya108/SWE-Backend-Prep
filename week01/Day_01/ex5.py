# Reverse a string two ways: (a) slicing, (b) a loop that builds a list and uses "".join.
# Then check if a word is a palindrome, ignoring case ("Racecar" → True).

st = input("Enter the string: ")
# First way of reversal
st1 = st[::-1]
print(f"st1: {st1}")

#Second way of reversal
letters_list=[]
for ch in range(len(st)-1, -1, -1):
    letters_list.append(st[ch])
st2="".join(letters_list)
print(f"st2: {st2}")

# if st.lower() == st1.lower():
#     result = True
# else:
#     result = False
result = st.lower == st1.lower()
print(f"Palindrome check Result: {result}")