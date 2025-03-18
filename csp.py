import tkinter as tk
from tkinter import ttk, messagebox
import csv
import random
import os

# Define Events and Categories
technical_events = [
    "Break the Query", "Dabang C", "Data Visualization", "Treasure Hunt", "Free Fire Event"
]
cultural_events = [
    "Dances", "Fashion Show", "Singing Competition", "Drama", 
    "Poetry Recitation", "Stand-up Comedy", "Instrumental Music Performance"
]
all_events = technical_events + cultural_events

dates = ["22 March", "23 March", "24 March"]
time_slots = ["11 AM - 1 PM", "1 PM - 3 PM", "3 PM - 5 PM", "5 PM - 7 PM"]

# Ensure no overlapping technical events
event_schedule = {}
assigned_time_slots = {}

for event in technical_events:
    while True:
        date = random.choice(dates)
        time = random.choice(time_slots[:-1])
        if (date, time) not in assigned_time_slots:
            event_schedule[event] = (date, time)
            assigned_time_slots[(date, time)] = event
            break

for event in cultural_events:
    event_schedule[event] = (random.choice(dates), "5 PM - 7 PM")

# Save & Load Participants from CSV
csv_file = "participants.csv"

def load_participants():
    if os.path.exists(csv_file):
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return {rows[0]: rows[1:] for rows in reader}
    return {}

participants = load_participants()

def save_participant(name, events):
    participants[name] = events
    with open(csv_file, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for participant, event_list in participants.items():
            writer.writerow([participant] + event_list)

# GUI Application
def register_participant():
    name = name_entry.get().strip()
    event = event_combo.get()
    if not name or not event:
        messagebox.showwarning("Warning", "Please enter participant name and select an event")
        return
    if name in participants and event in participants[name]:
        messagebox.showwarning("Warning", "Participant already registered for this event")
        return
    participants.setdefault(name, []).append(event)
    save_participant(name, participants[name])
    messagebox.showinfo("Success", f"{name} registered for {event}")
    name_entry.delete(0, tk.END)

def show_schedule():
    for row in schedule_tree.get_children():
        schedule_tree.delete(row)
    for event, (date, time) in event_schedule.items():
        schedule_tree.insert("", tk.END, values=(event, date, time))

def show_participants():
    event = event_combo_view.get()
    if not event:
        messagebox.showwarning("Warning", "Please select an event")
        return
    for row in participants_tree.get_children():
        participants_tree.delete(row)
    for participant, events in participants.items():
        if event in events:
            participants_tree.insert("", tk.END, values=(participant, event))

# Main Window
root = tk.Tk()
root.title("Technotsav 2025 Scheduler")
root.geometry("1000x700")
root.configure(bg="#f0f8ff")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Schedule Tab
schedule_tab = tk.Frame(notebook, bg="#f0f8ff")
notebook.add(schedule_tab, text="Event Schedule")
schedule_tree = ttk.Treeview(schedule_tab, columns=("Event", "Date", "Time"), show="headings", height=15)
schedule_tree.heading("Event", text="Event")
schedule_tree.heading("Date", text="Date")
schedule_tree.heading("Time", text="Time")
schedule_tree.pack(pady=10, padx=20, expand=True)
ttk.Button(schedule_tab, text="Show Schedule", command=show_schedule).pack(pady=10)

# Registration Tab
registration_tab = tk.Frame(notebook, bg="#f0f8ff")
notebook.add(registration_tab, text="Register Participant")
tk.Label(registration_tab, text="Enter Participant Name:", font=("Arial", 14), bg="#f0f8ff").pack()
name_entry = ttk.Entry(registration_tab, font=("Arial", 14), width=40)
name_entry.pack(pady=5)
tk.Label(registration_tab, text="Select Event:", font=("Arial", 14), bg="#f0f8ff").pack()
event_combo = ttk.Combobox(registration_tab, values=all_events, font=("Arial", 14), width=40)
event_combo.pack(pady=5)
ttk.Button(registration_tab, text="Register", command=register_participant).pack(pady=10)

# View Participants Tab
participants_tab = tk.Frame(notebook, bg="#f0f8ff")
notebook.add(participants_tab, text="View Participants")
tk.Label(participants_tab, text="Select Event:", font=("Arial", 14), bg="#f0f8ff").pack()
event_combo_view = ttk.Combobox(participants_tab, values=all_events, font=("Arial", 14), width=40)
event_combo_view.pack(pady=5)
ttk.Button(participants_tab, text="Show Participants", command=show_participants).pack(pady=5)
participants_tree = ttk.Treeview(participants_tab, columns=("Participant", "Event"), show="headings", height=15)
participants_tree.heading("Participant", text="Participant")
participants_tree.heading("Event", text="Event")
participants_tree.pack(pady=10, padx=20, expand=True)

root.mainloop()
