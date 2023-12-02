import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("You need to provide at least one argument")
        sys.exit(1)
    
    print ("Number of arguments: ", len(sys.argv))
    print ("The arguments are: " , str(sys.argv))
        
    print ("The program name argument is: " , str(sys.argv[0]))
    print ("The second argument is: " , str(sys.argv[1]))