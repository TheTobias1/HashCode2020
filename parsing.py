
class Library:

    def __init__(self, books, max_b, s_days):
        self.books = books
        self.max_books = max_b
        self.signup_days = s_days

class Book:
    def __init__(self, score):
        self.score = score



#####################################

class Parsing:
    
    def __init__(self, filepath):

        self.days = 0
        self.books = []
        self.libs = []

        with open(filepath) as fp:
        
            # General definition
            line = fp.readline()
            arr = line.split()
            arr = [ int(x) for x in arr ]

            days = arr[2]

            # Book scores
            line = fp.readline()
            books = line.split()

            self.books = [ int(x) for x in self.books ]

            while line:

                # Line 1
                line = fp.readline()
                values = line.split()
                values = [ int(x) for x in values ]

                if len(values) == 0:
                    break

                lib = Library([], values[2], values[1])
                
                # Line 2
                line = fp.readline()
                book_ids = line.split()
                book_ids = [ int(x) for x in book_ids ]

                for book_id in book_ids:
                    lib.books.append(book_id)

                if not line:
                    break
                
                self.libs.append(lib)
                

