import time

PROGRESS_BAR_SIZE = 20
load_str = "|\-/"

def ft_progress(listy):
    start_time = time.time()
    size = len(listy)
    prog_str = '>'.ljust(PROGRESS_BAR_SIZE)
    next_step = 1/PROGRESS_BAR_SIZE
    other_step = 0.2/PROGRESS_BAR_SIZE
    load_char = load_str[0]
    j = 1
    for i, item in enumerate(listy):
        progress = (i + 1)/size
        if progress > next_step:
            prog_str = '=' + prog_str[0:-1]
            next_step += 1/PROGRESS_BAR_SIZE
        if progress > other_step:
            load_char = load_str[j]
            j += 1
            if j >= 4:
                j = 0
            other_step += 0.2/PROGRESS_BAR_SIZE
        diff_time = time.time() - start_time
        remain_time = (1 - progress) * (diff_time / progress)
        if remain_time > 60:
            remain_time /= 60
            remain_time = f"{remain_time:6.2f} min"
        else:
            remain_time = f"{remain_time:6.2f} s  "
        if diff_time > 60:
            diff_time /= 60
            diff_time = f"{diff_time:6.2f} min"
        else:
            diff_time = f"{diff_time:6.2f} s  "
        print(f"\r-> ETA: {remain_time} [{prog_str[0:int(PROGRESS_BAR_SIZE/2)]} {progress*100:5.2f}% {prog_str[int(PROGRESS_BAR_SIZE/2):]}] {i+1:5d}/{size:5d} | elapsed time: {diff_time}  {load_char}", end = '')

        yield item

if __name__ == '__main__':
    
    listy = range(2000, 0, -1)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)
    print()
    print(ret)
