with open('mulcam.txt', 'r') as f:
    #읽을때는 r이라는 변수 사용
    lines = f.readlines()
    for line in lines:
        print(line)


    all_text = f.read()
    print(all_text)