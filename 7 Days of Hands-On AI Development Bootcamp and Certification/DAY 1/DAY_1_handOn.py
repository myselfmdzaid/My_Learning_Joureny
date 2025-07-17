# Read a txt file with multiple lines of numbers 
with open(r"D:/MY PERSONAL/Zaid Learnings/My_Learning_Journey/7 Days of Hands-On AI Development Bootcamp and Certification\DAY 1/Numbers.txt", 'r') as file:
    numbers = file.readlines()

# Process the data by converting each number to its Square
Square_numbers = [str(int(num.strip()) ** 2) + "\n" for num in numbers]

# Write the output to another file 
with open(r"D:/MY PERSONAL/Zaid Learnings/My_Learning_Journey/7 Days of Hands-On AI Development Bootcamp and Certification\DAY 1/Output File.txt", 'w') as file:
    file.writelines(Square_numbers)