# Git

## 기본명령어

1. git 저장소 (repository	

```bash
	$ git init
```

- 원하는 폴더를 저장소로 만들게 되면, `git` `bash` 에서는 ``(master)`` 라고 표기됨.

- 그리고 숨김폴더로 `.git/` 이 생성된다.

  

 2 .커밋할 목록에 담기 (Staging Area)

```bash
$ git add .
```

-  현재 작업공간 (Working Directory / Tree) 의 변경사항을 커밋할 목록에 추가한다. ( add )
-  . 리눅스에서 현재 디렉토리(폴더)를 표기하는 방법으로, 현재 내 포러에 있는 파일의 변경 사항을 전부 추갛나다.
-  단일 파일만 추가하려면 `git add "파일이름"`
-  폴더를 추가하려면 `git add "폴더 이름"`

3.

``` bash
$ git commit -m '________'
```

- 커밋을 할 때에는 해당버전의 이력 (이름)을 의미하는 메시지를 반드시 적어준다.
- 메시지는 지금 버전을 쉽게 이해할 수 있도록 작성한다.

- 커밋은 현재 코드의 상태를 스냅샷 찍는 것 (언제든 되돌아 갈 수 있게) .



4.로그 확인하기 

```bash
$ git log
   
   commit f2a532457233af652824db1e04b8928e32fcc327 (HEAD -> master)
   Author: HJ <slush0430@daum.net>
   Date:   Fri May 24 10:45:19 2019 +0900
   
       how to set git <ED><94><84><EB><A1><9C><EC><A0><9D><ED><8A><B8>
   
```


 - 현재까지 커밋 된 이력

5.git 상태 확인하기

```bash
   $ git status
```

- CLI ( Command Line Interface) 현재 사태를 알기 위해 반드시 영어를 통해 확인한다.
- 커밋할 목록에 담겨 있는지, untracked 인지,  커밋할 내용이 있는지 등등 다양한 정보를 확인 가능.

=============여기 까지는 local 저장소에 넣은 것 =====================



- git remote add orgin + git repository 의 url

​       git remote add origin https://github.com/iuiurm/python_project.git

​       git remote --v



- git push origin master  는 origin repository의 master 벤치에 push 하겠다.

- git clone https://github.com/iuiurm/python_project.git <- repository 의 내용을 복사해서

  다른 파일에 가져다 붙임



# 원격 저장소 활용하기

1. 원격 저장소 (remote repository) 등록하기 = 위 ==== 이하의 내용과 같으나 한번 더 정리한다.



```bash
$ git remote add origin 'url 주소 --- ~ '
```

- 원격 저장소 (remote)를 `origin` 이라는 이름으로  `git hub` 를 설정한다.

- 아래의 명령어로 현재 등록된 원격 저장소를 확인할 수 있다.

```bash
$ git remote --v 

를 하면 
origin  https://github.com/iuiurm/python_project.git (fetch)
origin  https://github.com/iuiurm/python_project.git (push) 의 결과가 나옴.
```

2. 원격 저장소 올리기 (push)

```bash
$ git push origin master
```

- git push origin 이라는 이름의 원격저장소에 master bench로 저장 됨.



3. 원격 저장소로부터 가져오기 (pull)

```bash
$ git pull origin master
```

- pull 은 push의 반대, pull을 가져온다



# 원격 저장소 복제(clone) 하기

```bash
git clone ____경로________
```

- 다운 받기를 원하는 폴더에서 git bash를 열고 위의 명령어를 입력한다.
- 경로는 `github` 에서 우측에 있는 초록색 버튼을 누르면 나타난다.



