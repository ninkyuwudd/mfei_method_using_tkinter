



from tkinter import Label


def custom_label(root,text,label_id):
    our_label = Label(root, text=text)
    our_label.pack(pady=10)
    label_id.set(our_label)

    