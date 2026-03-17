import random
def main():
    while True:
    
        first_random_integer = random.randint(1, 100)
        second_random_integer = random.randint(1, 100)
        see_numbers = input("Our flagship program generated two random intgers, do you want to see them? (type yes to see, or no to skip) ").strip().lower()
        if see_numbers == 'yes':
            print(f"Random numbers: {first_random_integer} and {second_random_integer}")
        elif see_numbers == 'no':
            print("Okay, let's proceed without showing the numbers.")
        elif see_numbers == 'q':
            break
        operator = input("Choose operation (+, -, *, /, or q to quit): ").strip()
        if operator == 'q':
            break
        
        if operator == '+':
            result = first_random_integer + second_random_integer
        elif operator == '-':
            result = first_random_integer - second_random_integer   
        elif operator == '*':
            result = first_random_integer * second_random_integer
        elif operator == '/':
            if second_random_integer == 0:
                print("Cannot divide by zero")
                continue
            result = first_random_integer / second_random_integer
        else:
            print("Invalid operation")
            continue
        
        print(f"{first_random_integer} {operator} {second_random_integer} = {result}")

if __name__ == "__main__":
    main()
#final Version