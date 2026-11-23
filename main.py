import tkinter as tk

# 1. Create the window
window = tk.Tk()
window.title("My Python App")
window.geometry("400x400")
window.configure(bg="white")

# 2. What happens when you click the square button
def go_to_new_page():
    # Clears everything on the current screen (makes a blank page)
    for item in window.winfo_children():
        item.destroy()
    
    # Writes "hello" on the blank page
    hello_text = tk.Label(window, text="hello", font=("Arial", 28), bg="white", fg="black")
    hello_text.pack(expand=True)

# 3. Create the small square button (80x80 pixels)
square_btn = tk.Button(window, text="Click", command=go_to_new_page)
square_btn.place(x=160, y=160, width=80, height=80)

# 4. Keep the window running
window.mainloop()
