# Technical Report — Hospital Appointment & Triage System  
**Course:** Data Structures (ENCS205 / ENCA201 / ENBC201)  
**Assignment:** Capstone Assignment 5  
**Theme:** Queues, Stacks, Linked Lists, Hash Tables, Heaps  
**Student Name:** Naman Yadav 
**Roll No.:**  24010112
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

### 2.1 Doctor Schedule (Linked List)
Each doctor has a linked list of time slots:  
`slotId, startTime, endTime, status(FREE/BOOKED)`.  
Operations:
- `scheduleAddSlot()`
- `scheduleCancel()`
- `findSlot()`
- `getNextFreeSlot()`

### 2.2 Routine Appointment Queue (Circular Queue)
Stores routine appointments as tokens in `O(1)`.  
Prevents overflow using modular arithmetic.

Key operations:
- `enqueueRoutine()`
- `dequeueRoutine()`
- `peek()`
- `isFull()`
- `isEmpty()`

### 2.3 Emergency Triage (Min Heap)
Stores `(severity, patientId)` where **lower severity = higher priority**.

Operations:
- `triageInsert()`
- `triagePop()`
- `peek()`

### 2.4 Patient Index (Hash Table)
Keyed by `patientId`, storing:
`name, age, severity, visits`.

Operations:
- `patientUpsert()`
- `patientGet()`
- `delete()`

### 2.5 Undo Stack
Stores actions: `"book"`, `"triage"`, `"serve"`.

Operations:
- `undoPush()`
- `undoPop()`

Undo supports:
- removing last booked routine token  
- removing last triage emergency  
- restoring last served patient (best effort)  

---

## 3. Core Methods

| Method | Description |
|--------|-------------|
| `bookRoutine(patientId, doctorId, slotId)` | Adds a routine token to circular queue |
| `triageInsert(patientId, severity)` | Inserts emergency case into min-heap |
| `serveNext()` | Emergency first, then routine |
| `undoLast()` | Reverts last operation |
| `report()` | Summaries per doctor and queue |

---

## 4. Sample Workflow

1. Register patients  
2. Add doctors and slots  
3. Book a routine appointment  
4. Add emergency case  
5. Call `serveNext()`  
   - Emergency patient gets priority  
6. Print report  
7. Undo last action  

Output example:

