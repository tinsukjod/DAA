from timeit import default_timer as timer

start = timer()

def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))

a = int(input("Enter number of elements in Fionacci Series : "))

for i in range(a):
    print(fib(i), end = " ")

end = timer()

print("\nTime Elapsed : ", end-start)