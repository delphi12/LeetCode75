#given an array of Integers nums, return an array which has elements as products of all the elements in the array
#except the value of the position. out[i] = product of values in all indices expect arr[i]

#should not use division operator, and time complexity should be 0(n)

def productArray(arr):
    out=[1]*(len(arr))
    prefix =1
    for i in range(len(arr)):
        out[i] = prefix
        prefix *=arr[i]
    postfix =1
    for i in range(len(arr)-1, -1, -1):
        out[i] *=postfix
        postfix *=arr[i]
    return out

#Postfix and prefix calculations are used as solution

arr=[1,2,3,4]
print(productArray(arr))
