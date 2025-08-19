total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:   
        break
    
    if 40 < num < 100:   
        total += num

print("Sum of valid inputs =", total)
