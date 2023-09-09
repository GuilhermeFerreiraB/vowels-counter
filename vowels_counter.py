sentence = input('Would you please write a sentence? ').lower()
vowels = ['a', 'e', 'i', 'o', 'u']  # w and y are sometimes not vowels
vowels_counter = 0
for letter in sentence:
    if letter in vowels:
        vowels_counter += 1
print(f'The sentence written has {vowels_counter} vowels.')
