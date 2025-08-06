import random

#Word list
word_list = ["apple", "banana", "cherry", "grape", "mango", "peach", "orange"]

print("🔎 Welcome to the Word Guessing Game!")

while True:
     secret_word = random.choice(word_list)
     attempts = 0

     print("\nI'm thinking of a fruit...🍓")
     print(f"Hint: The word starts with '{secret_word[0]}' and is {len(secret_word)} letters long.")

     while True:
         guess = input("Enter your guess: ").lower()
         attempts += 1

         if guess == secret_word:
             print(f"🎉 Correct! You guessed it in {attempts} tries!")
             break
         else:
             print("❌ Nope, try aggain.")

     play_again = input("Do you want to play again? (yes/no): ").lower()
     if play_again != "yes":
         print("Thanks for playing! 👋🏻")
         break 
     
