import sys

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}



def main():
    for key in kata:
        print(key, "was created by", kata[key])



if __name__ == "__main__":
    main()
