import os
import time
import subprocess
# Task 1: Process Creation Utility; 2301730163_Yashraj
def task1_process_creation(n):
    print("\n--- TASK 1: Creating Child Processes ---\n")
    child_pids = []
    for i in range(n):
        pid = os.fork()
        if pid == 0:  # Child
            print(f"[Child] PID: {os.getpid()}, Parent PID: {os.getppid()}, Message: Child {i} running")
            os._exit(0)
        else:
            child_pids.append(pid)
    # Parent waits for all children
    for pid in child_pids:
        os.waitpid(pid, 0)
    print("\n[Parent] All children finished.\n")
# Task 2: exec() Command Execution
def task2_exec_commands(n):
    print("\n--- TASK 2: Executing Commands in Child Processes ---\n")
    commands = [["ls"], ["date"], ["ps"]]
    for i in range(n):
        pid = os.fork()
        if pid == 0:  # Child
            print(f"\n[Child] PID {os.getpid()} executing command: {commands[i % len(commands)]}")
            os.execvp(commands[i % len(commands)][0], commands[i % len(commands)])
        else:
            os.waitpid(pid, 0)
# Task 3: Zombie & Orphan Simulation
def task3_zombie_orphan():
    print("\n--- TASK 3: Zombie & Orphan Simulation ---\n")
    # Zombie Process
    print("\n[Zombie Simulation]\n")
    pid = os.fork()
    if pid == 0:
        print(f"[Child-Zombie] PID {os.getpid()} exiting...")
        os._exit(0)
    else:
        print("[Parent] Not calling wait() → Child becomes zombie.")
        time.sleep(5)
        print("Run: ps -el | grep defunct")
    # Orphan Process
    print("\n[Orphan Simulation]\n")
    pid = os.fork()
    if pid == 0:
        print(f"[Child-Orphan] PID {os.getpid()} sleeping...")
        time.sleep(5)
        print(f"[Child-Orphan] New Parent PID after orphaning: {os.getppid()}")
        os._exit(0)
    else:
        print("[Parent] Exiting immediately → Child becomes orphan.")
        return  # Parent exits early
# Task 4: Inspecting /proc Information
def task4_proc_inspection():
    print("\n--- TASK 4: /proc Inspection ---\n")
    pid = input("Enter a PID to inspect: ")
    status_path = f"/proc/{pid}/status"
    exe_path = f"/proc/{pid}/exe"
    fd_path = f"/proc/{pid}/fd"
    try:
        print("\n[PROCESS STATUS]")
        with open(status_path, "r") as f:
            for line in f:
                if line.startswith(("Name:", "State:", "VmSize:")):
                    print(line.strip())
        print("\n[EXECUTABLE PATH]")
        print(os.readlink(exe_path))
        print("\n[OPEN FILE DESCRIPTORS]")
        print(os.listdir(fd_path))
    except FileNotFoundError:
        print(f"Invalid PID or process does not exist: {pid}")
# Task 5: Priority Scheduling Using nice()
def cpu_task(label):
    for i in range(5_000_000):
        pass
    print(f"[Child {label}] Completed")
def task5_priority():
    print("\n--- TASK 5: Priority Scheduling ---\n")
    priorities = [-5, 0, 5]  # High, normal, low
    labels = ["High Priority", "Normal Priority", "Low Priority"]
    for pr, label in zip(priorities, labels):
        pid = os.fork()
        if pid == 0:
            print(f"[Child] {label} → nice value: {pr}")
            os.nice(pr)
            cpu_task(label)
            os._exit(0)
        else:
            continue
    # Parent waits for all children
    while True:
        try:
            os.wait()
        except ChildProcessError:
            break
    print("\n[Parent] Priority execution complete.\n")
# MAIN PROGRAM; 2301730163_Yashraj
if __name__ == "__main__":
    print("\n===== Operating Systems Assignment: Process Management =====")
    # Task 1
    task1_process_creation(3)
    # Task 2
    task2_exec_commands(3)
    # Task 3
    task3_zombie_orphan()
    # Task 4
    task4_proc_inspection()
    # Task 5
    task5_priority()
    print("\n===== All Tasks Completed Successfully =====\n")
