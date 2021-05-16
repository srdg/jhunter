class Job:
	
	def __init__(self, company, role, rating, review, experience, location, salary, tags, link):

		self.company = company
		self.role = role
		self.rating = rating
		self.review = review
		self.experience = experience
		self.location = location
		self.salary = salary
		self.tags = tags
		self.job_link = link

	def __str__(self):
		
		line = self.role+','\
			+ self.company+','\
			+ self.rating+','\
			+ self.review+','\
			+ self.experience+','\
			+ self.location+','\
			+ self.salary+','\
			+ self.tags+','\
			+ self.job_link+'\n'
		
		return line	


		