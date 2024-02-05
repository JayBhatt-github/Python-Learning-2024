# Multilevel Inheritance in Python

class Manager:
	def final_review(self):
		print("Final Review")
 
class Reviewer(Manager):
	def review(self):
		print("Reviewing...")
 
class Writer(Reviewer):
	def writes(self):
		print("Writes the code")
 
o = Writer()
o.final_review()
o.review()
o.writes()