#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import re
import time


def main(html, outdir):
    """
    BS4 function to extract the comment-body divs
    """
    # Parse the HTML content of the file
    soup = BeautifulSoup(html, 'html.parser')

    # Find the element(s) in the HTML file you want to extract data from
    # x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r
    data = soup.find_all(
        'div', {'class': 'x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r'})

    # write the extracted data to a file
    # filename should have the timestamp
    filename = outdir + 'output-' + str(time.time()) + '.csv'
    with open(filename, 'w') as file:
        for item in data:
            file.write("\n\"")
            # remvoe tabs and new lines from the string
            text = item.text.replace('\t', '').replace('\n', '')
            text2 = re.sub(r'\s+', ' ', text)
            file.write(text2)
            file.write("\"")
        file.close()


if __name__ == '__main__':
    print("This module cannot be run directly. Please run main.py instead.")
