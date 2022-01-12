import os

curDir = os.getcwd()
print(curDir)

txtFiles = []

for path in os.listdir(curDir):
	if path[-4:] == '.txt':
		txtFiles.append(path)

#print(txtFiles)

def removeIfEmpty(filePath):
	with open(filePath) as openfile:
		lines = openfile.readlines()
		#print(lines)
		#print(len(lines))
		if len(lines) == 0:
			os.remove(filePath)
			print(filePath+' removed!')

for pathoftxtfile in txtFiles:
	removeIfEmpty(pathoftxtfile)