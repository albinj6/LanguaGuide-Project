import random

# Word dictionary for simple, intermediate, and hard levels
word_dict = {
    "simple": {
        'dog': {'Spanish': 'perro', 'Malayalam': 'പട്ടി', 'Hindi': 'कुत्ता'},
        'cat': {'Spanish': 'gato', 'Malayalam': 'പട്ടി', 'Hindi': 'बिल्ली'},
        'apple': {'Spanish': 'manzana', 'Malayalam': 'ആപ്പിൾ', 'Hindi': 'सेब'},
        'house': {'Spanish': 'casa', 'Malayalam': 'വീട്', 'Hindi': 'घर'},
        'food': {'Spanish': 'comida', 'Malayalam': 'ഭക്ഷണം', 'Hindi': 'खाना'},
        'book': {'Spanish': 'libro', 'Malayalam': 'പുസ്തകം', 'Hindi': 'किताब'},
        'water': {'Spanish': 'agua', 'Malayalam': 'ജലം', 'Hindi': 'पानी'},
        'sun': {'Spanish': 'sol', 'Malayalam': 'സൂര്യൻ', 'Hindi': 'सूरज'},
        'moon': {'Spanish': 'luna', 'Malayalam': 'ചന്ദ്രൻ', 'Hindi': 'चाँद'},
        'friend': {'Spanish': 'amigo', 'Malayalam': 'സുഹൃത്ത്', 'Hindi': 'दोस्त'},
        'family': {'Spanish': 'familia', 'Malayalam': 'കുടുംബം', 'Hindi': 'परिवार'},
        'school': {'Spanish': 'escuela', 'Malayalam': 'പഠനശാല', 'Hindi': 'विद्यालय'},
        'love': {'Spanish': 'amor', 'Malayalam': 'പ്രേമം', 'Hindi': 'प्रेम'},
        'car': {'Spanish': 'coche', 'Malayalam': 'കാറ്', 'Hindi': 'गाड़ी'},
        'tree': {'Spanish': 'árbol', 'Malayalam': 'മരം', 'Hindi': 'पेड़'},
        'bird': {'Spanish': 'pájaro', 'Malayalam': 'പക്ഷി', 'Hindi': 'पक्षी'},
        'mountain': {'Spanish': 'montaña', 'Malayalam': 'പർവതം', 'Hindi': 'पहाड़'},
        'river': {'Spanish': 'río', 'Malayalam': 'നദി', 'Hindi': 'नदी'},
        'rain': {'Spanish': 'lluvia', 'Malayalam': 'മഴ', 'Hindi': 'बारिश'},
        'fire': {'Spanish': 'fuego', 'Malayalam': 'അതിശയം', 'Hindi': 'आग'},
        'earth': {'Spanish': 'tierra', 'Malayalam': 'ഭൂമി', 'Hindi': 'पृथ्वी'},
        'chair': {'Spanish': 'silla', 'Malayalam': 'കസേര', 'Hindi': 'कुर्सी'},
        'table': {'Spanish': 'mesa', 'Malayalam': 'മേശ', 'Hindi': 'मेज़'},
        'window': {'Spanish': 'ventana', 'Malayalam': 'ജനല', 'Hindi': 'खिड़की'},
        'door': {'Spanish': 'puerta', 'Malayalam': 'ദ്വാരം', 'Hindi': 'दरवाजा'},
        'phone': {'Spanish': 'teléfono', 'Malayalam': 'ഫോൺ', 'Hindi': 'फोन'},
        'ball': {'Spanish': 'pelota', 'Malayalam': 'കുരുത്തല്', 'Hindi': 'गेंद'},
        'pencil': {'Spanish': 'lápiz', 'Malayalam': 'പെൻകല്', 'Hindi': 'पेंसिल'},
        'shoe': {'Spanish': 'zapato', 'Malayalam': 'പതുക്കൾ', 'Hindi': 'जूता'},
        'hat': {'Spanish': 'sombrero', 'Malayalam': 'തോപി', 'Hindi': 'टोपी'},
        'watch': {'Spanish': 'reloj', 'Malayalam': 'ഗഡ്ഡി', 'Hindi': 'घड़ी'},
        'fish': {'Spanish': 'pez', 'Malayalam': 'മീന്', 'Hindi': 'मछली'},
        'garden': {'Spanish': 'jardín', 'Malayalam': 'ഉദ്യാനം', 'Hindi': 'बाग़'},
        'park': {'Spanish': 'parque', 'Malayalam': 'പാർക്ക്', 'Hindi': 'पार्क'},
        'street': {'Spanish': 'calle', 'Malayalam': 'റാസ്ത', 'Hindi': 'गली'},
        'market': {'Spanish': 'mercado', 'Malayalam': 'മാർക്കറ്റ്', 'Hindi': 'बाज़ार'},
        'office': {'Spanish': 'oficina', 'Malayalam': 'ഓഫീസ്', 'Hindi': 'ऑफिस'},
        'teacher': {'Spanish': 'maestro', 'Malayalam': 'അധ്യാപിക', 'Hindi': 'शिक्षक'},
        'student': {'Spanish': 'estudiante', 'Malayalam': 'വിദ്യാർത്ഥി', 'Hindi': 'छात्र'},
        'cow': {'Spanish': 'vaca', 'Malayalam': 'ആരു', 'Hindi': 'गाय'},
        'horse': {'Spanish': 'caballo', 'Malayalam': 'കുതിര', 'Hindi': 'घोड़ा'},
        'lion': {'Spanish': 'león', 'Malayalam': 'സിംഹം', 'Hindi': 'शेर'},
        'tiger': {'Spanish': 'tigre', 'Malayalam': 'പുലി', 'Hindi': 'बाघ'},
    },
    "intermediate": {
        'airport': {'Spanish': 'aeropuerto', 'Malayalam': 'വിമാനത്താവളങ്ങള്', 'Hindi': 'विमानस्थल'},
        'hospital': {'Spanish': 'hospital', 'Malayalam': 'ആസ്പത്രി', 'Hindi': 'अस्पताल'},
        'restaurant': {'Spanish': 'restaurante', 'Malayalam': 'റെസ്റ്റോറന്റ്', 'Hindi': 'रेस्टोरेंट'},
        'bookstore': {'Spanish': 'librería', 'Malayalam': 'ഗ്രന്ഥാലയം', 'Hindi': 'किताब घर'},
        'museum': {'Spanish': 'museo', 'Malayalam': 'മ്യൂസിയം', 'Hindi': 'संग्रहालय'},
        'pharmacy': {'Spanish': 'farmacia', 'Malayalam': 'ആഷദാലയം', 'Hindi': 'दवाखाना'},
        'cinema': {'Spanish': 'cine', 'Malayalam': 'ചലച്ചിത്രം', 'Hindi': 'सिनेमाघर'},
        'bank': {'Spanish': 'banco', 'Malayalam': 'ബാങ്ക്', 'Hindi': 'बैंक'},
        'library': {'Spanish': 'biblioteca', 'Malayalam': 'പുസ്തകശാല', 'Hindi': 'पुस्तकालय'},
        'ticket': {'Spanish': 'boleto', 'Malayalam': 'ടിക്കറ്റ്', 'Hindi': 'टिकट'},
        'ticket counter': {'Spanish': 'taquilla', 'Malayalam': 'ടിക്കറ്റ് കൗണ്ടർ', 'Hindi': 'टिकट काउंटर'},
        'passport': {'Spanish': 'pasaporte', 'Malayalam': 'പാസ്‌പോർട്ട്', 'Hindi': 'पासपोर्ट'},
        'swimming': {'Spanish': 'natación', 'Malayalam': 'പുളിമുട്ട്', 'Hindi': 'तैरना'},
        'gym': {'Spanish': 'gimnasio', 'Malayalam': 'ജിം', 'Hindi': 'जिम'},
        'taxi': {'Spanish': 'taxi', 'Malayalam': 'ടാക്സി', 'Hindi': 'टैक्सी'},
        'train': {'Spanish': 'tren', 'Malayalam': 'പ്രീസിന്', 'Hindi': 'रेल'},
        'flight': {'Spanish': 'vuelo', 'Malayalam': 'വിമാനം', 'Hindi': 'उड़ान'},
        'bridge': {'Spanish': 'puente', 'Malayalam': 'പള' , 'Hindi': 'पुल'},
        'science': {'Spanish': 'ciencia', 'Malayalam': 'വൈജ്ഞാനികം', 'Hindi': 'विज्ञान'},
        'technology': {'Spanish': 'tecnología', 'Malayalam': 'പദം', 'Hindi': 'तकनीकी'}
    }
}

