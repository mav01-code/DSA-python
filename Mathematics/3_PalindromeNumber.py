"""
Problem: Palindrome Number
1)  Input: 121          | reverse --> 121
    Output: Palindrome
2)  Input: 4553          | reverse --> 3554
    Output: Not Palindrome
3)  Input: 7          | reverse --> 7
    Output: Palindrome
"""
n = int(input())
num = n
rev = 0
while(n>0):
    rev = rev*10+(n%10)
    n = n//10
if(num==rev):
    print("Palindrome")
else:
    print("Not Palindrome")