import sys, getopt
import functions

def main(argv):
   inputFile = ''
   opts, args = getopt.getopt(argv,"hi:")
   for opt, arg in opts:
      if opt == '-h':
         print ('encode.py -i <file>')
         sys.exit()
      elif opt in ("-i"):
         inputFile = arg

   if (not inputFile):
      print('error')
      sys.exit()
   
   functions.find_the_message(inputFile)
   sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])