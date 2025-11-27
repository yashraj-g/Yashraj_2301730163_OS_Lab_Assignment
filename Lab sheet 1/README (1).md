# Operating Systems Lab Assignment – Process Creation & Management (ENCS351)

This repository contains the complete solution for Operating Systems Lab Sheet 1 from the ENCS351 course.
The experiment demonstrates core Linux process management concepts using Python, including forking, executing commands, zombie/orphan processes, /proc inspection, and process prioritization.

## Folder Structure

```
Yashraj_2301730163_OS_Lab_Assignment/
 ├─ Lab_Sheet_1/
 │   ├─ process_management.py
 │   ├─ output.txt
 │   ├─ report_Lab_sheet_1.pdf
 │   └─ README(1).md
 └─ README.md  ← (this main file)

```

## Experiment Title

Process Creation and Management Using Python OS Module

## Objectives

-Understand the Linux process lifecycle

-Create child processes using os.fork()

-Execute system commands with os.execvp() and subprocess.run()

-Demonstrate zombie and orphan process behavior

-Inspect processes using /proc/<pid>

-Manipulate scheduling priority using os.nice()

## Concepts Used

-os.fork(), os.getpid(), os.getppid()

-os._exit(), os.wait()

-os.execvp(), subprocess.run()

-Reading /proc/[pid]/status, /proc/[pid]/exe, /proc/[pid]/fd

-os.nice() for process priority

## Lab Tasks Overview

### Task 1 — Process Creation

-Create N child processes

-Each child prints:

-Its PID

-Parent PID

-A message

-Parent waits for all children using os.wait()

### Task 2 — Command Execution Using exec()

-Each child executes a system command such as:

-ls

-date

-ps

-Using os.execvp() or subprocess.run().

### Task 3 — Zombie & Orphan Processes

-Zombie: Parent does not call wait()

-Orphan: Parent exits early, child reattached to init (PID 1)

-Verification via:

-ps -el | grep defunct

### Task 4 — Inspect /proc Information

-Given a PID:

-Read /proc/[pid]/status → Process name, state, memory

-Read /proc/[pid]/exe → Executable path

-Read /proc/[pid]/fd/ → Open file descriptors

### Task 5 — Process Prioritization with nice()

-Create CPU-intensive child processes

-Assign priorities:

-High priority (nice -5)

-Normal (nice 0)

-Low priority (nice +5)

-Observe execution order based on scheduling

## How to Run

### Prerequisites

Before running, ensure:

Linux system OR WSL (Ubuntu/Kali)

Python 3.x installed

Access to /proc filesystem (only available on Linux)

Check Python version:

python --version

Run the Program

Navigate to the Lab Sheet folder:

cd Lab_Sheet_1


Run the script:

python process_management.py

Output Files

output.txt → Sample outputs of all tasks

report.pdf → Experiment report with explanation

process_management.py → Main Python program

# Submitted by

Name: Yashraj Singh

Course: B.Tech CSE(AI/ML)

Roll No.: 2301730163

University: K.R. Mangalam University



