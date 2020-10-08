# p="DSFsdfsdf"
# k="dsadsf"
# reversed_k=k[::-1]

# f=(list(reversed(k)))
# # print(ord("s"))
# # e=ord("aas")
# # print(e)
# # 
# print("".join(f))
# print(f"{sum(map(ord, s)) / len(s):.1f}")
n = int(input())
d=[]
for i in range(n):
    shift = input()

    w=shift.split("->")

    hrs=24

    x1=w[0]
    x2=w[1]

    d.append(x1)
    d.append(x2)
g=[]
for i in range(25):
    if i not in d:
        g.append(i)

print("->".join(g))