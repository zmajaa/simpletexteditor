from tkinter import Tk, scrolledtext, Menu, filedialog, messagebox, END
import os

#Root for main window
root=Tk(className="Text Editor")
text_area=scrolledtext.ScrolledText(root, width=100, height=80)

def new_file():
    #is there anz contetnt
    if len(text_area.get("1.0"))>0:
        if messagebox.askyesno("Save","Do zou wish to save_"):
            save_file()
            text_area.delete("-1.0", END)
        else:
            text_area.delete("-1.0", END)



def open_file():
    text_area.delete("-1.0", END)
    file=filedialog.askopenfile(parent=root, title="Select a text file", filetypes=(("Text file","*.txt"),("All files","*.*")))
    if file != None:
        contents=file.read()
        text_area.insert("1.0", contents)
        file.close()

def save_file():
    file=filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(("HTML file","*.html"),("Text file","*.txt"),("All files","*.*")))
    if file !=None:
        data=text_area.get("1.0")
        file.write(data)
        file.close()

def exit_root():
    if messagebox.askyesno("Quit","Are you sure you want to quit?"):
        root.destroy()
def about():
    label=messagebox.showinfo("About", "My alternative to Notepad")

#Menu options
menu= Menu(root)
root.config(menu=menu)
fileMenu=Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit_root)


helpMenu=Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About", command=about)



text_area.pack()


#Keeping the window open
root.mainloop()