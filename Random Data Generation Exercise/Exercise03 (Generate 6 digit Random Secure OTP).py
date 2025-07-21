""" Generate 6 digit Random Secure OTP """
import secrets

#Getting systemRandom class instance out of secrets module
secretsGenerator = secrets.SystemRandom()

print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000,999999)

# Format with space after 3 digits
formatted_otp = f"{otp // 1000} {otp % 1000:03d}"
print("Secure random OTP is", formatted_otp)

