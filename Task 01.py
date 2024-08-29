# Design a text-based Hangman game. The program selects a random word, and the player guesses one
# letter at a time to uncover the word. You can set a limit on the number of incorrect guesses allowed.

import tkinter as tk
import random


class Hangaman:
    def __init__(self, word):
        self.word = word.lower()
        self.guesses = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 5
        self.root = tk.Tk()
        self.root.title('Hangaman')
        self.root.geometry('350x300')
        self.root.resizable(False, False)
        self.root.configure(background='silver')

        self.message = tk.Label(self.root, text='Welcome to Hangaman Game', font=("Times New Roman", 14))
        self.message.pack(padx=10, pady=10)
        self.label1 = tk.Label(self.root, text='', font=("Times New Roman", 16))
        self.label1.pack(padx=10, pady=10)
        self.entry1 = tk.Entry(self.root, font=("Times New Roman", 14))
        self.entry1.pack(padx=10, pady=10)
        self.guess_button = tk.Button(self.root, text="Guess", font=("Times New Roman", 14), bg='light grey',
                                      fg="black", command=self.process_guess)
        self.guess_button.pack(padx=10, pady=10)
        self.quit_button = tk.Button(self.root, text='Quit', font=("Times New Roman", 14), bg="light grey",
                                     command=self.root.destroy)
        self.quit_button.pack(padx=10, pady=10)
        self.start_game()

    def start_game(self):
        self.guesses = []
        self.incorrect_guesses = 0
        self.update_display()
        self.message.config(text='Welcome to Hangaman Game!')

    def process_guess(self):
        guess = self.entry1.get().lower()
        self.entry1.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.message.config(text='Please enter a single alphabetic letter!')
            return

        if guess in self.guesses:
            self.message.config(text='You already guessed that letter!')
            return

        if guess in self.word:
            self.guesses.append(guess)
            self.update_display()
            if self.check_winner():
                self.message.config(text='Congratulations! You won!')
                self.root.after(2000, self.root.destroy)
                return
        else:
            self.guesses.append(guess)
            self.incorrect_guesses += 1
            guesses_left = self.max_incorrect_guesses - self.incorrect_guesses
            if guesses_left > 0:
                self.message.config(text=f'Incorrect guess! You have {guesses_left} guesses left.')
            else:
                self.message.config(text=f"Sorry, You lose! The word was {self.word}.")
                self.root.after(2000, self.root.destroy)

    def check_winner(self):
        return all(letter in self.guesses for letter in self.word)

    def update_display(self):
        display = [letter if letter in self.guesses else '_' for letter in self.word]
        self.label1.config(text=" ".join(display))


list_words = ["python", "apple", "black", "moon", "table", "laptop", "star", "family", "biology", "light"]
word = random.choice(list_words)
game = Hangaman(word)
game.root.mainloop()
