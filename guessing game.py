import random
import tkinter as tk
from tkinter import messagebox


class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")
        self.master.geometry("300x150")

        self.random_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()

    def check_guess(self):
        guess = self.entry.get()
        self.entry.delete(0, 'end')

        try:
            guess = int(guess)
            self.attempts += 1

            if guess < self.random_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif guess > self.random_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations", f"Correct! You guessed the number in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def reset_game(self):
        self.random_number = random.randint(1, 100)
        self.attempts = 0


def main():
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
