import tkinter as tk
from tkinter import messagebox
import random

# Categories with words and their names in different languages
categories = {
    "fruits": {
        "hindi": ["सेब", "केला", "आम", "संतरा"],
        "malayalam": ["സേവനം", "കഴക്ക", "മാങ്ങ", "ഓറഞ്ച്"],
        "spanish": ["manzana", "plátano", "mango", "naranja"],
        "name": {"hindi": "फल", "malayalam": "പഴം", "spanish": "frutas"}
    },
    "animals": {
        "hindi": ["शेर", "हाथी", "बंदर", "कुत्ता"],
        "malayalam": ["സിംഹം", "ആന", "കുരങ്ങ്", "നായ"],
        "spanish": ["león", "elefante", "mono", "perro"],
        "name": {"hindi": "जानवर", "malayalam": "മൃഗങ്ങൾ", "spanish": "animales"}
    },
    "colors": {
        "hindi": ["लाल", "नीला", "हरा", "पीला"],
        "malayalam": ["ചുവപ്പ്", "നീല", "പച്ച", "മഞ്ഞ"],
        "spanish": ["rojo", "azul", "verde", "amarillo"],
        "name": {"hindi": "रंग", "malayalam": "നിറങ്ങൾ", "spanish": "colores"}
    }
}

def check_category(selected_category):
    """Check if the selected category is correct."""
    if selected_category == correct_category:
        messagebox.showinfo("Correct!", "You guessed the correct category!")
        load_new_set()  # Load new words and category
    else:
        messagebox.showwarning("Try Again", "That's not the correct category. Try again!")

def load_new_set():
    """Load a new set of words and categories."""
    global correct_category, words_list, selected_language

    # Select a random category and language
    correct_category = random.choice(list(categories.keys()))
    selected_language = random.choice(["hindi", "malayalam", "spanish"])

    # Get the words for the correct category and language
    words_list = categories[correct_category][selected_language]

    # Update the UI
    words_label.config(text=", ".join(words_list))
    category_var.set("Select the category")

    # Update the dropdown menu with translated category names
    dropdown_menu['menu'].delete(0, 'end')
    for category, data in categories.items():
        translated_name = data["name"][selected_language]
        dropdown_menu['menu'].add_command(
            label=f"{category.capitalize()} ({translated_name})",
            command=lambda value=category: category_var.set(value)
        )

# Initialize main window
root = tk.Tk()
root.title("Guess the Category Game")
root.geometry("600x400")

# UI Components
instructions = tk.Label(root, text="Guess the category of the following words:", font=("Helvetica", 14))
instructions.pack(pady=10)

words_label = tk.Label(root, text="", font=("Helvetica", 18), wraplength=500, justify="center")
words_label.pack(pady=20)

category_var = tk.StringVar(value="Select the category")
dropdown_menu = tk.OptionMenu(root, category_var, [])
dropdown_menu.config(font=("Helvetica", 14), width=25)
dropdown_menu.pack(pady=10)

check_button = tk.Button(root, text="Check Answer", font=("Helvetica", 14), command=lambda: check_category(category_var.get()))
check_button.pack(pady=20)

# Load the first set of words
load_new_set()

# Start the game loop
root.mainloop()
