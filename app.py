# Improved Support Worker Toolkit

import streamlit as st
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

# PWA injection
st.components.v1.html('''
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js').then(function(reg) {
    console.log('Service Worker registered');
  }).catch(function(err) {
    console.log('Service Worker registration failed: ', err);
  });
}
</script>
<link rel="manifest" href="/static/manifest.json">
''', height=0)

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

st.set_page_config(page_title="Support Worker Toolkit", page_icon="💪", layout="wide", initial_sidebar_state="expanded")

st.title("Support Worker Toolkit")
st.subheader("NDIS / Disability Support - Mobile Friendly")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Shift Summary", "Incident Report", "Pay Calculator", "Checklist", "Export"])

with tab1:
    st.header("Shift Summary Generator")
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("Date", datetime.date.today())
        client = st.text_input("Client")
    with col2:
        shift_type = st.selectbox("Shift Type", ["Day", "Evening", "Night"])
    activities = st.text_area("Activities / Supports", height=150)
    observations = st.text_area("Observations / Notes", height=150)
    if st.button("Generate Summary", type="primary"):
        summary = f"Shift Summary for {client} on {date} ({shift_type} shift)\n\nActivities: {activities}\n\nObservations: {observations}"
        st.success("Summary Generated!")
        st.text_area("Your Summary", summary, height=250)
        pdf = generate_pdf(summary)
        st.download_button("📥 Download PDF", pdf, f"shift_summary_{date}.pdf", "application/pdf")

with tab2:
    st.header("Incident Report")
    date = st.text_input("Date/Time", str(datetime.datetime.now()))
    client = st.text_input("Client")
    incident = st.text_area("Incident Description", height=200)
    action = st.text_area("Actions Taken / Follow-up", height=150)
    if st.button("Generate Report", type="primary"):
        report = f"Incident Report\nDate: {date}\nClient: {client}\n\nIncident: {incident}\n\nActions: {action}"
        st.text_area("Report", report, height=300)
        pdf = generate_pdf(report)
        st.download_button("📥 Download PDF", pdf, f"incident_report.pdf", "application/pdf")

with tab3:
    st.header("Improved SCHADS Pay Calculator")
    col1, col2 = st.columns(2)
    with col1:
        hours = st.number_input("Total Hours Worked", value=38.0, step=0.25, min_value=0.0)
        base_rate = st.number_input("Base Hourly Rate ($)", value=28.50, step=0.5)
    with col2:
        overtime = st.checkbox("Overtime (after 38hrs)")
        night_shift = st.checkbox("Night/Evening Penalty")
    regular = min(hours, 38)
    ot_hours = max(0, hours - 38) if overtime else 0
    pay = regular * base_rate
    if night_shift:
        pay += hours * base_rate * 0.15  # example 15% loading
    if ot_hours > 0:
        pay += ot_hours * base_rate * 0.5
    st.metric("Estimated Gross Pay", f"${pay:.2f}")
    st.caption("Based on SCHADS Level 2.1 approx. Customize for weekends/public holidays.")

with tab4:
    st.header("Daily Checklist")
    cols = st.columns(2)
    checklist = [
        "Medication (incl. PEG, epilepsy meds)",
        "Personal care / bed bath",
        "Meals with client choice",
        "Community activities supported",
        "PBS / Behavioural strategies",
        "Documentation & handover",
        "MHFA or de-escalation used if needed"
    ]
    checked = []
    for i, item in enumerate(checklist):
        with cols[i % 2]:
            checked.append(st.checkbox(item))

with tab5:
    st.header("Combined Export")
    notes = st.text_area("Additional Notes / Reflections")
    if st.button("Export All to PDF", type="primary"):
        combined = f"Support Notes - {datetime.date.today()}\n\n{notes}"
        pdf = generate_pdf(combined)
        st.download_button("📥 Download Combined PDF", pdf, "daily_support_notes.pdf", "application/pdf")

st.sidebar.success("Mobile Optimized + PWA Ready! Add to Home Screen on your phone.")
st.sidebar.info("Tailored for Tony Sule @ Rocky Bay")
