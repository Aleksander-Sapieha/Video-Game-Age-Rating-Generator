import sys
import os

def get_rating():
    print("Video Game Age Rating Generator")
    print("Answer the following questions:")
    
    # Questions
    violence = int(input("Rate the level of violence (0: None, 1: Mild, 2: Strong, 3: Extreme): "))
    language = int(input("Does the game include strong language? (0: No, 1: Mild, 2: Profanity): "))
    drugs = int(input("Are there references to drugs or alcohol? (0: No, 1: Yes): "))
    sexual_content = int(input("Rate sexual content (0: None, 1: Mild, 2: Strong): "))
    if sexual_content == 2:
        sexual_content = 16
    online = int(input("Does the game allow online interactions? (0: No, 1: Yes): "))
    gambling = int(input("Does the game contain gambling? (0: No, 1: Yes, but with play money, 2: Yes, with real money): "))
    if gambling == 2:
        gambling = 16
    discrimination = int(input("Rate discriminatory content (0: None, 1: Use of racist/homophobic jokes, 2: Genocide with racist/homophobic background): "))
    if discrimination == 2:
        discrimination = 16

    # Score calculation
    score = violence * 3 + language * 2 + drugs * 4 + sexual_content * 6 + online * 1 + gambling * 4 + discrimination * 6
    
    # Determine rating
    if score <= 0:
        rating = "0"
    elif score <= 3:
        rating = "3"
    elif score <= 5:
        rating = "7"
    elif score <= 10:
        rating = "13"
    elif score <= 15:
        rating = "16"
    else:
        rating = "18"
    
    print(f"\nThe recommended age rating for your game is: {rating}")

def main():
    get_rating()
    os.system("PAUSE")
    sys.exit

# Run the rating generator
if __name__ == "__main__":
    main()
