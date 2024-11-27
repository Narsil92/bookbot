# read content of the file located in frankenstein.txt

def read_book():
    with open("books/frankenstein.txt") as f:
     return f.read()
    

#function to count number of words inside fankenstein.txt
def number_of_words():
    words=read_book().lower() #makin all words to lower letters
    output_number=words.split()
    return(len(output_number)) 

#function to count number of character occurence in entire text without duplicates
def count_characters():
    text=read_book().lower() # all text to string and to lower letters
    char_count={} # dictionary that will keep track of each letter and how many times it's occured in text
    for char in text:
      if char.isalpha(): #check if character is alphabetical letter
       if char in char_count: 
        char_count[char]+=1 # Increment count if character exists in dictionary
       else: 
        char_count[char]=1 # # Add new character to dictionary with count 1

    return char_count  # Return the dictionary with character counts


# keep file content in variable
def main():
  book_contents = read_book()   
  print(book_contents)

 #addition to get info about number of words inside frankenstein.txt
  word_count= number_of_words() 
 #returning info about words number to the terminal
  print(f"number of words inside frankenstein.txt is: {word_count}") 

# returning info about how many time character occured in text
  char_count=count_characters() 
 # Sort the character count dictionary by character
  sorted_char_count = dict(sorted(char_count.items()))
 # Print out the sorted character counts
  print("Character counts in order:")
  for char, count in sorted_char_count.items():
        print(f"'{char}': {count}")


# call only in this file
if __name__ == "__main__":
 main()

