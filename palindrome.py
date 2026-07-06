num=int(input("enter num"))
rev=0
temp=num
while temp!=0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if num==rev:
    print("palindrome")