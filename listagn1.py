l =["mouse","rat",[1,3,5],['b','d','g']]
#print(l)
print(len(l[1]))
print(l[0][-2])
print(l[-1][-2])
 
m = [1,3,'new',12.3,[1,2,3],'old']
m.remove(12.3)
print(m)
m[-2].remove(2)
print(m)

n = [[7,5,3],[6,1,2],[8,2,9]]
n[0].sort()
n[1].sort()
n[2].sort()
n.reverse()
print(n)

o = [17.3,44,8,22.1]
o.sort()
print(o)
o.pop(-2)
print(o)