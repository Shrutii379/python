import streamlit as st
import random

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Number Hunt",
    page_icon="🎯",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

/* Reset & base */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

.stApp {
    background: #0d0d14;
    color: #e8e6f0;
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2.5rem; padding-bottom: 2rem; max-width: 600px; }

/* ── Hero title ── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.hero-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.22em;
    color: #7c6fcd;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}
.hero-title {
    font-size: 3.2rem;
    font-weight: 700;
    line-height: 1.1;
    background: linear-gradient(135deg, #a78bfa 0%, #60a5fa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}
.hero-sub {
    font-size: 1rem;
    color: #6b6880;
    margin-top: 0.75rem;
}

/* ── Stats bar ── */
.stats-row {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin: 1.5rem 0;
}
.stat-chip {
    background: #17172a;
    border: 1px solid #2a2840;
    border-radius: 12px;
    padding: 0.65rem 1.4rem;
    text-align: center;
}
.stat-value {
    font-family: 'Space Mono', monospace;
    font-size: 1.6rem;
    font-weight: 700;
    color: #a78bfa;
    line-height: 1;
}
.stat-label {
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    color: #4e4c60;
    text-transform: uppercase;
    margin-top: 0.25rem;
}

/* ── History list ── */
.history-wrap {
    background: #13131f;
    border: 1px solid #1e1e30;
    border-radius: 14px;
    padding: 1.1rem 1.4rem;
    margin: 1rem 0;
    max-height: 220px;
    overflow-y: auto;
}
.history-title {
    font-family: 'Space Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.15em;
    color: #3d3b52;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
}
.hist-item {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.45rem 0;
    border-bottom: 1px solid #1a1a28;
    font-size: 0.9rem;
}
.hist-item:last-child { border-bottom: none; }
.hist-num {
    font-family: 'Space Mono', monospace;
    font-size: 1rem;
    font-weight: 700;
    color: #c4b5fd;
    width: 3rem;
}
.badge {
    display: inline-block;
    font-size: 0.65rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 600;
    padding: 0.2rem 0.55rem;
    border-radius: 999px;
}
.badge-low  { background: #1a2e40; color: #60a5fa; }
.badge-high { background: #2e1a1a; color: #f87171; }

/* ── Feedback banner ── */
.feedback {
    border-radius: 12px;
    padding: 1rem 1.4rem;
    margin: 1rem 0;
    font-size: 0.95rem;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}
.feedback-low  { background: #0d1e2e; border-left: 3px solid #3b82f6; color: #93c5fd; }
.feedback-high { background: #2a0f0f; border-left: 3px solid #ef4444; color: #fca5a5; }
.feedback-win  { background: #0d2217; border-left: 3px solid #22c55e; color: #86efac; }
.feedback-lose { background: #1a1023; border-left: 3px solid #8b5cf6; color: #c4b5fd; }

/* ── Streamlit widget overrides ── */
div[data-testid="stNumberInput"] input {
    background: #17172a !important;
    border: 1.5px solid #2d2b45 !important;
    border-radius: 10px !important;
    color: #e8e6f0 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 1.15rem !important;
    text-align: center !important;
    padding: 0.75rem !important;
    transition: border-color 0.2s;
}
div[data-testid="stNumberInput"] input:focus {
    border-color: #7c6fcd !important;
    box-shadow: 0 0 0 2px rgba(124,111,205,0.18) !important;
}

div[data-testid="stButton"] button {
    width: 100%;
    padding: 0.8rem 0;
    background: linear-gradient(135deg, #7c6fcd, #4f8ef7);
    color: #fff;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: opacity 0.2s, transform 0.15s;
    letter-spacing: 0.03em;
}
div[data-testid="stButton"] button:hover {
    opacity: 0.88;
    transform: translateY(-1px);
}

/* divider */
.divider {
    border: none;
    border-top: 1px solid #1e1e2e;
    margin: 1.4rem 0;
}
</style>
""", unsafe_allow_html=True)


# ── Session state init ────────────────────────────────────────────────────────
def init_state():
    st.session_state.number   = random.randint(1, 100)
    st.session_state.count    = 0
    st.session_state.history  = []          # list of (guess, "low"|"high"|"win")
    st.session_state.status   = "playing"   # "playing" | "won" | "lost"
    st.session_state.max_tries = 7

if "number" not in st.session_state:
    init_state()

s = st.session_state


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-label">Mind vs Machine</div>
    <h1 class="hero-title">Number Hunt</h1>
    <p class="hero-sub">I'm thinking of a number between <strong style="color:#a78bfa">1</strong> and <strong style="color:#60a5fa">100</strong>. Can you crack it?</p>
</div>
""", unsafe_allow_html=True)


# ── Stats row ─────────────────────────────────────────────────────────────────
tries_left = s.max_tries - s.count
st.markdown(f"""
<div class="stats-row">
    <div class="stat-chip">
        <div class="stat-value">{s.count}</div>
        <div class="stat-label">Guesses</div>
    </div>
    <div class="stat-chip">
        <div class="stat-value">{tries_left}</div>
        <div class="stat-label">Remaining</div>
    </div>
    <div class="stat-chip">
        <div class="stat-value">1–100</div>
        <div class="stat-label">Range</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Input + guess button ──────────────────────────────────────────────────────
if s.status == "playing":
    guess = st.number_input(
        "Your guess",
        min_value=1, max_value=100,
        step=1, value=50,
        label_visibility="collapsed",
    )

    if st.button("Submit Guess →"):
        s.count += 1

        if guess == s.number:
            s.history.append((guess, "win"))
            s.status = "won"
        elif guess < s.number:
            s.history.append((guess, "low"))
            if s.count >= s.max_tries:
                s.status = "lost"
        else:
            s.history.append((guess, "high"))
            if s.count >= s.max_tries:
                s.status = "lost"

        st.rerun()


# ── Feedback ──────────────────────────────────────────────────────────────────
if s.history:
    last_guess, last_result = s.history[-1]

    if last_result == "win":
        st.markdown(f"""
        <div class="feedback feedback-win">
            ✅ <span><strong>{last_guess}</strong> is correct — you nailed it in {s.count} guess{"es" if s.count!=1 else ""}!</span>
        </div>""", unsafe_allow_html=True)

    elif s.status == "lost":
        st.markdown(f"""
        <div class="feedback feedback-lose">
            💀 <span>Out of tries. The number was <strong>{s.number}</strong>. Better luck next time!</span>
        </div>""", unsafe_allow_html=True)

    elif last_result == "low":
        st.markdown(f"""
        <div class="feedback feedback-low">
            ⬆️ <span><strong>{last_guess}</strong> is too low — aim higher.</span>
        </div>""", unsafe_allow_html=True)

    elif last_result == "high":
        st.markdown(f"""
        <div class="feedback feedback-high">
            ⬇️ <span><strong>{last_guess}</strong> is too high — come down a bit.</span>
        </div>""", unsafe_allow_html=True)


# ── Balloons on win or lose ───────────────────────────────────────────────────
if s.status == "won":
    st.balloons()

elif s.status == "lost":
    st.snow()           # snow for losing — distinct & still satisfying


# ── Guess history ─────────────────────────────────────────────────────────────
if s.history:
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    items_html = ""
    for i, (g, r) in enumerate(reversed(s.history), 1):
        seq  = len(s.history) - i + 1
        if r == "low":
            badge = '<span class="badge badge-low">Too Low</span>'
            icon  = "⬆️"
        elif r == "high":
            badge = '<span class="badge badge-high">Too High</span>'
            icon  = "⬇️"
        else:
            badge = '<span class="badge" style="background:#0d2217;color:#86efac">Correct!</span>'
            icon  = "✅"
        items_html += f"""
        <div class="hist-item">
            <span style="color:#3d3b52;font-family:Space Mono,monospace;font-size:0.7rem">#{seq}</span>
            <span class="hist-num">{g}</span>
            {badge}
            <span style="margin-left:auto;font-size:0.85rem">{icon}</span>
        </div>"""

    st.markdown(f"""
    <div class="history-wrap">
        <div class="history-title">Guess History</div>
        {items_html}
    </div>""", unsafe_allow_html=True)


# ── Play again ────────────────────────────────────────────────────────────────
if s.status in ("won", "lost"):
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    if st.button("Play Again"):
        init_state()
        st.rerun()