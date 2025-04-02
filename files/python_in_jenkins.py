import sys

print(sys.argv)
num = int(sys.argv[1])

print(f"Original number is : {num}")
print(f"Binary representation of {num} is : {bin(num)}")
print(f"Octal representation of {num} is : {oct(num)}")
print(f"Hexadecimal representation of {num} is : {hex(num)}")
print(f"Complex representation of {num} is : {complex(num)}")
