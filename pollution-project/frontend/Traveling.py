import random 

def main():
	Health = 100
	travel_cnt = 0
	while(travel_cnt < 10):
		if(Health < 0):
			print("You died of hunger and the toxic air around you")
			print("Air pollution heavily influence lives of all of us, be mindful of it!")
			return
		air_quality = random.randint(50,250)
		failed_chance = ((air_quality)-50)/2
		while(True):
			move = input("What to do now? type 1 for hunt, 2 for travel")
			if(int(move) == 1):
				if (random.randint(0,100) < failed_chance):
					print("Hunt successful! Gain 5 health!")
					Health = (Health+5)%100
				break
			elif(int(move) == 2):
				if (air_quality> 50):
					print("You felt hard to breath as you travel :(")
					Health -= int((air_quality-80)/5)
					print("Current health:",Health)
				travel_cnt += 1
				break
			else: 
				print('invalid output!')
	print("You arrived your destination to breed your offspring!")
	print("Air pollution heavily influence lives of all of us, be mindful of it!")

main()