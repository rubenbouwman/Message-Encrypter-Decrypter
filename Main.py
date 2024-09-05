import customtkinter as ctk

# ----------------- Setup -----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Message encrypter & decrypter")
root.geometry("500x650")

# ----------------- Variable Field -----------------
message = ""
key = ""
resultmessage = ""

# ----------------- Controller Functions -----------------
def EncryptButtonAction():
    message = message_textBox.get(0.0, "end")
    print("encrypt test " + message)

def DecryptButtonAction():
    message = message_textBox.get(0.0, "end")
    print("decrypt test " + message)

# ----------------- Front-End -----------------
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

message_textBox = ctk.CTkTextbox(master=frame, width=400)
message_textBox.pack(pady=20, padx=10)

entry2 = ctk.CTkEntry(master=frame, placeholder_text="Key", show="*")
entry2.pack(pady=12, padx=10)

encryptButton = ctk.CTkButton(master=frame, text="Encrypt message", command=EncryptButtonAction)
encryptButton.pack(pady=12, padx=10)

decryptButton = ctk.CTkButton(master=frame, text="Decrypt message", command=DecryptButtonAction)
decryptButton.pack(pady=12, padx=10)

result_textBox = ctk.CTkTextbox(master=frame, width=400)
result_textBox.pack(pady=20, padx=10)

# ----------------- Run -----------------
root.mainloop()