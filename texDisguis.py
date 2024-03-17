from colorama import Fore
from pyperclip import copy
from random import choice

print(Fore.RED + """█▀▀ █░░░█ █▀▀ █▀▀█ █▀▀█   █▀▀▄ █░░█ █▀▀█ █▀▀█ █▀▀ █▀▀
▀▀█ █▄█▄█ █▀▀ █▄▄█ █▄▄▀   █▀▀▄ █▄▄█ █░░█ █▄▄█ ▀▀█ ▀▀█
▀▀▀ ░▀░▀░ ▀▀▀ ▀░░▀ ▀░▀▀   ▀▀▀░ ▄▄▄█ █▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀\n\n\n""" + Fore.RESET)
# ‮ <--- left to right? more like right to left
while True:
     currentIndex = 0
     text = input(Fore.GREEN + "Original Text For Bypassing: " + Fore.MAGENTA)
     newText = ""
     Fore.RESET

     replacingValues = {
          "a": "а ạ ą ä à á ą",
          "c": "с ƈ ċ",
          "d": "ԁ ɗ",
          "g": "ġ",
          "e": "е ẹ ė é è",
          "h": "һ",
          "i": "і í ï",
          "j": "ј ʝ",
          "k": "κ",
          "l": "ӏ ḷ",
          "n": "ո",
          "o": "о ο օ ȯ ọ ỏ ơ ó ò ö",
          "p": "р",
          "u": "υ ս ü ú ù",
          "v": "ν ѵ",
          "x": "х ҳ",
          "y": "у ý",
          "?": "? Ɂ ʔ ॽ Ꭾ ꛫ ？",
          "t": "T Τ τ Т т Ꭲ ᴛ ⊤ ⟙ Ⲧ ꓔ ꭲＴ 𐊗 𐊱 𐌕 𑢼 𖼊 𝐓 𝑇 𝑻 𝒯 𝓣"
     }

     while True:
          try:
               if replacingValues.get(text[currentIndex]) != None:
                    newText = newText + choice(replacingValues.get(text[currentIndex]).split(" "))
               else:
                    newText = newText + text[currentIndex]
               currentIndex += 1
          except:
               break

     copy(newText)

     print(Fore.CYAN + newText)
     input(Fore.GREEN + "Text has been copied to clipboard!" + Fore.RESET)
