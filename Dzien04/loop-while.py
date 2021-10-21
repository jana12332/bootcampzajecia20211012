"""
 Pętla while

"""
counter = 10
while counter>0:
    print(f"counter={counter}")
    counter -= 1 #counter = counter - 1
    if counter==5:
        break

print("już po pętli...")

# Pętla while "nieskonczona" , prosimy usera o podanie liczny która jest >=100 lub <10
while True:
    value = int(input("Podaj liczbę >=100 lub <10:"))
    if value>=100 or value<10:
        print(f"Podałeś {value}")
        break
