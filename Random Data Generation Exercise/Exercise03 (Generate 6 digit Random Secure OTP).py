""" Generate 6 digit Random Secure OTP """
import secrets

#Getting systemRandom class instance out of secrets module
secretsGenerator = secrets.SystemRandom()

print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000,999999)

# Format with space after 3 digits
formatted_otp = f"{otp // 1000} {otp % 1000:03d}"
print("Secure random OTP is", formatted_otp)

#####################################################################################################################################################
import secrets
import tkinter as tk

def generate_otp():
    otp = secrets.SystemRandom().randrange(100000, 999999)
    formatted_otp = f"{otp // 1000} {otp % 1000:03d}"
    otp_label.config(text=f"🔐 Your OTP: {formatted_otp}", fg="green")

# GUI Setup
root = tk.Tk()
root.title("Secure OTP Generator")
root.geometry("300x150")
root.configure(bg="#f0f0f0")

# Button
generate_btn = tk.Button(root, text="Generate OTP", command=generate_otp, bg="blue", fg="white", font=("Arial", 12))
generate_btn.pack(pady=20)

# Label for OTP
otp_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
otp_label.pack()

root.mainloop()

