import random
L = ["Rawr", "that", "means", "I", "love", "you", "in", "dinosaur"]
match = set()
j = 1
while set(L) != set(match):
    i = random.sample(L, random.randint(1, j))
    print(i)
    match = match.union(i)
    if (j-1) < L.__len__():
        j = random.randint(j, j+1)

ui = input("All words said, insert your answer: ")
newL = ' '.join(L)
while True:
    if ui == newL:
        print("Correct!")
        break
    else:
        ui = input("Incorrect, try again: ")

