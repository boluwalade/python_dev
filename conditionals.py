counter = 0
attempts = 3
while counter <= 3:
    club = input("Hello, please enter a top 4 club:").lower()
    top_four = ['chelsea','arsenal','city','united']
    if club in top_four:
        print('your club is doing well')
    else:
        attempts_left = attempts - counter
        print(f'The club is not in top four. You have {attempts_left} left')
        counter = counter + 1
        continue
    key = input('please enter key:').upper()
    if key == 'PASSWORD':
        break
    else:
        print('wrong key')
if counter == 4:
    print('You have exceeded your number of attempts')
else:
    print('Welcome!')
    


    

