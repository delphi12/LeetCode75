
def reverse_vowels(s1):
    vowels =['a','e','i','o','u','A','E','I','O','U']
    l,r=0,len(s1)-1
    s=list(s1)
    while(l<r):
        if s[l] not in vowels:
            l+=1
            continue
        if s[r] not in vowels:
            r-=1
            continue
        s[l],s[r] = s[r], s[l]
        l+=1
        r-=1

    print(s)

s="LeetCode"
reverse_vowels(s)