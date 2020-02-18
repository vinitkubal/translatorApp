from googletrans import Translator


translator = Translator()

text = translator.translate(text="I was walking down the street and i saw him with his dog ", dest="mr")

#from translate import Translator

#translator = Translator(to_lang="hi")

#text = translator.translate(text="I want to have sex with you Hana")

print(text)