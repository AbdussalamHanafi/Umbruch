from Control import *
from tkinter import *

class TextUmbrecher:

    def __init__(self):

        root = Tk()
        root.title = "Textumbruch"
        root.minsize(width=666, height=666)

        vorher_label = Label(root, text="Vorher", font="bold")
        vorher_label.grid(row=0, column=0, padx=8, sticky=W)

        frame_vorher_text = Frame()
        vorher_text = Text(frame_vorher_text)
        scroll = Scrollbar(frame_vorher_text)
        scroll.grid(row=0, sticky=E+N+S)
        vorher_text.grid(row=0, sticky=W+E+N+S)
        scroll.config(command=vorher_text.yview)
        vorher_text.config(yscrollcommand=scroll.set)
        frame_vorher_text.grid(row=1, padx=10, pady=5, column=0, columnspan=2, sticky=W+E + N + S)
        frame_vorher_text.columnconfigure(0, weight=1)


        after_label = Label(root, text="Nachher", font="bold")
        after_label.grid(row=3, column=0, pady=(30,0), padx=8, sticky=W)

        frame_nachher_text = Frame()
        nachher_text = Text(frame_nachher_text)
        scroll_after = Scrollbar(frame_nachher_text)
        scroll_after.grid(row=0, sticky=E+N+S)
        nachher_text.grid(row=0, sticky=W+E+N+S)
        scroll_after.config(command=nachher_text.yview)
        nachher_text.config(yscrollcommand=scroll_after.set)
        frame_nachher_text.grid(row=4, padx=10, column=0, pady=5, columnspan=2, sticky=W+E + N + S)
        frame_nachher_text.columnconfigure(0, weight=1)

        frame_einstellungen = Frame(root)

        breite_label = Label(frame_einstellungen, text="Breite in Zeichen:",  font="bold")
        breite_label.grid(row=0, column=0)

        breite_entry = Entry(frame_einstellungen, width=30)
        breite_entry.grid(row=0, column=1, padx=(10,100))

        start_but = Button(frame_einstellungen, text="Umbrechen", command=self.__set_text)
        start_but.grid(row=0, column=2)

        frame_einstellungen.grid(row=5, padx=10, column=0, pady=5, columnspan=2, sticky=W+E + N + S)

        self.vorher_text = vorher_text
        self.nachher_text = nachher_text
        self.anz = breite_entry
        root.columnconfigure(0, weight=1)
        root.mainloop()

    def __set_text(self):
        text = self.vorher_text.get("1.0", END)
        anz = int(self.anz.get())
        nachher_text = get_umbruch_text(text, anz)
        self.nachher_text.delete("1.0", END)
        self.nachher_text.insert(END, nachher_text)



test = TextUmbrecher()


