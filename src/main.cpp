#include "../include/NavigationSystem.h"
#include <iostream>
#include <limits>

void printBanner() {
    std::cout << "\n=========================================================================\n";
    std::cout << "         SHORTEST PATH NAVIGATION SYSTEM (DIJKSTRA'S ALGORITHM)          \n";
    std::cout << "                     Data Structures & Algorithms Project                \n";
    std::cout << "=========================================================================\n";
}

void printMenu() {
    std::cout << "\n------------------------------ MAIN MENU ------------------------------\n";
    std::cout << " 1. Display All City Locations / Landmarks\n";
    std::cout << " 2. View Complete Road Network (Adjacency List)\n";
    std::cout << " 3. View ASCII Map Schematic\n";
    std::cout << " 4. Find Shortest Route (Optimized for Distance in km)\n";
    std::cout << " 5. Find Fastest Route (Optimized for Travel Time in mins)\n";
    std::cout << " 6. Add Custom Location / Landmark\n";
    std::cout << " 7. Add Custom Road / Edge Connection\n";
    std::cout << " 8. Exit System\n";
    std::cout << "-------------------------------------------------------------------------\n";
    std::cout << "Enter choice (1-8): ";
}

void clearInputStream() {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

int main() {
    NavigationSystem navSys;
    navSys.loadDefaultCityMap();

    printBanner();

    int choice = 0;
    while (true) {
        printMenu();
        if (!(std::cin >> choice)) {
            std::cout << "\n[Error] Invalid input. Please enter a number between 1 and 8.\n";
            clearInputStream();
            continue;
        }
        clearInputStream(); // consume leftover newline

        if (choice == 8) {
            std::cout << "\nThank you for using the Navigation System! Goodbye.\n";
            break;
        }

        switch (choice) {
            case 1:
                navSys.displayAllLandmarks();
                break;

            case 2:
                navSys.displayRoadNetwork();
                break;

            case 3:
                navSys.displayASCIIArtMap();
                break;

            case 4:
            case 5: {
                bool optimizeForTime = (choice == 5);
                std::string src, dest;

                navSys.displayAllLandmarks();
                std::cout << "\nEnter Source Location (Name or ID): ";
                std::getline(std::cin, src);
                std::cout << "Enter Destination Location (Name or ID): ";
                std::getline(std::cin, dest);

                navSys.findAndPrintShortestRoute(src, dest, optimizeForTime);
                break;
            }

            case 6: {
                std::string name, category;
                std::cout << "\nEnter Location Name: ";
                std::getline(std::cin, name);
                std::cout << "Enter Category (e.g. Landmark, Hospital, Park): ";
                std::getline(std::cin, category);

                int id = navSys.addLandmark(name, category);
                std::cout << "\n[Success] Added Location: '" << name << "' with ID: " << id << "\n";
                break;
            }

            case 7: {
                navSys.displayAllLandmarks();
                std::string srcStr, destStr, roadName;
                double dist, speed;

                std::cout << "\nEnter Source Location (Name or ID): ";
                std::getline(std::cin, srcStr);
                std::cout << "Enter Destination Location (Name or ID): ";
                std::getline(std::cin, destStr);

                int u = navSys.getLandmarkId(srcStr);
                int v = navSys.getLandmarkId(destStr);

                if (u == -1 || v == -1) {
                    std::cout << "\n[Error] Invalid source or destination location.\n";
                    break;
                }

                std::cout << "Enter Road Name: ";
                std::getline(std::cin, roadName);
                std::cout << "Enter Distance (in km): ";
                while (!(std::cin >> dist) || dist <= 0) {
                    std::cout << "Invalid distance. Enter positive number: ";
                    clearInputStream();
                }
                std::cout << "Enter Speed Limit (in km/h): ";
                while (!(std::cin >> speed) || speed <= 0) {
                    std::cout << "Invalid speed. Enter positive number: ";
                    clearInputStream();
                }
                clearInputStream();

                navSys.addRoad(u, v, dist, speed, roadName, true);
                std::cout << "\n[Success] Road '" << roadName << "' added between "
                          << navSys.getLandmarkName(u) << " and " << navSys.getLandmarkName(v) << "!\n";
                break;
            }

            default:
                std::cout << "\n[Error] Choice out of range. Please enter 1-8.\n";
                break;
        }
    }

    return 0;
}
