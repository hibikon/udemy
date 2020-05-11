"""
input function
"""

#while True:
#    word = input('Enter:')
    
#    if word == 'ok':
#        break
#    print('next')

'''
Default String

   int : int()
'''

"""
range function
"""

#num_list = [0, 1, 2, 3, 4, 5 ,6 ,7 ,8 , 9, 10]
#for i in num_list:
#    print(i)

#for i in range(10):
#    print(i, 'python')

'''
range(from, to, interval):
'''

"""
enumerate function
"""

#i = 0
#for fruit in ['apple', 'banana', 'orange']:
#    print(i, fruit)
#    i += 1

#for i, fruit in enumerate(['apple', 'banana', 'orange'])
#    print(i, fruit)


"""
zip function
"""

#days = ['Mon', 'Tue', 'Wed']
#fruits = ['apple', 'banana', 'orange']
#drinks = ['coffee', 'tea', 'beer']

#for i in range(len(days)):
#    print(days[i], fruits[i], drinks[i])

#for day, fruit, drink in zip(days, fruits, drinks):
#    print(day, fruit, drink)

"""
Built-in function

    URL : https://docs.python.org/ja/library/functions.html
"""

#import builtins

#builtins.print()

#ranking= {
#    'A': 100,
#    'B': 85,
#    'C': 95
#}

#print(sorted(ranking, key=ranking.get, reverse=True))

"""
Standard library

    URL : https://docs.python.jp/3/library/index.html
"""

#s = 'afrefffdsfdsfredfadf'

#d = {}
#for c in s:
#    if c not in d:
#        d[c] = 0
#    d[c] += 1
#print(d)

#d = {}
#for c in s:
#    d.setdefault(c, 0)
#    d[c] += 1
#print(d)


#from collections import defaultdict

#for c in s:
#    d[c] += 1
#print(d)

"""
Third party library

    URL : https://pypi.python.org/pypi

    pip install termcolor

    print(help(colored))
"""

#import termcolor

#print('test')

#print(colored('test', 'red'))

