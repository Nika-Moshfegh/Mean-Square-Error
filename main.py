def solution(array_a, array_b):
    res=0
    for i in range(0,len(array_a)):
        res+=abs(array_a[i]-array_b[i])**2
    return res/len(array_b)
print(solution([1, 2, 3], [4, 5, 6]))