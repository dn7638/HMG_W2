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
    # print(f"Process {name} Finished.")

# 멀티프로세싱 Pool을 사용하여 작업을 병렬로 실행
if __name__ == '__main__':
    # 2명의 작업자로 Pool 초기화
    with multiprocessing.Pool(processes=2) as pool:
        pool.map(work_log, tasks)
