import sys

positions={
    "punjabi":0,
    "hindi":1,
    "english":2
}

def query1(language, translate):
    lang=[]
    for words in translate:
        if (words[positions[language]]!="UNK"):
            lang.append(words[positions[language]])
    lang.sort(reverse=True)
    return lang

def query2(language1, language2, translate):
    ls=[]
    for words in translate:
        if (words[positions[language1]]!="UNK" and words[positions[language2]]!="UNK"):
            tup=(words[positions[language1]], words[positions[language2]])
            ls.append(tup)
    ls.sort()
    return ls

def query3(language1, language2, translate, word):
    for words in translate:
        if (words[positions[language1]]==word):
            return words[positions[language2]]
    return "UNK"


def makelist():
    translate=[]
    with open("translations.csv", "r") as file:
        for line in file:
            array=line.strip().split(',')
            found=False
            for words in translate:
                if words[positions[array[0]]]==array[1]:
                    words[positions[array[2]]]=array[3]
                    found=True
                    break
                if words[positions[array[2]]]==array[3]:
                    words[positions[array[0]]]=array[1]
                    found=True
                    break
            if (not found):
                ar=["UNK","UNK","UNK"]
                ar[positions[array[0]]]=array[1]
                ar[positions[array[2]]]=array[3]
                translate.append(ar)
    return translate


translations=makelist()
n=len(sys.argv)
if (n==3):
    response=query1(sys.argv[2], translations)
    print(response)
elif (n==4):
    response=query2(sys.argv[2], sys.argv[3], translations)
    print(response)
else:
    response=query3(sys.argv[2], sys.argv[3], translations, sys.argv[4])
    print(response)
