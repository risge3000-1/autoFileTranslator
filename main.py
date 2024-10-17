from os import listdir, rename
from deep_translator import GoogleTranslator
from os.path import isfile, join
mypath = 'I:\path\goes\here'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
failedFiles = []
for file in onlyfiles:
    fileOgName, extension = file.split('.', 1)
    print("translating \"" + fileOgName + "\"...")
    translated = GoogleTranslator(source='auto', target='en').translate(fileOgName)
    print("New name: " + translated)
    print("Attempting name replacement from \"" + fileOgName + "\" to \"" + translated + "\"..." )
    ogPath = mypath + '\\' + file
    transPath = mypath + '\\' + translated + '.' + extension

    if isfile(transPath):
        print(transPath + " already exists, skipping.")
        continue
    try:
        rename(ogPath, transPath)
    except:
        print("Something went wrong when changing the name of \"" + translated + "\"! Try manual name change.")
        failedFiles.append(fileOgName + '.' + extension + " → " + translated + "." + extension)
        continue
    print("Success fully renamed \"" + file + "\" to \"" + translated + "." + extension + "\"")

if failedFiles.__sizeof__() > 0:
    print(failedFiles)
