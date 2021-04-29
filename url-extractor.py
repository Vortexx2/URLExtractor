from datetime import datetime
import re
import os
import csv


class URLExtractor:

    def __init__(self, filename: str, dest_file: str, filepath: str = 'Assets/og_exports/',
                 dest_path: str = 'Assets/resource-list/', regexp: str = '(https?://\S+)'):

        """
        Used to extract URLS from a .txt file (made for extracting from exported whatsapp chats) and store it in a csv
        file ideally. Writes to csv in format [date, time, link].\n
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

        # 1st case: Everything right -> date, time, multiple links on the line
        # yield [date, time, each_url]

        # 2nd case: Nothing -> No date, time and no links
        # Nothing

        # 3rd case: Only links -> No date, time but there are links (links embedded inside the message)
        # yield [last_date, last_time, each_url]

        # 4th case: Only timestamp -> Only date and time, no links
        # Store last_date, last_time = date, time for future reference in the same block

        with open(os.path.join(self.filepath, self.filename)) as file:
            for line in file:
                urls = self.regexp.findall(line)

                try:

                    # The below code is done via indexing and not via regex is because if the line has a date
                    # and time as well as a link, it will break.
                    # date = "dd/mm/yyyy" or "%d/%m/%y"
                    # time = "hh/mm" or "%H:%M"
                    # date, time = line[0:10], line[12:17]
                    date_and_time = line[0:17]

                    date_and_time = datetime.strptime(date_and_time, "%d/%m/%Y, %H:%M")

                    last_d_t = date_and_time

                    if len(urls) == 0:
                        continue

                    else:
                        for url in urls:
                            yield [date_and_time, url]

                # When no timestamp
                except (ValueError, IndexError) as err:
                    if len(urls) == 0:
                        continue

                    else:
                        for url in urls:
                            yield [last_d_t, url]

    def write_to_csv(self) -> None:
        """
        Method to write each instance of the `generator` specified to a new row in
        the csv file specified with `dest_file`.
        :param generator: Generator to use to write to the csv fi
        :return: None
        """
        with open(os.path.join(self.dest_path, self.dest_file), 'w', newline='') as file:
            writer = csv.writer(file)

            for [date_time, url] in self.resource_list_generator():
                date, time = datetime.strftime(date_time, "%d/%m/%Y"), datetime.strftime(date_time, "%H:%M")
                writer.writerow([date, time, url])


extractor = URLExtractor(filename='WhatsApp Chat with meta_resources ∈ M68.txt', dest_file='result.csv')
extractor.write_to_csv()
