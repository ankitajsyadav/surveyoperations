import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="Campus Tour Survey Mockup", layout="centered")

st.title("Campus Tour Experience Survey (Mockup)")
st.caption("Demo survey to showcase skip logic, randomization, quotas, and loop & merge.")

st.write("---")

# ---------------------------
# 1. BASIC SCREENER + SKIP LOGIC
# ---------------------------

st.subheader("1. Screener")

attended = st.radio(
    "Did you attend a campus tour at Roosevelt University in the last 7 days?",
    ["Yes", "No"],
    key="attended"
)

if attended == "No":
    st.warning("This survey is only for students who attended a campus tour. (Skip logic demo)")
    st.stop()

tour_date = st.date_input(
    "Which date did you attend your campus tour?",
    value=date.today(),
    key="tour_date"
)

tour_type = st.radio(
    "What type of tour did you attend?",
    ["In-person", "Virtual"],
    key="tour_type"
)

st.write("---")

# ---------------------------
# 2. SIMULATED QUOTAS
# ---------------------------
st.subheader("2. Quota Demo (Simulated)")

# Fake current counts – in production this comes from a database / panel system
current_counts = {
    "Domestic": 48,
    "International": 20
}
quota_limits = {
    "Domestic": 50,
    "International": 25
}

student_type = st.radio(
    "Are you a domestic or international student?",
    ["Domestic", "International"],
    key="student_type"
)

remaining = quota_limits[student_type] - current_counts[student_type]

if remaining <= 0:
    st.error(f"Quota for {student_type} students is full. (Quota logic demo)")
    st.stop()
else:
    st.info(f"Remaining quota for {student_type} students: {remaining} spots.")

st.write("---")
# ---------------------------
# 3. RANDOMIZED EXPERIENCE BLOCKS
# ---------------------------

st.subheader("3. Tour Experience (Randomized Block Order)")

# Define block labels
blocks = ["Tour Guide", "Content & Flow", "Facilities/Virtual"]

# Randomize order every run (for demo purposes)
random.shuffle(blocks)

st.caption(f"Block order for this respondent (randomized): **{', '.join(blocks)}**")

# Helper functions for each block
def block_tour_guide():
    st.markdown("### Block: Tour Guide Experience")
    st.slider("How would you rate your tour guide overall?", 1, 5, 4, key="guide_overall")

    guide_items = [
        "Knowledge of the university",
        "Clarity of explanations",
        "Friendliness",
        "Ability to answer questions"
    ]
    # Randomize items
    random.shuffle(guide_items)
    st.caption(f"Randomized attributes: {', '.join(guide_items)}")

    for item in guide_items:
        st.slider(f"{item}", 1, 5, 4, key=f"guide_{item}")


def block_content_flow():
    st.markdown("### Block: Tour Content & Flow")
    st.slider("The overall tour was well organized.", 1, 5, 4, key="content_org")
    st.slider("The information shared was clear and helpful.", 1, 5, 4, key="content_clarity")

    st.radio(
        "How did you feel about the pace of the tour?",
        ["Too slow", "Just right", "Too fast"],
        key="pace"
    )


def block_facilities_or_virtual():
    if tour_type == "In-person":
        st.markdown("### Block: Campus Facilities (In-person)")
        facilities = st.multiselect(
            "Which of the following did you see during your tour?",
            ["Library", "Residence Halls", "Dining Hall", "Labs", "Recreation Center"],
            key="facilities_seen"
        )

        # LOOP & MERGE DEMO: ask the same questions for each facility selected
        if facilities:
            st.caption("Loop & merge demo: repeating questions for each selected facility.")
            for facility in facilities:
                st.markdown(f"**{facility}**")
                st.slider(
                    f"How satisfied were you with the {facility}?",
                    1, 5, 4,
                    key=f"sat_{facility}"
                )
                st.text_area(
                    f"Comments about the {facility} (optional):",
                    key=f"comment_{facility}"
                )
    else:
        st.markdown("### Block: Virtual Tour Experience")
        st.slider(
            "The virtual platform was easy to access and use.",
            1, 5, 4,
            key="virtual_access"
        )
        st.slider(
            "Audio and video quality were satisfactory.",
            1, 5, 4,
            key="virtual_quality"
        )

# Render the blocks in the randomized order
for block in blocks:
    if block == "Tour Guide":
        block_tour_guide()
    elif block == "Content & Flow":
        block_content_flow()
    else:
        block_facilities_or_virtual()

st.write("---")
# ---------------------------
# 4. NPS + SKIP LOGIC FOLLOW-UP
# ---------------------------

st.subheader("4. Net Promoter Score (NPS)")

nps_score = st.slider(
    "On a scale of 0–10, how likely are you to recommend this campus tour to a friend?",
    0, 10, 8,
    key="nps"
)

# Determine NPS group
if nps_score >= 9:
    nps_group = "Promoter"
elif nps_score >= 7:
    nps_group = "Passive"
else:
    nps_group = "Detractor"

st.caption(f"NPS group (based on score): **{nps_group}**")

# Skip-logic based open-ended question
if nps_group == "Promoter":
    followup = st.text_area(
        "What did you like most about your campus tour experience?",
        key="nps_promoter"
    )
elif nps_group == "Passive":
    followup = st.text_area(
        "What could we improve to make your experience excellent?",
        key="nps_passive"
    )
else:
    followup = st.text_area(
        "We’re sorry your experience wasn’t ideal. What were the main reasons for your rating?",
        key="nps_detractor"
    )

st.write("---")
# ---------------------------
# 5. FUTURE INTEREST & OUTREACH
# ---------------------------

st.subheader("5. Future Interest & Outreach")

intent = st.radio(
    "Based on your experience so far, how likely are you to apply to Roosevelt University?",
    ["Very likely", "Somewhat likely", "Not sure", "Unlikely"],
    key="intent"
)

wants_followup = st.radio(
    "Would you like us to follow up with more information?",
    ["Yes", "No"],
    key="followup"
)

contact_method = None
if wants_followup == "Yes":
    contact_method = st.multiselect(
        "How would you like us to contact you?",
        ["Email", "Phone call", "Text message"],
        key="contact_method"
    )

st.write("---")

# ---------------------------
# 6. "SUBMIT" + DEBUG SUMMARY FOR DEMO
# ---------------------------

if st.button("Submit (Mock)"):
    st.success("Thank you! This is a mock submission for demo purposes.")
    with st.expander("Show debug / explanation for interviewers"):
        st.write("### What this mockup demonstrates:")
        st.markdown("- **Skip logic** for non-attendees and virtual vs in-person tours.")
        st.markdown("- **Randomization** of experience blocks and guide attributes.")
        st.markdown("- **Quotas** simulated with domestic vs international limits.")
        st.markdown("- **Loop & merge** for multiple facilities (same questions per facility).")
        st.markdown("- **NPS routing** to different follow-up questions by Promoter/Passive/Detractor.")