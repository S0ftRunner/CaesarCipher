alphabet = "abcdefghijklmnopqrstuvwxyz" # basic english alphabet
mod = 26

def encryption(text, alphaNext):
    print("Your new text is:", end=' ')
    for i in text:
        if not i.isalpha():
            print(i, end='')
        else:
            print(alphabet[(alphabet.find(i) + alphaNext) % mod], end='')



text = input("Hello to Caesar Cipher program. Enter your text, please: ")

alphaNext = int(input("Enter a key: "))

print("Your text is:", text)
text.lower()
encryption(text, alphaNext)




