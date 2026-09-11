# for문

#for (int i=0; i<0; i++)
#for i in iterable객체:

for i in range(5):
    print(i,end="")
print()

#1~5
a=range(1,6)
print(a.start, a.stop ,a.step)
print()

#1~10, 2씩 띄어서
for i in range(1,10,2):
    print(i,end="")
print()

# 5, 4, 3, 2, 1
for i in range(5,0,-1):
    print(i,end="")
print()

#1~10까지의 합
tot=0

for i in range(1,11):
    tot+=i
print(tot)

print(sum(range(1,11)))

s= "feqomegkdsff"

for c in s:
    print(c, end="")
print()

print(len(s))

#구구단 출력
# 2 * 1 = 1  2 * 2 = 4 .. 2 * 9 = 18
#..
# 9 * 1 = 9  9 * 2 = 18 .. 9 * 9 = 81
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {1*j:<5d}",end="")
        print()
else:
    print("End")