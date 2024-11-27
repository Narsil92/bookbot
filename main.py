# read content of the file located in frankenstein.txt

def read_book():
    with open("books/frankenstein.txt") as f:
     return f.read()
    
# keep file content in variable
def main():
 book_contents = read_book()   
 print(book_contents)

# call only in this file
if __name__ == "__main__":
 main()

