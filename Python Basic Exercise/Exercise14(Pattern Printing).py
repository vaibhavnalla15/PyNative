# Pattern Printing in Python:-

print("Print a downward half-pyramid pattern of stars:- ")
rows = 5
for i in range(rows + 1, 0, -1):
    for j in range(0 , i - 1):
        print("*" , end=" ")
    print()
print()

print("Right triangle pyramid of Stars:-")
rows = 5
k = 2 * rows -2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("*", end=" ")
    print()
print()

print("Pyramid pattern of stars in python")
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

print("Number Patterns Programs In Python")
rows = 6
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=" ")
    # new line after each row
    print()
print()

print("Inverted pyramid pattern of numbers")
rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
print()

print("Pyramid pattern of numbers")
# In each row, every next number is incremented by 1.
rows = 6
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()

print("Inverted Pyramid pattern with the same digit")
rows  = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=" ")
    print()
print()

print("Reverse number pattern")
rows = 5
# revers loop
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=" ")
    print()
print()

print("Number triangle pattern")
rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0 , -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(num, end=" ")
            num += 1
    print()
print()

print("Square pattern with numbers")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1 ):
        if j <= i:
            print(i, end=" ")
        else:
            print(j, end=" ")
    print()

print("Print the reverse number pattern")
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
