from Encryption import encrypt
from Decryption import decrypt


statement=input("Enter the Statement: ")
selection=input("Enter the choice 1 to code and 2 to decode and 0 to exit")
def select(statement):
    while True:
        if(selection=="1"):
            print(encrypt(statement))
            break
        elif(selection=="2"):
            
            print(decrypt(statement))
            break
        elif(selection=="0"):
            break
        else:
            print("please select 1 or 2 or 0")

select(statement)



# ___________________________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________________________
# def select():
#     while True:
#         statement=input("Enter the Statement: ")
#         selection=input("Enter the choice 1 to code and 2 to decode and 0 to exit")
#         if(selection=="1"):
#             print(encrypt(statement))
#         elif(selection=="2"):
#             print(decrypt(statement))
#         elif(selection=="0"):
#             break
#         else:
#             print("please select 1 or 2 or 0")

# select()