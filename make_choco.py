# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

def make_choco(list) :
    choco = sum(list)%5
    if choco == 0 :
        print(-1)
    else :
        print(choco)

make_choco((4 , 5 , 7))
make_choco((4 , 1 , 9))
make_choco((4 , 1 , 10))
make_choco((4 , 1 , 7))