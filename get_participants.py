from bs4 import BeautifulSoup
import sys, getopt

def get_participants(input_file):
    with open(input_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    
    divs = soup.find_all('div')
    
    names = list()
    
    for div in divs:
        if 'role' in div.attrs and div.attrs['role'] == 'presentation':
            sort_key = div.contents[0].attrs['data-sort-key']
            name = sort_key[:sort_key.find('spaces/')]
            names.append(name)
    return names

def print_usage():
    print('get_participants.py -i <inputfile> -o <outputfile>')

def main(argv):
    input_file = str()
    output_file = str()

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print_usage()     
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg

    if input_file == '':
        print('Missing input file! Use -i option')
        sys.exit(1)
    if output_file == '':
        print('Missing output file! Use -o option')
        sys.exit(1)

    participants = get_participants(input_file)

    with open(output_file, 'w') as of:
        for participant in participants:
            of.write('%s\n' % participant)

if __name__ == '__main__':
    main(sys.argv[1:])
