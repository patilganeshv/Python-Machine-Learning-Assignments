def ChkPrime(no):
    flag = False
    for i in range(2, no):
        if (no % i) == 0:
            flag = True
            break
    
    if flag:
        return False
    else:
        return True 