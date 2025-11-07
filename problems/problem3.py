"""
Project Euler problem3
Find the max prime factor 
"""


import math

def main() -> None:

    my_list = []
    number = 600851475143

    def is_prime(n):
        if n < 1:
            return False
        
        for i in range(2,int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


    for i in range(2,int(math.sqrt(number)) + 1):
        if number % i == 0 and is_prime(i):
            my_list.append(i)
        
    print(max(my_list))

if __name__ == "__main__":
    main()

