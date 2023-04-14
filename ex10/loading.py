import time

def ft_progress(listy):
    start_time = time.time()
    for i, item in enumerate(listy):
        size = len(listy)
        now_time = time.time()
        print(f"ETA: {item:06d}s [{i/size*100:5.1f}%][====>] {i+1:04d}/{size:04d} | elapsed time: {now_time-start_time:.0f}s", end = '\r')
        yield item

if __name__ == '__main__':
    
    listy = range(2000, 0, -1)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)
    print()
    print(ret)
