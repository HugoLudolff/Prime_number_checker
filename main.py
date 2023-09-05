from menu import menu, menu_numero
import time

def checker(number):
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i+=6
    return True

def find_divisors(number):
    divisors = []
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors


def printer(number):
    if checker(number) == True:
        print(f'{number} is a prime number')
    else:
        divisors = find_divisors(number)
        print(f"{number} is not a prime number. It is divisible by {', ' .join(map(str, divisors))}.")


def function(number):
    while True:
        number = menu_numero()
        time.sleep(0.5)
        if number < 0:
            print('Negative numbers wont work')
        elif number == 0:
            break
        elif number == 1:
            print('One')
        else: 
            printer(number)


def generate_primes_range():
    primes_in_range = []
    number = int(input("Enter a positive integer: "))
    number2 = int(input("Enter another positive integer: "))
    
    for i in range(number, number2):
        #checker(i)
        if checker(i):
            primes_in_range.append(i)
    print(f'Prime numbers in the range {number} - {number2}: {primes_in_range}')

            
        


def main():
    number = 1
    while True:
        option = menu()
        if option == '1':
            time.sleep(0.5)
            function(number)
        elif option == '2':
            generate_primes_range()
        elif option == '3':
            print('Quiting...')
            time.sleep(1)
            break
        else: 
            print('Invalid Input!')





if __name__ == '__main__':
    main()