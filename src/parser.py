from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import os
import sys

from jobfilter import JobFilter
from job import Job


def clean(text):
	
	text = text.replace(',', ' ').replace('\n','  ')
	return text


def parse(num_pages):

	listings = ["Role, Company, Rating, Review Count, Experience, Location, Salary, Tags, Link\n"]

	options = Options()
	options.add_argument("--disable-extensions")
	options.add_argument("--disable-gpu")
	options.add_argument("--headless")

	naukri = JobFilter('jobFilterNaukri.txt')
	URL = naukri.get_url()
	slug = naukri.get_slug()

	for page in range(1,num_pages+1):
		url = URL+'-'+str(page)
		print(url)
		driver = webdriver.Chrome(os.path.join(os.getcwd(),'chromedriver'), options=options)
		driver.get(url)
		jobs = driver.find_elements_by_class_name('jobTuple')
		for job in jobs:
			try:
				job_link = job.find_element_by_tag_name('a').get_attribute('href')
				role = job.find_element_by_class_name('title').text	
				companyInfoElement = job.find_element_by_class_name('companyInfo')
				company = companyInfoElement.find_element_by_tag_name('a').text

				rating, reviews = '0','0' # default
				try:
					rating = companyInfoElement.find_element_by_class_name('starRating').text
					reviews = companyInfoElement.find_element_by_class_name('reviewsCount').text[1:-1].replace(' Reviews','')
				except:
					pass
				
				experience = job.find_element_by_class_name('experience').text
				salary = job.find_element_by_class_name('salary').text
				location = job.find_element_by_class_name('location').text
				tags = job.find_element_by_class_name('tags').text

				job_obj = Job(clean(company), clean(role), clean(rating), clean(reviews), clean(experience),
						clean(location), clean(salary), clean(tags), job_link)

				listings.append(job_obj.__str__())
			except:
				with open("jobs.csv", "a+") as f:
					f.writelines(listings)
				listings = []
				print("An exception occurred")

		with open("jobs.csv", "a+") as f:
			f.writelines(listings)
		listings = []

		print("Parsed page ", page)

		driver.close()
		driver.quit()

def main():
	num_pages = int(sys.argv[1])
	parse(num_pages)



if __name__ == "__main__":
	main()
