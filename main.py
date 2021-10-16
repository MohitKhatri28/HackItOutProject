from bs4 import BeautifulSoup
import requests
import time

def search(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Company Name: {company_name.strip()} \n")
                f.write(f"Required Skills: {skills.strip()} \n")
                f.write(f"More Info Here: {more_info.strip()} \n")
                print(f'File Saved: {index}')
#PythonJobs
def find_jobs(language):
    if (language=='Python'):  
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
    elif (language=='Java'):
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=java&txtLocation=')
    elif (language=='C++' or 'C'):
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=C%2B%2B&txtLocation=')
    elif (language=='Web development' or 'Web developer'):
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Web+Development&txtLocation=')
    elif (language=='Graphic designing' or 'Graphic designer'):
        search('timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Graphic+Designing&txtLocation=')
    elif (language=='Game developer' or 'Game development'):
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Game+Developer&txtLocation=')
    elif (language=='Content writing' or 'Content writer'):
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Content+Writing&txtLocation=')
    elif (language=='Video editing'):
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Video+Editing&txtLocation=')
    

print("Enter the skills that you are good at: ")
lang = input('>>')
print(f"Searching jobs for {lang}")

#if (lang==python || lang==Python): 

if __name__ == '__main__':
    while True:
        find_jobs(lang)
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

