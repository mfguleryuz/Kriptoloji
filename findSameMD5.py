
"""
091044044
mehmetfatihguleryuz

açıklama:
klasörde aynı md5 koduna sahip olan dosyaları buluyor 

"""

import hashlib
import os

def getAllFiles(path):
	l= {}
	for file in os.listdir(path):
		l[path+"/"+file] = ""
	return l

def hashfile(fname, blocksize=65536):
	hasher= hashlib.md5()
	afile= open(fname, 'rb')
	bf = afile.read(blocksize)
	while len(bf) > 0:
		hasher.update(bf)
		bf = afile.read(blocksize)
	return hasher.hexdigest()

files= getAllFiles("/Users/mehmetfatihguleryuz/Desktop/Resimler")
for filepath in files.keys():
	files[filepath]= hashfile(filepath)

for i in range(0,len(files.keys())):
	filepath= files.keys()[i]
	for j in range(i,len(files.keys())):
		filepath2= files.keys()[j]
		if filepath!=filepath2 and files[filepath]==files[filepath2]:
			print "\nThese files have same md5: \n%s\n%s \nwith %s\n" % (filepath, filepath2, files[filepath])

