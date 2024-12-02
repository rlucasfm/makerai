import streamlit_authenticator as stauth

passwords = ['bruna_pass']

hashed_passwords = stauth.Hasher(passwords).generate()

print(hashed_passwords)