import sys
import logging

if __name__ == "__main__":
    with (open('python.log', 'w')) as fitxer:
        fitxer.write("Starting program\n")
        fitxer.write("Number of arguments: " + str(len(sys.argv)) + "\n")
        fitxer.write("The arguments are: " + str(sys.argv) + "\n")
        fitxer.write("The program name argument is: " + str(sys.argv[0]) + "\n")
        fitxer.write("The second argument is: " + str(sys.argv[1]) + "\n")
        fitxer.write("This is a warning message\n")
        fitxer.write("This is an error message\n")
        fitxer.write("This is a critical message\n")
    
    with (open('python.log', 'r')) as fitxer:
        for linia in fitxer:
            print(linia)