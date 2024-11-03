import os
from tkinter import *


def load_file(filename, text_editor):
    file = open("./save/" + filename, "r")
    text_editor.delete("0.0", END)
    text_editor.insert(END, file.read())
    file.close()


def save_file(filename, text_editor):
    file = open("./save/" + filename, "w")
    file.write(text_editor)
    file.close()


def set_text_entery(entery, text):
    entery.delete(0, END)
    entery.insert(0, text)


def main():
    root = Tk()
    root.title("Text editor")
    root.geometry("1280x720")

    all_files = os.listdir("./save")

    list_box = Listbox(root, selectmode=SINGLE)
    text = Text(width=140, bg='#012', fg='white', wrap=WORD)
    input_file_name = Entry(width=20, bg='#234', fg='white')
    scroll = Scrollbar(command=text.yview)
    text.config(yscrollcommand=scroll.set)

    def save():
        save_file(input_file_name.get(), text.get("0.0", END))
        files = os.listdir("./save")
        list_box.delete(0, END)
        for file in files:
            list_box.insert(END, file)

    btn_save = Button(text="save", command=lambda: save())

    for filename in all_files:
        list_box.insert(END, filename)

    def event_list_box(event):
        name_file = all_files[list_box.curselection()[0]]
        set_text_entery(input_file_name, name_file)
        load_file(name_file, text)

    list_box.bind('<<ListboxSelect>>', event_list_box)

    scroll.pack(side=RIGHT, fill=Y)
    text.pack(side=RIGHT, fill=Y)
    input_file_name.pack()
    btn_save.pack(side=TOP)
    list_box.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
