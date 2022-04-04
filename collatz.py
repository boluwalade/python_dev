
from urllib import response


def collatz(number):
    if number % 2 == 0:
        collatz_output = number // 2  
    else:
        collatz_output = 3 * number + 1
    return(collatz_output)


try:
    user_input = int(input('Please enter an integer: '))
    response = collatz(number= user_input)
    while response != 1:
        print(response)
        if response != 1:
            response = collatz(number= response)
            print(response)
            continue
        else:
            break
except ValueError:
    print('Please enter an integer')


