from streamlit_authenticator.utilities.hasher import Hasher

passwords = []

hashed_passwords = Hasher(passwords).hash_passwords()

print(hashed_passwords)