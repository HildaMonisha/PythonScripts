# Fibonacci sequence using function
'''
def fibo_seq(n):
    if n<=1:
        return n
    else:
        return (fibo_seq(n-1)+fibo_seq(n-2))


num=int(input("how many numbers: "))
print("Fibonacci series:")
for i in range(num):
    print(fibo_seq(i))
'''
# Fibonacci using normal program

n1, n2 = 0, 1
count = 0
num = int(input("total number: "))
while count < num:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1


# Palindrome- string

#def reverse(s):
#   return s[::-1]


s1 = str(input("enter the word: "))
s2 = s1[::-1]
if s1 == s2:
    print("%s is palindrome" % s1)
else:
    print("%s is not palindrome" % s1)

#Palindrome- number

num=int(input("enter the number: "))
temp=num
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10
if (temp==rev):
    print("palindrome number")
else:
    print("not palindrome number")

