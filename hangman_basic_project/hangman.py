import random
import csv

with open('./hangman_basic_project/vocab.csv') as file:
    reader = csv.reader(file)
    words = list(reader)

ranWords = words

vocabu = random.choice(ranWords)


def hangman():
    if __name__ == '__main__':
        print("Welcome to the Hangman Game")
        print("You have to guess the word in 10 attempts")
        print("Let's start the game")
        print("The word is of length: ", len(vocabu[0]))

        word = vocabu[0]
        word = word.lower()
        word = list(word)

        guess = ['_']*len(word)
        print(' '.join(guess))

        attempts = 10
        while attempts > 0:
            print(f'You have {attempts} attempts left')
            letter = input('Enter your guess: ')
            letter = letter.lower()

            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        guess[i] = letter
                print(' '.join(guess))
            else:
                print(' '.join(guess))
                print('Oops! Wrong guess')
                attempts -= 1

            if '_' not in guess:
                print('Congratulations! You have guessed the word correctly')
                break
            
            

        if '_' in guess:
            print('Oops! You have exhausted all your attempts')
            print('The word was: ', ''.join(word))
            print('Better luck next time')
            
            tryagin = input('do you want to play again: y/n: ')
            if tryagin == 'y':
                hangman()
            elif tryagin == 'n':
                print('Thank you for playing the game')
                exit()
             
           
hangman()
        
      

        
            
        
    

