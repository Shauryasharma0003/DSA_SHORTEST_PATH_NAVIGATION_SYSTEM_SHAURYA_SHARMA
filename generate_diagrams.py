import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs("report_assets", exist_ok=True)

# 1. Create LPU Logo Graphic
def create_lpu_logo():
    fig, ax = plt.subplots(figsize=(6, 1.8), dpi=300)
    ax.axis('off')
    
    # Emblem circle
    circle = patches.Circle((0.15, 0.5), 0.35, linewidth=2.5, edgecolor='#E8631A', facecolor='none')
    ax.add_patch(circle)
    inner_circle = patches.Circle((0.15, 0.5), 0.30, linewidth=1, edgecolor='#1E293B', facecolor='none')
    ax.add_patch(inner_circle)
    
    # Sun rays
    for angle in np.linspace(-40, 40, 7):
        ax.plot([0.15, 0.15 + 0.25*np.cos(np.radians(angle))],
                [0.5, 0.5 + 0.25*np.sin(np.radians(angle))], color='#E8631A', lw=1.8)
                
    ax.text(0.15, 0.90, "LOVELY PROFESSIONAL UNIVERSITY", fontsize=5, fontweight='bold', ha='center', color='#1E293B')
    ax.text(0.15, 0.08, "PUNJAB (INDIA)", fontsize=4.5, fontweight='bold', ha='center', color='#E8631A')

    # Main LPU Text Boxes
    # L Box
    ax.add_patch(patches.Rectangle((0.42, 0.68), 0.09, 0.24, facecolor='#E8631A'))
    ax.text(0.465, 0.80, "L", color='white', fontsize=13, fontweight='bold', ha='center', va='center')
    ax.text(0.53, 0.80, "OVELY", color='#1E293B', fontsize=13, fontweight='bold', va='center')

    # P Box
    ax.add_patch(patches.Rectangle((0.42, 0.38), 0.09, 0.24, facecolor='#E8631A'))
    ax.text(0.465, 0.50, "P", color='white', fontsize=13, fontweight='bold', ha='center', va='center')
    ax.text(0.53, 0.50, "ROFESSIONAL", color='#1E293B', fontsize=13, fontweight='bold', va='center')

    # U Box
    ax.add_patch(patches.Rectangle((0.42, 0.08), 0.09, 0.24, facecolor='#E8631A'))
    ax.text(0.465, 0.20, "U", color='white', fontsize=13, fontweight='bold', ha='center', va='center')
    ax.text(0.53, 0.20, "NIVERSITY", color='#1E293B', fontsize=13, fontweight='bold', va='center')

    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.savefig("report_assets/lpu_logo.png", bbox_inches='tight', transparent=True, dpi=300)
    plt.close()

# 2. Create Certificate Graphic
def create_certificate():
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
    ax.axis('off')
    
    # Outer Border
    rect = patches.Rectangle((0.02, 0.02), 0.96, 0.96, linewidth=3, edgecolor='#B8860B', facecolor='#FFFEFA')
    ax.add_patch(rect)
    rect_inner = patches.Rectangle((0.04, 0.04), 0.92, 0.92, linewidth=1, edgecolor='#D4AF37', facecolor='none')
    ax.add_patch(rect_inner)
    
    # Header Logo & Title
    ax.text(0.5, 0.88, "Cipher", fontsize=16, fontweight='bold', ha='right', color='#000000')
    ax.text(0.5, 0.88, " Schools", fontsize=16, fontweight='bold', ha='left', color='#E8631A')
    
    ax.text(0.5, 0.76, "CERTIFICATE OF COMPLETION", fontsize=14, fontweight='bold', ha='center', color='#1E293B')
    ax.text(0.5, 0.68, "This is to certify that", fontsize=10, fontstyle='italic', ha='center', color='#475569')
    
    # Name
    ax.text(0.5, 0.58, "Shaurya Sharma", fontsize=18, fontweight='bold', fontstyle='italic', ha='center', color='#0F172A')
    ax.plot([0.3, 0.7], [0.55, 0.55], color='#B8860B', lw=1.5)
    
    ax.text(0.5, 0.48, "studying at Lovely Professional University (Reg No: 12412213)", fontsize=9, ha='center', color='#334155')
    ax.text(0.5, 0.42, "has successfully completed training in", fontsize=9, ha='center', color='#334155')
    
    # Subject
    ax.text(0.5, 0.33, "Data Structures and Algorithms", fontsize=13, fontweight='bold', ha='center', color='#0F172A')
    ax.text(0.5, 0.26, "organized by CipherSchools during the period of June-July 2026", fontsize=8.5, ha='center', color='#475569')
    
    # Signature & Footer
    ax.text(0.2, 0.14, "Scan to Verify", fontsize=7, ha='center', color='#64748B')
    qr_box = patches.Rectangle((0.16, 0.17), 0.08, 0.08, facecolor='#1E293B')
    ax.add_patch(qr_box)
    
    ax.text(0.8, 0.18, "Anurag Mishra", fontsize=10, fontweight='bold', fontstyle='italic', ha='center', color='#0F172A')
    ax.plot([0.7, 0.9], [0.16, 0.16], color='#94A3B8', lw=1)
    ax.text(0.8, 0.12, "ANURAG MISHRA\nFounder CipherSchools", fontsize=7, ha='center', color='#475569')
    ax.text(0.8, 0.07, "Certificate ID: CSW2026-12412213", fontsize=6.5, ha='center', color='#64748B')
    
    plt.tight_layout()
    plt.savefig("report_assets/certificate.png", bbox_inches='tight', dpi=300)
    plt.close()

