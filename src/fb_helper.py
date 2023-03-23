#!/usr/local/bin/python3
import time
import re

def _login(browser, email, password):
    browser.get("http://facebook.com")
    browser.find_element("name", "email").send_keys(email)
    browser.find_element("name", "pass").send_keys(password)
    browser.find_element("name", 'login').click()
    print("Logged in")
    time.sleep(5)


def _get_comment_amount(browser):
    temp = browser.find_elements("xpath", "//span[contains(text(), 'of')]")
    for item in temp:
        """
        check if item matches the regex pattern 100 of 499
        """
        if re.match(r'\d+\sof\s\d+', item.text):
            num = item.text
            print("Getting Comments " + num)
            break

    # try catch block
    try:
        num_list = num.split(' ')
        num1 = int(num_list[0])
        num2 = int(num_list[2])
    except:
        num1 = 0
        num2 = 0
    return num1, num2


def _get_more_comments(browser):
    browser.find_element(
        "xpath", "//span[contains(text(), 'View more comments')]").click()
    time.sleep(5)


def _get_comments(browser):
    # loop until the amount of comments is equal to the total amount of comments
    while True:
        num1, num2 = _get_comment_amount(browser)
        if num1 + 50 > num2:
            break
        else:
            _get_more_comments(browser)

if __name__ == '__main__':
    # _process_bs()
    print("This module cannot be run directly. Please run main.py instead.")