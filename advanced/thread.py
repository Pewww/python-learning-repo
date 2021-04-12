# 5초의 시간이 걸리는 함수를 5번 반복해서 실행할 때
# 쓰레드를 사용하면 25초가 아닌 5초가 걸린다. (동시에 작업 수행)

import time
import threading

def long_task():
  for i in range(5):
    time.sleep(1)
    print(f'Working: {i}')

print('Start')

threads = []

for i in range(5):
  t = threading.Thread(target=long_task)
  threads.append(t)

for t in threads:
  t.start()

for t in threads:
  t.join() # 해당 스레드가 종료될 때 까지 기다리게 한다.

print('End')
