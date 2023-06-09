print("Welcome to my computer quiz!")

# ask user if they want to play a game, if no, quit code
playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("Okay!, Let's play!")
score = 0

# sequence a number of questions and make all inputs lower case
answer = input("\nWhat does CPU stand for? ")

if answer.lower() == 'central processing unit':
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("\nWhat does GPU stand for? ")

if answer.lower() == 'graphics processing unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat does RAM stand for? ")

if answer.lower() == 'random access memory':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat does PSU stand for? ")

if answer.lower() == 'power supply':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# display the score and correct answers percentage
print(f"\nYou've got {str(score)} questions correct!")
print(f"You've got {str(score/4 * 100)}%")