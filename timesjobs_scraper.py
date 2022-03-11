import csv                         
from cgitb import text
import requests
from bs4 import BeautifulSoup  

    #ask input city
city = input('What city do you want to explore?: ')

print("Website Scraper" + '\n' + 'Scraping jobs on timesjobs.com in' , city.capitalize() + '\n' + '---------------------------------------')

def find_jobs():
    # use get to access the desired url. use .text at the end to receive the html from get
    html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=&txtLocation={city}').text
    soup = BeautifulSoup(html_text , 'lxml')

    # find all the jobs posts
    jobs = soup.find_all('li' , class_ = 'clearfix job-bx wht-shd-bx')  
 
    # initialize file to export
    export_file = open('timesjobs_posts.csv' , 'w', encoding= 'utf-8')                 
    writer = csv.writer(export_file)

    # set the header in the csv
    writer.writerow(['Position' , 'Company' , 'Skills', 'Link', 'Published'])     
    
    #loop through the job posts
    for index , job in enumerate(jobs):  
        published_date = job.find('span' , class_ = 'sim-posted').text                      
        role = job.find('h2').text
        company_name = job.find('h3' , class_ ='joblist-comp-name').text  
        skills = job.find('span' , class_ = 'srp-skills').text             
        link = job.header.h2.a['href']         

    #remove undesired characters
        role = role.strip()
        company_name = company_name.strip()   
        skills = skills.strip()
        link = link.strip()
        published_date = published_date.strip() 

    #write and save the csv file
        writer.writerow([role , company_name , skills , link , published_date])
    
    export_file.close()
    print("CSV Saved - If the file is empty, it's because no jobs were listed")

#call the function
find_jobs()           
