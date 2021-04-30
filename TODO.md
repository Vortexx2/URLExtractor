# URLExtractor
A script to extract URLs into a csv file and annotate them, from exported WhatsApp chats.

## Todo

- [ ] Make retrieving the last date in the exported chat faster.

- [ ] Make parsing URLs faster with BeautifulSoup.
    - [Resource for it](https://thehftguy.com/2020/07/28/making-beautifulsoup-parsing-10-times-faster/)
  
- [ ] Make metadata parsing for particular websites much more detailed (eg. YouTube, Github):
  - [Library for extracting metadata](https://github.com/erikriver/opengraph)
  
- [ ] Make script able to extract titles of PDFs, might need downloading each PDF.
  - [pip package pdfrw](https://github.com/pmaupin/pdfrw)