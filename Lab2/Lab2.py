

def main():
    sentence = str(input("Write a sentence: "))
    print(sentence[0:sentence.index(" ")])
    print(sentence[(sentence.index(" ")+1):])

if __name__ == "__main__":
    main()
