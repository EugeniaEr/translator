from translate import Translator

translator = Translator(from_lang="english", to_lang="russian")
phrase = input('Write the phrase that needs to be translated: ')
translation = translator.translate(phrase)
print(translation)
