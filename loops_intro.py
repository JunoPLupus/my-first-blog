def hi(name):
    print('Hello {}!'.format(name))

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola']

for name in girls:
    hi(name)

person = {
    'name' : 'Ola', 
    'height' : 21, 
    'favourite_language' : 'python'
    }

for key, value in person.items():
    print("Person's " + str(key) + " is " + str(value))

for number in range(1, 11):
    print(number)