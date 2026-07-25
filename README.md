# Shortest Path Navigation System (Dijkstra's Algorithm)

A C++ Data Structures & Algorithms (DSA) project implementing a **Shortest Path Navigation System** using **Dijkstra's Algorithm**.

This application models a realistic city network where locations (landmarks, transit hubs, hospitals, airports) are graph vertices and roads are weighted edges with distance (km) and speed limits (km/h).

---

## 🌟 Key Features

1. **Adjacency List Graph Representation**: Efficient graph data structure storing vertices, edges, distances, speed limits, and road names.
2. **Dijkstra's Algorithm Implementation**: Calculates shortest paths using a Min-Priority Queue (`std::priority_queue`).
3. **Dual Optimization Modes**:
   - **Shortest Distance**: Finds the path with the minimum total distance (in km).
   - **Fastest Travel Time**: Calculates estimated travel time using speed limits to find the quickest route (in minutes).
4. **Turn-by-Turn Guidance**: Detailed step-by-step navigation instructions showing road names, individual segment distances, and travel times.
5. **Interactive Console Menu**: Easy-to-use menu allowing users to view map schematics, list landmarks, run queries, and dynamically add custom locations/roads.
6. **ASCII Map Schematic**: Visual layout representation of the pre-loaded city map directly in the terminal.

---

## 📐 Data Structures & Complexity Analysis

### 1. Graph Representation
- **Data Structure**: Adjacency List (`std::vector<std::vector<Edge>>`)
- **Space Complexity**: $\mathcal{O}(V + E)$ where $V$ is the number of locations and $E$ is the number of roads.

### 2. Dijkstra's Algorithm
- **Data Structure**: Min-Heap Priority Queue (`std::priority_queue<std::pair<double, int>, ..., std::greater<...>>`)
- **Time Complexity**: $\mathcal{O}((V + E) \log V)$
  - Extract min operation takes $\mathcal{O}(\log V)$.
  - Every edge is relaxed once, taking $\mathcal{O}(E \log V)$.
- **Space Complexity**: $\mathcal{O}(V)$ for storing distance arrays, predecessor pointers, and priority queue items.

---

## 📂 Project Structure

```
project/
├── include/
│   ├── Graph.h            # Core Graph data structure & Dijkstra declaration
│   └── NavigationSystem.h # High-level navigation manager header
├── src/
│   ├── Graph.cpp            # Implementation of Graph & Dijkstra's Algorithm
│   ├── NavigationSystem.cpp # Pre-loaded city map, navigation & display handlers
│   └── main.cpp             # Interactive CLI menu loop
├── CMakeLists.txt           # CMake build script
├── Makefile                 # GNU Make build script
└── README.md                # Project documentation
```

---

## 🛠️ How to Build and Run

### Option 1: Using `g++` directly (Recommended for Windows / Linux / macOS)
```bash
g++ -std=c++17 -Iinclude src/main.cpp src/Graph.cpp src/NavigationSystem.cpp -o navigation_system
./navigation_system
```

### Option 2: Using `make`
```bash
make
./navigation_system
```

### Option 3: Using `CMake`
```bash
mkdir build
cd build
cmake ..
cmake --build .
./navigation_system
```

---

## 🗺️ Pre-loaded City Locations

| ID | Location Name | Category |
|---|---|---|
| 0 | Central Station | Transit Hub |
| 1 | Downtown Hub | Commercial Center |
| 2 | City General Hospital | Healthcare |
| 3 | Tech Park | Business District |
| 4 | State University | Education |
| 5 | Metropolitan Airport | Airport |
| 6 | Sunset Mall | Shopping |
| 7 | Grand Park | Recreation |
| 8 | Riverside District | Residential |

---

## 🚀 Sample Usage / Output

```text
=========================================================================
                  OPTIMAL NAVIGATION ROUTE FOUND                         
=========================================================================
 Origin        : Central Station (ID: 0)
 Destination   : Metropolitan Airport (ID: 5)
 Optimization  : Shortest Distance
-------------------------------------------------------------------------
 TURN-BY-TURN NAVIGATION INSTRUCTIONS:
-------------------------------------------------------------------------
 Step 1: [0] Central Station
         |--> Drive along 'Main Street' (3.5 km @ 40 km/h ~ 5.3 mins)
 Step 2: [1] Downtown Hub
         |--> Drive along 'Tech Boulevard' (8.2 km @ 70 km/h ~ 7.0 mins)
 Step 3: [3] Tech Park
         |--> Drive along 'Airport Highway' (12 km @ 90 km/h ~ 8.0 mins)
 Step 4: [5] Metropolitan Airport  (ARRIVED!)
-------------------------------------------------------------------------
 SUMMARY:
 Total Distance      : 23.70 km
 Est. Travel Time    : 20.3 mins
 Number of Segments  : 3 road segments
=========================================================================
```
