from timeit import default_timer as timer

start = timer()

a=0
b=1
n=int(input("Enter the number of terms needed : "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1

end = timer()

print("\nTime elapsed : ", end-start)