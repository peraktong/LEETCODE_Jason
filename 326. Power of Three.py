"""


def three(num):
    res=0
    while num>2:
        res = num % 3
        num = (num - res) / 3+res
    if res==0:
        return True
    else:
        return False


"""
def three(num):


    while num%3==0:
        num=num/3

    if num==0:
        return True
    elif num==1:
        return True
    else:
        return False




print(three(num=9))
