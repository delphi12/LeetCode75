

str1 = "bat"
str2 ="cat"
check = (sorted(str1) == sorted(str2))

if check:
    print("Two strings are anagrams")
else:
    print("Not an anagram")