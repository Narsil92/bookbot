# read content of the file located in frankenstein.txt

def read_book(book_path):
    with open(book_path) as f: # we'are getting book_path from main()
     return f.read()
    

#function to count number of words inside fankenstein.txt

def number_of_words(book_contents):
    words=book_contents.lower() # Reading book_contents from main and makin all words to lower letters
    output_number=words.split()
    return(len(output_number)) 

#function to count number of character occurence in entire text without duplicates

def count_characters(book_contents):
    text=book_contents.lower() # Reading book_contents from main and makin all words to lower letters
    char_count={}              # dictionary that will keep track of each letter and how many times it's occured in text 
    for char in text:
      if char.isalpha():       #check if character is alphabetical letter
       if char in char_count: 
        char_count[char]+=1    # Increment count if character exists in dictionary
       else: 
        char_count[char]=1     # Add new character to dictionary with count 1

    return char_count          # Return the dictionary with character counts

#Function that will operate as my print into console
def print_report(word_count, sorted_char_count, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("\n")      
    print("Characters (and how many times they occuring) in that document are:")
    for char, count in sorted_char_count.items():
        print(f"The '{char}' character was found {count} times")
    
    


# keep file content in variable
def main():
  book_path = "books/frankenstein.txt"
  book_contents = read_book(book_path)   
  word_count= number_of_words(book_contents) #addition to get info about number of words inside frankenstein.txt
  char_count=count_characters(book_contents) # returning info about how many time character occured in text
  sorted_char_count = dict(sorted(char_count.items())) # Sort the character count dictionary by character
  print_report(word_count, sorted_char_count, book_path)
  #print(sorted_char_count) # just my quick way to lookup if each part of main behave as im expecting 

# call only in this file
if __name__ == "__main__":
 main()

