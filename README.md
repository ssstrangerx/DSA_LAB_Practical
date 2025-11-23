# Data Structures and Algorithms - Lab Programs

This repository contains Python implementations of various Data Structures and Algorithms lab assignments.

## Programs Included

## Searching Algorithms

### 1. Linear_Search.py
Implements linear search algorithm to find an element in an array.

**How to run:**
```bash
python Linear_Search.py
```
Enter the element you want to search when prompted.

**Time Complexity:**
- Best Case: O(1)
- Worst Case: O(n)

---

### 2. Binary_Search.py
Implements binary search algorithm to find an element in a sorted array.

**How to run:**
```bash
python Binary_Search.py
```
Enter the element you want to search when prompted.

**Time Complexity:**
- Best Case: O(1)
- Worst Case: O(log n)

**Note:** Array must be sorted for binary search to work correctly.

---

### 3. binary_search.py
Alternative implementation of binary search with user input.

**How to run:**
```bash
python binary_search.py
```

---

## Sorting Algorithms

### 4. Bubble_Sort.py
Implements bubble sort algorithm to sort an array in ascending order.

**How to run:**
```bash
python Bubble_Sort.py
```

**Time Complexity:**
- Best Case: O(n)
- Worst Case: O(n²)

---

### 5. bubble_sort.py
Optimized bubble sort implementation with multiple test cases.

**How to run:**
```bash
python bubble_sort.py
```

---

## Stack Operations

### 6. functions.py
Implements stack data structure with basic operations.

**Operations:**
- Push - Add element to stack
- Pop - Remove element from stack
- Peek - View top element
- Display - Show all stack elements

**How to run:**
```bash
python functions.py
```

---

### 7. History.py
Browser history simulation using stack data structure.

**Features:**
- Visit web pages
- Go back to previous pages
- Go forward to next pages
- View browsing history
- Clear history
- Opens actual URLs in browser

**How to run:**
```bash
python History.py
```

**Commands:**
- `visit <URL>` - Visit a webpage
- `back` - Go back
- `forward` - Go forward
- `current` - Show current page
- `show` - Display history
- `delete` - Clear history
- `exit` - Exit program

---

## Linked List

### 8. Circular_Linked_List_Deletion.py
Implements a circular linked list with deletion operations at beginning and end.

**Operations:**
- Insert elements
- Delete from beginning
- Delete from end
- Display the list

**How to run:**
```bash
python Circular_Linked_List_Deletion.py
```

---

## Queue Operations

### 9. Circular_Queue.py
Implements a circular queue with enqueue and dequeue operations.

**Operations:**
- Enqueue (insert element)
- Dequeue (remove element)
- Display queue elements
- Check if queue is full or empty

**How to run:**
```bash
python Circular_Queue.py
```

---

## Application Programs

### 10. inventory.py
Complete inventory management system using data structures.

**Features:**
- Insert products with SKU, name, and quantity
- Display entire inventory
- Search products by SKU or name
- Delete products from inventory
- Input validation and error handling

**How to run:**
```bash
python inventory.py
```

---

### 11. inventory_buy_a_product.py
Enhanced inventory management system with purchase functionality.

**Additional Feature:**
- Buy products with quantity validation
- Automatic stock reduction after purchase
- All features from inventory.py included

**How to run:**
```bash
python inventory_buy_a_product.py
```

---

### 12. weather.py
Weather data storage system using 2D arrays and sparse matrices.

**Features:**
- Add weather records (date, city, temperature)
- Remove records
- Retrieve data by city and year
- Row-wise and column-wise data access
- Sparse matrix representation
- Performance comparison of access methods
- Sparseness analysis

**How to run:**
```bash
python weather.py
```

**Concepts Demonstrated:**
- 2D array implementation
- Sparse matrix storage
- Time complexity analysis
- Data grid operations

---

## Requirements

- Python 3.x
- webbrowser module (built-in)
- time module (built-in)

## Usage

Clone or download all files and run them individually using Python 3.

```bash
python <program_name>.py
```

---

## Program Categories

**Basic Data Structures:**
- Stack (functions.py, History.py)
- Queue (Circular_Queue.py)
- Linked List (Circular_Linked_List_Deletion.py)

**Algorithms:**
- Searching (Linear_Search.py, Binary_Search.py, binary_search.py)
- Sorting (Bubble_Sort.py, bubble_sort.py)

**Applications:**
- Inventory Management (inventory.py, inventory_buy_a_product.py)
- Browser History (History.py)
- Weather Data Storage (weather.py)

---

## Author

Pranav Tripathi
B.Tech Computer Science
KR Mangalam University

---

## License

GPL-2.0 license
