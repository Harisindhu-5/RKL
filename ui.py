import tkinter as tk

def get_input():
    def submit():
        nonlocal user_input
        user_input = entry.get()  
        root.destroy()           

    root = tk.Tk()
    root.title("Input Window")
    window_width, window_height = 300, 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    user_input = None 
    tk.Label(root, text="Enter a string:", font=("Arial", 12)).pack(pady=10)
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus_set()  
    tk.Button(root, text="Submit", font=("Arial", 12), command=submit).pack(pady=10)

    
    root.mainloop()
    return user_input
