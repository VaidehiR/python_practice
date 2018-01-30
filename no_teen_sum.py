# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 

def fix_teen(n) :
    teen_list = (13 , 14 , 16 , 17 , 18 , 19)
    if n in teen_list :
        return 0

    else :
        return n

def no_teen_sum (a , b, c):

    print(fix_teen(a) + fix_teen(b) + fix_teen(c))

no_teen_sum(14 , 5, 6)
no_teen_sum(2, 1, 14)
no_teen_sum(15, 1, 19)
no_teen_sum(2, 0, 16)
no_teen_sum(13, 19, 14) 