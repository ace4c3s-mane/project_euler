"""
Project Euler Problem 1
Sum of multiples of 3 & 5 below 1000
"""

# List comperehension
multiples = [i for i in range(1000) if (i % 3 == 0 or i % 5 == 0)]
print(sum(multiples))

# For loop
total = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

# Generator Expression
five_three_multiples = (i for i in range(1000) if (i % 3 == 0 or i % 5 == 0))
print(sum(five_three_multiples))