# 3. Create System Architecture Diagram
def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
    ax.axis('off')
    
    layers = [
        ("Presentation Layer", ["TerminalUI", "ScreenManager", "MenuHandler", "ASCII Visualizer"], "#DBEAFE", "#1E40AF"),
        ("Controller Layer", ["NavigationSystem Controller", "Query Processor"], "#FEF3C7", "#92400E"),
        ("Business Logic & DSA Layer", ["Dijkstra Engine", "Min-Priority Queue", "Path Backtracker", "Cost Calculator"], "#DCFCE7", "#166534"),
        ("Data Model Layer", ["Graph (Adjacency List)", "Landmark Node", "Road Edge (Dist & Speed)"], "#F3E8FF", "#6B21A8")
    ]
    
    y_starts = [0.75, 0.52, 0.29, 0.06]
    
    for idx, (title, comps, bg_color, text_color) in enumerate(layers):
        y = y_starts[idx]
        rect = patches.FancyBboxPatch((0.05, y), 0.9, 0.17, boxstyle="round,pad=0.02",
                                      facecolor=bg_color, edgecolor=text_color, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(0.08, y + 0.11, title, fontsize=10, fontweight='bold', color=text_color, va='center')
        
        comp_str = "   |   ".join(comps)
        ax.text(0.08, y + 0.04, comp_str, fontsize=8, color='#334155', va='center')
        
        if idx < 3:
            ax.annotate('', xy=(0.5, y - 0.02), xytext=(0.5, y),
                        arrowprops=dict(arrowstyle="->", color="#64748B", lw=2))

    plt.tight_layout()
    plt.savefig("report_assets/architecture_diagram.png", bbox_inches='tight', dpi=300)
    plt.close()

# 4. Create Class Diagram
def create_class_diagram():
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
    ax.axis('off')

    boxes = [
        ("Graph", ["- numVertices: int", "- adjList: vector<vector<Edge>>"], ["+ addEdge()", "+ runDijkstra()", "+ reconstructPath()"], 0.05, 0.50, 0.40, 0.42),
        ("NavigationSystem", ["- graph: Graph", "- landmarks: vector<Landmark>", "- nameToIdMap: unordered_map"], ["+ loadDefaultCityMap()", "+ findAndPrintShortestRoute()", "+ displayAllLandmarks()"], 0.55, 0.50, 0.40, 0.42),
        ("Edge", ["+ destination: int", "+ distance: double", "+ speedLimit: double", "+ roadName: string"], ["+ getTravelTimeMinutes()"], 0.05, 0.05, 0.40, 0.35),
        ("Landmark", ["+ id: int", "+ name: string", "+ category: string"], [], 0.55, 0.05, 0.40, 0.35),
    ]

    for title, fields, methods, x, y, w, h in boxes:
        rect = patches.Rectangle((x, y), w, h, facecolor='#F8FAFC', edgecolor='#1E293B', lw=1.5)
        ax.add_patch(rect)
        title_rect = patches.Rectangle((x, y + h - 0.09), w, 0.09, facecolor='#334155')
        ax.add_patch(title_rect)
        ax.text(x + w/2, y + h - 0.045, title, color='white', fontweight='bold', fontsize=9, ha='center', va='center')
        
        content_y = y + h - 0.12
        for f in fields:
            ax.text(x + 0.02, content_y, f, fontsize=7, color='#0F172A', va='top')
            content_y -= 0.04
        if fields and methods:
            ax.plot([x, x + w], [content_y + 0.01, content_y + 0.01], color='#CBD5E1', lw=1)
            content_y -= 0.03
        for m in methods:
            ax.text(x + 0.02, content_y, m, fontsize=7, color='#0369A1', va='top')
            content_y -= 0.04

    ax.annotate('', xy=(0.45, 0.70), xytext=(0.55, 0.70), arrowprops=dict(arrowstyle="<|-", color="#475569", lw=1.5))
    ax.annotate('', xy=(0.25, 0.50), xytext=(0.25, 0.40), arrowprops=dict(arrowstyle="<|-", color="#475569", lw=1.5))
    ax.annotate('', xy=(0.75, 0.50), xytext=(0.75, 0.40), arrowprops=dict(arrowstyle="<|-", color="#475569", lw=1.5))

    plt.tight_layout()
    plt.savefig("report_assets/class_diagram.png", bbox_inches='tight', dpi=300)
    plt.close()

# 5. Create Terminal Snapshots
def create_terminal_snapshots():
    text1 = """
=========================================================================
         SHORTEST PATH NAVIGATION SYSTEM (DIJKSTRA'S ALGORITHM)          
                     Data Structures & Algorithms Project                
=========================================================================

------------------------------ MAIN MENU ------------------------------
 1. Display All City Locations / Landmarks
 2. View Complete Road Network (Adjacency List)
 3. View ASCII Map Schematic
 4. Find Shortest Route (Optimized for Distance in km)
 5. Find Fastest Route (Optimized for Travel Time in mins)
 6. Add Custom Location / Landmark
 7. Add Custom Road / Edge Connection
 8. Exit System
-------------------------------------------------------------------------
=======================================================
                 AVAILABLE CITY LOCATIONS              
=======================================================
ID    Location Name               Category            
-------------------------------------------------------
0     Central Station             Transit Hub         
1     Downtown Hub                Commercial Center   
2     City General Hospital       Healthcare          
3     Tech Park                   Business District   
4     State University            Education           
5     Metropolitan Airport        Airport             
6     Sunset Mall                 Shopping            
7     Grand Park                  Recreation          
8     Riverside District          Residential         
=======================================================
"""
    text2 = """
=========================================================================
                  OPTIMAL NAVIGATION ROUTE FOUND                         
=========================================================================
 Origin        : Central Station (ID: 0)
 Destination   : Metropolitan Airport (ID: 5)
 Optimization  : Fastest Travel Time
-------------------------------------------------------------------------
 TURN-BY-TURN NAVIGATION INSTRUCTIONS:
-------------------------------------------------------------------------
 Step 1: [0] Central Station
         |--> Drive along 'Main Street' (3.5 km @ 40.0 km/h ~ 5.2 mins)
 Step 2: [1] Downtown Hub
         |--> Drive along 'Tech Boulevard' (8.2 km @ 70.0 km/h ~ 7.0 mins)
 Step 3: [3] Tech Park
         |--> Drive along 'Airport Highway' (12.0 km @ 90.0 km/h ~ 8.0 mins)
 Step 4: [5] Metropolitan Airport  (ARRIVED!)
-------------------------------------------------------------------------
 SUMMARY:
 Total Distance      : 23.70 km
 Est. Travel Time    : 20.3 mins
 Number of Segments  : 3 road segments
=========================================================================
"""

    def render_term_img(text, filename):
        fig, ax = plt.subplots(figsize=(8, 4.2), dpi=300)
        ax.axis('off')
        rect = patches.Rectangle((0, 0), 1, 1, facecolor='#0F172A', edgecolor='#334155', lw=2)
        ax.add_patch(rect)
        bar = patches.Rectangle((0, 0.92), 1, 0.08, facecolor='#1E293B')
        ax.add_patch(bar)
        ax.add_patch(patches.Circle((0.03, 0.96), 0.012, facecolor='#EF4444'))
        ax.add_patch(patches.Circle((0.06, 0.96), 0.012, facecolor='#F59E0B'))
        ax.add_patch(patches.Circle((0.09, 0.96), 0.012, facecolor='#10B981'))
        ax.text(0.5, 0.96, "NaviPath Terminal - C++ Dijkstra Engine", color='#94A3B8', fontsize=8, ha='center', va='center')

        ax.text(0.03, 0.88, text.strip(), color='#38BDF8', fontfamily='monospace', fontsize=6, va='top')
        
        plt.tight_layout()
        plt.savefig(filename, bbox_inches='tight', dpi=300)
        plt.close()

    render_term_img(text1, "report_assets/snapshot_menu.png")
    render_term_img(text2, "report_assets/snapshot_route.png")

create_lpu_logo()
create_certificate()
create_architecture_diagram()
create_class_diagram()
create_terminal_snapshots()
print("All diagram assets regenerated!")
