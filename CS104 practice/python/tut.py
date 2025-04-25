# // does integer division and reports floor as the answer not the estimate value.
# string.strip() function deletes the whitespace characters if any at both ends of the string
line = "  hehEBoi wassup "
print(line.strip())
#string.split() function breaks words of the line and returns an array of the words.
words=line.split()
print(words)
print(line.upper())
print(line.lower())
print("_".join(words))
print(line.replace("was", "joker is back")) #replaces all occurences of was with "joker is back"...like here it becomes hehEBoi joker is backsup
g=4.4305847507452            
print(f"g till 3 decimal places is {g:.3f}")
l=[1,2,3,2,4]
l.remove(2) #becomes [1,3,2,4]
print(l)
l.remove(2) #becomes [1,3,4]
print(l)
#l.remove(x) removes the first occurence of x in the list l.
a=(1,2,3,1,1) #tuple
print(a.count(1)) #gives 3 cause 3 occurences
print(a.index(3)) #gives 2 cause 3 is at index 2
b={1,2,4,3}
print(b)
b.add(69)
print(b)
b.add(42)
print(b)

#dictionaries require key to be of a hashable type. Eg. numpy arrays are NOT hashable and cannot directly be used in a dictionary

print(bool([])) #empty list is false nic, 0 is also false ofc
print(bool({})) #okay so i guess anything "empty" is false

def add(x:int,y:int) -> int : #this is for code readability, python does not fix data type
    return x+y

print(gcd(998244359987710471,99824435698771045))