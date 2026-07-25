#include "../include/NavigationSystem.h"

NavigationSystem::NavigationSystem() {}

std::string NavigationSystem::toLowerCase(const std::string& str) const {
    std::string lower = str;
    std::transform(lower.begin(), lower.end(), lower.begin(), ::tolower);
    return lower;
}

int NavigationSystem::addLandmark(const std::string& name, const std::string& category) {
    std::string lowerName = toLowerCase(name);
    if (nameToIdMap.find(lowerName) != nameToIdMap.end()) {
        return nameToIdMap[lowerName];
    }

    int newId = graph.addVertex();
    landmarks.push_back({newId, name, category});
    nameToIdMap[lowerName] = newId;
    return newId;
}

void NavigationSystem::addRoad(int u, int v, double distance, double speedLimit, const std::string& roadName, bool bidirectional) {
    graph.addEdge(u, v, distance, speedLimit, roadName, bidirectional);
}

int NavigationSystem::getLandmarkId(const std::string& name) const {
    std::string lowerName = toLowerCase(name);
    auto it = nameToIdMap.find(lowerName);
    if (it != nameToIdMap.end()) {
        return it->second;
    }
    // Try partial matching by index if user inputs an integer
    try {
        int id = std::stoi(name);
        if (id >= 0 && id < (int)landmarks.size()) {
            return id;
        }
    } catch (...) {
        // Not a number
    }
    return -1;
}

std::string NavigationSystem::getLandmarkName(int id) const {
    if (id >= 0 && id < (int)landmarks.size()) {
        return landmarks[id].name;
    }
    return "Unknown Landmark";
}

void NavigationSystem::loadDefaultCityMap() {
    // Add default city landmarks
    int cs  = addLandmark("Central Station", "Transit Hub");
    int dt  = addLandmark("Downtown Hub", "Commercial Center");
    int hosp= addLandmark("City General Hospital", "Healthcare");
    int tp  = addLandmark("Tech Park", "Business District");
    int uni = addLandmark("State University", "Education");
    int apt = addLandmark("Metropolitan Airport", "Airport");
    int mall= addLandmark("Sunset Mall", "Shopping");
    int park= addLandmark("Grand Park", "Recreation");
    int river= addLandmark("Riverside District", "Residential");

    // Add connecting roads (u, v, distance_km, speed_limit_kmh, road_name)
    addRoad(cs, dt, 3.5, 40.0, "Main Street");
    addRoad(cs, hosp, 5.0, 50.0, "Hospital Expressway");
    addRoad(dt, hosp, 2.8, 45.0, "Park Avenue");
    addRoad(dt, tp, 8.2, 70.0, "Tech Boulevard");
    addRoad(dt, park, 4.0, 40.0, "Green Way");
    addRoad(hosp, uni, 6.1, 50.0, "University Drive");
    addRoad(tp, apt, 12.0, 90.0, "Airport Highway");
    addRoad(uni, tp, 4.5, 60.0, "Innovation Way");
    addRoad(uni, apt, 15.0, 80.0, "Outer Ring Road");
    addRoad(cs, mall, 6.0, 45.0, "Commercial Drive");
    addRoad(mall, park, 3.2, 40.0, "Sunset Boulevard");
    addRoad(park, river, 4.8, 50.0, "River Road");
    addRoad(river, apt, 10.5, 85.0, "East Bypass");
}

void NavigationSystem::displayAllLandmarks() const {
    std::cout << "\n=======================================================\n";
    std::cout << "                 AVAILABLE CITY LOCATIONS              \n";
    std::cout << "=======================================================\n";
    std::cout << std::left << std::setw(6) << "ID"
              << std::setw(28) << "Location Name"
              << std::setw(20) << "Category" << "\n";
    std::cout << "-------------------------------------------------------\n";
    for (const auto& lm : landmarks) {
        std::cout << std::left << std::setw(6) << lm.id
                  << std::setw(28) << lm.name
                  << std::setw(20) << lm.category << "\n";
    }
    std::cout << "=======================================================\n";
}

void NavigationSystem::displayRoadNetwork() const {
    std::cout << "\n=========================================================================\n";
    std::cout << "                        CITY ROAD NETWORK ADJACENCY                      \n";
    std::cout << "=========================================================================\n";
    for (const auto& lm : landmarks) {
        std::cout << "[" << lm.id << "] " << lm.name << " connects to:\n";
        const auto& edges = graph.getEdges(lm.id);
        if (edges.empty()) {
            std::cout << "    (No outgoing connections)\n";
        } else {
            for (const auto& edge : edges) {
                std::cout << "    --> " << std::left << std::setw(25) << getLandmarkName(edge.destination)
                          << " | Dist: " << std::setw(5) << edge.distance << " km"
                          << " | Speed: " << std::setw(4) << edge.speedLimit << " km/h"
                          << " | Road: " << edge.roadName << "\n";
            }
        }
        std::cout << "-------------------------------------------------------------------------\n";
    }
}

