import hashlib

A=input("ENTER A STRING:  ")
B=int(input("Select an algorithm to hash: \n\n 1.hash \n 2.md5 \n 3.sha1 \n 4.sha256 \n 5.sha384 \n 6.sha512 \n\n"))
        
if(B==1):
    print(hash(A))

elif(B==2):
    result = hashlib.md5(A.encode())
    print(result.hexdigest())


elif(B==3):
    result=hashlib.sha1(A.encode())
    print(result.hexdigest())

elif(B==4):
    result=hashlib.sha256(A.encode())
    print(result.hexdigest())

elif(B==5):
    result=hashlib.sha384(A.encode())
    print(result.hexdigest())

elif(B==6):
    result=hashlib.sha512(A.encode())
    print(result.hexdigest())
