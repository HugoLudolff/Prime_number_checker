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
    


def main():
    number = 1
    while True:
        option = menu()
        if option == '1':
            time.sleep(0.5)
            function(number)
        elif option == '2':
            print('Quiting...')
            time.sleep(1)
            break
        else: 
            print('Invalid Input!')





if __name__ == '__main__':
    main()