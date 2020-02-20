
class Library:

    def __init__(self, id, books, max_b, s_days):
        self.id = id
        self.books = books
        self.max_books = max_b
        self.signup_days = s_days
        self.signed_up = False

    '''
    def get_books_score():
        score = 0 
        for book in books:
            score += 

    '''
    

class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
        self.scanned = False



#####################################

class Parsing:
    
    def __init__(self, filepath):

        self.days = 0
        self.books = []
        self.libs = []

        book_counter = 0
        lib_counter = 0

        with open(filepath) as fp:
        
            # General definition
            line = fp.readline()
            arr = line.split()
            arr = [ int(x) for x in arr ]

            days = arr[2]

            # Book scores
            line = fp.readline()
            book_vals = line.split()

            book_vals = [ int(x) for x in book_vals ]

            # Saving objects
            for score in book_vals:
                b = Book(counter, score)
                self.books.append(b)
                book_counter += 1

            while line:

                # Line 1
                line = fp.readline()
                values = line.split()
                values = [ int(x) for x in values ]

                if len(values) == 0:
                    break

                lib = Library([], lib_counter, values[2], values[1])
                print(lib.id)

                # Line 2
                line = fp.readline()
                book_ids = line.split()
                book_ids = [ int(x) for x in book_ids ]

                for book_id in book_ids:
                    lib.books.append(self.books[book_id])

                if not line:
                    break
                
                self.libs.append(lib)
                lib_counter += 1
                

