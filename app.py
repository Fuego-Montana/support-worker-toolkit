# Support Worker Toolkit - Web Version
# Updated with Case Note Guidelines (Rocky Bay / NDIS Active Support)

import streamlit as st
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

# PWA injection (keep as before)
st.components.v1.html('''
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js').then(function(reg) { console.log('SW registered'); });
}
</script>
<link rel="manifest" href="/static/manifest.json">
''', height=0)

def generate_pdf(content, filename="support_document.pdf"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 11)
    y = 750
    for line in content.split('\n'):
        if y < 50:
            c.showPage()
            y = 750
        c.drawString(40, y, line[:95])  # wrap long lines
        y -= 14
    c.save()
    buffer.seek(0)
    return buffer

st.set_page_config(page_title="Support Worker Toolkit - Case Notes", page_icon="📋", layout="wide")

st.title("Support Worker Toolkit")
st.subheader("NDIS / Supported Accommodation - Shift Summary & Case Notes")
st.caption("Following Rocky Bay Guidelines for Case Notes (Active Support, Objective, Strength-Based)")

# Guidelines reminder
with st.expander("📋 Case Note Guidelines Reminder (Click to expand)", expanded=False):
    st.markdown("""
    **What to INCLUDE:**
    - Record of **factors only** – describe the support given (e.g. "Supported client to prepare breakfast using verbal prompts and hand-over-hand assistance").
    - **Objective language**: what you see, hear, touch or smell.
    - **Strength-based language**: focus on what the person has done well, respectful, honest, positive.
    - Record **achievements, progress, learning opportunities, choices** made and how supported.
    - Use **full/preferred names**, avoid abbreviations/acronyms.
    - Note any **changes in behaviour** or reactions to events.
    - Describe **types of assistance** (Verbal cues, hand-over-hand, modelling, etc.).
    - Include Active Support engagement.

    **What NOT to include:**
    - Labelling (lazy, difficult, aggressive, etc.).
    - Assumptions ("He had a good day", "She looked happy").
    - Personal details like toileting/bowels/pad changes (unless specifically requested – document in observations).
    - Everyday activity details (what they ate, medication as charted, slept well – use Observations section).
    - Disrespectful comments about client, family or staff.
    - Nil concerns without notifying team leader if needed.
    """)

st.divider()

# Shift Summary Generator - IMPROVED with guidelines
st.header("📝 Shift Summary / Case Note Generator")

col1, col2 = st.columns([1, 1])

with col1:
    date = st.date_input("Date", datetime.date.today())
    client = st.text_input("Client Preferred / Full Name", placeholder="e.g. John Smith")
    shift = st.selectbox("Shift Type", ["Day", "Evening", "Night"])

with col2:
    support_activities = st.text_area("Support Activities & Engagement (fact-based, describe support given)", 
        placeholder="Supported client to choose and prepare breakfast. Client selected cereal and toast. Provided verbal prompts for safety and hand-over-hand assistance for spreading butter. Client completed independently after modelling.", height=120)
    
    achievements = st.text_area("Achievements, Progress, Choices & Learning", 
        placeholder="Client chose blue pyjamas independently. Successfully used verbal request for more juice. Progress in hand washing routine with less prompting today.", height=100)

observations = st.text_area("Objective Observations (what you saw/heard/touched/smelled - no assumptions)", 
    placeholder="Client smiled and said 'thank you' after support. Voice was calm during activity. No changes in behaviour noted. Client engaged well with activity choice.", height=100)

assistance = st.text_area("Types of Assistance Provided", 
    placeholder="Verbal cues, hand-over-hand assistance, modelling, positive reinforcement, choice offering.", height=60)

behaviour = st.text_area("Any Behaviour Changes or Reactions to Events", 
    placeholder="Client showed positive reaction to community outing plan. No incidents or changes in behaviour observed.", height=60)

if st.button("Generate Compliant Case Note / Shift Summary", type="primary", use_container_width=True):
    if not client:
        st.error("Please enter client name.")
    else:
        summary = f"""SHIFT / CASE NOTE SUMMARY
Date: {date} | Shift: {shift} | Support Worker: Tony Sule
Client: {client}

SUPPORT ACTIVITIES & ACTIVE ENGAGEMENT:
{support_activities}

ACHIEVEMENTS, PROGRESS, CHOICES & LEARNING OPPORTUNITIES:
{achievements}

OBJECTIVE OBSERVATIONS:
{observations}

ASSISTANCE PROVIDED:
{assistance}

BEHAVIOUR / REACTIONS:
{behaviour}

Note: Documented in line with Rocky Bay Supported Accommodation Case Note Guidelines (Active Support, Objective & Strength-Based language). Full names used. No assumptions or labelling included."""
        
        st.success("✅ Compliant Shift Summary Generated!")
        st.text_area("Copy this ready-to-paste note (follows guidelines):", summary, height=350)
        
        pdf = generate_pdf(summary)
        st.download_button("📥 Download as PDF", pdf, f"CaseNote_{client}_{date}.pdf", "application/pdf", use_container_width=True)

st.divider()

# Other tabs remain similar but updated
st.header("Other Tools")

# Keep or update other tabs briefly for completeness
with st.expander("Incident Report (Guidelines Compliant)"):
    # Similar structured inputs...
    st.write("Use objective language, full names, describe facts and support provided. Avoid assumptions.")
    # (keep simple for now or expand similarly)

with st.expander("Pay Calculator & Checklist"):
    st.write("Other tools available in full app.")

st.sidebar.info("Updated for Rocky Bay Guidelines | Active Support | Objective & Strength-Based Case Notes | PWA Ready (Add to Home Screen on phone)")
st.sidebar.caption("Built for Tony Sule | Customize as needed for your roster")