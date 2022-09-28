print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("see you later!")
    quit()
else:
    print("Okay let´s go! :)")

answer = input("Wer hat dieses Spiel programmiert? ")
if answer.lower() == "irfan":
    print("Richtig! :)")
else:
    print("LEIDER FALSCH :(")

answer = input("Wie heißt seine Frau? ")
if answer.lower() == "rana":
    print("Richtig! :)")
else:
    print("LEIDER FALSCH :(")

answer = input("Wie heißen seine eltern? ")
if answer.lower() == "fatma und olcay":
    print("Richtig! :)")
else:
    print("LEIDER FALSCH :(")

answer = input("Wie heißen seine Geschwister? ")
if answer.lower() == "emirhan, azra und zümra":
    print("DU HAST DAS SPIEL DURCHGESPIELT! GRATULATION! :)")
else:
    print("LEIDER FALSCH :(")