username = input('Enter your username: ')
password = input('Enter your password: ')
encrypted_password = '*' * len(password)
print(encrypted_password)

print(f'Hello {username} your password {encrypted_password} is {len(password)} long!')
