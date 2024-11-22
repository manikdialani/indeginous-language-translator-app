from tkinter import *
from cree_sro_syllabics import sro2syllabics,syllabics2sro
# https://crk-orthography.readthedocs.io/en/stable/#


# Conversion app between Western Cree Standard Roman Orthography (SRO) and Cree Syllabics
Screen = Tk()
Screen.title("Roman to Cree Syllabics Convertor")

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

LanguageChoices = {'Roman', 'Cree Syllabics'}
InputLanguageChoice.set('Roman')
TranslateLanguageChoice.set('Cree Syllabics')

def Convert():
    input_text = TextVar.get()
    if InputLanguageChoice.get() == 'Roman' and TranslateLanguageChoice.get() == 'Cree Syllabics':
        Conversion = sro2syllabics(input_text)
    elif InputLanguageChoice.get() == 'Cree Syllabics' and TranslateLanguageChoice.get() == 'Roman':
        Conversion = syllabics2sro(input_text)
    else:
        Conversion = "Invalid Conversion"
    OutputVar.set(Conversion)

InputLanguageChoiceMenu = OptionMenu(Screen, InputLanguageChoice, *LanguageChoices)
Label(Screen, text="Input Type").grid(row=0,column=0)
InputLanguageChoiceMenu.grid(row=1,column=0)

# Choice for output type
NewLanguageChoiceMenu = OptionMenu(Screen, TranslateLanguageChoice, *LanguageChoices)
Label(Screen, text="Output Type").grid(row=0, column=1)
NewLanguageChoiceMenu.grid(row=1, column=1)

Label(Screen, text="Enter Text").grid(row=2, column=0)
TextVar = StringVar()
TextBox = Entry(Screen, textvariable=TextVar).grid(row=2, column=1)

Label(Screen, text="Output Text").grid(row=3, column=0)
OutputVar = StringVar()
TextBox = Entry(Screen, textvariable=OutputVar).grid(row=3, column=1)

B = Button(Screen, text="Convert", command=Convert, relief=GROOVE).grid(row=4, column=0, columnspan=2)

mainloop()