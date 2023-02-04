import time

from bs4 import BeautifulSoup
import requests

print('Enter some unfamiliar skills ')
unfamiliar_skill=input('>')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python'
        '&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").span.text
        if published_date == 'Posted few days ago':
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '').strip()
            skills = job.find("span", class_='srp-skills').text.replace(" ", "").strip()
            more_info=job.find("header",class_="clearfix").h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'''
                    Company Name: {company_name}
                    Required Skills: {skills}
                    More Info: {more_info}''')
                print(f'File saved : {index}.txt')


if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes')
        time.sleep(60*time_wait)
