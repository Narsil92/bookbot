# read content of the file located in frankenstein.txt

def read_book():
    with open("books/frankenstein.txt") as f:
     return f.read()
    

#function to count number of words inside fankenstein.txt
def number_of_words():
    words=read_book()
    output_number=words.split()
    return(len(output_number))    
    
# keep file content in variable
def main():
 book_contents = read_book()   
 print(book_contents)
 word_count= number_of_words() #addition to get info about number of words inside frankenstein.txt
 print(f"number of words inside frankenstein.txt is: {word_count}") #returning info about words number to the terminal

# call only in this file
if __name__ == "__main__":
 main()

