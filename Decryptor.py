import numpy as np

storage = []
#Creates an alphabet array to map to
alphabet = ["A","B","C","D","E","F","G","H",
"I","J","K","L","M","N","O","P","Q","R","S",
"T","U","V","W","X","Y","Z",]

#takes input from user
value = input("Please enter a key, the encrypted word, and the extra:\n")
storage = value.split(" ")
#finds the dimension of the key
div = (len(storage) - 2) ** 0.5
#assigns the encrypted word to a string
encryptedWord = storage[-2].upper()
#stores the extra value
extra = int(storage[-1])

#creates a key in matrix form
def keyMaker (stor):
    key = stor[0:len(stor)-2]
    key = np.asarray(key)
    key = key.astype(int)
    key = key.reshape([int(div), int(div)])
    return key

#finds the inverse of the key
def keyInverse ():
    invMod = 0
    x = keyMaker(storage)
    inverse = np.linalg.inv(x) * (np.linalg.det(x))
    inverse = np.around(inverse)
    determinant = (np.linalg.det(x))
    determinant = int(round(determinant))
    invMod = modInverse(determinant, 26)
    x = (invMod * inverse) % 26
    return x.astype(int)

#Euclid's Extended Algorithm for Inverses
def modInverse (a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1

#Converts an array to a string
def convert(s):
    new = ""
    for i in s:
        new+=i
    return new

#converts a string into an arraylist
hold = list(encryptedWord)

#converts a word into a number
def wordToNumber (r):
    for i in range(0, len(r)):
        for j in range (0, len(alphabet)):
            if r[i] == alphabet[j]:
                r[i] = j
    return r

#decodes the encrypted word
def decryptA (t):
    keyI = keyInverse()
    strArr = []
    holder = np.array([])
    t = wordToNumber(t)
    for i in range (0, len(t), int(div)):
        y = i + int(div) 
        tempArr = t[i:y]
        tempArr = np.asarray(tempArr)
        temp = tempArr.reshape([int(div), 1])
        ans = np.matmul(keyI, temp)
        ans = np.around(ans)
        ans = ans%26
        ans = ans.reshape([1,int(div)])
        holder = np.append(holder, ans)
    for i in range (0, len(holder)):
        strArr.append(i)
    for i in range (0, len(holder)):
        temp = int(holder[i])
        strArr[i] = alphabet[temp]
    z = int(len(encryptedWord)) - extra
    dWord = strArr[0:z]
    return convert(dWord)


#prints solution
decryptedText = decryptA(hold)
print("The decrypted word is: ")
print(decryptedText)