import math

class BagOfWords():
	dict1, dict2, bag = {}, {}, []
	def __init__(self, file1, file2):
		self.readFiles(file1, file2)

	def readFiles(self, file1, file2):
		self.f1 = open(file1, "r")
		self.f2 = open(file2, "r")
		self.str1 = self.f1.read()
		self.str2 = self.f2.read()
		self.createDictionaries(self.str1, self.str2)

	def createDictionaries(self, str1, str2):
		temp1 = str1.split()
		temp2 = str2.split()
		for i in temp1:
			if i in BagOfWords.dict1:
				BagOfWords.dict1[i] += 1
			else:
				BagOfWords.dict1[i] = 1
		for i in temp2:
			if i in BagOfWords.dict2:
				BagOfWords.dict2[i] += 1
			else:
				BagOfWords.dict2[i] = 1

		for key in BagOfWords.dict1:
			BagOfWords.bag.append(key)

		for key in BagOfWords.dict2:
			if key not in BagOfWords.bag:
				BagOfWords.bag.append(key)

		self.findDistance()

	def findDistance(self):
		#print BagOfWords.dict1, BagOfWords.dict2
		total = 0
		val1 = 0
		val2 = 0
		for i in BagOfWords.bag:
			if i in BagOfWords.dict1:
				val1 = BagOfWords.dict1[i]
				if i in BagOfWords.dict2:
					val2 = BagOfWords.dict2[i]
				else:
					val2 = 0
			else:
				val1 = 0
			total += val1 * val2

		denom1 = sum(map(lambda key: BagOfWords.dict1[key] ** 2, BagOfWords.dict1.keys()))
		denom1 = denom1 ** (1/2.0)
		denom2 = sum(map(lambda key: BagOfWords.dict2[key] ** 2, BagOfWords.dict2.keys()))
		denom2 = denom2 ** (1/2.0)
		self.result = round(math.acos(total / (denom1 * denom2)),2)

	def __str__(self):
		return "<" + str(self.result) + ">"

a = BagOfWords("file1.txt", "file2.txt")
print (a)
