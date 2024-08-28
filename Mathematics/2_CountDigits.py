"""
Problem: Count Digits
Input: 9253
Output: 4
Input: 38
Output: 2
[x>0]
"""

"""
# Method 1:
n = str(input())
print(len(n))
"""

# Method 2:
n = int(input())
res = 0
while n>0:
    n = n//10
    res+=1
print("Count of digits is: ",res)