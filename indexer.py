#   WORD INDEXER
#   words in text file have to be provided one by one in a single line.
#   index and words are delimited by tab

file = input("Input file: ")

with open(file, "r") as src:
    with open("output.txt", "w") as dst:
        index = 1
        for x in src:
            dst.write(str(index) + '\t' + x)
            index = index + 1
