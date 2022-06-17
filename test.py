from sys import argv
print('Hello From Test')
print(type(argv)) # <class 'list'>
print(argv) # ['test.py', '10', '20', '30']

print( argv[1] +argv[2] +argv[3]) # '102030'

print( int(argv[1]) + int(argv[2]) + int(argv[3])) # '60'
