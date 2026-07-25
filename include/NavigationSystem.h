#ifndef NAVIGATION_SYSTEM_H
#define NAVIGATION_SYSTEM_H

#include "Graph.h"
#include <unordered_map>
#include <iomanip>

struct Landmark {
    int id;
    std::string name;
    std::string category; // e.g. "Airport", "Hospital", "University", "Downtown"
};

class NavigationSystem {
private:
    Graph graph;
    std::vector<Landmark> landmarks;
    std::unordered_map<std::string, int> nameToIdMap;

    std::string toLowerCase(const std::string& str) const;

public:
    NavigationSystem();

    // Populate pre-configured city map
    void loadDefaultCityMap();

    // Landmark operations
    int addLandmark(const std::string& name, const std::string& category);
    int getLandmarkId(const std::string& name) const;
    std::string getLandmarkName(int id) const;

    // Edge/Road operations
    void addRoad(int u, int v, double distance, double speedLimit, const std::string& roadName, bool bidirectional = true);

    // Display & Navigation functions
    void displayAllLandmarks() const;
    void displayRoadNetwork() const;
    void displayASCIIArtMap() const;

    // Navigation query execution
    void findAndPrintShortestRoute(const std::string& srcName, const std::string& destName, bool optimizeForTime = false) const;
};

#endif // NAVIGATION_SYSTEM_H
