import os,sys,zipfile

original_file = "name.zip"

while True:
    try:
        original_file = zipfile.ZipFile(original_file)


        for z in original_file.namelist():

            password = os.path.splitext(z)[0]

            print(password)
        new_file = original_file.namelist()[0]
        original_file.setpassword(password)
        original_file.extractall()

        original_file = new_file
    except:
        break
