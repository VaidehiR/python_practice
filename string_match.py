# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


def string_match(a , b) :
    count = 0
    for i in range(0, len(a) -1):
        for j in range(0 ,  len(b) - 1):
            if a[i : i+2] == b[j : j+2]:
                count = count+1

    print(count)

string_match('bcf' , 'aabrrcbcet')
string_match('xxcaazz', 'xxbaaz')
string_match('abc', 'abc')
string_match('abc', 'axc') 