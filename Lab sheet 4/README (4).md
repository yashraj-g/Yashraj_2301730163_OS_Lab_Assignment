# Operating Systems Lab – Assignment 4

## System Calls, VM Detection, and File System Operations

Course Code: ENCS351

Program: B.Tech CSE(AI/ML)-C

Student: Yashraj Singh

Roll No.: 2301730163

# Overview

This repository contains all scripts and files for Lab Assignment 4, which focuses on advanced Operating System concepts including:

-System call simulation (fork(), exec(), wait(), pipe())

-Batch processing execution using Python

-System startup & shutdown simulation with logging

-VM (Virtual Machine) detection using Python & Shell scripts

-CPU scheduling algorithms (FCFS, SJF, RR, Priority Scheduling)

This lab bridges OS theory with practical implementation.


# Folder Structure

```

OS_Lab_Sheet_4/
│
├── os4task1.py
├── os4task2.py
├── os4task3.py
├── os4task4.py
├── os4task5.py
├── system_log.txt
├──report_Lab_Sheet_4.pdf
└── README.md


```


# Assignment Tasks

✔ Task 1: Batch Processing System

A Python script executes multiple .py files sequentially using subprocess.call().
Simulates early OS batch execution.

✔ Task 2: System Startup Simulation

Simulates OS boot process using multiple child processes.

Uses multiprocessing.Process

Logs start/end timestamps

Output stored in system_log.txt

✔ Task 3: System Calls & IPC

Simulates:

fork() – Creating child processes

exec() – Replacing process memory

wait() – Synchronizing parent & child

pipe() – One-way communication

Parent sends data → child receives it.

✔ Task 4: Virtual Machine (VM) Detection

Includes:

Bash script to check kernel & hardware info

Python script checking /proc/cpuinfo, CPU flags, virtualization hints

Detects environments like VMware, VirtualBox, WSL.

✔ Task 5: CPU Scheduling Algorithms

Simulates:

FCFS

SJF

Priority Scheduling

Round Robin (RR)

Outputs include:

Waiting Time

Turnaround Time

Gantt Chart order

# Requirements

Python 3.x

Linux or WSL recommended

Bash for VM detection script


No external Python libraries required

