from parsing import *;
from operator import itemgetter, attrgetter

def start(libraries):
    
    sortedLibraries = sorted(libraries, key=attrgetter('signup_days'))
    parsing = Parsing()
    
        
        
if __name__ == "__main__":
    #stuff