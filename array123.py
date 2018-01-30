# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere


def array123(num):

    for i in range(0, len(num) - 2):
        if [1, 2, 3] == num[i: i + 3]:
            return True
        else :
            return False

array123([1, 2, 1, 2, 5, 5])
array123([1, 1, 2, 3, 1]) 
array123([1, 1, 2, 4, 1]) 
array123([1, 1, 2, 1, 2, 3]) 