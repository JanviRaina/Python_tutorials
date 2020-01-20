# Suppose there is a work which takes  a lot of time and we want ki it  does half work and then next time we start from that half
# and continue our task we use coroutines

def searcher():
    import time
    # some 4 seconds time consuming task
    book="this is a text from book"
    time.sleep(4)   

    #we want ki next time it starts from here

    while(True):
        text=(yield)              # use searcher as coroutine
        if text in book:
            print("your text is in book")
        else:
            print("text is not in book")

search=searcher()
next(search)
search.send("book")
input("press any key")      # at this point it doesnt take time at all
search.send("from book")