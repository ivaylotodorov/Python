# STRINGS

import datetime
username = 'superuser'
password = 'supersecret'
long_string = '''
W W W
 O 0
 ----
 '''
print(long_string)

first_name = 'ivaylo'
last_name = 'todorov'
full_name = first_name + ' ' + last_name
print(full_name)
print(full_name.title())
print('Hello my name is ' + full_name.title() + '!')

weather = "It\'s \"kind of\" sunny \n hope you have a good day!"
print(weather)

print('Languages: \n \t Python \n \t C Sharp \n\t Javascript')

print('')
# formatted strings

name = 'ivaylo'
age = 39
message = f'Hello {name.title()}, soon you will be {age} years old!'
print(message)

# string indexes
print(name[5])
numbers = '1234567'
print(numbers[1:4:2])
print(numbers[1:7:1])
print(numbers[-1])
print(numbers[::2])
print(numbers[:-1])

################ Program determine your age ##################################
first_name = input('What\'s your first name:')
last_name = input('What\'s your last name:')
birth_year = input('What year were you born?:')
now = datetime.datetime.now()
present_year = now.year
full_name = first_name + ' ' + last_name
age = present_year - int(birth_year)
print(f'Hello {full_name.title()}. You are {age} years old!')

############## Pasword generator #####################################

username = input('Enter your username: ')
password = input('Enter your password: ')
encrypted_passowrd = '*' * password.len()