import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# Define NumberedCanvas for Page X of Y and Running Header/Footer
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return  # Skip cover page

        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#475569"))

        # Running Header
        self.drawString(54, 750, "School of Computer Science and Engineering | LPU")
        self.drawRightString(612 - 54, 750, "CSE433 - Summer Internship Project Report")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 742, 612 - 54, 742)

        # Running Footer
        self.line(54, 45, 612 - 54, 45)
        self.drawString(54, 32, "NaviPath – Terminal-Based Shortest Path & Navigation System")
        self.drawRightString(612 - 54, 32, f"Page {self._pageNumber} of {page_count}")

        self.restoreState()


def build_pdf():
    pdf_filename = "Shaurya_Sharma_12412213_Project_Report.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom Color Palette
    PRIMARY = colors.HexColor("#1E293B")   # Slate Dark
    ACCENT = colors.HexColor("#E8631A")    # LPU Orange
    NAVY = colors.HexColor("#1E40AF")      # Deep Navy Blue
    TEXT_DARK = colors.HexColor("#0F172A") # Near Black
    BG_LIGHT = colors.HexColor("#F8FAFC")  # Off-white

    # Custom Typography Styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        alignment=1, # Center
        textColor=PRIMARY
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        alignment=1,
        textColor=ACCENT
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        spaceBefore=14,
        spaceAfter=8,
        textColor=PRIMARY,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        spaceBefore=10,
        spaceAfter=6,
        textColor=NAVY,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        spaceBefore=4,
        spaceAfter=4,
        textColor=TEXT_DARK,
        alignment=4 # Justified
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=15,
        spaceBefore=2,
        spaceAfter=2
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#0F172A"),
        backColor=colors.HexColor("#F1F5F9"),
        borderColor=colors.HexColor("#CBD5E1"),
        borderWidth=0.5,
        borderPadding=6,
        spaceBefore=6,
        spaceAfter=6
    )

    story = []

    # =========================================================================
    # PAGE 1: COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 10))
    if os.path.exists("report_assets/lpu_logo.png"):
        story.append(Image("report_assets/lpu_logo.png", width=340, height=110))
    story.append(Spacer(1, 20))

    story.append(Paragraph("School of Computer Science and Engineering", ParagraphStyle('SubHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=13, alignment=1, textColor=PRIMARY)))
    story.append(Spacer(1, 25))

    story.append(Paragraph("SUMMER TRAINING/INTERNSHIP<br/>PROJECT REPORT", ParagraphStyle('ReportType', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=16, leading=20, alignment=1, textColor=PRIMARY)))
    story.append(Spacer(1, 6))
    story.append(Paragraph("(Term June-July 2026)", ParagraphStyle('Term', parent=styles['Normal'], fontName='Helvetica', fontSize=11, alignment=1, textColor=colors.HexColor("#475569"))))
    story.append(Spacer(1, 30))

    # Project Title
    story.append(Paragraph("NaviPath – Terminal-Based Shortest Path & City Navigation System", title_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Graph Algorithms and Shortest Path Optimization in C++17", subtitle_style))
    story.append(Spacer(1, 40))

    # Submission Table
    table_data = [
        [Paragraph("<b>NAME</b>", ParagraphStyle('THead', fontName='Helvetica-Bold', fontSize=10, textColor=PRIMARY)),
         Paragraph("<b>REGISTRATION NUMBER</b>", ParagraphStyle('THead', fontName='Helvetica-Bold', fontSize=10, textColor=PRIMARY))],
        [Paragraph("Shaurya Sharma", ParagraphStyle('TCell', fontName='Helvetica', fontSize=10, textColor=TEXT_DARK)),
         Paragraph("12412213", ParagraphStyle('TCell', fontName='Helvetica', fontSize=10, textColor=TEXT_DARK))]
    ]
    sub_table = Table(table_data, colWidths=[200, 200], hAlign='CENTER')
    sub_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.HexColor("#F1F5F9")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#1E293B")),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(sub_table)
    story.append(Spacer(1, 35))

    story.append(Paragraph("<b>Course Code : CSE433</b>", ParagraphStyle('Course', fontName='Helvetica-Bold', fontSize=11, alignment=1, textColor=PRIMARY)))
    story.append(Spacer(1, 15))

    story.append(Paragraph("<u>Under the Guidance of</u>", ParagraphStyle('GuidanceTitle', fontName='Helvetica', fontSize=10, alignment=1, textColor=colors.HexColor("#334155"))))
    story.append(Spacer(1, 4))
    story.append(Paragraph("– <b>CipherSchools</b>", ParagraphStyle('Guidance', fontName='Helvetica-Bold', fontSize=11, alignment=1, textColor=ACCENT)))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: CERTIFICATE OF COMPLETION
    # =========================================================================
    story.append(Paragraph("CERTIFICATE OF COMPLETION", h1_style))
    story.append(Paragraph("Awarded by the Centre for Professional Enhancement, CipherSchools.", body_style))
    story.append(Spacer(1, 10))

    if os.path.exists("report_assets/certificate.png"):
        story.append(Image("report_assets/certificate.png", width=460, height=310))
    story.append(Spacer(1, 15))

    cert_text = (
        "This certificate, issued upon successful completion of the Summer Training program, "
        "reflects the strong technical foundation that underpins the project presented in this "
        "report — from object-oriented system design and algorithm implementation to "
        "terminal UI development, graph data structures, and Dijkstra's shortest path algorithm in C++17."
    )
    story.append(Paragraph(cert_text, body_style))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: DECLARATION
    # =========================================================================
    story.append(Paragraph("DECLARATION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=15))

    dec_p1 = (
        "I, <b>Shaurya Sharma</b> (Reg. No. <b>12412213</b>), hereby declare that the Summer "
        "Training/Internship Project Report entitled <b>\"NaviPath – Terminal-Based Shortest Path & "
        "City Navigation System\"</b> submitted to the School of Computer Science and "
        "Engineering, Lovely Professional University, is a record of original work carried out "
        "by me during the period June–July 2026."
    )
    story.append(Paragraph(dec_p1, body_style))
    story.append(Spacer(1, 12))

    dec_p2 = (
        "I further declare that this report, or any part thereof, has not been submitted to any "
        "other University or Institute for the award of any degree, diploma, or similar title, and "
        "that all sources of information used have been duly acknowledged."
    )
    story.append(Paragraph(dec_p2, body_style))
    story.append(Spacer(1, 40))

    story.append(Paragraph("<b>Shaurya Sharma (Reg. No. 12412213)</b>", ParagraphStyle('Sign', fontName='Helvetica-Bold', fontSize=10, textColor=PRIMARY)))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Date: July 2026", ParagraphStyle('DateStr', fontName='Helvetica', fontSize=10, textColor=colors.HexColor("#475569"))))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: ACKNOWLEDGEMENT
    # =========================================================================
    story.append(Paragraph("ACKNOWLEDGEMENT", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=15))

    ack_p1 = (
        "I would like to express my sincere gratitude to my project guide and the faculty "
        "members of the School of Computer Science and Engineering for their invaluable "
        "guidance, constant supervision, and continuous support throughout the duration of our "
        "summer internship. Their encouragement and insightful feedback have been "
        "instrumental in the successful completion of our project titled <b>\"NaviPath – "
        "Terminal-Based Shortest Path & City Navigation System.\"</b>"
    )
    story.append(Paragraph(ack_p1, body_style))
    story.append(Spacer(1, 12))

    ack_p2 = (
        "I am especially thankful for the resources, constructive suggestions, and the structured "
        "training in Data Structures and Algorithms provided by <b>CipherSchools</b> (13th June – "
        "24th July 2026) that enabled us to strengthen our programming foundation and apply it "
        "directly to this project."
    )
    story.append(Paragraph(ack_p2, body_style))
    story.append(Spacer(1, 12))

    ack_p3 = (
        "I also extend my heartfelt thanks to Lovely Professional University and the "
        "Department of Computer Science and Engineering for providing the opportunity to "
        "undertake this internship project and for fostering an environment that encourages "
        "learning and innovation."
    )
    story.append(Paragraph(ack_p3, body_style))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: TABLE OF CONTENTS
    # =========================================================================
    story.append(Paragraph("TABLE OF CONTENTS", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=15))

    toc_items = [
        ("Declaration", "3"),
        ("Certificate", "2"),
        ("Acknowledgement", "4"),
        ("Chapter 1: Introduction of Organization", "6"),
        ("  1.1 About CipherSchools", "6"),
        ("  1.2 Overview of Training Domain", "6"),
        ("  1.3 Objective of the Project", "6"),
        ("Chapter 2: Summer Training / Internship Content Detail", "7"),
        ("  2.1 Tools & Technologies Used", "7"),
        ("  2.2 Areas Covered During Training", "7"),
        ("  2.3 Summary of Work", "7"),
        ("Chapter 3: Summer Training / Internship Project Detail", "8"),
        ("  3.1 Problem Statement", "8"),
        ("  3.2 Scope and Objectives", "8"),
        ("  3.3 System Architecture and Layer Breakdown", "8"),
        ("  3.4 Methodology / Design", "9"),
        ("  3.5 Project Outcomes", "9"),
        ("  3.6 Technologies Used", "9"),
        ("Chapter 4: Source Code and System Snapshots", "10"),
        ("  4.1 Graph & Dijkstra Algorithm Code", "10"),
        ("  4.2 NavigationSystem – Core Routing Engine", "10"),
        ("  4.3 Model Layer – Key Class Structures", "11"),
        ("  4.4 System Architecture & Terminal Snapshots", "11"),
        ("Chapter 5: Bibliography & Project Links", "12")
    ]

    for title, pg in toc_items:
        is_chap = title.startswith("Chapter") or title in ["Declaration", "Certificate", "Acknowledgement"]
        font = 'Helvetica-Bold' if is_chap else 'Helvetica'
        size = 10 if is_chap else 9
        col = PRIMARY if is_chap else colors.HexColor("#334155")
        
        dots = ". " * int((400 - len(title)*6) / 10)
        p_text = f"<b>{title}</b>" if is_chap else title
        
        story.append(Paragraph(f"<font color='{col.hexval()}'>{p_text}</font> <font color='#CBD5E1'>{dots}</font> <b>{pg}</b>",
                               ParagraphStyle('TOCItem', fontName=font, fontSize=size, leading=14, spaceBefore=3)))

    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 1: INTRODUCTION OF ORGANIZATION
    # =========================================================================
    story.append(Paragraph("CHAPTER 1: INTRODUCTION OF ORGANIZATION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))

    story.append(Paragraph("1.1 About CipherSchools", h2_style))
    c1_1 = (
        "The online summer internship was an intensive training experience focused on Data "
        "Structures and Algorithms (DSA), organized by <b>CipherSchools</b> from 13th June till "
        "24th July 2026. The program combined structured learning with continuous practical "
        "problem-solving, helping us strengthen our programming foundation and analytical thinking.<br/><br/>"
        "This project was carried out as part of the Summer Internship Course conducted from June to July 2026. "
        "The internship simulated a real-world software engineering scenario, treating city transportation "
        "and route optimization as the target industry. The objective was to apply theoretical concepts of "
        "Data Structures, Graph Theory, Greedy & Priority-Queue Algorithms, Object-Oriented Programming, and "
        "Modular Architecture learned throughout the curriculum to a comprehensive terminal-based navigation system."
    )
    story.append(Paragraph(c1_1, body_style))

    story.append(Paragraph("1.2 Overview of Training Domain", h2_style))
    c1_2 = (
        "The online summer internship provided an intensive hands-on experience in Data Structures and "
        "Algorithms (DSA). Throughout the internship, we followed a consistent routine of solving approximately "
        "five LeetCode problems daily, supported by regular homework and practice exercises. This helped us "
        "improve our ability to analyze complex computational problems, identify suitable algorithmic approaches, "
        "write efficient code, and debug systematically.<br/><br/>"
        "The internship emphasized the practical value of DSA in developing logical thinking and algorithmic efficiency. "
        "Working with different data structures (Graphs, Priority Queues, Adjacency Lists, Hash Maps) and optimization "
        "techniques strengthened our understanding of how to manage data effectively, optimize graph traversals, and "
        "approach computational pathfinding with optimal time and space complexity."
    )
    story.append(Paragraph(c1_2, body_style))

    story.append(Paragraph("1.3 Objective of the Project", h2_style))
    story.append(Paragraph("The primary objective was to develop a comprehensive, terminal-based navigation and route optimization system in C++17 demonstrating real-world software engineering principles. This involved:", body_style))
    story.append(Paragraph("• Designing a 4-layer modular architecture separating presentation, control, business logic (DSA engine), and data models.", bullet_style))
    story.append(Paragraph("• Implementing an Adjacency List graph representation for city locations, distance weights, and road speed limits.", bullet_style))
    story.append(Paragraph("• Implementing Dijkstra's Shortest Path Algorithm with a Min-Priority Queue for fast $\\mathcal{O}((V+E)\\log V)$ performance.", bullet_style))
    story.append(Paragraph("• Supporting dual optimization criteria: Shortest Physical Distance (km) and Fastest Travel Time (minutes).", bullet_style))
    story.append(Paragraph("• Providing detailed step-by-step turn-by-turn guidance and visual ASCII map schematics.", bullet_style))

    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 2: SUMMER TRAINING / INTERNSHIP CONTENT DETAIL
    # =========================================================================
    story.append(Paragraph("CHAPTER 2: SUMMER TRAINING / INTERNSHIP CONTENT DETAIL", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))

    story.append(Paragraph("2.1 Tools & Technologies Used", h2_style))
    story.append(Paragraph("• <b>Programming Language:</b> C++17 (Standard Template Library, `<queue>`, `<unordered_map>`, `<vector>`)", bullet_style))
    story.append(Paragraph("• <b>Build Systems:</b> CMake & GNU Make", bullet_style))
    story.append(Paragraph("• <b>Development Environment:</b> VS Code, GCC / MSVC Compiler", bullet_style))
    story.append(Paragraph("• <b>Version Control:</b> Git & GitHub", bullet_style))
    story.append(Paragraph("• <b>Terminal Interface:</b> ANSI Escape Codes, Clean CLI Box Drawing", bullet_style))

    story.append(Paragraph("2.2 Areas Covered During Training", h2_style))
    story.append(Paragraph("• <b>Data Structures & Algorithms:</b> Daily LeetCode practice (~5 problems/day across Graph Theory, Dynamic Programming, Trees, Priority Queues).", bullet_style))
    story.append(Paragraph("• <b>Object-Oriented Programming:</b> Encapsulation, abstraction, separation of concerns, modular header/source design.", bullet_style))
    story.append(Paragraph("• <b>Graph Theory & Pathfinding:</b> Adjacency lists, edge weighting, Dijkstra's algorithm, priority queues, path backtracking.", bullet_style))
    story.append(Paragraph("• <b>Software Architecture Design:</b> Clean multi-layer design isolating presentation, application logic, and core algorithms.", bullet_style))

    story.append(Paragraph("2.3 Summary of Work", h2_style))
    c2_3 = (
        "The project followed a structured, modular development workflow. It commenced with architectural planning — "
        "defining the multi-layer design (Presentation, Controller, Core Graph Logic, Data Models) — followed by model design "
        "for core navigation entities (Landmark, Edge, Graph, DijkstraResult).<br/><br/>"
        "The core algorithmic layer was implemented in `Graph.cpp`, featuring Dijkstra's algorithm accelerated by a Min-Heap "
        "Priority Queue (`std::priority_queue`). Predecessor tracking was built to reconstruct the exact path back to the origin.<br/><br/>"
        "<b>Key Outcomes:</b><br/>"
        "• Improved consistency in solving complex algorithmic & graph problems.<br/>"
        "• Strengthened understanding of graph data structures and priority queues.<br/>"
        "• Applied learning in a clean C++17 codebase pushed to GitHub with clean build automation."
    )
    story.append(Paragraph(c2_3, body_style))

    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 3: SUMMER TRAINING / INTERNSHIP PROJECT DETAIL
    # =========================================================================
    story.append(Paragraph("CHAPTER 3: SUMMER TRAINING / INTERNSHIP PROJECT DETAIL", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))

    story.append(Paragraph("3.1 Problem Statement", h2_style))
    c3_1 = (
        "NaviPath is a terminal-based shortest path and city navigation system developed in C++17. "
        "Modern navigation applications require fast, accurate route calculations under different constraints "
        "(such as distance minimization vs travel time optimization considering speed limits). Rather than being designed "
        "as a simplistic menu-driven program, NaviPath is structured as a modular application with clean graph representation, "
        "Dijkstra algorithm optimization, predecessor path tracking, and interactive CLI rendering."
    )
    story.append(Paragraph(c3_1, body_style))

    story.append(Paragraph("3.2 Scope and Objectives", h2_style))
    story.append(Paragraph("<b>Scope:</b> Full simulation of a city navigation system including landmark mapping, road adjacency view, turn-by-turn route guidance, ASCII map schematic, and dynamic addition of custom locations and road connections.", body_style))
    story.append(Paragraph("<b>Objectives:</b>", body_style))
    story.append(Paragraph("• Design and implement an Adjacency List graph structure with dual edge metrics (distance & speed limit).", bullet_style))
    story.append(Paragraph("• Implement Dijkstra's algorithm with Min-Priority Queue achieving $\\mathcal{O}((V+E)\\log V)$ time complexity.", bullet_style))
    story.append(Paragraph("• Support dual optimization modes (Shortest Distance in km and Fastest Travel Time in minutes).", bullet_style))
    story.append(Paragraph("• Provide turn-by-turn navigation output detailing individual segment distances, speed limits, and time estimates.", bullet_style))

    story.append(Paragraph("3.3 System Architecture and Layer Breakdown", h2_style))
    story.append(Paragraph("The overall application architecture follows a 4-layer design:", body_style))
    story.append(Spacer(1, 4))

    arch_table_data = [
        [Paragraph("<b>Layer</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=9, textColor=PRIMARY)),
         Paragraph("<b>Components</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=9, textColor=PRIMARY)),
         Paragraph("<b>Responsibility</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=9, textColor=PRIMARY))],
        [Paragraph("Presentation", body_style), Paragraph("TerminalUI, MenuHandler, ASCII Map Render", body_style), Paragraph("CLI menu rendering, input parsing, turn-by-turn route display", body_style)],
        [Paragraph("Controller", body_style), Paragraph("NavigationSystem Controller", body_style), Paragraph("Coordinates user requests, invokes graph queries, formats output", body_style)],
        [Paragraph("Business Logic / DSA", body_style), Paragraph("Graph Engine, Dijkstra Algorithm, Priority Queue", body_style), Paragraph("Shortest path traversal, cost relaxation, predecessor tracking", body_style)],
        [Paragraph("Model", body_style), Paragraph("Landmark, Edge, DijkstraResult", body_style), Paragraph("Data entities representing vertices, weighted edges, and search results", body_style)]
    ]
    arch_table = Table(arch_table_data, colWidths=[100, 160, 240])
    arch_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F1F5F9")),
        ('BORDER', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(arch_table)
    story.append(Spacer(1, 10))

    if os.path.exists("report_assets/architecture_diagram.png"):
        story.append(Image("report_assets/architecture_diagram.png", width=480, height=220))

    story.append(PageBreak())

    story.append(Paragraph("3.4 Methodology / Design (Personal Contribution)", h2_style))
    c3_4 = (
        "As the primary developer of this project, my main focus was on designing the <b>Graph Data Structure</b> "
        "and implementing the <b>Dijkstra Algorithmic Core</b>.<br/><br/>"
        "<b>Dijkstra's Algorithm Implementation:</b><br/>"
        "The graph is represented using an adjacency list `std::vector<std::vector<Edge>>`. Dijkstra's algorithm uses "
        "a min-priority queue `std::priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>>` "
        "to continuously extract the node with the minimum distance or travel time.<br/><br/>"
        "During relaxation, if `costs[u] + edgeWeight < costs[v]`, the distance/time array is updated, and the predecessor "
        "`predecessors[v] = u` is recorded. Upon reaching the destination, the route is reconstructed by stepping backward "
        "from the destination to the source, then reversing the sequence."
    )
    story.append(Paragraph(c3_4, body_style))

    story.append(Paragraph("3.5 Project Outcomes", h2_style))
    story.append(Paragraph("Key Technical Outcomes:", body_style))
    story.append(Paragraph("• Complete navigation workflow supporting both shortest distance and fastest travel time queries.", bullet_style))
    story.append(Paragraph("• High algorithmic performance: $\\mathcal{O}((V+E)\\log V)$ query execution time.", bullet_style))
    story.append(Paragraph("• Interactive turn-by-turn directions detailing road names, speed limits, and segment travel times.", bullet_style))
    story.append(Paragraph("• Cross-platform compilation using standard C++17 tools (GCC, Clang, MSVC, CMake).", bullet_style))

    story.append(Paragraph("3.6 Technologies Used", h2_style))
    tech_table_data = [
        [Paragraph("<b>Layer</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=9, textColor=PRIMARY)),
         Paragraph("<b>Technology</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=9, textColor=PRIMARY))],
        [Paragraph("Programming Language", body_style), Paragraph("C++17", body_style)],
        [Paragraph("Build Systems", body_style), Paragraph("CMake, GNU Make", body_style)],
        [Paragraph("Core Data Structures", body_style), Paragraph("Graph Adjacency List, Min-Priority Queue, Hash Map", body_style)],
        [Paragraph("Terminal UI", body_style), Paragraph("ANSI Escape Codes, Clean Box Drawing", body_style)],
        [Paragraph("Version Control", body_style), Paragraph("Git & GitHub", body_style)]
    ]
    tech_table = Table(tech_table_data, colWidths=[200, 300])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F1F5F9")),
        ('BORDER', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(tech_table)

    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 4: SOURCE CODE AND SYSTEM SNAPSHOTS
    # =========================================================================
    story.append(Paragraph("CHAPTER 4: SOURCE CODE AND SYSTEM SNAPSHOTS", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))

    story.append(Paragraph("4.1 Graph & Dijkstra Algorithm Code", h2_style))
    story.append(Paragraph("File: <code>src/Graph.cpp</code> (Core Dijkstra Implementation)", ParagraphStyle('SubF', fontName='Helvetica-Oblique', fontSize=8.5, textColor=colors.HexColor("#475569"))))

    code_dijkstra = """
DijkstraResult Graph::runDijkstra(int startNode, bool optimizeForTime) const {
    DijkstraResult result;
    const double INF = std::numeric_limits<double>::infinity();
    result.costs.assign(numVertices, INF);
    result.distances.assign(numVertices, INF);
    result.travelTimes.assign(numVertices, INF);
    result.predecessors.assign(numVertices, -1);

    using QueueElement = std::pair<double, int>;
    std::priority_queue<QueueElement, std::vector<QueueElement>, std::greater<QueueElement>> pq;

    result.costs[startNode] = 0.0;
    pq.push({0.0, startNode});

    while (!pq.empty()) {
        auto topPair = pq.top();
        double currentCost = topPair.first;
        int u = topPair.second;
        pq.pop();

        if (currentCost > result.costs[u]) continue;

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
"""
    story.append(Paragraph(code_dijkstra.strip().replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))

    story.append(Paragraph("4.2 NavigationSystem – Turn-by-Turn Route Guidance Code", h2_style))
    story.append(Paragraph("File: <code>src/NavigationSystem.cpp</code>", ParagraphStyle('SubF2', fontName='Helvetica-Oblique', fontSize=8.5, textColor=colors.HexColor("#475569"))))

    code_nav = """
void NavigationSystem::findAndPrintShortestRoute(const std::string& srcName, 
                                                 const std::string& destName, 
                                                 bool optimizeForTime) const {
    int srcId = getLandmarkId(srcName);
    int destId = getLandmarkId(destName);

    DijkstraResult result = graph.runDijkstra(srcId, optimizeForTime);
    std::vector<int> path = graph.reconstructPath(srcId, destId, result.predecessors);

    std::cout << "\\n=========================================================\\n";
    std::cout << "                  OPTIMAL NAVIGATION ROUTE FOUND         \\n";
    std::cout << "=========================================================\\n";
    for (size_t i = 0; i < path.size(); ++i) {
        std::cout << " Step " << (i + 1) << ": [" << path[i] << "] " << getLandmarkName(path[i]);
        if (i < path.size() - 1) {
            std::cout << "\\n         |--> Drive along road segment\\n";
        }
    }
    std::cout << " Total Distance   : " << result.distances[destId] << " km\\n";
    std::cout << " Est. Travel Time : " << result.travelTimes[destId] << " mins\\n";
}
"""
    story.append(Paragraph(code_nav.strip().replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))

    story.append(PageBreak())

    story.append(Paragraph("4.3 Model Layer – Key Class Structures", h2_style))
    if os.path.exists("report_assets/class_diagram.png"):
        story.append(Image("report_assets/class_diagram.png", width=480, height=250))
    story.append(Spacer(1, 10))

    story.append(Paragraph("4.4 System Snapshots & Execution Output", h2_style))
    if os.path.exists("report_assets/snapshot_route.png"):
        story.append(Image("report_assets/snapshot_route.png", width=480, height=230))

    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 5: BIBLIOGRAPHY & PROJECT LINKS
    # =========================================================================
    story.append(Paragraph("CHAPTER 5: BIBLIOGRAPHY & PROJECT LINKS", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=15))

    bibs = [
        "ISO C++17 Standard (ISO/IEC 14882:2017). https://isocpp.org/std/the-standard",
        "Dijkstra, E. W. (1959). \"A note on two problems in connexion with graphs\". Numerische Mathematik. 1: 269–271.",
        "CMake Documentation & Build Automation. https://cmake.org/documentation/",
        "CipherSchools – Data Structures and Algorithms Training. https://cipherschools.com",
        "LeetCode – Algorithmic Practice Platform. https://leetcode.com"
    ]
    for b in bibs:
        story.append(Paragraph(f"• {b}", bullet_style))

    story.append(Spacer(1, 20))
    story.append(Paragraph("Project Links", h2_style))
    story.append(Paragraph("The complete source code, documentation, build scripts, and tests for this project are publicly available at the link below:", body_style))
    story.append(Spacer(1, 8))

    link_text = (
        "<b>GitHub Repository:</b><br/>"
        "<font color='#1E40AF'><u>https://github.com/Shauryasharma0003/DSA_SHORTEST_PATH_NAVIGATION_SYSTEM_SHAURYA_SHARMA.git</u></font>"
    )
    story.append(Paragraph(link_text, ParagraphStyle('LinkBox', parent=body_style, backColor=colors.HexColor("#F1F5F9"), borderColor=colors.HexColor("#CBD5E1"), borderWidth=1, borderPadding=10)))

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Report generated successfully: {pdf_filename}")

if __name__ == "__main__":
    build_pdf()
