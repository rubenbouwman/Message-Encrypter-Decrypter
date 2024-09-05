import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def EncodeButtonAction():
    print("Test ...Encoding")

def DecodeButtonAction():
    print("Test ...Decoding")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Vigenere Cipher")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Message")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Key", show="*")
entry2.pack(pady=12, padx=10)

encodeButton = customtkinter.CTkButton(master=frame, text="Encode message", command=EncodeButtonAction)
encodeButton.pack(pady=12, padx=10)

decodeButton = customtkinter.CTkButton(master=frame, text="Decode message", command=DecodeButtonAction)
decodeButton.pack(pady=12, padx=10)

root.mainloop()