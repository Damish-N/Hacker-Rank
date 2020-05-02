'''
x=int(input())
for i in range(1,x+1):
    print(i,end='')

n = int(input())
arr = map(int, input().split())
list1=list(arr)
#print(list1)
list1=list(dict.fromkeys(list1))
print(list1)
list1.remove(max(list1))
print(max(list1))
'''
list1=[]
if __name__ == '__main__':
    for _ in range(0,int(input())): 
        list1.append([input(),float(input())])


print(list1)

second_highest = sorted(list(set([marks for name, marks in list1])))[1]
print('\n'.join([a for a,b in sorted(list1) if b == second_highest]))
