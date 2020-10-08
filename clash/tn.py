https://www.codingame.com/clashofcode/clash/13281109b2089805bf6d16d691522870b23fe32
I=input
w,h=int(I()),int(I())
g=p=['0'*(w+2)]
for i in range(h):g=g+['0'+I()+'0']
g,b=g+p,0
for x in range(1,w+1):
 for y in range(1,h+1):
  s=''.join(g[y+z][x-1:x+2]for z in [-1,0,1])
  if 'A' not in s:
   k=sum(map(int,s))
   if k > b:q,w,b=x,y,k
print(q-1,w-1)                