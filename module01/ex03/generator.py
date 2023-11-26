import sys


def random_shuffle(words):
    for i in range(len(words)):
        j = random.randint(0, len(words) - 1)
        words[i], words[j] = words[j], words[i]
    return words




def generator(text, sep=" ", option=None):
    if not isinstance(text, str):
        print("ERROR")
        sys.exit()

    words = text.split(sep)
    if option == "shuffle":
        random_shuffle(words)
    elif option == "unique":
        words = list(set(words))
    elif option == "ordered":
        words.sort(key=str.lower)
    for word in words:
        yield word


if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
   