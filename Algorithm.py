n = int(input())

def weird(n):
    
    string = str(n)
    
    while n != 1:
        if n%2 == 0:
            n = n//2
            string += ' ' + str(n)
        else:
            n = n*3 + 1
            string += ' ' + str(n)
    
    
    return string

print(weird(n))