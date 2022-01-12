import os, numpy

curPath = os.getcwd()
folderList = os.listdir(curPath)

fileExtension = numpy.str(curPath.split('/')[-2]+'__'+curPath.split('/')[-1])

#searchfor folder and find and change all .jpg or .xml files
for folder in folderList:
	#separate the folders from the files
	if len(folder.split('.')) < 2:
		print(curPath)
		print(folder)
		pathFolder = os.path.join(curPath,folder)
		#print(pathFolder)
		fileList = os.listdir(pathFolder)
		for file in fileList:
			#print(file[-4:])
			if file[-4:] == '.xml' or file[-4:] == '.jpg':
				newFileName = fileExtension+'__'+file
				#print(newFileName)
				oldFile = os.path.join(curPath+'/'+folder+'/'+file)
				print(oldFile)
				newFile = os.path.join(curPath+'/'+folder+'/'+newFileName)
				print(newFile)
				os.rename(oldFile,newFile)