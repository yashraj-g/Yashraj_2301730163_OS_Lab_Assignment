# Operating Systems Lab – Assignment 3

## Simulation of File Allocation, Memory Management, and CPU Scheduling in Python

### Course Code: ENCS351
### Program: B.Tech CSE(AI/ML)-C
### Student: Yashraj Singh
### Roll No.: 2301730163

# Overview

This repository contains the Python implementations for Lab Assignment 3 of Operating Systems.
The assignment covers the simulation of:

-CPU Scheduling Algorithms

-File Allocation Methods

-Memory Management Techniques

-MFT & MVT Schemes

Each task is implemented using simple Python scripts that reflect how real operating systems manage CPU time, disk blocks, and memory partitions.

# Folder Structure

```
Lab_Sheet_3/
│
├── Task_1_os3task1.py
├── Task_2_os3task2.py
├── Task_3_os3task3.py
├── Task_4_os3task4.py
├── Task_5_os3task5.py
└── report_LabSheet-3.pdf
└── README.md


```

# 🧪 Assignment Tasks
## ✅ Task 1: CPU Scheduling (Priority & Round Robin)

-Implements Priority Scheduling (lower value → higher priority)

-Implements Round Robin Scheduling

-Calculates Waiting Time (WT) and Turnaround Time (TAT)

-Displays a simple Gantt chart order

-Helps understand preemption and priority handling

## ✅ Task 2: Sequential File Allocation

-Simulates block-based sequential file allocation

-Checks availability of contiguous free blocks

-Allocates or rejects a file based on block status

## ✅ Task 3: Indexed File Allocation

-Uses an index block to map all data blocks

-Ensures each selected data block is free

-Displays index → data block linkage

## ✅ Task 4: Contiguous Memory Allocation (First-Fit, Best-Fit, Worst-Fit)

-Simulates all three allocation strategies

-Allocates processes to partitions

-Shows internal & external fragmentation behavior

## ✅ Task 5: MFT & MVT Memory Management

-MFT (Fixed Partitions):

-Divides memory equally

-Allocates processes if size <= partition size

-MVT (Variable Partitions):

-Allocates memory dynamically

-Demonstrates fragmentation reduction

# Requirements

Python 3.x

Terminal / CMD / WSL

No external libraries required

## Submitted by 

Name: Yashraj Singh

Roll No.: 2301730163


Program: B.Tech CSE(AI/ML) , K.R. Mangalam University

