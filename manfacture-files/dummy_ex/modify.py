import os
os.chdir(r'C:/Users/ssobi/PycharmProjects/manfacture-files/dummy_ex')
filenames = os.listdir('.')
print(filenames)

for filename in filenames:
    txt = os.path.splitext(filename)[-1]
    if txt == '.txt':

        newFilename = filename.replace('지원자_지원자_지원자', '합격자')
        print(newFilename)
        os.rename(filename, newFilename )