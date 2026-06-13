# Support Worker Toolkit - Web Version with PDF Export
import streamlit as st
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(content, filename="support_document.pdf"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 12)
    y = 750
    for line in content.split('\n'):
        c.drawString(50, y, line)
        y -= 15
        if y < 50:
            c.showPage()
            y = 750
    c.save()
    buffer.seek(0)
    return buffer

st.title("Support Worker Toolkit")
st.subheader("For NDIS / Disability Support Workers")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Shift Summary", "Incident Report", "Pay Calculator", "Checklist", "Export PDF"])

with tab1:
    st.header("Shift Summary Generator")
    date = st.date_input("Date", datetime.date.today())
    client = st.text_input("Client")
    activities = st.text_area("Activities / Supports")
    observations = st.text_area("Observations")
    summary = f"Shift Summary for {client} on {date}\nActivities: {activities}\nObservations: {observations}"
    if st.button("Generate Summary"):
        st.text_area("Summary", summary, height=200)
        pdf = generate_pdf(summary)
        st.download_button("Download PDF", pdf, f"shift_summary_{date}.pdf", "application/pdf")

with tab2:
    st.header("Incident Report")
    date = st.text_input("Date/Time", str(datetime.datetime.now()))
    client = st.text_input("Client")
    incident = st.text_area("Incident Description")
    action = st.text_area("Actions Taken")
    report = f"Incident Report\nDate: {date}\nClient: {client}\nIncident: {incident}\nActions: {action}"
    if st.button("Generate Report"):
        st.text_area("Report", report, height=300)
        pdf = generate_pdf(report)
        st.download_button("Download PDF", pdf, f"incident_{date}.pdf", "application/pdf")

with tab3:
    st.header("Improved SCHADS Pay Calculator")
    hours = st.number_input("Hours worked", value=38.0, step=0.5)
    base_rate = st.number_input("Base hourly rate ($)", value=28.50)
    overtime_hours = max(0, hours - 38)
    regular_hours = min(hours, 38)
    # Simple penalties example
    penalty_rate = base_rate * 1.15  # e.g. night shift
    total = (regular_hours * base_rate) + (overtime_hours * base_rate * 1.5) + (10 * penalty_rate)  # example 10 penalty hours
    st.write(f"Estimated Gross Pay: ${total:.2f}")
    st.write("Note: Customize rates, add weekend/public holiday loadings as needed.")

with tab4:
    st.header("Daily Checklist")
    checklist = [
        "Medication administered (incl. PEG if applicable)",
        "Personal care / bed bath supported",
        "Meals offered with choice respected",
        "Community participation / activities",
        "Behavioural strategies / PBS used",
        "Documentation completed",
        "Handover given"
    ]
    checked = [st.checkbox(item) for item in checklist]

with tab5:
    st.header("Export All to PDF")
    notes = st.text_area("Additional notes for PDF")
    if st.button("Export Combined PDF"):
        combined = f"Support Worker Notes\nDate: {datetime.date.today()}\n{notes}"
        pdf = generate_pdf(combined)
        st.download_button("Download Combined PDF", pdf, "support_notes.pdf", "application/pdf")

st.sidebar.info("Built for Tony Sule - Rocky Bay & more. Tailor as needed!")