# Technical Report — Hospital Appointment & Triage System  
**Course:** Data Structures (ENCS205 / ENCA201 / ENBC201)  
**Assignment:** Capstone Assignment 5  
**Theme:** Queues, Stacks, Linked Lists, Hash Tables, Heaps  
**Student Name:**Naman Yadav  
**Roll No.:**  2401010112
**Section:**  B

---

## 1. Introduction

Outpatient Departments (OPDs) manage a high volume of routine appointments, walk-ins, and emergency cases.  
To model such real-world workflows, this project implements a **Hospital Appointment & Triage System** using multiple data structures:

- **Singly Linked List** → Doctor schedules  
- **Circular Queue** → Routine appointment tokens  
- **Min Heap** → Emergency triage with severity-based priority  
- **Hash Table** → Fast patient lookup  
- **Stack** → Undo/rollback actions  

The project integrates these structures to support booking, serving, emergency handling, reporting, and undo operations.

---

## 2. System Architecture & ADTs

### 2.1 Doctor Schedul
