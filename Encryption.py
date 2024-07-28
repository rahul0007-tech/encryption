import random
import string



def encrypt(statement):
    words=statement.split(" ")
    output=[]
    for word in words:
        if(len(word)>=3):
            randomLetters=[random.choice(string.ascii_letters.lower())for _ in range(3)]
            randomLetters1=[random.choice(string.ascii_letters.lower())for _ in range(3)]
            coded="".join(randomLetters)+word[1:]+word[0]+"".join(randomLetters1)
            output.append(coded.lower())
        else:
            output.append(word.lower()[::-1])
    return (" ".join(output))










