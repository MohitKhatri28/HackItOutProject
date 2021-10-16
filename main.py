from bs4 import BeautifulSoup
import requests
import time

#PythonJobs
def find_jobs(language):

    if (language=='Python'):  
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python+&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
                more_info = job.header.h2.a['href']
                with open(f'posts/python/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info Here: {more_info.strip()} \n")
                    print(f'File Saved: {index}')
    elif (language=='Java'):
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=java&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
                more_info = job.header.h2.a['href']
                with open(f'posts/java/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info Here: {more_info.strip()} \n")
                    print(f'File Saved: {index}')
    elif (language=='C++' or 'C'):
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=C%2B%2B&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
                more_info = job.header.h2.a['href']
                with open(f'posts/c/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info Here: {more_info.strip()} \n")
                    print(f'File Saved: {index}')
    elif (language=='Web development' or 'Web developer'):
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Web+Development&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
                more_info = job.header.h2.a['href']
                with open(f'posts/webdev/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info Here: {more_info.strip()} \n")
                    print(f'File Saved: {index}')
    elif (language=='Graphic designing' or 'Graphic designer'):
        html_text = requests.get('timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Graphic+Designing&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
                more_info = job.header.h2.a['href']
                with open(f'posts/graphicdesign/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info Here: {more_info.strip()} \n")
                    print(f'File Saved: {index}')
    elif (language=='Game developer' or 'Game development'):
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Game+Developer&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
                more_info = job.header.h2.a['href']
                with open(f'posts/gamedev/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info Here: {more_info.strip()} \n")
                    print(f'File Saved: {index}')
    elif (language=='Content writing' or 'Content writer'):
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Content+Writing&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
                more_info = job.header.h2.a['href']
                with open(f'posts/contentwriter/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info Here: {more_info.strip()} \n")
                    print(f'File Saved: {index}')
    elif (language=='Video editing'):
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Video+Editing&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
                more_info = job.header.h2.a['href']
                with open(f'posts/videoedit/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info Here: {more_info.strip()} \n")
                    print(f'File Saved: {index}')
    

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

