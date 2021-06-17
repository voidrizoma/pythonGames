import random 

guessesTaken = 0

print("Hola crayola.... ¿Cómo te llamas?")
myName = input()

number = random.randint(1,20)
print("Hola" + myName + "Adivina el número en el que estoy pensando")

while guessesTaken < 6:
    print("date con un número")
    guess = input()
    guess = int(guess)
    
    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print("ay no!..... es un número más alto")
              
    if guess > number:
        print("estás muy muy arriba, ve más abajo")
    
    if guess == number:
        break
        
if guess == number:
    guessesTaken = str(guessesTaken)
    print("Esoooo" + myName + "es el bueno")
    
if guess != number:
    number = str(number)
    print("nope! ese no es. Estuve pensando en" + number)
    