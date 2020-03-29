import re

print("welcome to the magic calculator")
print("type 'quit' to exit")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
         equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("GoodBye Hooman")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        print("result", previous)
while run:
    performMath()
