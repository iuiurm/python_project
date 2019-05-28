# numbers.txt 파일d 내용을 뒤집어서 저장ㅎㄴ다.

with open('numbers.txt', 'r') as f:
    #읽을때는 r이라는 변수 사용
    lines = f.readlines()
    lines.reverse()

with open('numbers.txt','w')as f:
    for line in lines:
        f.write(line.rstrip() + '\n')

#f.write(line.rstrip() + '\n')
