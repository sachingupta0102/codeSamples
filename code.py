import string

class Tagging(object):

	def __init__(self, mysentence=None, name_list=None, num_list=None):
		if mysentence==None:
			print 'Empty Input error'
		else:
			self.mysentence1 = mysentence.split(' ')
			self.mysentence = mysentence.lower().split(' ')
			Name = set()
			for i in name_list:
				Name.add(i)
			Num = set()
			Num.add(i for i in num_list)
			for i in num_list:
				Num.add(i)
			attr = [Name,Num]
			self.attr = attr

	def checkatt(self, k):
		result = []
		for i in range(len(self.mysentence)):
			if self.mysentence[i] in self.attr[k]:
				if k ==0:
					myatt = 'NAME'
				else:
					myatt = 'NUM'
				result.append((self.mysentence[i], i, myatt))#self.attr[k]
		return result

	def Tagged(self):
		count = len(self.attr)
		Result_Tagged = ''
		Tagged_class = ''
		for i in range(count):
			mywords = self.checkatt(i)
			if i==0:
				Result_Tagged = Result_Tagged + ' '.join(c[0] for c in mywords)
				Tagged_class = Tagged_class + ' '.join(c[2] for c in mywords)
			else:
				Result_Tagged = Result_Tagged + ' ' + ' '.join(c[0] for c in mywords)
				Tagged_class = Tagged_class + ' ' + ' '.join(c[2] for c in mywords)
		return (Result_Tagged, Tagged_class)

	def unTagged(self):
		count = len(self.mysentence)
		inputsentence = ' '.join(c for c in self.mysentence1)
		Tagged_result = self.Tagged()
		Tagged_words = ' '.join(c for c in self.mysentence1 if c.lower() in Tagged_result[0])
		Result_unTagged = ' '.join(self.mysentence1[j] for j,c in enumerate(self.mysentence) if c not in Tagged_result[0])
		class_Tagged =''
		counter = 0
		for i,c in enumerate(self.mysentence):
			if c not in Tagged_result[0]:
				class_Tagged = class_Tagged + self.mysentence1[i] + ' '
			else:
				class_Tagged = class_Tagged + Tagged_result[1].split()[counter] + ' '
				counter +=1
		return (inputsentence, Result_unTagged, Tagged_words, class_Tagged)

if __name__=='__main__':
	name_list = ['jack', 'jill', 'john']
	num_list = ['one', 'two', 'three', 'four', 'five']
	mysentence = "I'm Jack and I'm three years old"
	myobject = Tagging(mysentence, name_list, num_list)
	result = myobject.unTagged()
	labels = ['input       ', 'untagged    ', 'tagged      ', 'class tagged']
	for i,c in enumerate(result):
		print labels[i], ':', c
