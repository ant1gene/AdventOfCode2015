def main():
    ListCalc = 0
    general = 0
    f = open("input.txt", "r")
    inputFile = list(f.read())
    while len(inputFile) > ListCalc:
        if inputFile[ListCalc] == "(":
            general += 1
        elif inputFile[ListCalc] == ")":
            general -= 1
        else:
           print("read_error") 
        ListCalc += 1
    print(general)

if __name__ == "__main__":
    main()
