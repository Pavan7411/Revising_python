word=""
sentence=""
print("Please enter some words.")
print("Include a period(.) when you are finsihed. ")
while "." not in word:
    word = input("Next word: ")
    sentence= word + " " + sentence
    
print()
print("You said the following:")
print(sentence)
