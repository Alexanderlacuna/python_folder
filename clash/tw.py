def rotate(word):
    temp=word[0]
    df=[]
    for i in range(len(word)-1):
        df+=word[i+1]
    df+=temp
    return "".join(df)

f=rotate("abcd")
g=rotate(f)
h=rotate(g)
print(h)

def leftRotate(arri):
    temp=arri[0]
    for i in range(0,(len(arri)-1)):
        arri[i]=arri[i+1]

    arri[-1]=temp

    return arri
k=leftRotate([1,2,3,4])
def rightRotate(arri):
    temp=arri[-1]
    for i in reversed(range(0,len(arri))):
        arri[i]=arri[i-1]
        # arri[i]=arri[i-1]

    arri[0]=temp
    return arri

print(leftRotate(k))
print(rightRotate([1,2,3,4]))