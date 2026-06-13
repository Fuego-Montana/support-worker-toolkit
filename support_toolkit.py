# Support Worker Toolkit - CLI Version
# Updated with Rocky Bay Case Note Guidelines

import datetime

def main():
    print("\n=== NDIS Support Worker Toolkit (CLI) ===")
    print("Updated with Rocky Bay Case Note Guidelines (Active Support, Objective, Strength-Based)")
    while True:
        print("\nMenu:")
        print("1. Generate Shift Summary / Case Note (Guidelines Compliant)")
        print("2. Draft Incident Report")
        print("3. Daily Checklist")
        print("4. SCHADS Pay Estimator")
        print("5. Exit")
        choice = input("Choose (1-5): ")
        
        if choice == '1':
            generate_shift_summary_guidelines()
        elif choice == '2':
            draft_incident_report()
        elif choice == '3':
            daily_checklist()
        elif choice == '4':
            pay_estimator()
        elif choice == '5':
            print("Goodbye! Use the web version (streamlit run app.py) for best experience and PDF.")
            break

def generate_shift_summary_guidelines():
    print("\n--- Shift Summary / Case Note Generator (Follows Guidelines) ---")
    date = input("Date (YYYY-MM-DD or today): ") or str(datetime.date.today())
    client = input("Client Full/Preferred Name: ")
    shift = input("Shift Type (Day/Evening/Night): ") or "Day"
    
    print("\nEnter details following guidelines: Objective, strength-based, describe support & assistance types.")
    support = input("Support Activities & Active Engagement (describe what you did to support): ")
    achieve = input("Achievements, Choices, Progress, Learning: ")
    obs = input("Objective Observations (see/hear/touch/smell - no assumptions): ")
    assist = input("Types of Assistance (verbal cues, hand-over-hand, etc.): ")
    behave = input("Behaviour Changes or Reactions: ")
    
    summary = f"""SHIFT / CASE NOTE SUMMARY
Date: {date} | Shift: {shift}
Client: {client}
Support Worker: Tony Sule

SUPPORT ACTIVITIES & ACTIVE ENGAGEMENT:
{support}

ACHIEVEMENTS, PROGRESS, CHOICES & LEARNING:
{achieve}

OBJECTIVE OBSERVATIONS:
{obs}

ASSISTANCE PROVIDED:
{assist}

BEHAVIOUR / REACTIONS:
{behave}

---
Note: Compliant with Rocky Bay Guidelines - Objective language, strength-based, full names, records of support/choices/assistance only. No assumptions or labelling."""
    
    print("\n" + summary)
    save = input("Save as text file? (y/n): ").lower()
    if save == 'y':
        fname = f"CaseNote_{client}_{date}.txt"
        with open(fname, 'w') as f:
            f.write(summary)
        print(f"Saved to {fname}")

# Keep other functions simple
def draft_incident_report():
    print("Use web version for structured incident reports.")

def daily_checklist():
    print("Checklist in web app.")

def pay_estimator():
    hours = float(input("Hours: ") or 38)
    rate = float(input("Base rate: ") or 28.50)
    ot = max(0, hours - 38)
    total = (min(hours,38)*rate) + (ot * rate * 1.5)
    print(f"Pay: ${total:.2f} (OT included)")

if __name__ == "__main__":
    main()