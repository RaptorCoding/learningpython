RESULT = 0
print("Please input numbers: ")
print("1.ADD")
print("2.SUBSTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
VALUEA = input("awaiting...")
print(VALUEA)

if int(VALUEA) == 1:
    print("Loading...")
elif int(VALUEA) == 2:
    print("Loading...")
elif int(VALUEA) == 3:
    print("Loading...")
elif int(VALUEA) == 4:
    print("Loading...")
else:
    print("Error : Input invalid")

VALUEB = input("1# Input awaiting...")
VALUEC = input("2# Input awaiting...")

if int(VALUEA) == 1:
    RESULT = (int(VALUEB) + int(VALUEC))
elif int(VALUEA) == 2:
    RESULT = (int(VALUEB) - int(VALUEC))
elif int(VALUEA) == 3:
    RESULT = (int(VALUEB) * int(VALUEC))
elif int(VALUEA) == 4:
    RESULT = (int(VALUEB) / int(VALUEC))

else:
    print("Error: Invalid operation")
    
print(RESULT)