A = input()

# Please write your code here.
def isDifferent(A):
    arr = list(A)
    s = set()
    for elem in arr:
        s.add(elem)
    
    if len(s) > 3:
        return 'Yes'
    return 'No'

print(isDifferent(A))