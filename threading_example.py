import threading
import time


def thread_func(num1, num2):
    print(f"Thread: starting ...")
    time.sleep(1)  # simulate expensive calculation
    print(f"Thread: Result of {num1} + {num2} is {num1 + num2}")
    print(f"Thread: finished ...")


if __name__ == '__main__':
    thread = threading.Thread(target=thread_func, args=(1, 2))
    # thread.setDaemon(True)
    print("Main: launch Thread")
    thread.start()
    # print('Main: Waiting for thread to finish')
    # thread.join()
    print('Main: finished')
