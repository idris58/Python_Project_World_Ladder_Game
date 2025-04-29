import tkinter as tk
import random
from nltk.corpus import wordnet

ladder_sets = [
    ["cold", "worm"], ["game", "malt"], ["bake", "cure"], ["lead", "goof"], ["fast", "cash"],
    ["make", "goon"], ["spin", "scar"], ["word", "goal"], ["tail", "pale"], ["hunt", "ward"],
    ["life", "love"], ["star", "head"], ["find", "tome"], ["long", "bunk"], ["coat", "cake"],
    ["port", "coat"], ["fast", "look"], ["head", "tail"], ["word", "pole"], ["star", "feat"]
]

def is_valid_word(word):
    return len(wordnet.synsets(word)) > 0

def one_letter_diff(w1, w2):
    if len(w1) != len(w2):
        return False
    return sum(a != b for a, b in zip(w1, w2)) == 1

def pick_ladder():
    return random.choice(ladder_sets)

start_word, end_word = pick_ladder()
max_steps = 6
ladder_words = ["" for x in range(max_steps)]
ladder_words[0] = start_word
ladder_words[-1] = end_word
current_index = 1

window = tk.Tk()
window.title("Word Ladder Game")
window.geometry("450x650")
window.configure(bg="#f0f8ff") 

main_frame = tk.Frame(window, bg="#f0f8ff")
main_frame.pack(fill="both", expand=True)

tk.Label(main_frame, text=" ", font=("Arial", 16, "bold"), bg="#f0f8ff").pack(pady=65, anchor="center")
headline = tk.Label(main_frame, text="Welcome to the Word Ladder Game!", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="purple")
headline.pack(pady=30, anchor="center")

description = tk.Label(main_frame, text="Transform one word\nto another by changing one letter at a time.", font=("Arial", 13, "bold"), bg="#f0f8ff", fg="#333333")
description.pack(pady=10, anchor="center")

start_btn = tk.Button(main_frame, text="▶️ Start Game", font=("Arial", 14, "bold"), bg="dark green", fg="white", width=15, command=lambda: show_game_page())
start_btn.pack(pady=20, anchor="center")

game_frame = tk.Frame(window, bg="#f0f8ff")

def show_game_page():
    main_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)

    frame = tk.Frame(game_frame, bg="#f0f8ff")
    frame.pack(pady=10)

    global headline
    headline = tk.Label(frame, text=f"Transform '{start_word}' to '{end_word}'", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="purple")
    headline.pack()

    ladder_frame = tk.Frame(frame, bg="#f0f8ff")
    ladder_frame.pack(pady=5)

    global labels
    labels = []

    for i in range(max_steps):
        row_frame = tk.Frame(ladder_frame, bg="#f0f8ff")
        row_frame.pack()

        tk.Label(row_frame, text="│", font=("Courier", 22, "bold"), bg="#f0f8ff", fg="brown").pack(side="left", padx=10)
        lbl = tk.Label(row_frame, text=" ", font=("Courier", 18, "bold"), width=10, bg="#f0f8ff", fg="black")
        lbl.pack(side="left")
        labels.append(lbl)
        tk.Label(row_frame, text="│", font=("Courier", 22, "bold"), bg="#f0f8ff", fg="brown").pack(side="left", padx=10)

        if i < max_steps - 1:
            tk.Label(ladder_frame, text="─────────────────", font=("Courier", 14, "bold"), bg="#f0f8ff", fg="brown").pack(pady=2)

    labels[0].config(text=start_word)
    labels[-1].config(text=end_word)

    global entry
    entry = tk.Entry(frame, font=("Arial", 14), width=15, justify="center", bd=3)
    entry.pack(pady=10)
    entry.focus_set()

    global msg
    msg = tk.Label(frame, text="", font=("Arial", 12, "bold"), bg="#f0f8ff", fg="red")
    msg.pack()

    submit_btn = tk.Button(frame, text="Submit", font=("Arial", 12, "bold"), bg="#008000", fg="white", width=10, command=submit_word)
    submit_btn.pack(pady=5)

    restart_btn = tk.Button(frame, text="Reset Game", font=("Arial", 12, "bold"), bg="#d11541", fg="white", width=10, command=restart)
    restart_btn.pack(pady=5)

    window.bind('<Return>', lambda e: submit_word())

def submit_word():
    global current_index
    guess = entry.get().strip().lower()
    entry.delete(0, tk.END)

    if current_index >= max_steps - 1:
        msg.config(text="Game already finished!")
        return

    msg.config(text="", fg="red")

    if len(guess) != 4:
        msg.config(text="Enter a 4-letter word.")
        return

    if not is_valid_word(guess):
        msg.config(text="Invalid English word.")
        return

    prev_word = ladder_words[current_index - 1]
    if not one_letter_diff(prev_word, guess):
        msg.config(text="Must differ by 1 letter.")
        return

    ladder_words[current_index] = guess
    labels[current_index].config(text=guess)

    if current_index == max_steps - 2:
        if one_letter_diff(guess, end_word):
            msg.config(text="🎉 You completed the ladder!", fg="green")
        else:
            msg.config(text="❌ End word not reachable from here!", fg="red")

    current_index += 1

def restart():
    global start_word, end_word, ladder_words, current_index
    start_word, end_word = pick_ladder()
    ladder_words = ["" for x in range(max_steps)]
    ladder_words[0] = start_word
    ladder_words[-1] = end_word
    current_index = 1

    headline.config(text=f"Transform '{start_word}' to '{end_word}'")
    for i in range(max_steps):
        labels[i].config(text=" ")
    labels[0].config(text=start_word)
    labels[-1].config(text=end_word)
    msg.config(text="", fg="red")
    entry.delete(0, tk.END)
    entry.focus_set()

window.mainloop() 