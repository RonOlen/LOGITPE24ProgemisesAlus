num1 = float(input("Sisesta esimene number: "))
matapask = input("Sisesta (+, -, *, /): ")
num2 = float(input("Sisesta teine number: "))


if matapask == "+":
    mata = num1 + num2
    print("Tulemus on:", mata)
elif matapask == "-":
    mata = num1 - num2
    print("Tulemus on:", mata)
elif matapask == "*":
    mata = num1 * num2
    print("Tulemus on:", mata)
elif matapask == "/":
    if num2 != 0:
        mata = num1 / num2
        print("Tulemus on:", mata)
    else:
        print("Pole voimalik bro!")
else:
    print("nii ei saa teha, oled mata tunnis kainud vahepeal ?")
