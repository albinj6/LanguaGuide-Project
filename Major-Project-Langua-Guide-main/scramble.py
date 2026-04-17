import tkinter as tk
from tkinter import messagebox
import random
from itertools import permutations

# Words to scramble
words = {
    "hindi": ["घर", "पुस्तक", "बाग़", "विद्यालय"],
    "malayalam": ["കൂടാരം", "പുസ്തകം", "കുടുംബം", "പാചകം"],
    "spanish": ["casa", "libro", "jardín", "escuela"]
}

def scramble_word(word):
    """Scramble the letters of a word."""
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def generate_anagrams(word):
    """Generate up to 4 unique anagrams, including the correct word."""
    all_anagrams = set([''.join(p) for p in permutations(word)])
    all_anagrams = list(all_anagrams)
    random.shuffle(all_anagrams)
    if word in all_anagrams:
        all_anagrams.remove(word)
    anagrams = random.sample(all_anagrams, min(3, len(all_anagrams))) + [word]
    random.shuffle(anagrams)
    return anagrams

def check_word(word):
    """Check if the selected word is correct."""
    selected_word = dropdown_var.get()
    if selected_word == word:
        messagebox.showinfo("Correct!", f"You unscrambled the word correctly!")
        load_new_word()  # Load the next word
    else:
        messagebox.showwarning("Try Again", "That's not the correct word. Try again!")

def load_new_word():
    """Reset the UI and load a new scrambled word with anagram options."""
    global word, scrambled_word, options

    # Select a random language and word
    selected_language = random.choice(list(words.keys()))
    word = random.choice(words[selected_language])
    scrambled_word = scramble_word(word)

    # Generate multiple-choice options (anagrams of the correct word)
    options = generate_anagrams(word)

    # Update UI components
    language_label.config(text=f"Language: {selected_language.capitalize()}")
    scrambled_label.config(text=f"Scrambled Word: {scrambled_word}")
    dropdown_var.set("Select the correct word")
    dropdown_menu['menu'].delete(0, 'end')
    for option in options:
        dropdown_menu['menu'].add_command(label=option, command=lambda value=option: dropdown_var.set(value))

# Initialize main window
root = tk.Tk()
root.title("Word Scramble Game - Anagram Multiple Choice")
root.geometry("600x400")

# UI Components
language_label = tk.Label(root, text="", font=("Helvetica", 14))
language_label.pack(pady=10)

scrambled_label = tk.Label(root, text="", font=("Helvetica", 18))
scrambled_label.pack(pady=10)

dropdown_var = tk.StringVar(value="Select the correct word")
dropdown_menu = tk.OptionMenu(root, dropdown_var, [])
dropdown_menu.config(font=("Helvetica", 14), width=20)
dropdown_menu.pack(pady=10)

check_button = tk.Button(root, text="Check Answer", font=("Helvetica", 14), command=lambda: check_word(word))
check_button.pack(pady=20)

# Load the first word
load_new_word()

# Start the game loop
root.mainloop()
