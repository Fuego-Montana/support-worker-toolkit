# Updated Support Worker Toolkit with PDF Export (CLI)
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(content, filename="document.pdf"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 12)
    y = 750
    for line in content.split('\n'):
        if y < 50:
            c.showPage()
            y = 750
        c.drawString(50, y, line)
        y -= 15
    c.save()
    buffer.seek(0)
    with open(filename, "wb") as f:
        f.write(buffer.getvalue())
    print(f"PDF saved as {filename}")

def main():
    print("\n=== Support Worker Toolkit ===")
    print("Welcome! Now with PDF export.")
    while True:
        print("\nMenu:")
        print("1. Generate Shift Summary")
        print("2. Draft Incident Report")
        print("3. Daily Checklist")
        print("4. SCHADS Pay Estimator (Improved)")
        print("5. Client Goal Tracker")
        print("6. Exit")
        choice = input("Choose (1-6): ")
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
            break

def generate_shift_summary():
    date = input("Date: ") or str(datetime.date.today())
    client = input("Client: ")
    activities = input("Activities: ")
    observations = input("Observations: ")
    summary = f"Shift Summary\nDate: {date}\nClient: {client}\nActivities: {activities}\nObservations: {observations}"
    print(summary)
    if input("Save as PDF? (y/n): ").lower() == 'y':
        generate_pdf(summary, f"shift_{date}.pdf")

def draft_incident_report():
    date = input("Date: ")
    client = input("Client: ")
    incident = input("Incident: ")
    action = input("Actions: ")
    report = f"Incident Report\nDate: {date}\nClient: {client}\nIncident: {incident}\nActions: {action}"
    print(report)
    if input("Save PDF? (y/n): ").lower() == 'y':
        generate_pdf(report, f"incident_{date}.pdf")

def daily_checklist():
    print("Checklist items - mark manually")

def pay_estimator():
    hours = float(input("Hours: ") or 38)
    rate = float(input("Base rate: ") or 28.50)
    ot = max(0, hours - 38)
    total = (min(hours,38)*rate) + (ot * rate * 1.5)
    print(f"Pay: ${total:.2f} (OT included)")

def goal_tracker():
    print("Goal tracker - simple")

if __name__ == "__main__":
    main()