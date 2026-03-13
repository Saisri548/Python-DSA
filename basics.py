# =============================
# Python Basics: Variables, Operators, Loops, and If-Else
# =============================

# -----------------------------
# 1️⃣ Variable Declaration & Assignment
# -----------------------------
a = 100
b = 12.5
c = "Python"

# Multiple assignment
a1, b1 = 100, 10
c1, d1 = 100, 90

print("Initial values:")
print("a1 =", a1, "b1 =", b1, "c1 =", c1, "d1 =", d1)

# -----------------------------
# 2️⃣ Swapping Variables
# -----------------------------
a1, b1 = b1, a1
print("\nAfter swapping a1 and b1:")
print("a1 =", a1, "b1 =", b1, "c1 =", c1, "d1 =", d1)

# -----------------------------
# 3️⃣ Arithmetic Operations
# -----------------------------
a2, b2, c2, d2 = 20, 30, 40, 50

sum_a2b2 = a2 + b2
diff_a2b2 = b2 - a2
mul_a2c2 = a2 * c2
div_a2b2 = a2 / b2
floor_div_a2b2 = a2 // b2

print("\nArithmetic Operations:")
print("Sum:", sum_a2b2)
print("Difference:", diff_a2b2)
print("Product:", mul_a2c2)
print("Division (float):", div_a2b2)
print("Floor Division:", floor_div_a2b2)

# -----------------------------
# 4️⃣ Logical Operators
# -----------------------------
x = True
y = False

print("\nLogical Operators:")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
print("not y:", not y)

# -----------------------------
# 5️⃣ Assignment Operators
# -----------------------------
print("\nAssignment Operators:")
a = 4
b = 5
a += 2
print("a += 2 →", a)
a *= 3
print("a *= 3 →", a)
a -= 3
print("a -= 3 →", a)
a /= 3
print("a /= 3 →", a)
a **= 2
print("a **= 2 →", a)

# -----------------------------
# 6️⃣ If-Else Statements
# -----------------------------
# Even or Odd
num = int(input("\nEnter a number for Even/Odd check: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# Positive, Negative, Zero
num1 = int(input("Enter a number for Positive/Negative check: "))
if num1 > 0:
    print("Positive")
elif num1 == 0:
    print("Zero")
else:
    print("Negative")

# Grading System
marks = int(input("Enter marks for grading system: "))
if marks >= 90:
    print("A GRADE")
elif 75 < marks < 90:
    print("B GRADE")
elif 50 < marks <= 75:
    print("C GRADE")
else:
    print("F GRADE")

# -----------------------------
# 7️⃣ For Loops
# -----------------------------
print("\nFor loop - range 5 to 9:")
for i in range(5, 10):
    print(i)

# For loop over a string
word = "Python"
print("\nFor loop over string:")
for ch in word:
    print(ch, end=" ")
print()  # for newline

# -----------------------------
# 8️⃣ While Loop
# -----------------------------
print("\nWhile loop - print 1 to 5:")
i = 1
while i <= 5:
    print(i)
    i += 1

# -----------------------------
# 9️⃣ Loop Control Statements
# -----------------------------
print("\nFor loop with continue (skip i >= 5):")
for i in range(1, 10):
    if i >= 5:
        continue
    else:
        print(i)