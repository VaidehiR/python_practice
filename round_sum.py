# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 time

def round10(num) :
    rightmost_digit = num%10
    if rightmost_digit < 5 :
        return num - rightmost_digit
    else :
        return 10 - rightmost_digit + num

def round_sum(a , b , c) :
    print(round10(a) + round10(b) + round10(c))   


round_sum(16, 17, 18) 
round_sum(12, 13, 14) 
round_sum(4, 4, 4)
round_sum(6, 4, 4)
round_sum(322 , 343 , 2345) 