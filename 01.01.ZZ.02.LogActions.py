import sys
import logging
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("You need to provide at least one argument")
        sys.exit(1)
    
    directory=os.path.dirname(sys.argv[1])

    if not os.path.isdir(directory):
        print ("The directory does not exist")
        sys.exit(2)

    logging.basicConfig(filename=sys.argv[1],level=logging.DEBUG, 
                        format='%(asctime)s %(message)s')
    
    logging.info(f"{os.getenv('USER')} Starting program")

    logging.debug("Number of arguments: " + str(len(sys.argv)))
    logging.debug("The arguments are: " + str(sys.argv))

    logging.debug("The program name argument is: " + str(sys.argv[0]))
    logging.debug("The second argument is: " + str(sys.argv[1]))

    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")