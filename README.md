---

# PropMatch: Property Search Portal

## Overview

**PropMatch** is a SaaS-based Property Portal Software System designed to simplify real estate search and management.  
The system allows users to enter natural language queries (e.g., *"Find me a 2-bedroom apartment in San Francisco"*) and returns a list of matching properties.  
Built using a **Layered Architecture**, PropMatch ensures clean separation of concerns across UI, Business Logic, and Data Services layers.

The project leverages:
- **Natural Language Processing (NLP)** for user queries
- **MongoDB** for semi-structured property and user data storage
- **Flask (Python)** for backend development
- **Simple UI** (Command Line) and **Complex UI** (Web-based)

---

## Features

- 🔍 **Natural Language Query Parsing**: Users can search properties conversationally.
- 🏠 **Property Storage**: Staff users can upload property files with metadata (address, city, owner details, amenities, etc.).
- 🔒 **Authentication System**: User-specific session management for customers and staff.
- 📈 **Layered Architecture**: UI Layer, Core Business Layer, Technical Services Layer.
- 📂 **MongoDB Integration**: Efficient storage and retrieval of semi-structured property data.
- 🖥️ **Deployable**: Can run on local systems, WSL, or Virtual Machines (VMs).

---

## Project Architecture

```
User Interface Layer (Simple UI / Complex UI)
            ↓
Core Business Logic Layer (SessionHandler, PropertyHandler, NLPHandler)
            ↓
Technical Services Layer (Database Services, File Management, Logging)
```

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/PropMatch.git
   cd PropMatch
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install MongoDB**
   Ensure MongoDB is installed and running on your system.

4. **Setup NLTK Resources**
   ```bash
   python3 download.py
   ```

5. **Run the Application**
   - **Simple UI**:
     ```bash
     python simple_ui.py
     ```
   - **Complex UI (Web Interface)**:
     ```bash
     python complex_ui.py
     ```
   Then open your browser and navigate to `http://localhost:5000/`

---

## Technologies Used

- **Backend**: Python (Flask)
- **Database**: MongoDB
- **NLP Tools**: NLTK (WordNet, POS Tagging, Lemmatization)
- **Deployment Environments**: WSL / VM / Local Machine

---

## User Roles

- **Staff**
  - Upload property listings
  - Manage metadata (owner name, amenities, address, etc.)
- **Customer**
  - Search for properties using natural language queries

---

## Screenshots

*(Add screenshots of your Simple UI, Complex UI login page, dashboard, property search results, etc. if available.)*

---

## Known Limitations

- Containerization (Docker) not implemented in the current version.
- The UI is kept simple for demonstration purposes.
- Designed for single-tenant architecture only (one client per instance).

---

## Future Enhancements

- Add containerization (Docker Compose) for production deployment.
- Extend NLP query capabilities using Deep Learning models.
- Introduce multi-tenant SaaS architecture.
- Add payment and booking modules.

---

## Authors

- **Anirudh Venkatesh**

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# 🚀 Get Started Now!

Find your dream property in seconds with PropMatch!
```

---