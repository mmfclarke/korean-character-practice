import random
import tkinter as tk
import json

# Load the JSON file with Korean characters and romanizations
with open('korean_common_romanization.json', 'r', encoding='utf-8') as f:
    korean_romanization_dict = json.load(f)

# Function to generate a random Korean character from the dictionary
def generate_korean_char():
    # Randomly choose a Korean character from the dictionary keys
    korean_char = random.choice(list(korean_romanization_dict.keys()))
    romanization = korean_romanization_dict[korean_char]
    return korean_char, romanization

# Function to update the Korean character and its romanization
def update_character():
    korean_char, correct_romanization = generate_korean_char()
    character_label.config(text=f"{korean_char}")  # Just the character, no "Character: " text
    global correct_answer
    correct_answer = correct_romanization
    feedback_label.config(text="")  # Clear previous feedback

# Function to check the user's input and update feedback
def check_answer():
    user_input = entry.get().lower()
    if user_input == correct_answer.lower():
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text=f"Incorrect! The correct romanization is: {correct_answer}", fg="red")

# Function to copy the character to clipboard manually (using Tkinter)
def copy_to_clipboard():
    character = character_label.cget("text")  # Get the character from the label
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(character)  # Append the character to the clipboard
    root.update()  # Ensure the clipboard update is immediate
    feedback_label.config(text="The character has been copied to the clipboard!", fg="blue")

# Function to go to the next character
def next_character():
    update_character()

# Create the main application window
root = tk.Tk()
root.title("Korean Character Practice")

# Set up a label to show the Korean character
character_label = tk.Label(root, font=("Arial", 48))
character_label.pack(pady=20)

# Set up an entry widget to allow the user to input their answer
entry_label = tk.Label(root, text="Enter the romanization:")
entry_label.pack()
entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

# Set up a label for feedback (Correct/Incorrect messages)
feedback_label = tk.Label(root, font=("Arial", 16), fg="black")
feedback_label.pack(pady=10)

# Set up buttons
submit_button = tk.Button(root, text="Submit Answer", command=check_answer, font=("Arial", 16))
submit_button.pack(side=tk.LEFT, padx=20, pady=10)

# Add a "Next" button to go to the next character
next_button = tk.Button(root, text="Next", command=next_character, font=("Arial", 16))
next_button.pack(side=tk.LEFT, padx=20, pady=10)

# Add a "Copy" button to copy the character to clipboard
copy_button = tk.Button(root, text="Copy Character", command=copy_to_clipboard, font=("Arial", 12))
copy_button.pack(side=tk.LEFT, padx=20, pady=10)

# Start the game by generating the first character
update_character()

# Run the Tkinter event loop
root.mainloop()