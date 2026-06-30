name = 'Sonia'
age = 21

if age < 18:
    print('You\'re not allowed to see this!')
elif name == 'Ola':
    print('Hey Ola')
elif name == 'Sonia':
    print('Hey Sonia')
else:
    print('Hey anonymous')

person = {'name' : 'Mariana', 'age' : 21, 'favourite_language' : 'python'}

if person['age'] < 18:
    print('You\'re not allowed to see this!')

else:
    for name, age, favourite_language in person.items():
        print(f'{name} has {str(age)} years and loves {favourite_language}')