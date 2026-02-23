A = input()

# Please write your code here.
def palindrome(A):
    B = A[::-1]
    if B == A:
        return 'Yes'
    else:
        return 'No'

print(palindrome(A))
