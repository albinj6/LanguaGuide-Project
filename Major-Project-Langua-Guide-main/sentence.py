import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import random
import tkinter.messagebox

# Example sentences in different languages
sentences = {
    "hindi": {
        "words": ["मैं", "हाथी", "हूँ", "एक"],
        "correct_order": ["मैं", "एक", "हाथी", "हूँ"],
    },
    "malayalam": {
        "words": ["ഞാൻ", "ആന", "ആണ്", "ഒരുപാട്"],
        "correct_order": ["ഞാൻ", "ഒരുപാട്", "ആന", "ആണ്"],
    },
    "spanish": {
        "words": ["yo", "elefante", "soy", "un"],
        "correct_order": ["yo", "soy", "un", "elefante"],
    }
}

# Function to check if the sentence is correct
def check_sentence():
    selected_words = [word_var.get() for word_var in word_vars]
    if selected_words == correct_order:
        tkinter.messagebox.showinfo("Correct!", "You have arranged the words correctly!")
        load_new_sentence()  # Load new words and sentence
    else:
        tkinter.messagebox.showwarning("Try Again", "That's not the correct sentence. Try again.")

# Function to load a new set of words and sentence
def load_new_sentence():
    global correct_order, word_vars, selected_language

    # Select a random language
    selected_language = random.choice(["hindi", "malayalam", "spanish"])

    # Get the jumbled words and the correct order for the selected language
    words_list = sentences[selected_language]["words"]
    correct_order = sentences[selected_language]["correct_order"]

    # Update the jumbled words display
    words_label.config(text=" ".join(words_list))

    # Create word entry widgets for sentence building
    for widget in word_frame.winfo_children():
        widget.destroy()  # Clear previous widgets

    word_vars = []
    random.shuffle(words_list)  # Shuffle words for the player to rearrange

    for word in words_list:
        word_var = tk.StringVar(value=word)
        word_vars.append(word_var)

        word_button = tk.Button(word_frame, text=word, font=("Helvetica", 14), width=10, height=2,
                                command=lambda word=word: word_var.set(word))
        word_button.grid(row=0, column=words_list.index(word), padx=5, pady=5)

        # Enable drag-and-drop functionality
        word_button.drop_target_register(DND_FILES)
        word_button.dnd_bind('<<Drop>>', lambda event, word=word: on_drop(event, word))

# Function for the drop event (when a word is dropped in the target area)
def on_drop(event, word):
    drop_target_var.set(word)

# Initialize the main window
root = TkinterDnD.Tk()
root.title("Sentence Builder Game")
root.geometry("600x400")

# UI Components
instructions = tk.Label(root, text="Rearrange the words to form a correct sentence:", font=("Helvetica", 14))
instructions.pack(pady=10)

words_label = tk.Label(root, text="", font=("Helvetica", 18), wraplength=500, justify="center")
words_label.pack(pady=20)

word_frame = tk.Frame(root)
word_frame.pack(pady=10)

# Create a drop area to arrange words
drop_area = tk.Label(root, text="Drop words here in order", font=("Helvetica", 14), width=40, height=5,
                     relief="solid")
drop_area.pack(pady=20)

# Create a variable for the drop target area
drop_target_var = tk.StringVar()

# Check button
check_button = tk.Button(root, text="Check Sentence", font=("Helvetica", 14), command=check_sentence)
check_button.pack(pady=20)

# Load the first set of words and sentence
load_new_sentence()

# Start the game loop
root.mainloop()
