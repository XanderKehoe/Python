# Xander Kehoe
ui = input("Insert word: ")  # User Input
letters = {}
for x in range(len(ui)):  # Iterate through each letter
    if ui[x] in letters:
        letters[ui[x]] += 1
    else:
        letters[ui[x]] = 1

print(letters)