from googletrans import Translator
def translate(the_text):
    translator = Translator()
    return translator.translate(the_text,dest='ru').text

print(translate('What have we found? Same old fears'))
print(translate("Pink Floyd or Avenged Sevenfold"))
print(translate("July 2019"))
