import sys


class Evaluator:
    
    @staticmethod
    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            print("ERROR")
            sys.exit()
        if len(coefs) != len(words):
            return -1
        return sum([len(word) * coef for word, coef in zip(words, coefs)])

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            print("ERROR")
            sys.exit()

        if len(coefs) != len(words):
            return -1
        return sum([len(words[i]) * coefs[i] for i in range(len(words))])
    


if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    res = Evaluator.zip_evaluate(coefs, words)

    print(res)
