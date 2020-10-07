from googletrans import Translator
def translate(the_text):
    translator = Translator()
    return translator.translate(the_text,dest='ru').text
print(translate('hello, how are you?'))
