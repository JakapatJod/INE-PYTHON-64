inputmsg = input('In put string you want to swap words: ').split()
print(inputmsg.split())
separatewords = inputmsg.split()

print("seprate words")
for i in separatewords:
    print(i)

print("Modify each words")
print(len(separatewords))
for j in range(len(separatewords)):
    separatewords[j] = 'G' + separatewords[j]
    print(separatewords[j])

print(separatewords)
print(" ".join(separatewords))