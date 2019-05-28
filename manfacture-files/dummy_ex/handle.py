import os
# os. chdir( 폴더경로1)  == 체인지 디렉토리
#os.listdir('폴더경로')폴더에 지정된 전체 파일 성적을
# list로 변환

# os.rename('현재파일명', '바꿀파이멸명' 파일 (파일이름) - ~
# os.path.splitext('파일이름')
# 파일 경로와, 저장자를 분리하는 것
# 폴더 경로 C:/ Users/student/PycharmProjects/

#filename = os.path.splitext(r'C:/Users/ssobi/PycharmProjects/manfacture-files/dummy_ex')
#print(filename)

os.chdir(r'C:/Users/ssobi/PycharmProjects/manfacture-files/dummy_ex')
filenames = os.listdir('.')
print(filenames)

for filename in filenames:
    txt = os.path.splitext(filename)[-1]
    if txt == '.txt':
    #앞에 지원자를붙ㅇ
        os.rename(filename, f'{filename}')