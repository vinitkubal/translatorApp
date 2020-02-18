from googletrans import Translator


translator = Translator()
def convert(data, dest):
    sen = translator.translate(text=data, dest=dest)
    return sen.text