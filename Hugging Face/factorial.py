# example 1
print(1*2*3*4*5)




# example 2
fact = 5
ans = 1
for f in range(1, fact+1):
    ans *= f
print(ans)




# example 3
def recursive_fact(n):
    if n == 0:
        return 1
    else:
        print(f"{n} *" , end=" ")
        return n * recursive_fact(n-1)
recursive_fact(5)
