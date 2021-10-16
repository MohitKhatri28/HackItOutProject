from bs4 import BeautifulSoup
import requests
import time
import pyttsx3
import speech_recognition as sr 
import re


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

def find_jobs(language):
    if (language=='python'):  
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
    elif (language=='java'):
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=java&txtLocation=')
    elif (language=='c++' or language=='c'):
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=C%2B%2B&txtLocation=')
    elif (language=='web development' or language=='web developer'):
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Web+Development&txtLocation=')
    elif (language=='graphic designing' or language=='graphic designer'):
        search('timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Graphic+Designing&txtLocation=')
    elif (language=='game developer' or language=='game development'):
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Game+Developer&txtLocation=')
    elif (language=='content writing' or language=='content writer'):
        search('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Content+Writing&txtLocation=')
    else:
        print("Sorry, didn't get you...")
        return -1

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception: ", str(e))

    return said.lower()

if __name__ == '__main__':
    print("Started Program")
    END_PHRASE = "stop"

    while True:
        print("What skills do you have?")
        speak("What skills do you have?")
        print("Listening...")
        text = get_audio()
        print(text)
        if text.find(END_PHRASE) != -1:
            print('Exit')
            break
        else:
            find_jobs(text)
            break



