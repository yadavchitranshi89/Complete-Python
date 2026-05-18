
# PYTHON TYPE CASTING / TYPE CONVERSION

# IMPLICIT TYPE CASTING
a = 10
b = 5.5
c = a + b
print(c)
print(type(c))


# EXPLICIT TYPE CASTING
# int() TYPE CONVERSION

# float to int
pi = 3.14
print(type(pi))
num = int(pi)
print("Integer number:", num)
print(type(num))


# bool to int
flag_true = True
flag_false = False
print(type(flag_true))
num1 = int(flag_true)
num2 = int(flag_false)
print("Integer number 1:", num1)
print(type(num1))
print("Integer number 2:", num2)
print(type(num2))


# string to int
string_num = "225"
print(type(string_num))
num3 = int(string_num)
print("Integer number 3:", num3)
print(type(num3))


# invalid string to int
# string_num2 = "Score is 25"
# num4 = int(string_num2)

# float() TYPE CONVERSION

# int to float
num = 725
print(type(num))
num1 = float(num)
print("Float number:", num1)
print(type(num1))


# bool to float
flag_true = True
flag_false = False
print(type(flag_true))
num2 = float(flag_true)
num3 = float(flag_false)
print("Float number 1:", num2)
print(type(num2))
print("Float number 2:", num3)
print(type(num3))


# string to float
string_num = "725.535"
print(type(string_num))
num4 = float(string_num)
print("Float number:", num4)
print(type(num4))


# complex() TYPE CONVERSION

# int to complex(x)
r_num = 135
print(type(r_num))
c_num = complex(r_num)
print("Complex number:", c_num)
print(type(c_num))


# int to complex(x, y)
r_num = 135
i_num = 235
c_num2 = complex(r_num, i_num)
print("Complex number:", c_num2)
print(type(c_num2))

# float to complex(x)
r_num = 53.250
print(type(r_num))
c_num3 = complex(r_num)
print("Complex number:", c_num3)
print(type(c_num3))


# float to complex(x, y)
r_num = 53.250
i_num2 = 350.750
c_num4 = complex(r_num, i_num2)
print("Complex number:", c_num4)
print(type(c_num4))


# bool to complex(x)
boolean_true = True
print(type(boolean_true))
c_num5 = complex(boolean_true)
print("Complex number:", c_num5)
print(type(c_num5))


# bool to complex(x, y)
r_bool = False
i_bool = True
c_num6 = complex(r_bool, i_bool)
print("Complex number:", c_num6)
print(type(c_num6))


# bool() TYPE CONVERSION

# int to bool
num1 = 10
num2 = 0
print(type(num1))
b1 = bool(num1)
b2 = bool(num2)
print(b1)
print(b2)
print(type(b1))


# float to bool
f_num1 = 25.35
f_num2 = 0.0
print(type(f_num1))
b3 = bool(f_num1)
b4 = bool(f_num2)
print(b3)
print(b4)
print(type(b3))


# string to bool
s1 = "False"
s2 = "True"
s3 = "812"
s4 = ""
print(type(s1))
b5 = bool(s1)
b6 = bool(s2)
b7 = bool(s3)
b8 = bool(s4)
print(b5)
print(b6)
print(b7)
print(b8)
print(type(b5))


# complex to bool
c1 = 33 + 9j
c2 = 0 + 0j
print(type(c1))
b9 = bool(c1)
b10 = bool(c2)
print(b9)
print(b10)
print(type(b9))


# str() TYPE CONVERSION

# int to str
num = 15
print(type(num))
s1 = str(num)
print(s1)
print(type(s1))

# float to str
num = 75.35
print(type(num))
s2 = str(num)
print(s2)
print(type(s2))

# complex to str
complex_num = 15 + 5j
print(type(complex_num))
s3 = str(complex_num)
print(s3)
print(type(s3))


# bool to str
b1 = True
b2 = False
print(type(b1))
s4 = str(b1)
s5 = str(b2)
print(s4)
print(s5)
print(type(s4))



# input() function

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)


a = input("Enter first number: ")
b = input("Enter second number: ")
print(a + b)

b1 = input("Enter name: ")
print(b1)
