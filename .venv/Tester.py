import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
from secrets import API_KEY

# OpenAI client
client = OpenAI(api_key=API_KEY)

# Generate a response using GPT
def generate_response(prompt):
    completions = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=300
    )
    return completions.choices[0].message.content

# Display the response
def display_response():
    input_text = input_field.get("1.0", tk.END).strip()
    if not input_text:
        return
    response = generate_response(input_text)
    output_field.config(state='normal')
    output_field.insert(tk.END, f"You: {input_text}\nBot: {response}\n\n")
    output_field.see(tk.END)  # Auto-scroll
    output_field.config(state='disabled')
    input_field.delete("1.0", tk.END)  # Clear input

# Main window
root = tk.Tk()
root.title("OpenAI Chatbot")
root.geometry("700x800")
root.configure(bg="#f4f4f4")

# Input label
tk.Label(root, text="Enter your message:", font=("Arial", 14), bg="#f4f4f4").pack(pady=(10, 0))

# Larger input field (multi-line)
input_field = tk.Text(root, font=("Arial", 14), height=4, wrap=tk.WORD, bd=2, relief="groove")
input_field.pack(padx=20, pady=10, fill="x")

# Submit button
submit_button = tk.Button(root, text="Send", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white",
                          activebackground="#45a049", command=display_response)
submit_button.pack(pady=10)

# Output label
tk.Label(root, text="Conversation:", font=("Arial", 14), bg="#f4f4f4").pack(pady=(20, 0))

# Larger output area with scrollbar
output_field = scrolledtext.ScrolledText(root, font=("Arial", 14), wrap=tk.WORD, state='disabled',
                                         bg="#ffffff", fg="#000000", bd=2, relief="groove")
output_field.pack(padx=20, pady=10, fill="both", expand=True)

root.mainloop()