def display_instructions():
    print("\nWelcome to the Word Match Game!")
    print("You will be given words in one language and need to match them with their translations.")
    print("Choose the correct match from the options.")
    print("Type 'exit' to quit the game at any time.\n")

def match_words(word, language, options, level):
    print(f"\nTranslate the word '{word}' to {language}:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    try:
        choice = int(input("\nYour choice (1-4): "))
        if options[choice - 1] == word_dict[level][word][language]:  # Include level here
            print("Correct!\n")
            return True
        else:
            print("Incorrect! Try again.\n")
            return False
    except (ValueError, IndexError):
        print("Invalid choice! Please select a valid number.\n")
        return False


def play_game(level):
    if level not in word_dict:
        print("Invalid level. Please select a valid level (simple, intermediate, hard).")
        return

    print(f"\nYou are now playing the {level.capitalize()} level!")
    display_instructions()

    # Game Loop
    while True:
        # Select a random word and language
        word = random.choice(list(word_dict[level].keys()))
        language = random.choice(list(word_dict[level][word].keys()))

        # Correct answer in the target language
        correct_answer = word_dict[level][word][language]

        # Generate options from the same language only
        options = [correct_answer]
        all_words_in_language = [
            word_dict[level][w][language]
            for w in word_dict[level].keys()
            if language in word_dict[level][w]
        ]

        # Add incorrect options
        while len(options) < 4:
            random_translation = random.choice(all_words_in_language)
            if random_translation not in options:
                options.append(random_translation)

        # Shuffle the options
        random.shuffle(options)

        # Start the match
        if match_words(word, language, options, level):
            continue

        # Asking user if they want to play again or exit
        play_again = input("Do you want to continue playing? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break


# Start the game
if _name_ == "_main_":
    # Choose a level: 'simple', 'intermediate', or 'hard'
    level = input("Choose a level to play (simple, intermediate, hard): ").lower()
    play_game(level)