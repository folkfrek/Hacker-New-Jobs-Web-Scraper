import requests
from bs4 import BeautifulSoup
import pprint
from datetime import date

today = date.today().strftime('%B %d, %Y')

def recent_job_posting(jobs, ages):
	"""Creates a list of most recent job postings from Hacker News"""
	titles = []
	for idx, item in enumerate(jobs):
		title = jobs[idx].getText()
		href = jobs[idx].get('href', None)
		release = ages[idx].getText()
		titles.append({'title': title, 'link': href, 'posted': release})
	return titles

def jobs_text_file(jobs):
	"""Create a text file of the most recent job postings on Hacker News"""
	with open('jobs.txt', 'w') as file:
		file.write(f"Recent Hacker News Job Postings: {today} \n")
		for job in jobs:
			output = 'Job Description: ' + str(job['title'] + ' | Link: ' + str(job['link']) + ' | Posted: ' + str(job['posted']))
			file.write("%s\n" % output)

if __name__ == '__main__':
	res = requests.get('https://news.ycombinator.com/jobs') 
	soup = BeautifulSoup(res.text, 'html.parser')
	jobs = soup.select('.titlelink')
	ages = soup.select('.age')

	new_jobs = recent_job_posting(jobs, ages)
	jobs_text_file(new_jobs)
	pprint.pprint(recent_job_posting(jobs, ages))

