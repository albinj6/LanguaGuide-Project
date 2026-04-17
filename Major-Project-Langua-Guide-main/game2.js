const words = {
    hindi: ["घर", "पुस्तक", "बाग़", "विद्यालय", "दरवाज़ा"],
    malayalam: ["കൂടാരം", "പുസ്തകം", "കുടുംബം", "പാചകം", "വീട്"],
    spanish: ["casa", "libro", "jardín", "escuela", "puerta"]
};

let correctWord = "";

function scrambleWord(word) {
    let shuffled = word.split("").sort(() => Math.random() - 0.5).join("");
    return shuffled !== word ? shuffled : scrambleWord(word);
}

function generateOptions(correct) {
    let options = new Set();
    options.add(correct);

    while (options.size < 4) {
        let randomWord = words[document.getElementById("language").value][Math.floor(Math.random() * words[document.getElementById("language").value].length)];
        options.add(randomWord);
    }

    return Array.from(options).sort(() => Math.random() - 0.5);
}

function loadNewWord() {
    let language = document.getElementById("language").value;
    if (!language) {
        document.getElementById("message").textContent = "Please select a language!";
        return;
    }

    let wordList = words[language];
    correctWord = wordList[Math.floor(Math.random() * wordList.length)];
    let scrambled = scrambleWord(correctWord);
    document.getElementById("scrambledWord").textContent = "Scrambled Word: " + scrambled;

    let options = generateOptions(correctWord);
    let dropdown = document.getElementById("options");
    dropdown.innerHTML = '<option value="">Select the correct word</option>';
    options.forEach(option => {
        let opt = document.createElement("option");
        opt.value = option;
        opt.textContent = option;
        dropdown.appendChild(opt);
    });

    document.getElementById("message").textContent = "";
}

function checkAnswer() {
    let selectedWord = document.getElementById("options").value;
    if (!selectedWord) {
        document.getElementById("message").textContent = "Please select an answer!";
        return;
    }

    if (selectedWord === correctWord) {
        document.getElementById("message").textContent = "Correct! 🎉";
    } else {
        document.getElementById("message").textContent = "Try again! ❌";
    }
}