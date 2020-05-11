"""
Error
"""

#l = [1, 2, 3]
#i = 5

#try:
#    l[i]
#except:
#    print("Don't worry")

#print("last")


#try:
#    l[i]
#except IndexError as ex:
#    print("Don't worry: {}".format(ex))
#except NameError as ex:
#    print(ex)
#except Exception as ex:
#    print('other: {}'.format(ex))
#else:
#    print('done')
#finally:
#    print('clean up')

"""
finally : Must Run
"""



"""
Original exception

   Create the exception yourself and return the error.

   UppercaseError : original exception
"""

#class UppercaseError(Exception):
#    pass

#def check():
#    words = ['APPLE', 'orange', 'banana']
#    for word in words:
#        if word.isupper():
#            raise UppercaseError(word)

#check()


# try:
#    check()
# except UppercaseError as exc:
#    print('This is my fault. Go next')



"""
ImportError

Can be used when moved to a different folder
"""


#try:
#    from package import utils
#except ImportError:
#    from package.tools import utils

#utils.say_twice('word')

