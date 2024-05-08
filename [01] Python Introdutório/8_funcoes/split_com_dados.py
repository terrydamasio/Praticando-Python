def split_word(text):
    return text.split(" ")

text = "Olá meu nome é Terry Damasio Santos"
print(split_word(text))

token = split_word(text)

def split_letter(text):
    text = text.upper()
    for letter in text:
        print(letter)
        
split_letter(text)