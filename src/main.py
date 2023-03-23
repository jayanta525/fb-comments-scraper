#!/usr/local/bin/python3
import sys
import argparse

import parse_url
import parse_credentials
import fb_scrapper

def main():
    """
    Entrypoint for the program

    This function parses the command line arguments and calls the other functions
    """
    parser = argparse.ArgumentParser(description='Facebook Post Comments Scrapper')
    parser.add_argument('credentials_file', type=str,
                        help='A txt file with username and password')
    parser.add_argument('input_file', type=str,
                        help='A input file with list of urls')
    parser.add_argument('out_dir', type=str,
                        help='Output directory to store the comments')

    args = parser.parse_args()
    if args.credentials_file.endswith('.txt'): # check if the file is a txt file
        print("Credentials file: " + args.credentials_file)
    else:
        print("Credentials file not found")
        sys.exit(1)
    if args.input_file.endswith('.txt') | args.input_file.endswith('.csv'):
        print("Input file: " + args.input_file)
    else:
        print("Input file must be a .txt or .csv file")
        sys.exit(1)
    if args.out_dir.endswith('/'):
        print("Output directory: " + args.out_dir)
    else:
        print("Output directory must end with /")
        sys.exit(1)
    urls = parse_url.main(args.input_file)
    email, password = parse_credentials.main(args.credentials_file)
    fb_scrapper.main(email, password, urls, args.out_dir)


if __name__ == '__main__':
    main()
