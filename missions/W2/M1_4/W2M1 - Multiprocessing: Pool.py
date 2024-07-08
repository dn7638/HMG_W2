import multiprocessing
import time

# 작업 정의 (이름과 지속 시간)
tasks = [
    ('A', 5),
    ('B', 2),
    ('C', 1),
    ('D', 3)
]

# 작업을 시뮬레이션하는 함수
def work_log(task):
    name, duration = task
    print(f"Process {name} waiting {duration} seconds")
    time.sleep(duration)
    
    print(f"Process {name} Finished.")
    return name

# 멀티프로세싱 Pool을 사용하여 작업을 병렬로 실행
if __name__ == '__main__':
    # 2명의 작업자로 Pool 초기화
    '''
    multiprocessing 모듈은 파이썬에서 병렬 처리를 구현하기 위한 기능을 제공하는 모듈
    이중 Pool 클래스의 경우 여러 프로세스를 풀에서 관리하고 작업을 수행할 수 있음.
    출력 결과를 보면 최대 2개의 작업이 병렬적으로 수행됨.
    하나의 작업이 끝나면 다른 작업이 시작됨을 알 수 있음
    '''
    with multiprocessing.Pool(processes=2) as pool:
        pool.map(work_log, tasks)
