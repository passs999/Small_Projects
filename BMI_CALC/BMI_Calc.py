import time

print(5 * '_--_', "Bmi Calculator", 5 * '_--_', '\n')

def calculate_bmi():
    try:
        mass = float(input("Enter your mass example-->( kg 65 ): "))
        height = float(input("Enter your height in example-->( m 1.80 ): "))
    
        height2 = height ** 2
        bmi = mass / height2
        bmi_round = (round(bmi, 2))
        print("Your bmi is ", bmi_round)

        if bmi <= 18.5:
            print("It's underweight")
        elif bmi >= 18.5 and bmi <= 25 :
            print("It's normal")
        elif bmi > 25:
            print("It's overweight ")
            if bmi >= 35:
                time.sleep (1)
                print("and you are")
                time.sleep (2)
                print("fat pig")
                time.sleep (0.5)
                quit()
        else:
            print("Error")
        time.sleep(1.5)
        restart = input("One more time y/n: ")
        if restart == "y":
            calculate_bmi()
        else:
            quit()
        
    except ValueError:
        print(50 * "-")
        print("Error")
        print(50 * "-")
        calculate_bmi()


calculate_bmi()

