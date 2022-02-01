import random

def Leg_Start(player1, player2):
	global first_throw, start_score, player1_score, player2_score
	player1_score, player2_score = start_score, start_score

	print("\nScoreboard: "+  player1 + " " + str(player1_legs) + " - " + str(player2_legs) + " " + player2)
	print("\n>>> " + first_throw + " throws first. <<<\n")

	Leg()

	if first_throw == player1:
		first_throw = player2
	else:
		first_throw = player1


def Leg():
	global throw, leg_finished
	throw = first_throw
	leg_finished = False

	while leg_finished == False:
		Throw()
		if throw == player1:
			throw = player2
		else:
			throw = player1


def Throw():
	global player1_score, player2_score, player1_legs, player2_legs, checkout_dict, throw1, throw2, throw3, int_throw1, int_throw2, int_throw3, leg_finished
	bust = False
	temp_score = 0

	print(">>> " + throw + " to throw. <<<\n")

	if throw == player1 and player1_score <= 170:
		temp_score = player1_score
		print(">>> " + throw + ", you require " + str(player1_score) + " <<<")
		print("Possible checkout: " + checkout_dict[str(player1_score)] + "\n")

		throw1 = input("Throw 1 score: ")
		doublesTriples(throw1, 1)

		if (temp_score - int_throw1) == 0 and ("D" in throw1 or throw1 == "50"):
			leg_finished = True
		elif (temp_score - int_throw1) == 1 or (temp_score - int_throw1 < 0) or ((temp_score - int_throw1) == 0 and "D" not in throw1):
			bust = True
		else:
			temp_score -= int_throw1
			throw2 = input("Throw 2 score: ")
			doublesTriples(throw2, 2)
			
			if (temp_score - int_throw2) == 0 and ("D" in throw2 or throw2 == "50"):
				leg_finished = True
			elif (temp_score - int_throw2) == 1 or (temp_score - int_throw2 < 0) or ((temp_score - int_throw2) == 0 and "D" not in throw2):
				bust = True
			else:
				temp_score -= int_throw2
				
				throw3 = input("Throw 3 score: ")
				doublesTriples(throw3, 3)

				if (temp_score - int_throw3) == 0 and ("D" in throw3 or throw3 == "50"):
					leg_finished = True
				elif (temp_score - int_throw3) == 1 or (temp_score - int_throw3 < 0) or ((temp_score - int_throw3) == 0 and "D" not in throw3):
					bust = True
	elif throw == player2 and player2_score <= 170:
		temp_score = player2_score
		print(">>> " + throw + ", you require " + str(player2_score) + " <<<")
		print("Possible checkout: " + checkout_dict[str(player2_score)] + "\n")

		throw1 = input("Throw 1 score: ")
		doublesTriples(throw1, 1)

		if (temp_score - int_throw1) == 0 and ("D" in throw1 or throw1 == "50"):
			leg_finished = True
		elif (temp_score - int_throw1) == 1 or (temp_score - int_throw1 < 0) or ((temp_score - int_throw1) == 0 and "D" not in throw1):
			bust = True
		else:
			temp_score -= int_throw1
			throw2 = input("Throw 2 score: ")
			doublesTriples(throw2, 2)
			
			if (temp_score - int_throw2) == 0 and ("D" in throw2 or throw2 == "50"):
				leg_finished = True
			elif (temp_score - int_throw2) == 1 or (temp_score - int_throw2 < 0) or ((temp_score - int_throw2) == 0 and "D" not in throw2):
				bust = True
			else:
				temp_score -= int_throw2
				throw3 = input("Throw 3 score: ")
				doublesTriples(throw3, 3)

				if (temp_score - int_throw3) == 0 and ("D" in throw3 or throw3 == "50"):
					leg_finished = True
				elif (temp_score - int_throw3) == 1 or (temp_score - int_throw3 < 0) or ((temp_score - int_throw3) == 0 and "D" not in throw3):
					bust = True
	else:
		throw1 = input("Throw 1 score: ")
		doublesTriples(throw1, 1)

		if throw == player1:
			temp_score = player1_score
			if (temp_score - int_throw1) < 2:
				bust = True
			else:
				temp_score -= int_throw1
				throw2 = input("Throw 2 score: ")
				doublesTriples(throw2, 2)

				if (temp_score - int_throw2) < 2:
					bust = True
				else:
					temp_score -= int_throw2
					throw3 = input("Throw 3 score: ")
					doublesTriples(throw3, 3)

					if (temp_score - int_throw3) < 2:
						bust = True
		else:
			temp_score = player2_score

			if (temp_score - int_throw1) == 1 or (temp_score - int_throw1 < 0):
				bust = True
			else:
				temp_score -= int_throw1
				throw2 = input("Throw 2 score: ")
				doublesTriples(throw2, 2)

				if (temp_score - int_throw2) == 1 or (temp_score - int_throw2 < 0):
					bust = True
				else:
					temp_score -= int_throw2
					throw3 = input("Throw 3 score: ")
					doublesTriples(throw3, 3)

					if (temp_score - int_throw3) == 1 or (temp_score - int_throw3 < 0):
						bust = True

	if bust == True:
		print("\n!!! No score !!!\n")
		tot_score = 0
	elif leg_finished == True:
		print("\n!!! " + throw + " wins the leg !!!\n")
		if throw == player1:
			player1_legs += 1
		else:
			player2_legs += 1
	else:
		tot_score = sum((int_throw1, int_throw2, int_throw3))
		print("\n!!! " + str(tot_score) + " !!!\n")
		if throw == player1:
			player1_score -= tot_score
		else:
			player2_score -= tot_score

def doublesTriples(throw, count):
	global throw1, throw2, throw3, int_throw1, int_throw2, int_throw3

	if "D" in throw:
		if count == 1:
			int_throw1 = 2 * int(throw1[1:])
			return int_throw1
		elif count == 2:
			int_throw2 = 2 * int(throw2[1:])
			return int_throw2
		elif count == 3:
			int_throw3 = 2 * int(throw3[1:])
			return int_throw3
	elif "T" in throw:
		if count == 1:
			int_throw1 = 3 * int(throw1[1:])
			return int_throw1
		elif count == 2:
			int_throw2 = 3 * int(throw2[1:])
			return int_throw2
		elif count == 3:
			int_throw3 = 3 * int(throw3[1:])
			return int_throw3
	else:
		if count == 1:
			int_throw1 = int(throw1)
			return int_throw1
		elif count == 2:
			int_throw2 = int(throw2)
			return int_throw2
		elif count == 3:
			int_throw3 = int(throw3)
			return int_throw3

print("\nDarts Match Program")
print("-" * 19 + "\n")

checkout_dict = {}
with open("checkouts.txt", 'r') as checkouts:
	for line in checkouts:
		a = line.rstrip('\n')
		a = a.split(": ")
		checkout_dict[a[0]] = a[1]

player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")
start_score = int(input("Starting score: "))
best_of_legs = int(input("Best of how many legs: "))
first_throw = random.choice([player1, player2])

throw = "" 
throw1, throw2, throw3 = "", "", ""
int_throw1, int_throw2, int_throw3 = 0, 0, 0
player1_score, player2_score = start_score, start_score
player1_legs, player2_legs = 0, 0
match_finished, leg_finished = False, False

while match_finished == False:
	if player1_legs == best_of_legs / 2 + 0.5:
		match_finished = True
	elif player2_legs == best_of_legs / 2 + 0.5:
		match_finished = True
	else:
		Leg_Start(player1, player2)

if player1_legs > player2_legs:
	print(player1 + " Wins!")
else:
	print(player2 + " Wins!")