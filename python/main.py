"""
Write an algorithm for a program that asks a game's user to choose their level: 1-6. 
If they choose outside that, display an error message, otherwise display something like,
"Level 5" (whatever level they chose).
"""

# Get user level between 1-6
user_level = int(input("Enter your level between 1-6: "))

# Use indefinite loop as number of trials is unknown

while user_level not in range(1, 7):
    print("Error: Level must be between 1-6")
    user_level = int(input("Enter your level between 1-6: "))
print(f"Level {user_level}") 