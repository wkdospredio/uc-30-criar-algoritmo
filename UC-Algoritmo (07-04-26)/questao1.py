P = int(input("Dê a quantidade de P: "))
D = int(input("Dê a quantidade de D: "))
B = int(input("Dê a quantidade de B: "))

total = P*1 + D*2 + B*3 

if total >= 150:
    print("B") 
elif total >= 120:
    print("D")
elif total >= 100:
    print("P")
else:
    print("N")