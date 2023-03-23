#!/usr/local/bin/python3
import re


def _validate_url(url):
    """
    validate the url, check if it begins with http or https
    check for proper domain name
    regex to check for valid url
    """

    return url.startswith("http") and url.startswith("https") and "facebook.com" in url and re.match(
        r'^(?:http|ftp)s?://'  # http:// or https://
        # domain...
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', url, re.IGNORECASE)


def _parse_urls():
    """
    check each line in the file
    if it has m.facebook in it,
    or if it is a valid facebook url
    then add it to the array
    """
    urls = []
    for line in lines:
        if line.startswith('#'):
            print("Skipping line with #")
            continue
        elif 'm.facebook.com' in line:
            print("Unsupported Link: " + line)
            exit()
        elif 'facebook.com' in line:
            if _validate_url(line):
                urls.append(line)
            else:
                print("Invalid url: " + line)
                exit()
    return urls


def main(input_file):
    """
    call the _parse_urls function
    print the number of urls parsed
    """
    try:
        with open(input_file, 'r') as f:
            global lines
            lines = f.readlines()
            lines = [line.rstrip('\n') for line in lines]
    except FileNotFoundError:
        print("File not found")
        exit()
    except IndexError:
        print("File is empty")
        exit()
    print("Parsing input urls")
    urls = _parse_urls()
    print("Successfully parsed url: " + str(len(urls)))
    return urls


if __name__ == '__main__':
    print("This script is not meant to be run directly")
