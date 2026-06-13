# Support Worker Toolkit
# For NDIS / Disability Support Workers

import datetime

def main():
    print("\n=== Support Worker Toolkit ===")
    print("Welcome, Support Worker! Built for efficient, person-centred care.")
    while True:
        print("\nMenu:")
        print("1. Generate Shift Summary")
        print("2. Draft Incident Report")
        print("3. Daily Checklist")
        print("4. SCHADS Pay Estimator")
        print("5. Client Goal Tracker")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            generate_shift_summary()
        elif choice == '2':
            draft_incident_report()
        elif choice == '3':
            daily_checklist()
        elif choice == '4':
            pay_estimator()
        elif choice == '5':
            goal_tracker()
        elif choice == '6':
            print("Goodbye! Stay safe and keep empowering your clients.")
            break
        else:
            print("Invalid choice. Try again.")

def generate_shift_summary():
    print("\n--- Shift Summary Generator ---")
    date = input("Date (YYYY-MM-DD) or today: ") or str(datetime.date.today())
    client = input("Client name/initials: ")
    activities = input("Key activities/supports provided: ")
    observations = input("Observations/notes: ")
    print(f"\nShift Summary for {client} on {date}:")
    print(f"Activities: {activities}")
    print(f"Observations: {observations}")
    print("\nCopy this into Lumary or your documentation.")

def draft_incident_report():
    print("\n--- Incident Report Drafter ---")
    date = input("Date/Time: ") or str(datetime.datetime.now())
    client = input("Client: ")
    incident = input("Describe incident: ")
    action = input("Actions taken: ")
    print(f"\nIncident Report Draft:")
    print(f"Date: {date}")
    print(f"Client: {client}")
    print(f"Incident: {incident}")
    print(f"Actions: {action}")
    print("Recommend reviewing with line manager.")

def daily_checklist():
    print("\n--- Daily Support Checklist ---")
    items = [
        "Medication administered correctly",
        "Personal care / hygiene supported",
        "Meals prepared and offered (choice respected)",
        "Community access / activities",
        "Behavioural support strategies used",
        "Documentation completed (notes, incidents)",
        "Handover thorough"
    ]
    for i, item in enumerate(items, 1):
        print(f"{i}. {item} [ ]")
    print("Mark off as completed. Person-centred focus!")

def pay_estimator():
    print("\n--- SCHADS Level 2.1 Pay Estimator ---")
    hours = float(input("Hours worked this week: ") or 38)
    rate = 28.50  # Approx Level 2.1 casual/permanent base
    total = hours * rate
    print(f"Estimated gross pay: ${total:.2f} (based on ~${rate}/hr)")
    print("Note: Use actual award rates, penalties, etc.")

def goal_tracker():
    print("\n--- Client Goal Tracker ---")
    goal = input("Client goal (e.g., attend AFL game): ")
    progress = input("Progress/update: ")
    print(f"Goal: {goal}")
    print(f"Progress: {progress}")
    print("Document in client plan.")

if __name__ == "__main__":
    main()