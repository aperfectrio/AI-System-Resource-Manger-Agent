# AI System Resource Manager Agent

A system monitoring and optimization application developed as part of an Operating Systems project.

The project monitors CPU, RAM, and Disk usage, analyzes running processes, evaluates system health, generates recommendations, and provides safe optimization actions through a web-based dashboard.

The application was developed using Python, Flask, and psutil.

---

# Project Overview

The system follows the basic structure of an intelligent agent:

```text
Observe → Analyze → Decide → Act
```

### Observe

Collects real-time system information:

- CPU Usage
- RAM Usage
- Disk Usage

### Analyze

Identifies:

- Top RAM-consuming processes
- Top CPU-consuming processes
- Potential optimization candidates

### Decide

Evaluates the current system state and generates recommendations based on predefined rules.

### Act

Allows the user to execute safe optimization actions through the dashboard.

---

# Features

- Real-time CPU monitoring
- Real-time RAM monitoring
- Real-time Disk monitoring
- Top CPU process analysis
- Top RAM process analysis
- System health evaluation
- Rule-based recommendation engine
- Safe optimization candidate detection
- Process termination actions
- Activity logging
- Web-based monitoring dashboard
- Responsive user interface

---

# Optimization Mechanism

The system includes an optimization module that can take corrective actions when the user decides to optimize the system.

The optimization process follows these steps:

1. Analyze currently running processes.
2. Compare processes against a predefined safe-process list.
3. Identify the highest resource-consuming processes among the safe candidates.
4. Display these processes in the **Optimization Candidates** section.
5. When the user clicks the **Optimize System** button, the system:
   - Selects the top resource-consuming candidate processes.
   - Terminates the selected processes.
   - Records the action in the activity log.

Example:

```text
Optimization Candidates

Spotify.exe            245 MB
Discord.exe            180 MB
WindowsCamera.exe      120 MB
```

After clicking **Optimize System**, the agent will terminate the listed candidate processes and write the action to `logs/history.log`.

Only processes included in the predefined safe-process list are eligible for automatic termination. Critical operating system processes are excluded to prevent system instability.

---

# Development History

The project was developed in three stages.

## Stage 1 — Terminal Application

File:

```text
main.py
```

Implemented:

- CPU monitoring
- RAM monitoring
- Disk monitoring
- Process analysis
- Recommendation generation

through a terminal interface.

---

## Stage 2 — Desktop GUI

File:

```text
dashboard.py
```

Implemented:

- CustomTkinter interface
- Live monitoring dashboard
- Process visualization

through a desktop application.

---

## Stage 3 — Web Dashboard (Final Version)

File:

```text
app.py
```

Implemented:

- Flask web application
- Modern monitoring dashboard
- Decision engine visualization
- Optimization candidates section
- Activity log viewer
- Process optimization actions

**Final Version:** `app.py`

---

# Screenshots

## Main Dashboard

![Dashboard](screenshots/dashboard.png)

## Resource Monitoring

![Monitoring](screenshots/monitoring.png)

## Optimization Interface

![Optimization](screenshots/optimization.png)

---

# Technologies Used

- Python
- Flask
- psutil
- HTML
- CSS
- Bootstrap
- CustomTkinter

---

# Project Structure

```text
AI-System-Resource-Manager-Agent
│
├── modules/
│   ├── monitor.py
│   ├── analyzer.py
│   ├── decision_engine.py
│   ├── actions.py
│   ├── notifier.py
│   └── logger.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── screenshots/
│   ├── dashboard.png
│   ├── monitoring.png
│   └── optimization.png
│
├── logs/
│   └── .gitkeep
│
├── app.py
├── dashboard.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/aperfectrio/AI-System-Resource-Manager-Agent.git
```

Move into the project directory:

```bash
cd AI-System-Resource-Manager-Agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run the Flask application:

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

---

# Future Improvements

Potential future enhancements include:

- Automatic dashboard refresh using AJAX/WebSockets
- Machine learning-based resource prediction
- User-configurable optimization policies
- Process whitelist and blacklist management
- Email or desktop notifications
- Historical resource usage graphs
- Multi-system monitoring support

---

# Author

Ahammed Tanim

Computer Science Undergraduate Student

Sejong University

---

