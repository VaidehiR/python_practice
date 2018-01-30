# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

def arr(list):
    if len(list) == 0 :
        print(0)
    elif len(list) < 2:
        print(list[0])
    else:
        print(list[0] + list[1])


arr([1 , 3, 4])
arr([])
arr([2])
arr([1,1])
arr(('2'))
arr((2,))