string = input("Enter a string(small letters): ")
hash_arr = [0]*26

for char in string:
    hash_arr[ord(char) - ord('a')] += 1

queries = int(input("Enter number of queries: "))
while(queries):
    char = input("Enter character to find frequency: ")
    print(f"frequency of {char}: {hash_arr[ord(char) - ord('a')]}")
    