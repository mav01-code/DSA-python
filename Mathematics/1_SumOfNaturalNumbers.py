"""
Problem - Sum of n Natural Numbers

Day 1: 1
Day 2: 2
Day 3: 3
Day 4: 4
Day 5: 5
Day 6: 6
........
Day 10: 10

Find total money saved after 10 days.
1+2+3+4+5+6+7+8+9+10
sum = (n*(n+1))/2
"""

n=int(input())
sum = (n*(n+1))//2
print("Sum: ",sum)

"""
How does this formula work?
Sn = 1 + 2 + 3 + 4 + .... n
Sn = n + (n-1) + (n-2) + (n-3) ... 1 --> In reverse order
_____________________________________
2Sn = (n+1) + (n+1) + (n+1) +...(n+1)
      -------------------------------> (n+1) is repeated n times
2Sn = n*(n+1)
Sn = (n*(n+1))/2
"""