#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

# Create two lists with 10 random numbers between 1 and 50
player_one = [random.randint(1, 50) for _ in range(10)]
player_two = [random.randint(1, 50) for _ in range(10)]

# Keep track of wins
p1_wins = 0
p2_wins = 0

# Compare the lists in order
for i in range(10):
    if player_one[i] > player_two[i]:
        p1_wins += 1
    elif player_two[i] > player_one[i]:
        p2_wins += 1
    # Ties are ignored

# Find highest and lowest values and their first index
p1_high = max(player_one)
p1_high_index = player_one.index(p1_high)
p1_low = min(player_one)
p1_low_index = player_one.index(p1_low)

p2_high = max(player_two)
p2_high_index = player_two.index(p2_high)
p2_low = min(player_two)
p2_low_index = player_two.index(p2_low)

# Display results
print("Player One =", player_one)
print("Player Two =", player_two)

print(f"Player one won {p1_wins} times")
print(f"Player two won {p2_wins} times")

print(f"Player one's highest number is {p1_high} at index {p1_high_index}")
print(f"Player two's highest number is {p2_high} at index {p2_high_index}")
print(f"Player one's lowest number is {p1_low} at index {p1_low_index}")
print(f"Player two's lowest number is {p2_low} at index {p2_low_index}")
