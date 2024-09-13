import tkinter as tk
from tkinter import messagebox

def show_popup(text, artist, title, completed_lyric):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Recognized Text", f"Recognized Text: {text}\n\nArtist: {artist}\nTitle: {title}\n\nCompleted Lyric:\n{completed_lyric}")
    root.destroy()