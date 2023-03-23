#!/usr/local/bin/python3
import re


def _validate_email(email):
    """
    validate the email
    regex to check for valid email
    """
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def main(input_file):
    """
    call the _parse_urls function
    print the number of urls parsed
    """
    try:
        with open(input_file, 'r') as f:
            EMAIL = f.readline().split('"')[1]
            PASSWORD = f.readline().split('"')[1]
    except FileNotFoundError:
        print("Credentials file not found")
        exit()
    except IndexError:
        print("Credentials file is empty")
        exit()
    if _validate_email(EMAIL):
        print("Successfully parsed email")
    else:
        print("Invalid email")
        exit()
    print("Successfully parsed password")
    return EMAIL, PASSWORD


if __name__ == '__main__':
    print("This script is not meant to be run directly")
