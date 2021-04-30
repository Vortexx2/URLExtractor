from url_extractor import URLExtractor
from annotate_links import AnnotateLinks

extractor = URLExtractor(filename='test.txt', dest_file='extracted_links.csv')
extractor.write_to_csv()

annotate = AnnotateLinks('extracted_links.csv', 'final_result.csv')
annotate.write_to_csv()
