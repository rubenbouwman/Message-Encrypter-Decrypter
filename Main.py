import customtkinter as ctk
from VigenereCipher import encrypt, decrypt
from PIL import Image

# ----------------- Setup -----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Message encrypter & decrypter")
root.iconbitmap('Images/FalloutHackingIcon.ico')
root.geometry("550x700")
font = ctk.CTkFont('Roboto light', 20)
font_button = ctk.CTkFont('Roboto light', 14)
font_box = ctk.CTkFont('Roboto', 20)

# ----------------- Variable Field -----------------
message = ""
key = ""
logo = ctk.CTkImage(dark_image=Image.open('Images/FalloutHackingIcon.png'), size=(120, 120))
# ----------------- Controller Functions -----------------
def GetData():
    global message
    global key
    message = message_textBox.get(0.0, "end")
    key = Key_entry.get()

def EncryptButtonAction():
    GetData()
    resultMessage = encrypt(message, key)
    result_textBox.delete(0.0, "end")
    result_textBox.insert("end", resultMessage)
    print("encrypt result: " + resultMessage)

def DecryptButtonAction():
    GetData()
    resultMessage = decrypt(message, key)
    result_textBox.delete(0.0, "end")
    result_textBox.insert("end", resultMessage)
    print("decrypt result: " + resultMessage)

# ----------------- Front-End -----------------
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label1 = ctk.CTkLabel(master=frame, text="", image=logo)
label1.pack(pady=(10))

label1 = ctk.CTkLabel(master=frame, text="Your message", font=font)
label1.pack(pady=(20, 5))

message_textBox = ctk.CTkTextbox(master=frame, width=400, height=125, wrap="word", font=font_box)
message_textBox.pack(pady=(5, 20), padx=10)

Key_entry = ctk.CTkEntry(master=frame, placeholder_text="Key")
Key_entry.pack(pady=12, padx=10)

buttonFrame1 = ctk.CTkFrame(master=frame)
buttonFrame1.pack(pady=10)

encryptButton = ctk.CTkButton(master=buttonFrame1, text="Encrypt", command=EncryptButtonAction, font=font_button)
decryptButton = ctk.CTkButton(master=buttonFrame1, text="Decrypt", command=DecryptButtonAction, font=font_button)
encryptButton.grid(row=0, column=0, pady=10, padx=10)
decryptButton.grid(row=0, column=1, pady=10, padx=10)

label1 = ctk.CTkLabel(master=frame, text="Results", font=font)
label1.pack(pady=5)
result_textBox = ctk.CTkTextbox(master=frame, width=400, height=125, wrap="word", font=font_box)
result_textBox.pack(pady=(5, 20), padx=10)

# ----------------- Run -----------------
root.mainloop()