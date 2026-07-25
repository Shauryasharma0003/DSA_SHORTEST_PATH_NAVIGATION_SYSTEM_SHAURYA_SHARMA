#include "../include/Graph.h"

Graph::Graph(int vertices) : numVertices(vertices) {
    adjList.resize(vertices);
}

void Graph::addEdge(int u, int v, double distance, double speedLimit, const std::string& roadName, bool bidirectional) {
    if (u < 0 || u >= numVertices || v < 0 || v >= numVertices) {
        std::cerr << "[Error] Invalid vertex index when adding edge: " << u << " -> " << v << std::endl;
        return;
    }

    adjList[u].push_back({v, distance, speedLimit, roadName});
    if (bidirectional) {
        adjList[v].push_back({u, distance, speedLimit, roadName});
    }
}

int Graph::addVertex() {
    adjList.emplace_back();
    return numVertices++;
}

DijkstraResult Graph::runDijkstra(int startNode, bool optimizeForTime) const {
    DijkstraResult result;
    if (startNode < 0 || startNode >= numVertices) {
        return result;
    }

    const double INF = std::numeric_limits<double>::infinity();
    result.costs.assign(numVertices, INF);
    result.distances.assign(numVertices, INF);
    result.travelTimes.assign(numVertices, INF);
    result.predecessors.assign(numVertices, -1);

    // Min priority queue storing std::pair<cost, node>
    using QueueElement = std::pair<double, int>;
    std::priority_queue<QueueElement, std::vector<QueueElement>, std::greater<QueueElement>> pq;

    result.costs[startNode] = 0.0;
    result.distances[startNode] = 0.0;
    result.travelTimes[startNode] = 0.0;
    pq.push({0.0, startNode});

    while (!pq.empty()) {
        auto topPair = pq.top();
        double currentCost = topPair.first;
        int u = topPair.second;
        pq.pop();

        if (currentCost > result.costs[u]) {
            continue; // Stale queue item
        }

        for (const auto& edge : adjList[u]) {
            int v = edge.destination;
            double edgeWeight = optimizeForTime ? edge.getTravelTimeMinutes() : edge.distance;
            double newCost = result.costs[u] + edgeWeight;

            if (newCost < result.costs[v]) {
                result.costs[v] = newCost;
                result.distances[v] = result.distances[u] + edge.distance;
                result.travelTimes[v] = result.travelTimes[u] + edge.getTravelTimeMinutes();
                result.predecessors[v] = u;
                pq.push({newCost, v});
            }
        }
    }

    return result;
}

std::vector<int> Graph::reconstructPath(int startNode, int endNode, const std::vector<int>& predecessors) const {
    std::vector<int> path;
    if (endNode < 0 || endNode >= numVertices || predecessors.empty()) {
        return path;
    }

    for (int curr = endNode; curr != -1; curr = predecessors[curr]) {
        path.push_back(curr);
        if (curr == startNode) break;
    }

    std::reverse(path.begin(), path.end());

    // If path doesn't start at startNode, no valid path exists
    if (path.empty() || path.front() != startNode) {
        return {};
    }

    return path;
}

int Graph::getNumVertices() const {
    return numVertices;
}

const std::vector<Edge>& Graph::getEdges(int u) const {
    return adjList[u];
}
