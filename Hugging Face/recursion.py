# defining functions

def recursive_add(x,y):
    ans = x+y
    return ans

def recursive_fact(n):
    if n == 0:
        return 1
    else:
        print(f"{n} *" , end=" ")
        return n * recursive_fact(n-1)






# calling functions
output = recursive_fact(6)
print(output)
