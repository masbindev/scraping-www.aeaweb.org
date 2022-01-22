import requests
from bs4 import BeautifulSoup
import csv

# this script collect all searchable journal issues urls from start_url
# and save it to csv file

root_url = 'https://www.aeaweb.org'
start_url = 'https://www.aeaweb.org/journals/aer/issues'

res = requests.get(start_url)
print(res.status_code)
# print(res.content)
soup_data = BeautifulSoup(res.content, 'html.parser')
journal_all = soup_data.find('section', class_ ='journal-preview-group')
journal_preview = journal_all.find_all('article', class_ = 'journal-preview')
#print(journal_preview[0])
print('start')

with open('journal_record.csv', mode='w', newline='') as journal_record:
    journal_writer = csv.writer(journal_record, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for journal_item in journal_preview:
        
        volume = journal_item.find('span', class_ = 'news-item').text
        # print(volume)


        volume_urls = journal_item.find_all('a')

        for item_url in volume_urls:
            issue_url = item_url['href']
            # print("  |")
            # print("   --" + root_url + issue_url)

            volume_txt = item_url.text
            # print("   --" + volume_txt)
            journal_writer.writerow([volume, root_url+issue_url, volume_txt])
        # print('-----------------')

print('end')