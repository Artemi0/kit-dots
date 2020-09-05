import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

a,b,c = [int(s) for s in input().split()]
l,h = [int(s) for s in input().split()]

s = (a*b + a*c*2 + b *c*2) * 0.85 
sr = ((l/1000) * (h/1000) ) * 0.9 

k = s/sr 
if k // 1 != 0 : 
    k += 1    

print(int(k))
