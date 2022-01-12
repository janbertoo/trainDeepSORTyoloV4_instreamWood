import os

#get current work directory
curDir = os.getcwd()
print(curDir)

#create empty variable to store the txt files in
txtFiles = []

#find all text files, change the extension to .jpg and store them in the txtFiles list
for path in os.listdir(curDir):
	if path[-4:] == '.txt':
		#print(path)
		path = path[:-4]+'.jpg'
		#print(path)
		txtFiles.append(path)

#create empty variable to store jpg files in
jpgFiles = []

#find all jpg files in current directory and store them in the jpgFile list
for path in os.listdir(curDir):
	if path[-4:] == '.jpg':
		jpgFiles.append(path)
		#print(path)

#create empty variable to store xml files in
xmlFiles = []

#find all xml files in current directory and store them in the xmlFile list
for path in os.listdir(curDir):
	if path[-4:] == '.xml':
		xmlFiles.append(path)
		#print(path)

#create list
tobeRemoved = []

for jpg in jpgFiles:
	found = 0
	for txt in txtFiles:
		if txt[:-4]+'.jpg' == jpg:
			print('found '+jpg)
			found = 1
			break
	if found == 0:
		tobeRemoved.append(jpg)

tobeRemovedxml = []

for xml in xmlFiles:
	found = 0
	for txt in txtFiles:
		if txt[:-4]+'.xml' == xml:
			print('found '+xml)
			found = 1
			break
	if found == 0:
		tobeRemoved.append(xml)

print('length jpgs = '+str(len(jpgFiles)))
print('length txts = '+str(len(txtFiles)))
print('length to be removed = '+str(len(tobeRemoved)))

for badjpg in tobeRemoved:
	print('removing '+str(badjpg))
	os.remove(badjpg)

for badxml in tobeRemovedxml:
	print('removing '+str(badxml))
	os.remove(badxml)
