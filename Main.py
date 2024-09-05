import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x450")

def EncodeButtonAction():
    resultTextBox.set
    print("Test ...Encoding")

def DecodeButtonAction():
    print("Test ...Decoding")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Vigenere Cipher")
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Message")
entry1.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master=frame, placeholder_text="Key", show="*")
entry2.pack(pady=12, padx=10)

encodeButton = ctk.CTkButton(master=frame, text="Encode message", command=EncodeButtonAction)
encodeButton.pack(pady=12, padx=10)

decodeButton = ctk.CTkButton(master=frame, text="Decode message", command=DecodeButtonAction)
decodeButton.pack(pady=12, padx=10)

resultTextBox = ctk.CTkTextbox(master=frame, width=250, height=100)
resultTextBox.configure(state=ctk.DISABLED)
resultTextBox.pack(pady=12, padx=10)


root.mainloop()