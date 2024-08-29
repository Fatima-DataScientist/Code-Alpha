# Create a text-based chatbot that can have conversations with users. You can use natural
# language processing libraries like NLTK or spaCy to make your chatbot more conversational.


import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections
pairs=[
    [r"hey|hello|hi",
     ["Hey! What's on your mind?"]],
    [r"how are you",
     ["I'm doing well, thank you! How about you?"]],
    [
        r"what is your name",
        ["I go by Chatbot. What can I do for you today?"]],
    [
        r"want to ask a question",
        ["Sure! Feel free to ask anything. I'm here to help."]],
    [
        r"(.*)sorry|apologize(.*)",
        ["No need to apologize. It's alright."]],
    [
        r"goodbye|quit|exit",
        ["Goodbye! If you ever need help again, feel free to reach out. Take care"]],
    [
        r"what is your favourite color?",
        ["I don't have personal preferances, but I can help with information about colors or their meanings if you're interested."]],
    [
        r"do you know about tech?",
        ["Absolutely, I can help with wide range of tech-related topics! This includes:\n* Programming\n* Software Development\n* Cyber Security\n* Information Technology\n* Tech Trends" ]],
    [
        r"what is programming",
        ["Programming is the process of creating instructions that a computer can follow to perform specific tasks.\nDifferent programming languages includes:\nJava\nPython\nC\nC++\nC#\nJavaScript"]]
]



chatbot = Chat(pairs, reflections)
def chatbot_response(user_input):
    response= chatbot.respond(user_input)
    if response:
        return response
    else:
        return "Sorry, I don't understand that."
def send_message():
    message = entry.get()
    entry.delete(0, tk.END)
    if message.lower() == 'quit':
        chat_area.insert(tk.END, "You: " + message + "\n")
        chat_area.insert(tk.END, "Chatbot: " + chatbot_response(message) + "\n")
        chat_area.insert(tk.END, "Chatbot: Bye! Take care.\n")
        entry.config(state=tk.DISABLED)
        send_button.config(state=tk.DISABLED)
    else:
        chat_area.insert(tk.END, "You: " + message + "\n")
        chat_area.insert(tk.END, "Chatbot: " + chatbot_response(message) + "\n")
        chat_area.see(tk.END)

# Create the main window
root = tk.Tk()
root.geometry('500x500')
root.title("Chatbot")
root.resizable(False, False)

# Create a frame to hold the chat area
chat_frame = tk.Frame(root,bg="silver")
chat_frame.pack(padx=10, pady=10)

# Create a scrolled text widget to display the chat
chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, background="silver")
chat_area.pack(padx=10, pady=10)

# Create a frame to hold the message entry field and send button
entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=10, fill=tk.BOTH)

# Create an entry widget to type messages
entry = tk.Entry(entry_frame, width=40)
entry.pack(side=tk.LEFT, padx=0,pady=0)

# Create a button to send messages
send_button = tk.Button(entry_frame, text="Send", width=10,font=("Arial Black",10), command=send_message)
send_button.pack(side=tk.LEFT,padx=4,pady=0)
root.bind('<Return>', lambda event=None: send_message())
entry.focus()
root.mainloop()