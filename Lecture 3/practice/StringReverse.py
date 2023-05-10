#4. Đảo ngược một chuỗi

def reverse(sentence):
    if len(sentence) == 0:
        return sentence
    else:
        return reverse(sentence[1:]) + sentence[0]

sentence = input("Original: ")
print("The reverse sentence is:", reverse(sentence))