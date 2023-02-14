import sys, getopt
import functions

def main(argv):
   inputFile = ''
   message = ''
   opts, args = getopt.getopt(argv,"hm:i:")
   for opt, arg in opts:
      if opt == '-h':
         print ('encode.py -m <message> -i <file>')
         sys.exit()
      elif opt in ("-m"):
            message = arg
      elif opt in ("-i"):
         inputFile = arg

   if (not inputFile) or (not message):
      print('error')
      sys.exit()

   functions.hide_the_message(message, inputFile)
   sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])