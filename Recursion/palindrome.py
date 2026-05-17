name = "markram"
n = len(name)

def palindrome(i):
    if i >= n/2:
        return True
    if name[i] != name[n-i-1]:
        return False
    return palindrome(i+1)

isPalindrome = palindrome(0)

if isPalindrome:
    print("Palindrome")
else:
    print("Not Palindrome")