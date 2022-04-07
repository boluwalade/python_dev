from platform import python_version


username = input('Enter Username:')
password = input('Enter Password:')

password_length = len(password)
hidden_password = '*' * password_length

if password_length > 10:
    hidden_password = '*' * 10
else:
    hidden_password

print(f'your  password {hidden_password} is {password_length} characters long')
