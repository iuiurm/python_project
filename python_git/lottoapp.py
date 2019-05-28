# 아래에 코드를 작성하세요.

import random

lists = list(range(1, 46))
lotto = random.sample(lists, 6)
lotto.sort()



print(lotto)
print(f'오늘의 숫자는 {lotto} 입니다')
