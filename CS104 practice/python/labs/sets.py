myset=set()
with open("q2-input.txt", "r") as file:
    for line in file:
        ar=set(line.strip().split(','))
        myset.update(ar)
print(len(myset))