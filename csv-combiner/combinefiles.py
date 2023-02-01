#Gianna Jarmain

import csv
import sys
import os.path as path
import pandas as pd


def write_to_stdout(inputFile):
    fileContents = pd.read_csv(inputFile)
    for i, row in fileContents.iterrows():
         sys.stdout.write(row['email_hash'] + '\t' + row['category'] + '\t' + path.basename(inputFile).split('/')[-1] + '\n')


def main():
    arguments = sys.argv
    
    
    sys.stdout.write('email_hash' + '\t' +'category' +'\t' +'filename')
    sys.stdout.write('\n')

    for inputFile in arguments[1:]:
        write_to_stdout(inputFile)


if __name__ == '__main__':
    main()
        
