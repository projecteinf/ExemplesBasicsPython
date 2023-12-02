import sys
import logging

if __name__ == "__main__":
    logging.basicConfig(filename='python.log',level=logging.DEBUG, 
                        format='%(asctime)s %(message)s')
    
    logging.info("Starting program")

    logging.debug("Number of arguments: " + str(len(sys.argv)))
    logging.debug("The arguments are: " + str(sys.argv))

    logging.debug("The program name argument is: " + str(sys.argv[0]))
    logging.debug("The second argument is: " + str(sys.argv[1]))

    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")