def decrypt(statement):
    try:
        words=statement.split(" ")
        output=[]
        for word in words:
            if(len(word)>=3):
                decoded=word[3:-3]
                decoded=decoded[-1]+decoded[:-1]
                output.append(decoded)
            else:
                output.append(word[::-1])
        return(" ".join(output))
    except:
        print("Looks Like The statement is already decrypted (Readable)")

