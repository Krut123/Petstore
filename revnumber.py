n = 1111
temp = n
rev = 0
while(n>0):
    digit = n % 10
    """ print("digit: ",digit) """
    rev=(rev*10)+digit
    """ print("rev=",rev) """
    n//=10
print("n=",rev)

if temp == rev:
    print("no is palindrome")
else:
    print("no is not pallindrome")