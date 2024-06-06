import spacy
import pandas as pd
import numpy as np
import re
import collections

def main():
    f = open("test.txt","r", encoding="utf-8")
    df = f.read()
    f.close()

    df = df[:4000]  #4000文字抜き出す

    nlp = spacy.load('ja_ginza')
    doc = nlp(df)

    count_word = collections.Counter(token.text for token in doc)
    print("形態素:",count_word)
    print("形態素の数 ：",len(count_word))

    #形態素毎の出現頻度
    output =[]
    for word, count in count_word.most_common():
        if count > 1:
            output.append([word, count])

    df = pd.DataFrame(output)
    df = df.rename(columns={0: "word", 1: "count"})
    df.to_csv("output.csv")

if __name__ == "__main__":
    main()