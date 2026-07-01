import tkinter as tk
import json
import random
try:
    with open("flashcards.json", "r") as file:
        data = json.load(file)
        if isinstance(data, list):
            flashcards = data
        else:
            flashcards = data.get("flashcards", [])
except Exception as e:
    flashcards = [{"question": "Error loading file", "answer": str(e)}]
current_card = {}
def next_card():
    global current_card
    if flashcards:
        current_card = random.choice(flashcards)
        question_label.config(text=current_card.get("question", "No 'question' key found"))
    else:
        question_label.config(text="No flashcards found!")
def show_answer():
    if current_card:
        question_label.config(text=current_card.get("answer", "No 'answer' key found"))
root = tk.Tk()
root.title("Flashcard Quiz App")
root.geometry("500x350")

title = tk.Label(root, text="Flashcard Quiz App", font=("Arial", 18, "bold"))
title.pack(pady=20)
question_label = tk.Label(root, text="Click 'Next card' to start!", font=("Arial", 14), wraplength=400)
question_label.pack(pady=30)
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
show_btn = tk.Button(button_frame, text="Show Answer", font=("Arial", 12), command=show_answer)
show_btn.pack(side="left", padx=10)
next_btn = tk.Button(button_frame, text="Next Card", font=("Arial", 12),command=next_card)
next_btn.pack(side="left", padx=10)
root.mainloop()