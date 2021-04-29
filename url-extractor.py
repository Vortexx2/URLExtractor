import re
import os
import csv


class URLExtractor:

    def __init__(self, filename: str, dest_file: str, filepath: str = 'Assets/og_exports/',
                 dest_path: str = 'Assets/resource-list/', regexp: str = '(https?://\S+)'):

        """
        Used to extract URLS from a .txt file (made for extracting from exported whatsapp chats) and store it in a csv
        file ideally. \n
        :param filename: Name of file to extract URLS from.
        :param dest_file: Name of CSV file to save URLS in
        :param filepath: Directory in which `filename` is stored
        :param dest_path: Directory in which `dest_file` is stored
        :param regexp: The regexp used to extract URLs.
        """
        self.dest_path = dest_path
        self.dest_file = dest_file
        self.filename = filename
        self.filepath = filepath
        self.regexp = re.compile(regexp)

    def resource_list_generator(self):
        """
        Method which uses a generator to return all the urls in the text file.
        :return: Generator for url
        """
        with open(os.path.join(self.filepath, self.filename)) as file:
            for line in file:
                urls = self.regexp.findall(line)
                if len(urls) == 0:
                    continue
                for url in urls:
                    yield url

    def write_to_csv(self) -> None:

        """
        Method to write each instance of the `generator` specified to a new row in
        the csv file specified with `dest_file`.
        :param generator: Generator to use to write to the csv fi
        :return: None
        """
        with open(os.path.join(self.dest_path, self.dest_file), 'w', newline='') as file:
            writer = csv.writer(file)

            for url in self.resource_list_generator():
                writer.writerow([url])


extractor = URLExtractor(filename='WhatsApp Chat with Me.txt', dest_file='result.csv')

extractor.write_to_csv()
