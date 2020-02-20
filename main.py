from parsing import *
from operator import *

def start():
    output = ""
    submittedBooks = []
    
    parsing = Parsing('a_example.txt')
    libraries = parsing.libs
    books = parsing.books
    
    sortedLibraries = sorted(libraries, key=attrgetter('signup_days'))
    
    numLibraries = 0
    
    libraryString = ""
    
    for l in sortedLibraries:

        sortedBooks = sorted(books, key=attrgetter('score'))
        booksToSubmit = ""
        header = ""
        
        for b in sortedBooks:
            
            numBooks = 0
            
            if(not(b.id in submittedBooks)):
                
                #add it to submitted books
                submittedBooks.append(b.id)
                numBooks += 1
                booksToSubmit += str(b.id) + " "
                
        header = header + str(l.id) + " " + str(numBooks) + "\n"
        booksToSubmit += "\n"
        libraryString += header
        libraryString += booksToSubmit
        
        numLibraries += 1
        
    output += str(numLibraries)
    output += libraryString
    print(libraryString)
                
                
                
        
            
    

        
    

    
        
        
if __name__ == "__main__":
    start()