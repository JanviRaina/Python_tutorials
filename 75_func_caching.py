import time
from functools import lru_cache

@lru_cache(maxsize=3)           #last 3 calls
def some_work(n):               # taken sleep for function..it could be any func taking 3 seconds
    time.sleep(n)
    return

if  __name__ == "__main__":
    print("calling func")
    some_work(3)
    print("again calling")
    some_work(3)
    print("called again")


    #using caching it can retrieve from cached memory

