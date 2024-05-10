from gtts import gTTS
import os
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

# Create the main Tkinter window
root = tk.Tk()
root.title("Text-to-Speech Converter")

# Function to convert text to speech and play
def convert_and_play():
    text_to_speech = entry.get()
    if text_to_speech:
        filename = 'output.mp3'

        # Create a gTTS object
        speech = gTTS(text=text_to_speech, lang='en', slow=False)

        # Save the speech to a file
        speech.save(filename)

        # Play the speech using a platform-specific command
        try:
            os.system("xdg-open " + filename)
        except Exception as e:
            messagebox.showerror("Error", "Error playing speech: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

# Create GUI elements
label = Label(root, text="Enter text to convert:")
label.pack(pady=10)

entry = Entry(root, width=50)
entry.pack(pady=10)

convert_button = Button(root, text="Convert and Play", command=convert_and_play)
convert_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
