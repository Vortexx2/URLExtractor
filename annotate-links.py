import os
import csv
from bs4 import BeautifulSoup
import requests


class AnnotateLinks:

    def __init__(self, filename: str, dest_file: str, filepath: str = 'Assets/resource-list',
                 dest_path='Assets/resource-list'):
        self.filename = filename
        self.dest_file = dest_file
        self.filepath = filepath
        self.dest_path = dest_path

    def annotate_link(self, url: str) -> dict:
        page = requests.get(url).content
        soup = BeautifulSoup(page, 'lxml')
        return {'title': soup.title.string}

    def write_to_csv(self):
        # with open(os.path.join(self.filepath, self.filename), 'r', newline='') as file:
        #     csv_reader = csv.reader(file, delimiter=',')
        #
        #     for row in csv_reader:
        #         with open(os.path.join(self.dest_path, self.dest_file), 'w', newline='') as file:
        #             writer = csv.writer(file)
        #
        #             writer.writerow([row[0], row[1], self.annotate_link(row[2])['title']])

        with open(os.path.join(self.dest_path, self.dest_file), 'w', newline='') as file:
            writer = csv.writer(file)

            with open(os.path.join(self.filepath, self.filename), 'r') as file2:
                csv_reader = csv.reader(file2, delimiter=',')

                for row in csv_reader:
                    writer.writerow[row[0], row[1], self.annotate_link(row[2])['title']]


# URL = 'https://vsitzmann.github.io/siren/'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'lxml')
# print(soup.title.string)

annotate = AnnotateLinks('result.csv', 'something.csv')
annotate.write_to_csv()