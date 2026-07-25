#ifndef GRAPH_H
#define GRAPH_H

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <limits>
#include <algorithm>

// Structure to represent an edge in the graph
struct Edge {
    int destination;
    double distance;    // Distance in kilometers
    double speedLimit;  // Speed limit in km/h
    std::string roadName;

    // Calculate travel time in minutes based on distance and speed limit
    double getTravelTimeMinutes() const {
        if (speedLimit <= 0) return distance * 2.0; // fallback default
        return (distance / speedLimit) * 60.0;
    }
};

// Result structure returned by Dijkstra's algorithm
struct DijkstraResult {
    std::vector<double> costs;         // Distance or time costs from source
    std::vector<int> predecessors;    // To reconstruct shortest path
    std::vector<double> distances;    // Total cumulative physical distance (km)
    std::vector<double> travelTimes;  // Total cumulative travel time (mins)
};

class Graph {
private:
    int numVertices;
    std::vector<std::vector<Edge>> adjList;

public:
    explicit Graph(int vertices = 0);

    // Add an edge to the graph (bidirectional by default)
    void addEdge(int u, int v, double distance, double speedLimit, const std::string& roadName, bool bidirectional = true);

    // Dynamic vertex addition
    int addVertex();

    // Core Dijkstra's Algorithm
    // If optimizeForTime is true, weight = travel time (mins); else weight = distance (km)
    DijkstraResult runDijkstra(int startNode, bool optimizeForTime = false) const;

    // Backtrack using predecessor array to get node order
    std::vector<int> reconstructPath(int startNode, int endNode, const std::vector<int>& predecessors) const;

    // Getters
    int getNumVertices() const;
    const std::vector<Edge>& getEdges(int u) const;
};

#endif // GRAPH_H
