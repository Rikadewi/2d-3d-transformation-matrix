import algeo2d
import algeo3d


print(" _     _                         _____                    __                           _   _             ")
print("| |   (_)                       |_   _|                  / _|                         | | (_)            ")
print("| |    _ _ __   ___  __ _ _ __    | |_ __ __ _ _ __  ___| |_ ___  _ __ _ __ ___   __ _| |_ _  ___  _ __  ")
print("| |   | | '_ \ / _ \/ _` | '__|   | | '__/ _` | '_ \/ __|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \ ")
print("| |___| | | | |  __/ (_| | |      | | | | (_| | | | \__ \ || (_) | |  | | | | | | (_| | |_| | (_) | | | |")
print("\_____/_|_| |_|\___|\__,_|_|      \_/_|  \__,_|_| |_|___/_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|")
print("                                                                                                         ")
print("                                                                                                         ")

valid = False
while not(valid):
	valid = True
	print("DIPILIH YAA!")
	print("1. 2 Dimensi")
	print("2. 3 Dimensi")
	pilihan = int(input("Your Choice: "))

	if (pilihan == 1):
		algeo2d.main2d()
	elif (pilihan == 2):
		algeo3d.main3d()
	else:
		valid = False
		print("input tidak valid\n")

