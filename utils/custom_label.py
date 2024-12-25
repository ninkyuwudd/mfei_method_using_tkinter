



from tkinter import Label


def custom_label(root,text,label_id):
    our_label = Label(root, text=text, font=("Helvetica", 15))
    our_label.grid(pady=10)
    label_id.set(our_label)

    