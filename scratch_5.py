# Exercice 4
# Write a program that calculates the Fibonacci sequence.

# function who create the Fibonacci sequence
def FibonacciSequence():
    t1, t2 = 0, 1
    while t2 <= 1000000:
        print(t1)
        A = t1 + t2
        t1 = t2
        t2 = A

FibonacciSequence()
