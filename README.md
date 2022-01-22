# scraping- aeaweb.org
scraping journals from American Economic Association website

## how to run the script

Make sure all libraries/modules are installed (see requirement.txt)

1. Run collect_vlm_urls.py --> this will collect volume urls from starting_url (will create a .csv fle - initally 'journal_record.csv')
2. Run collect_issues_urls.py --> this will scrap volume urls(in step1) and create list of individual issues urls in another csv file (initially:'issue_record.csv')
3. Run get_issue_detail.py --> this is the script that will scrap list in no.2 and will produce final excel file contains all the required information.

