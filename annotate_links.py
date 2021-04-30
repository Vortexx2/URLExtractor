import os
import csv
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from utils import utilities


class AnnotateLinks:

    def __init__(self, filename: str, dest_file: str, filepath: str = 'Assets/resource-list',
                 dest_path='Assets/resource-list'):
        self.filename = filename
        self.dest_file = dest_file
        self.filepath = filepath
        self.dest_path = dest_path

    def last_date_of_previous(self) -> datetime:
        """
        Method which returns the last date and time of the input file.
        :return: `datetime` object
        """

        try:
            with open(os.path.join(self.dest_path, self.dest_file), mode='r') as file:
                last_datetime = datetime.min
                while True:

                    line = file.readline()

                    if not line:
                        break

                    try:
                        last_datetime = utilities.datetime_from_line(line, from_csv=True)

                    except Exception as err:
                        print(type(err), err)

                return last_datetime

        except FileNotFoundError:
            return datetime.min

    def annotate_link(self, url: str) -> dict:
        page = requests.get(url).content
        soup = BeautifulSoup(page, 'lxml')

        metas = soup.find_all('meta')

        return {'title': soup.title.string, 'meta': [meta.attrs['content'] for meta in metas if 'name' in meta.attrs]}

    def write_to_csv(self, app_to_csv: bool = False):

        last_dt = self.last_date_of_previous()
        with open(os.path.join(self.dest_path, self.dest_file), 'a' if app_to_csv else 'w', newline='') as file:
            writer = csv.writer(file)

            if not app_to_csv:
                writer.writerow(['date', 'time', 'url', 'title', 'meta_tags'])

            with open(os.path.join(self.filepath, self.filename), 'r') as file2:
                csv_reader = csv.DictReader(file2, delimiter=',')

                for row in csv_reader:
                    try:

                        current_dt = utilities.datetime_from_line(row['date'] + ',' + row['time'] + ',', from_csv=True)

                        if current_dt <= last_dt:
                            continue

                        described_dict = self.annotate_link(row['url'])
                        row['title'] = described_dict['title'].strip()
                        row['meta'] = described_dict['meta']

                        writer.writerow([row[key] for key in row])
                    except Exception as err:
                        print(err)
                        row['title'] = 'PDF'

                        if row['url'][-4:] == '.pdf':
                            writer.writerow(row[key] for key in row)


# annotate = AnnotateLinks('extracted_links.csv', 'final_result.csv')
# annotate.write_to_csv()
