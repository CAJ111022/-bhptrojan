import os

def run(**args):
    print("[*] In dirlister modiles.")
    files = os. listdir(".")
    return str(files)

