n=int(input())
points=list(map(int, input().split()))
max_point=points[0]
min_point=points[0]
count=0
for i in range(1,n):
    if points[i]>max_point:
        count+=1
        max_point=points[i]
    if points[i]<min_point:
        count+=1
        min_point=points[i]
print(count)