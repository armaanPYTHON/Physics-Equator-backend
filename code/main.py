import solve
import symbols
import mathbo
import time


print('Hello! Welcome to Physics Equator!')
print('instructions\nsolve\nadd formula\nupdate formula database')
in1 = input('Choose type the initial letter of one of the above options to continue: ')
print('\n...\n')
time.sleep(1)

dict1 = {
    'i':'symbols.main()',
    's':'solve.main()',
    'a': 'print("This feature is soon coming!")',
    'u':'mathbo.main()'
}

eval(dict1[in1])