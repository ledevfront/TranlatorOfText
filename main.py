from googletrans import Translator

translater = Translator()

your_text = "the text you want to translate"

out = translater.translate(your_text, dest="en")#en =the target language

print(out)

#don't forget to install that "pip install googletrans==3.1.0a0"