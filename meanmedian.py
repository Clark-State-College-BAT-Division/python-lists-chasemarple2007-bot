#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class


myNumbers = [0,0,0,0,0]

for i in range(5):
  myNumbers[i] = int(input("Enter a number: "))

print(myNumbers)
myNumbers.sort()
print(myNumbers)
myNumbers.sort(reverse=True)
print(myNumbers)

sum = 0
for i in range(5):
  sum += myNumbers[i]

average = sum / 5

print(f"The mean is {average} and the median is {myNumbers[2]}")
