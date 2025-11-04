"""
Project Euler problem 2
Find the sum of an even fibonnaci sequence
"""
def main() -> None:
    first_number = 0
    second_number = 1

    factorials = []
 
    while True:
        next_number = first_number + second_number
        if next_number < 4000000:
            if next_number % 2 == 0:
                factorials.append(next_number)
        else:
            print(f"The sum of even fibonnaci sequence is {sum(factorials)}")
            break
        first_number = second_number
        second_number = next_number

if __name__ == "__main__":
    main()