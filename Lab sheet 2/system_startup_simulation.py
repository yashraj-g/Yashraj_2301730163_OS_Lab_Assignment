import multiprocessing
import time
import logging

# Sub-Task 1: Initialize logging; 2301730163_Yashraj
logging.basicConfig(
    filename='process_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

# Sub-Task 2: Dummy system process
def system_process(task_name):
    logging.info(f"{task_name} started")
    time.sleep(2)
    logging.info(f"{task_name} ended")

if __name__ == "__main__":
    print("System Starting...")

    # Sub-Task 3: Create processes
    p1 = multiprocessing.Process(target=system_process, args=("Process-1",))
    p2 = multiprocessing.Process(target=system_process, args=("Process-2",))

    # Start processes
    p1.start()
    p2.start()

    # Sub-Task 4: Join/wait for termination
    p1.join()
    p2.join()

    print("System Shutdown.")
