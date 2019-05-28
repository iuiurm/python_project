# 파일을 여는 함수 open , 1번째 매개변수로 파일 이름이 들어감
# 2번째 매개변수로 open option
# r : 읽기
# w : 쓰기 - write(overwrite)
# a : 추가 - append


#f.write('hphk')
# ```
# 파이썬에서 with 구문은 ' 컨텍스트 매니저'이다.
# with 블럭을 통해 명시적으로 파일을 불러서 작업하는 코드 블럭을 만들 수 있다.
# ```
with open('mulcam.txt', 'w') as f :
    for i in range( 5) :
        f.write(f'hphk {i+1} \n')
    f.close()