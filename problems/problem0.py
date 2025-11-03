"""
Project Euler problem0
Find the sum of odd squares for a given range
"""

# Using list comprehensions
squared_odd_numbers = [i*i for i in range(473000) if (i * i) % 2 != 0]
print(sum(squared_odd_numbers))

# Using generator Expressions
squared_odds = ((i * i) for i in range (473000) if (i * i) % 2 != 0)
print(sum(list(squared_odds)))


# Alternative Method using for loop
squared_numbers = []
for i in range(473000):
    if i * i % 2 != 0:
        squared_numbers.append(i * i)
print(sum(squared_numbers))
