from urllib.parse import quote

class JobFilter:
	
	def __init__(self, prop_path):

		self.prop_path = prop_path
		self.website = ''
		self.url = ''
		self.keywords = ''
		self.experience = ''
		self.location = ''
		self.salary = ''
		self.slug = ''
		

	def get_value(self, line):

		return line.split('=')[1].strip()

	def parse_properties(self):

		props = []
		with open(self.prop_path) as f:
			props = f.readlines()
		
		props = [line.strip() for line in props]
	
		for line in props:
			if line.startswith('#'):
				continue
			elif line.startswith('Website='):
				self.website = self.get_value(line)
			elif line.startswith('Keywords='):
				self.keywords = self.get_value(line)
			elif line.startswith('Experience='):
				self.experience = self.get_value(line)
			elif line.startswith('Location='):
				self.location = self.get_value(line)
			elif line.startswith('Salary='):
				self.salary = self.get_value(line)

	def make_url(self):

		self.parse_properties()

		url = ''

		if 'naukri' in self.website:
			url = self.website
			keys = self.keywords.replace(', ','-') #space after comma is important
			keys = keys.replace(' ','-').lower() + '-jobs'	
			self.slug = keys
			url = url + keys 
			if self.experience is not '':
				url = url + '?experience=' + self.experience 		
					#'&k=' + quote(self.keywords)

		
		self.url = url
		
	def get_url(self):
		
		self.make_url()
		return self.url
		
	def get_slug(self):
		return self.slug
	
