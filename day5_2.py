def countdown_loop(n):
    for i in range(n, -1, -1):
        if i == 0:
            print("boom")
        else:
            print(i)

def countdown_recursion(n):
    if n < 0:
        return
    if n == 0:
        print("boom")
    else:
        print(n)
    countdown_recursion(n-1)

n = int(input("enter an integer\n"))

print("loop")
countdown_loop(n)

print("\nrecursion")
countdown_recursion(n)