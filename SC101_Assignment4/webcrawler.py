"""
File: webcrawler.py
Name: matt
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    m=0
    f=0
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        items = soup.find_all('tr')
        for item in items[:-1]:
            td = item.find_all('td')
            if len(td) == 5:
                m += int(td[2].text.replace(",", ""))
                f += int(td[4].text.replace(",", ""))
        print(f'Male Number: {m}')
        print(f'Female Number: {f}')

        # ----- Write your code below this line ----- #




if __name__ == '__main__':
    main()
