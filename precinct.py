import optparse
import sys
from string import printable

def parse_args():
    """Parse and return command-line arguments"""

    parser = optparse.OptionParser(description='precinct filtering')
    parser.add_option('-p', '--precinct_filename', type='string', help='path to input precinct list file')
    parser.add_option('-e', '--election_filename', type='string', help='path to input election data file')
    (opts, args) = parser.parse_args()

    mandatories = ['precinct_filename','election_filename']
    for m in mandatories:
        if not opts.__dict__[m]:
            print('mandatory option ' + m + ' is missing\n')
            parser.print_help()
            sys.exit()

    return opts

def parse_precinct(precinct_filename):
    """ Return array of precinct names """
    precincts = []
    with open(precinct_filename, 'r') as p_file:
        for line in p_file:
            line = line.replace(" ", "")
            line = line.replace("\r", "")
            line = line.replace("\n", "")
            line = ''.join(char for char in line if char in printable)
            print(repr(line))
            precincts.append(line.upper())

    p_file.close()

    return precincts

def parse_params(in_file, out_file, p_array):

    with open(in_file,"r") as inputFile:
        with open(out_file,"w") as outputFile:
            for line in inputFile:
                lineList = line.split(",")
                precinctData = lineList[20]
                precinctData = precinctData.replace(" ", "")
                precinctData = precinctData.replace('"', '')
                matchBool = False
                for p in p_array:
                    print("printing data from input file")
                    print(precinctData)
                    print(type(precinctData))
                    print(len(precinctData))
                    print("printing array parameter")
                    print(p)
                    print(type(p))
                    print(len(p))
                    if (p == precinctData):
                        matchBool = True
                if (matchBool == True):
                    print("TRUUUUUUUUUUEEEEEEEEEEE")
                    outputFile.write(line)
    outputFile.close()
    inputFile.close()
    return

def main():

    # parse commandline arguments
    opts = parse_args()

    precincts = parse_precinct(opts.precinct_filename)
    parse_params(opts.election_filename, "output.txt", precincts)


if __name__ == "__main__":
  main()
