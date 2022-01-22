import requests
from bs4 import BeautifulSoup
import csv

# this script collect all searchable issuesurls from collected volume urls
# volume urls was previously scrapped and stored in 'journal_record.csv'

def get_vlm_urls_from_csv(filename):
    vlm_url_list=[]         #an empty list to store the urls
    with open(filename, 'r') as vlm_csv:
        reader = csv.reader(vlm_csv, delimiter=',')
        for row in reader:
            vlm_url_list.append(row[1])
    return vlm_url_list

vol_urls = get_vlm_urls_from_csv('journal_record.csv')
issue_filename = 'issue_record.csv'

root_url = 'https://www.aeaweb.org'
    

#writing urls with new csv filename
with open(issue_filename, mode='w', newline='') as issue_record:
    issue_writer = csv.writer(issue_record, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    write_row = 2

    #looping through the volume list to scrapped individual journal issue urls
    
    for item_url in range(0,len(vol_urls)):
    
        
        issue_url = vol_urls[item_url]
        print(f'Scraping {issue_url}...')

        issue_res = requests.get(issue_url)
        soap_issue = BeautifulSoup(issue_res.content, 'html.parser')

        journal_items = soap_issue.find_all('h3', class_ = 'title')
        for i in range(2, len(journal_items)):
            print(f' Found issue titled: {journal_items[i].find("a").get_text()}')
            issue_url_found = root_url + journal_items[i].find('a')['href']
            issue_writer.writerow([issue_url_found])

print('end')