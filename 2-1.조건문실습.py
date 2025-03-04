print("현재의 계절을 구해봅시다.")
print("~"*30)

import datetime

# 시스템에서 현재 시간을 읽어옴
a = datetime.datetime.now()

# if 3 <= a.month <=5 :
#     print(f"이번달은 {a.month}월로 봄 입니다.")
# elif 6 <= a.month <= 8 :
#     print(f"이번달은 {a.month}월로 여름 입니다.")
# elif 9 <= a.month <= 11 :
#     print(f"이번달은 {a.month}월로 가을 입니다.")
# else :
#     print(f"이번달은 {a.month}월로 겨울 입니다.")
#     print('추워요?')


if 3 <= a.month <=5 :
    print(f"이번달은 {a.month}월로 봄 입니다.")
if 6 <= a.month <= 8 :
    print(f"이번달은 {a.month}월로 여름 입니다.")
if 9 <= a.month <= 11 :
    print(f"이번달은 {a.month}월로 가을 입니다.")
if a.month == 12 or 1 <= a.month <= 2 :
    print(f"이번달은 {a.month}월로 겨울 입니다.")
    print('추워요?')
