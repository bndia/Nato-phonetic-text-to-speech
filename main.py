import pandas
import os
import gtts
from playsound import playsound

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {nato.letter: nato.code for (index, nato) in nato_data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic_word = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Soory. only letters in the alphabet plaese.")
        generate_phonetic()
    else:
        print(phonetic_word)
        for nato_word in phonetic_word:
            sound = os.path.dirname(__file__) + f"/sounds/{nato_word}.mp3"
            playsound(sound)
            # tts = gtts.gTTS(f"{nato_word}", lang="en")
            # tts.save(f"{nato_word}.mp3")
            # playsound(f"{nato_word}.mp3")
            # os.remove(f"{nato_word}.mp3")


generate_phonetic()
