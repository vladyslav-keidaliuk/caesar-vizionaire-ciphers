import customtkinter
import functions

app = customtkinter.CTk()
app.title("Caesar's & Vizionaire's cipher with a keyword")
app.geometry("1000x1000")
app.grid_columnconfigure((0, 1), weight=1)

Font = ("Arial", 20, "bold")


def enchipher_click():
    if combobox.get() == "Caesar's cipher":

        text = functions.enchip(entry_phrase_enchip.get(1.0,"end"), entry_key_enchip.get())
        result = f"Result: \n{text}"

        textbox_enchip_result.delete(1.0, "end")
        textbox_enchip_result.insert(1.0, result)

    elif combobox.get() == "Vizionaire's cipher":

        text = functions.enchip_vigenere(entry_phrase_enchip.get(1.0, "end"), entry_key_enchip.get())
        result = f"Result: \n{text}"
        textbox_enchip_result.delete(1.0, "end")
        textbox_enchip_result.insert(1.0, result)


def dechipher_click():
    if combobox.get() == "Caesar's cipher":
        text = functions.dechip(entry_phrase_dechip.get(1.0,"end"), entry_key_dechip.get())
        result = f"Result: \n{text}"

        textbox_dechip_result.delete(1.0, "end")
        textbox_dechip_result.insert(1.0, result)

    elif combobox.get() == "Vizionaire's cipher":

        text = functions.dechip_vigenere(entry_phrase_dechip.get(1.0, "end"), entry_key_dechip.get())
        result = f"Result: \n{text}"
        textbox_dechip_result.delete(1.0, "end")
        textbox_dechip_result.insert(1.0, result)


label = customtkinter.CTkLabel(app, text="Enchipher", fg_color="transparent", font=Font)
label.grid(row=0, column=0, padx=20, pady=20)

label = customtkinter.CTkLabel(app, text="Dechipher", fg_color="transparent", font=Font)
label.grid(row=0, column=1, padx=20, pady=20)

entry_phrase_enchip = customtkinter.CTkTextbox(app, font=Font, height=300, width=500, wrap="word")
entry_phrase_enchip.grid(row=1, column=0, padx=20, pady=20)

entry_phrase_dechip = customtkinter.CTkTextbox(app, font=Font, height=300, width=500, wrap="word")
entry_phrase_dechip.grid(row=1, column=1, padx=20, pady=20)

entry_key_enchip = customtkinter.CTkEntry(app, placeholder_text="Key", font=Font, height=3, width=250)
entry_key_enchip.grid(row=2, column=0, padx=20, pady=20)

entry_key_dechip = customtkinter.CTkEntry(app, placeholder_text="Key", font=Font, height=3, width=250)
entry_key_dechip.grid(row=2, column=1, padx=20, pady=20)

button_enchip = customtkinter.CTkButton(app, text="To enchip", command=enchipher_click, font=Font)
button_enchip.grid(row=3, column=0, padx=20, pady=20)

button_dechip = customtkinter.CTkButton(app, text="To dechip", command=dechipher_click, font=Font)
button_dechip.grid(row=3, column=1, padx=20, pady=20)

textbox_enchip_result = customtkinter.CTkTextbox(app, font=Font, height=300, width=500, wrap="word")
textbox_enchip_result.grid(row=4, column=0, padx=20, pady=20)

textbox_dechip_result = customtkinter.CTkTextbox(app, font=Font, height=300, width=500, wrap="word")
textbox_dechip_result.grid(row=4, column=1, padx=20, pady=20)


def combobox_callback(choice):
    # print("combobox dropdown clicked:", choice)
    entry_phrase_enchip.delete(1.0, "end")
    entry_key_enchip.delete(0, "end")
    textbox_enchip_result.delete("1.0","end")
    entry_phrase_dechip.delete(1.0, "end")
    entry_key_dechip.delete(0, "end")
    textbox_dechip_result.delete("1.0", "end")

combobox = customtkinter.CTkComboBox(app, values=["Caesar's cipher", "Vizionaire's cipher"],
                                     command=combobox_callback, font=Font, width=250)
combobox.set("Caesar's cipher")
combobox.grid(row=5, column=0, padx=20, pady=20)

app.mainloop()
