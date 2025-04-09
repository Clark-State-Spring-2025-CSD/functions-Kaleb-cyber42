#This is a teacher led demo.
#Watch this video or follow along in class.


def AddTwoNumber(number1, number2):
    result = number1 + number2
    return result

def HelloTen():
    for _ in range(10):
        print("Hello!")


def CheckHit(hitTarget, diceRoll):
    result = False
    if diceRoll >= hitTarget:
        print("That is a hit!")
        return True
    else:
        print("That is a miss!")
        return False
    return result 

x = 5
y = 10

result = AddTwoNumber(x,y)

HelloTen()

print(result)

print(CheckHit(5,10))
print()
print(CheckHit(10,5))