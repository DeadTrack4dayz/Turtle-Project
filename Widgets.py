import tkinter as tk

root = tk.Tk()
root.wm_geometry("400x400")

blue = tk.Frame(root, bg = 'blue',width = 250, height = 200)
blue.grid(row = 0,column = 0)

red = tk.Frame(root, bg = 'red',width = 250, height = 200)
red.grid(row = 1, column = 0)

green = tk.Frame(root, bg = 'lime',width = 150, height = 200)
green.grid(row = 0, column = 1)

yellow = tk.Frame(root, bg = 'yellow',width = 150, height = 200)
yellow.grid(row = 1, column = 1)

root.mainloop()