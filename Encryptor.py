import numpy as np
import sys

#storage holds the key and the word in an array
storage = []
#array for the alphabet
alphabet = ["A","B","C","D","E","F","G","H",
"I","J","K","L","M","N","O","P","Q","R","S",
"T","U","V","W","X","Y","Z",]

#takes input fromo user
value = input("Please enter a key and then the word:\n")
#stores it into the array 
storage = value.split(" ")
#dimension of the key
div = (len(storage) - 1) ** 0.5
word = storage[-1].upper()

#creates the key in matrix form
def keyMaker (stor):
    key = stor[0:len(stor)-1]
    key = np.asarray(key)
    key = key.astype(int)
    key = key.reshape([int(div), int(div)])
    return key

#maps the word to the alphabet array and converts it to its corresponding number
def wordToNumber (r):
    for i in range(0, len(r)):
        for j in range (0, len(alphabet)):
            if r[i] == alphabet[j]:
                r[i] = j
    return r

#converts the word into an array of numbers 
hold = wordToNumber(list(word))

#finds the extra in the encrypted code
def extra():
    w = 0
    z = int(div)
    x = int(len(word)%z)
    if(x == 0):
        w = 0
    else:
        w= (z - x)
    return w

#finds the encrypted word in array form  
def encryptNum(w):
    key = keyMaker(storage)
    ans = np.array([])
    determinant = int(np.linalg.det(key))
    #checks for invalid key
    if(determinant%2 == 0 or determinant%13 == 0):
        print("Invalid Key, enter a key whose determinant has no common factor with 26")
        #quits program
        sys.exit()
    else:
        w = extra()
        for i in range (0, w):
            hold.append(1)
        for j in range (0, len(hold), int(div)):
            y = j + int(div)
            temp = hold[j:y]
            temp = np.asarray(temp)
            temp = temp.reshape([int(div), 1])
            mat = np.matmul(key, temp)
            mat = mat%26
            mat.reshape(1, int(div))
            ans = np.append(ans, mat)
    return ans

#converts array to string
def convert(s):
    new = ""
    for i in s:
        new+=i
    return new

#converts the array of the encrypted word into a string
def encrypt (num):
    strArr = []
    for i in range (0, len(num)):
        strArr.append(i)
    for i in range (0, len(num)):
        temp = int(num[i])
        strArr[i] = alphabet[temp]
    return convert(strArr)



#prints encrypted word, key and extra
text = encryptNum(word)
answer = encrypt(text)
extraLetter = extra()
print("The key is: ")
print(keyMaker(storage))
print("The encrypted text is: ")
print(answer)
print("The extra is: ")
print(extraLetter)