a = int(input("enter the first term"))
r = int(input ("enter the ratio "))
n = int(input("enter the number"))
for i in range (1,n+1) :
    n_term = a*r**(n-1)
print(n_term)

for i in range (1,n+1) :
    if r > 1 :
        sum_nums = (a -(r**(n-1) - 1 ))/(r - 1)
    elif r < 1 :  
        sum_nums = (a - (1 - (r**(n-1))))/(1 - r)
print(sum_nums)
