#!/usr/bin/python3

import csv, json, sys
from jinja2 import Environment, FileSystemLoader

def ImportCSV(csvFileName):
    csvFileItemsFinal = []
    with open (csvFileName, newline='') as csvFile:
        csvData = csv.reader(csvFile, delimiter=',')
        for row in csvData:
            if row:
                csvFileItemsFinal.append(row)
    return csvFileItemsFinal

def MakeFromTemplate(csvFileItems):
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    env.filters['jsonify'] = json.dumps
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.rstrip_blocks = True
    template = env.get_template(activeTemplate)
    output = template.render(csvFileItems=csvFileItems)
    return (output)

def WriteOutputfFile(outputData):
    outputFile = open(outputFileName, "w")
    outputFile.write(outputData)
    outputFile.close()

def CheckForArgs(argv):
    numberOfArgs = len(sys.argv) - 2
    if not numberOfArgs:
        print ("I need more food: csvExport.py <csvfile> <templates/jinja2 template> <optional output file name>")
        print ("")
        return False
    else:
        return True

if __name__ == '__main__':
    canWeRun = CheckForArgs(sys.argv)
    if canWeRun:
        csvFileName = sys.argv[1]
        print ("using csv file:", csvFileName)
        activeTemplate = sys.argv[2]
        print ("   template is:", activeTemplate)
        if len(sys.argv) > 3:
            outputFileName = sys.argv[3]
            print ("   output file:", outputFileName)
        else:
            outputFileName = ''
            print ("   output file: <nada>")
        csvFileItems = ImportCSV(csvFileName)               # Import CSV and put into variable
        processedCSVData = MakeFromTemplate(csvFileItems)   # Create output using jinja2 template and csv
        if outputFileName:
            WriteOutputfFile(processedCSVData)
        else:                                               # Print to screen if no filename given
            print ("\n*** Copy starting with next line ***")
            print (processedCSVData)
            print("*** Copy ending with previous line ***")
        print ("I'm done now!")
        print ("*** WARNING: A list added via API MAY need to include new AND EXISTING entries or existing entries may be deleted.")



