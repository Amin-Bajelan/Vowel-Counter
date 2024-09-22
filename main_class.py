import tkinter as tk
from tkinter import messagebox

background_color = '#FCDE70'
list_vowel_word = ['a', 'e', 'i', 'o', 'u']

def del_label():
    global label_answer
    label_answer.destroy()


def count_vowel():

    num_vowel_word = int(0)
    if len(entry_word.get()) == 0:
        messagebox.showinfo('Error', 'Please make sure to enter word.')
    else:
        list_my_str = list(str(entry_word.get().lower()))
        for i in range(len(list_my_str)):
            for j in range(len(list_vowel_word)):
                if list_my_str[i] == list_vowel_word[j]:
                    num_vowel_word += 1
        print(num_vowel_word)

        global label_answer
        label_answer = tk.Label(text=f'number of your vowel word: {num_vowel_word}', font=('Arial', 15))
        label_answer.place(x=110, y=170)
        label_answer.after(3000, del_label)

window = tk.Tk()
window.title('Vowel Counter')
window.geometry('500x300')
window.maxsize(500, 300)
window.minsize(500, 300)
window.configure(background=background_color)

entry_word = tk.Entry(window, width=40, font=('Helvetica', 15))
entry_word.config()
entry_word.place(x=30, y=40)

btn_count_vowel = tk.Button(width=20, text='Count Vowel', command=count_vowel)
btn_count_vowel.config(font=('Helvetica', 15))
btn_count_vowel.place(x=130, y=100)


window.mainloop()
