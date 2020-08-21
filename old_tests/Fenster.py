import tkinter as tk
import time

root = tk.Tk()
root.title("GUI Text")
text1 = tk.Text(root, height=10, width=50)
text1.config(state="normal")
text1.insert(tk.INSERT,"SCHEISSE")
text1.config(state="disabled")

text1.pack()

root.mainloop()
while True:
    time.sleep(1)
    text1.config(state="normal")
    text1.insert(tk.INSERT, "Test")
    text1.config(state="disabled")
    win.update()
    time.sleep(1)
    text1.config(state="normal")
    text1.insert(tk.INSERT, "WOW")
    text1.config(state="disabled")
    win.update()
    
    