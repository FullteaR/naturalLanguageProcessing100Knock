from knock53 import root, marks

if __name__ == "__main__":
    document = root[0]
    scentences = document[1]
    for scentence in scentences:
        tokens = scentence[0]
        for token in tokens:
            for e in token:
                if e.tag=="word" and (e.text not in marks):
                    word=e.text
                if e.tag == "POS" and e.text=="NNP":
                    print(word)
