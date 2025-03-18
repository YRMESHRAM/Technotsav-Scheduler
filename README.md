# Technotsav 2025 Scheduler

## Overview
Technotsav 2025 Scheduler is a GUI-based event management application built using Python's Tkinter. It allows users to:
- View the schedule of technical and cultural events.
- Register participants for specific events.
- View participants registered for each event.

## Features
- **Event Scheduling:** Ensures that technical events do not overlap and that cultural events occur in the evening slot.
- **Participant Registration:** Users can register participants for different events.
- **CSV-based Data Storage:** Participant registrations are saved in a CSV file for persistence.
- **User-friendly Interface:** Uses Tkinter's Notebook widget for easy navigation between different functionalities.

## Technologies Used
- **Python** (Tkinter for GUI, CSV for data storage, and Random for scheduling)
- **Tkinter** (GUI framework)
- **CSV** (File storage for participants' data)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YRMESHRAM/Technotsav-Scheduler.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Technotsav-Scheduler
   ```
3. **Run the application:**
   ```bash
   python technotsav_gui.py
   ```

## Usage
- **View Schedule:** Navigate to the "Event Schedule" tab and click "Show Schedule" to display the events.
- **Register Participant:** Go to the "Register Participant" tab, enter a participant's name, select an event, and click "Register."
- **View Participants:** In the "View Participants" tab, select an event and click "Show Participants" to see the list of registered participants.

## Contributing
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the MIT License.

