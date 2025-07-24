#password generator

import random
import string

passwordlist=[]
passLen =int(input("hello! please enter the password length: \n"))
print(passLen)


def genrateChar(passLen):
    count=0
    letters = list(string.ascii_letters)
    punc= list(string.punctuation)
    print(passLen)
    while count<passLen:
        
        randNum = random.randint(1, passLen)
        randgenstr=random.randint(1, len(letters)-2)
        randgenchar=random.randint(1, len(punc)-2)

    
        randchar = str(randNum)+letters[randgenstr]+punc[randgenchar]+""
        passwordlist.append(randchar)
        count+=1

    return passwordlist

def passwordConv(password):
    passSet=set(password)
    passstr=''.join(str(i) for i in passSet)
    passSet=set(passstr)
    passstr=''.join(str(i) for i in passSet)
    passstr=passstr[2:passLen+2]

    return passstr


def printPass(length):

    if passLen<length:
        print("please enter more than 4 charcter")
    else:
        genrateChar(passLen)
        print(passwordConv(passwordlist))
        
printPass(passLen)
