from math import floor

word = input()
most_powerful_word = ""
most_powerful = 0

while word != "End of words":
    power = 0
    for w in word:
        power += ord(w)

    if word[0] in ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'):
        power = power * len(word)
    else:
        power = power / len(word)

    if power > most_powerful:
        most_powerful_word = word
        most_powerful = floor(power)
    word = input()

print(f'The most powerful word is {most_powerful_word} - {most_powerful}')