""" Generate Random Token and URL """
# Write a code to generate random secure token of 64 bytes and random URL.

import secrets

print("Random secure Hexadecimal token is:-", secrets.token_hex(64))
print("Random secure URL is:-", secrets.token_urlsafe(64))