void NavigationSystem::displayASCIIArtMap() const {
    std::cout << "\n";
    std::cout << "=========================================================================\n";
    std::cout << "                      CITY GRAPH SCHEMATIC MAP                           \n";
    std::cout << "=========================================================================\n";
    std::cout << "   [6] Sunset Mall ---- (3.2 km) ---- [7] Grand Park ---- (4.8 km) ---- [8] Riverside\n";
    std::cout << "          |                                 |                                  |\n";
    std::cout << "       (6.0 km)                          (4.0 km)                           (10.5 km)\n";
    std::cout << "          |                                 |                                  |\n";
    std::cout << "   [0] Central Station - (3.5 km) - [1] Downtown Hub                         |\n";
    std::cout << "          |                                 |                                  |\n";
    std::cout << "       (5.0 km)                          (8.2 km)                           |\n";
    std::cout << "          |                                 |                                  |\n";
    std::cout << "   [2] City Hospital - (6.1 km) - [4] State Uni - (4.5 km) - [3] Tech Park   |\n";
    std::cout << "                                        |                         |            |\n";
    std::cout << "                                     (15.0 km)                (12.0 km)        |\n";
    std::cout << "                                        |                         |            |\n";
    std::cout << "                                        +---> [5] Airport <-------+------------+\n";
    std::cout << "=========================================================================\n";
}

void NavigationSystem::findAndPrintShortestRoute(const std::string& srcName, const std::string& destName, bool optimizeForTime) const {
    int srcId = getLandmarkId(srcName);
    int destId = getLandmarkId(destName);

    if (srcId == -1) {
        std::cout << "\n[Error] Source location '" << srcName << "' not found in city map.\n";
        return;
    }
    if (destId == -1) {
        std::cout << "\n[Error] Destination location '" << destName << "' not found in city map.\n";
        return;
    }

    if (srcId == destId) {
        std::cout << "\n[Notice] Source and destination are identical: " << getLandmarkName(srcId) << "\n";
        return;
    }

    // Run Dijkstra's Algorithm
    DijkstraResult result = graph.runDijkstra(srcId, optimizeForTime);
    std::vector<int> path = graph.reconstructPath(srcId, destId, result.predecessors);

    if (path.empty()) {
        std::cout << "\n[Notice] No route exists between " << getLandmarkName(srcId)
                  << " and " << getLandmarkName(destId) << ".\n";
        return;
    }

    std::cout << "\n=========================================================================\n";
    std::cout << "                  OPTIMAL NAVIGATION ROUTE FOUND                         \n";
    std::cout << "=========================================================================\n";
    std::cout << " Origin        : " << getLandmarkName(srcId) << " (ID: " << srcId << ")\n";
    std::cout << " Destination   : " << getLandmarkName(destId) << " (ID: " << destId << ")\n";
    std::cout << " Optimization  : " << (optimizeForTime ? "Fastest Travel Time" : "Shortest Distance") << "\n";
    std::cout << "-------------------------------------------------------------------------\n";
    std::cout << " TURN-BY-TURN NAVIGATION INSTRUCTIONS:\n";
    std::cout << "-------------------------------------------------------------------------\n";

    double accumDist = 0.0;
    double accumTime = 0.0;

    for (size_t i = 0; i < path.size(); ++i) {
        int currentId = path[i];
        std::cout << " Step " << (i + 1) << ": [" << currentId << "] " << getLandmarkName(currentId);

        if (i < path.size() - 1) {
            int nextId = path[i + 1];
            // Find edge information
            const auto& edges = graph.getEdges(currentId);
            for (const auto& e : edges) {
                if (e.destination == nextId) {
                    accumDist += e.distance;
                    accumTime += e.getTravelTimeMinutes();
                    std::cout << "\n         |--> Drive along '" << e.roadName << "' ("
                              << e.distance << " km @ " << e.speedLimit << " km/h ~ "
                              << std::fixed << std::setprecision(1) << e.getTravelTimeMinutes() << " mins)\n";
                    break;
                }
            }
        } else {
            std::cout << "  (ARRIVED!)\n";
        }
    }

    std::cout << "-------------------------------------------------------------------------\n";
    std::cout << " SUMMARY:\n";
    std::cout << " Total Distance      : " << std::fixed << std::setprecision(2) << result.distances[destId] << " km\n";
    std::cout << " Est. Travel Time    : " << std::fixed << std::setprecision(1) << result.travelTimes[destId] << " mins\n";
    std::cout << " Number of Segments  : " << (path.size() - 1) << " road segments\n";
    std::cout << "=========================================================================\n";
}
