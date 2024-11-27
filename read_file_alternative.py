# open file frankenstein.txt and printing its content 

def main():
 with open("books/frankenstein.txt") as f:
     file_contents = f.read()
     print(file_contents)

main()
