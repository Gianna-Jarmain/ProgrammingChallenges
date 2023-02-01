import csv
import sys
import os.path as path
import pandas as pd

readAccessories = pd.read_csv('/Users/giannajarmain/Desktop/ProgrammingChallenges/csv-combiner/fixtures/accessories.csv')
readClothing = pd.read_csv('/Users/giannajarmain/Desktop/ProgrammingChallenges/csv-combiner/fixtures/clothing.csv')
readHouseholdItems = pd.read_csv('/Users/giannajarmain/Desktop/ProgrammingChallenges/csv-combiner/fixtures/household_cleaners.csv')
#outputFile = ('newCombined.csv')

def write_to_outFile(writer, inputFile):
    fileContents = pd.read_csv(inputFile)
    for i, row in fileContents.iterrows():
         writer.writerow([
               row['email_hash'],
               row['category'],
               path.basename(inputFile).split('/')[-1]
         ])

         sys.stdout.write(row['email_hash'] + '\t' + row['category'] + '\t' + path.basename(inputFile).split('/')[-1] + '\n')


def main():
    arguments = sys.argv
    
    with open('combined.csv', 'w', encoding='utf-8') as outputFile:
        writer = csv.writer(outputFile, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
        writer.writerow(['email_hash', 'category', 'filename'])

        #Write to stdout
        sys.stdout.write('email_hash' + '\t' +'category' +'\t' +'filename')
        sys.stdout.write('\n')

        #We don't want the python script, just the input files. Write to output file.
        for inputFile in arguments[1:]:
            write_to_outFile(writer, inputFile)


if __name__ == '__main__':
    main()
        
