from tkinter import * 
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title('Aisier Code Editor')
file_path = ''
compiler.geometry("1920x1080")
compiler.config(bg="#020202")


def lang(Syntax):
    printState = 0
    Token = ""
    String = ""
    oldtxt = ""
    for Char in Syntax:
        Token += Char
        if Token == " ":
            if printState == 0:
                Token = ""
 
        elif Token == "\n":
            Token = ""
 
        elif Token == "txt":
            Token = ""
 
        elif Token == "\"":
            if printState == 0:
                printState = 1
                Token = ""
 
            elif printState == 1:
                printState = 0

        elif Token == "//":
            break
 
        elif printState == 1:
            String += Token
            Token = ""
    
    print(String)
    code_output.insert('1.0', String)


def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Aisier Source Code', '*.asr')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Aisier Source Code', '*.asr')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    code_output.delete("1.0", END)
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    Content = open(file_path, "r").readlines()
    for Line in Content:
        lang(Line)


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New Window")
file_menu.add_command(label='Open File', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()