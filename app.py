# ============================================================
# Ananya Communication - Streamlit Website
# Run with: streamlit run app.py
# ============================================================

import streamlit as st
from datetime import datetime

# ── Page Configuration ────────────────────────────────────────
st.set_page_config(
    page_title="Ananya Communication",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;900&display=swap');

/* ── Global Reset ── */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* ── Hide Streamlit Branding ── */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ── Root Variables ── */
:root {
    --blue:   #1a3c6e;
    --teal:   #0d9488;
    --gold:   #f59e0b;
    --light:  #f0f9ff;
    --white:  #ffffff;
    --text:   #1e293b;
    --muted:  #64748b;
    --radius: 16px;
    --shadow: 0 8px 30px rgba(0,0,0,0.10);
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #1a3c6e 0%, #0d9488 100%);
    padding-top: 1rem;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
[data-testid="stSidebar"] .stRadio label {
    font-size: 1rem;
    padding: 6px 0;
    cursor: pointer;
}

/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg, #1a3c6e 0%, #0d9488 60%, #0f766e 100%);
    border-radius: var(--radius);
    padding: 3.5rem 2.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 2rem;
    box-shadow: var(--shadow);
}
.hero-banner::before {
    content: "";
    position: absolute;
    top: -60px; right: -60px;
    width: 260px; height: 260px;
    background: rgba(255,255,255,0.06);
    border-radius: 50%;
}
.hero-banner::after {
    content: "";
    position: absolute;
    bottom: -80px; left: -40px;
    width: 300px; height: 300px;
    background: rgba(255,255,255,0.04);
    border-radius: 50%;
}
.hero-title {
    font-size: 3rem;
    font-weight: 900;
    color: #ffffff;
    letter-spacing: -1px;
    margin-bottom: 0.4rem;
}
.hero-tagline {
    font-size: 1.2rem;
    font-weight: 600;
    color: #f59e0b;
    margin-bottom: 1rem;
    letter-spacing: 0.5px;
}
.hero-welcome {
    font-size: 1rem;
    color: rgba(255,255,255,0.85);
    max-width: 550px;
    margin: 0 auto 1.8rem auto;
    line-height: 1.7;
}
.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.3);
    color: #fff;
    padding: 6px 18px;
    border-radius: 50px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 2rem;
    backdrop-filter: blur(4px);
}

/* ── Contact Strip ── */
.contact-strip {
    display: flex;
    justify-content: center;
    gap: 2rem;
    flex-wrap: wrap;
    margin-top: 1rem;
}
.contact-item {
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 50px;
    padding: 8px 20px;
    color: #fff;
    font-size: 0.9rem;
    font-weight: 500;
    backdrop-filter: blur(4px);
}

/* ── Section Heading ── */
.section-heading {
    text-align: center;
    margin-bottom: 2rem;
}
.section-heading h2 {
    font-size: 1.9rem;
    font-weight: 800;
    color: var(--blue);
    margin-bottom: 0.3rem;
}
.section-heading p {
    color: var(--muted);
    font-size: 1rem;
}
.divider {
    width: 60px;
    height: 4px;
    background: linear-gradient(90deg, #1a3c6e, #0d9488);
    border-radius: 4px;
    margin: 0.6rem auto 0.8rem auto;
}

/* ── Service Card ── */
.service-card {
    background: var(--white);
    border-radius: var(--radius);
    padding: 1.6rem 1.2rem;
    text-align: center;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 16px rgba(0,0,0,0.07);
    transition: transform 0.25s, box-shadow 0.25s, border-color 0.25s;
    margin-bottom: 1.2rem;
    min-height: 160px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}
.service-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 32px rgba(13,148,136,0.18);
    border-color: #0d9488;
}
.service-icon {
    font-size: 2.4rem;
    margin-bottom: 0.3rem;
}
.service-name {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--blue);
    line-height: 1.3;
}
.service-sub {
    font-size: 0.78rem;
    color: var(--muted);
}

/* ── Info Card (About / Contact) ── */
.info-card {
    background: var(--white);
    border-radius: var(--radius);
    padding: 2rem;
    border: 1px solid #e2e8f0;
    box-shadow: var(--shadow);
    margin-bottom: 1.5rem;
}
.info-card h3 {
    color: var(--blue);
    font-weight: 700;
    margin-bottom: 0.8rem;
    font-size: 1.2rem;
}
.info-card p, .info-card li {
    color: var(--text);
    font-size: 0.95rem;
    line-height: 1.8;
}

/* ── Highlight Box ── */
.highlight-box {
    background: linear-gradient(135deg, #eff6ff, #f0fdfa);
    border-left: 5px solid #0d9488;
    border-radius: 10px;
    padding: 1.2rem 1.5rem;
    margin: 1rem 0;
    font-size: 0.95rem;
    color: var(--text);
    line-height: 1.7;
}

/* ── Action Buttons ── */
.btn-row {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    margin: 1.5rem 0;
}
.btn-call {
    background: linear-gradient(90deg, #1a3c6e, #2563eb);
    color: #fff;
    padding: 14px 32px;
    border-radius: 50px;
    font-weight: 700;
    font-size: 1rem;
    text-decoration: none;
    box-shadow: 0 4px 16px rgba(26,60,110,0.3);
    transition: opacity 0.2s;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}
.btn-whatsapp {
    background: linear-gradient(90deg, #16a34a, #22c55e);
    color: #fff;
    padding: 14px 32px;
    border-radius: 50px;
    font-weight: 700;
    font-size: 1rem;
    text-decoration: none;
    box-shadow: 0 4px 16px rgba(22,163,74,0.3);
    transition: opacity 0.2s;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}
.btn-call:hover, .btn-whatsapp:hover { opacity: 0.88; }

/* ── Footer ── */
.footer {
    background: linear-gradient(135deg, #1a3c6e, #0d9488);
    border-radius: var(--radius);
    padding: 2rem;
    text-align: center;
    color: rgba(255,255,255,0.85);
    margin-top: 3rem;
    font-size: 0.88rem;
    line-height: 1.8;
}
.footer strong { color: #f59e0b; }

/* ── Date/Time Chip ── */
.datetime-chip {
    background: linear-gradient(90deg, #eff6ff, #f0fdfa);
    border: 1px solid #bfdbfe;
    border-radius: 50px;
    padding: 6px 18px;
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--blue);
    display: inline-block;
    margin-bottom: 1.5rem;
}

/* ── Contact Detail Row ── */
.contact-detail {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 10px 0;
    border-bottom: 1px solid #f1f5f9;
}
.contact-detail:last-child { border-bottom: none; }
.contact-icon { font-size: 1.4rem; flex-shrink: 0; margin-top: 2px; }
.contact-text { font-size: 0.95rem; color: var(--text); line-height: 1.5; }
.contact-label { font-weight: 700; color: var(--blue); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px; }

/* ── Responsive tweaks ── */
@media (max-width: 640px) {
    .hero-title { font-size: 2rem; }
    .hero-tagline { font-size: 1rem; }
}
</style>
""", unsafe_allow_html=True)

# ── Constants ────────────────────────────────────────────────
SHOP_NAME   = "Ananya Communication"
TAGLINE     = "All Digital & Banking Services at One Place"
PHONE       = "8743897051"
EMAIL       = "rajusahu0748@gmail.com"
ADDRESS     = "Gali No. 67B, Near Bharat Mata Mandir,\nSwatantra Nagar, Narela, Delhi – 110040"
WHATSAPP    = f"https://wa.me/91{PHONE}?text=Hello%2C%20I%20need%20your%20services."
CALL_LINK   = f"tel:{PHONE}"
MAPS_EMBED  = "https://maps.google.com/maps?q=Narela+Delhi+110040&t=&z=14&ie=UTF8&iwloc=&output=embed"

SERVICES = [
    ("💸", "Money Transfer",         "NEFT / IMPS / UPI"),
    ("🏧", "Cash Withdrawal",        "All Banks Supported"),
    ("📱", "Mobile Recharge",        "All Operators"),
    ("🚆", "Train Ticket Booking",   "IRCTC Authorised"),
    ("📄", "Bill Payments",          "Electricity / Water / Gas"),
    ("🖥️", "Online Form Filling",    "Govt & Private Forms"),
    ("🏦", "SBI Account Opening",    "Zero Balance Account"),
    ("🪪", "PAN Card Services",      "New / Correction"),
    ("🆔", "Aadhaar Card Update",    "Address / Mobile Update"),
    ("🖨️", "Photocopy Services",     "B&W / Colour"),
    ("📲", "All UPI Services",       "PhonePe / GPay / Paytm"),
    ("📡", "Other Digital Services", "Ask Us Anything"),
]

# ── Sidebar Navigation ───────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style='text-align:center; padding: 1rem 0 1.5rem 0;'>
        <div style='font-size:2.5rem;'>📡</div>
        <div style='font-weight:800; font-size:1.1rem; letter-spacing:0.5px;'>{SHOP_NAME}</div>
        <div style='font-size:0.75rem; opacity:0.8; margin-top:4px;'>{TAGLINE}</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["🏠  Home", "🛠️  Services", "ℹ️  About Us", "📞  Contact"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    now = datetime.now()
    st.markdown(f"""
    <div style='text-align:center; opacity:0.85; font-size:0.8rem; line-height:1.8;'>
        🕐 {now.strftime('%I:%M %p')}<br>
        📅 {now.strftime('%A, %d %B %Y')}
    </div>
    """, unsafe_allow_html=True)

# ── Routing ─────────────────────────────────────────────────
selected = page.split("  ", 1)[1] if "  " in page else page

# ╔══════════════════════════════════════════════╗
# ║                  HOME PAGE                   ║
# ╚══════════════════════════════════════════════╝
if selected == "Home":

    # Date/time chip
    now = datetime.now()
    st.markdown(f"""
    <div style='text-align:center; margin-bottom:0.5rem;'>
        <span class='datetime-chip'>
            🕐 {now.strftime('%I:%M %p')} &nbsp;|&nbsp; 📅 {now.strftime('%A, %d %B %Y')}
        </span>
    </div>""", unsafe_allow_html=True)

    # Hero Banner
    st.markdown(f"""
    <div class='hero-banner'>
        <div class='hero-badge'>✅ Trusted · Fast · Reliable</div>
        <div class='hero-title'>📡 {SHOP_NAME}</div>
        <div class='hero-tagline'>✦ {TAGLINE} ✦</div>
        <div class='hero-welcome'>
            Welcome to <strong>{SHOP_NAME}</strong> — your one-stop digital service center
            in Narela, Delhi. From money transfers to government form filling,
            we make every service fast, easy, and affordable.
        </div>
        <div class='contact-strip'>
            <div class='contact-item'>📍 Gali No. 67B, Swatantra Nagar, Narela, Delhi – 110040</div>
            <div class='contact-item'>📞 {PHONE}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Action Buttons
    st.markdown(f"""
    <div class='btn-row'>
        <a class='btn-call' href='{CALL_LINK}'>📞 Call Now</a>
        <a class='btn-whatsapp' href='{WHATSAPP}' target='_blank'>💬 WhatsApp Us</a>
    </div>
    """, unsafe_allow_html=True)

    # Quick Services Preview (first 6)
    st.markdown("""
    <div class='section-heading'>
        <h2>Our Popular Services</h2>
        <div class='divider'></div>
        <p>Quick access to our most-used services</p>
    </div>""", unsafe_allow_html=True)

    cols = st.columns(3)
    for i, (icon, name, sub) in enumerate(SERVICES[:6]):
        with cols[i % 3]:
            st.markdown(f"""
            <div class='service-card'>
                <div class='service-icon'>{icon}</div>
                <div class='service-name'>{name}</div>
                <div class='service-sub'>{sub}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align:center; margin-top:0.5rem;'>
        <span style='color:#64748b; font-size:0.9rem;'>👆 See all 12+ services in the <strong>Services</strong> section</span>
    </div>""", unsafe_allow_html=True)


# ╔══════════════════════════════════════════════╗
# ║               SERVICES PAGE                  ║
# ╚══════════════════════════════════════════════╝
elif selected == "Services":

    st.markdown("""
    <div class='section-heading'>
        <h2>All Our Services</h2>
        <div class='divider'></div>
        <p>Everything digital & banking — right here in your neighbourhood</p>
    </div>""", unsafe_allow_html=True)

    cols = st.columns(3)
    for i, (icon, name, sub) in enumerate(SERVICES):
        with cols[i % 3]:
            st.markdown(f"""
            <div class='service-card'>
                <div class='service-icon'>{icon}</div>
                <div class='service-name'>{name}</div>
                <div class='service-sub'>{sub}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='btn-row' style='margin-top:1.5rem;'>
        <a class='btn-whatsapp' href='{WHATSAPP}' target='_blank'>💬 Ask on WhatsApp</a>
        <a class='btn-call' href='{CALL_LINK}'>📞 Call Us</a>
    </div>""", unsafe_allow_html=True)


# ╔══════════════════════════════════════════════╗
# ║               ABOUT US PAGE                  ║
# ╚══════════════════════════════════════════════╝
elif selected == "About Us":

    st.markdown("""
    <div class='section-heading'>
        <h2>About Us</h2>
        <div class='divider'></div>
        <p>Know us better — your trusted local service partner</p>
    </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown(f"""
        <div class='info-card'>
            <h3>📡 Who We Are</h3>
            <p>
                <strong>Ananya Communication</strong> is a trusted digital and banking
                service centre located in the heart of Swatantra Nagar, Narela, Delhi.
                We have been proudly serving our community by offering a wide range of
                essential digital services under one roof — so you never have to travel
                far for important tasks.
            </p>
            <br>
            <p>
                Whether you need to send money, recharge your phone, book train tickets,
                open a bank account, or update your Aadhaar card — we handle it all with
                speed, accuracy, and care.
            </p>
        </div>

        <div class='info-card'>
            <h3>🌟 Why Choose Us?</h3>
            <ul>
                <li>✅ <strong>Trusted Service</strong> — Hundreds of satisfied customers</li>
                <li>⚡ <strong>Fast Processing</strong> — Minimal waiting time</li>
                <li>💰 <strong>Affordable Charges</strong> — Best rates in the area</li>
                <li>🤝 <strong>Customer Friendly</strong> — We guide you every step</li>
                <li>🔒 <strong>Secure & Private</strong> — Your data stays safe with us</li>
                <li>📆 <strong>Open 7 Days</strong> — Here when you need us</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='info-card' style='background: linear-gradient(135deg, #1a3c6e, #0d9488); color:#fff; border:none;'>
            <h3 style='color:#f59e0b;'>📍 Find Us Here</h3>
            <p style='color:rgba(255,255,255,0.9);'>{ADDRESS.replace(chr(10), '<br>')}</p>
            <br>
            <p style='color:rgba(255,255,255,0.9);'>📞 <strong style='color:#f59e0b;'>{PHONE}</strong></p>
            <br>
            <p style='color:rgba(255,255,255,0.9);'>📧 <strong style='color:#f59e0b;'>{EMAIL}</strong></p>
            <br>
            <p style='color:rgba(255,255,255,0.75); font-size:0.85rem;'>
                🕐 Mon – Sun: 8:00 AM – 9:00 PM
            </p>
        </div>

        <div class='info-card'>
            <h3>🏆 Our Promise</h3>
            <div class='highlight-box' style='margin:0;'>
                "We treat every customer like family and every task like our own.
                Your satisfaction is our success."
            </div>
        </div>
        """, unsafe_allow_html=True)


# ╔══════════════════════════════════════════════╗
# ║               CONTACT PAGE                   ║
# ╚══════════════════════════════════════════════╝
elif selected == "Contact":

    st.markdown("""
    <div class='section-heading'>
        <h2>Contact Us</h2>
        <div class='divider'></div>
        <p>We'd love to hear from you — reach out anytime!</p>
    </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        # Contact Details Card
        st.markdown(f"""
        <div class='info-card'>
            <h3>📬 Get In Touch</h3>
            <div class='contact-detail'>
                <div class='contact-icon'>📍</div>
                <div>
                    <div class='contact-label'>Address</div>
                    <div class='contact-text'>{ADDRESS.replace(chr(10), '<br>')}</div>
                </div>
            </div>
            <div class='contact-detail'>
                <div class='contact-icon'>📞</div>
                <div>
                    <div class='contact-label'>Phone / WhatsApp</div>
                    <div class='contact-text'><strong>{PHONE}</strong></div>
                </div>
            </div>
            <div class='contact-detail'>
                <div class='contact-icon'>📧</div>
                <div>
                    <div class='contact-label'>Email</div>
                    <div class='contact-text'><a href='mailto:{EMAIL}' style='color:#0d9488;'>{EMAIL}</a></div>
                </div>
            </div>
            <div class='contact-detail'>
                <div class='contact-icon'>🕐</div>
                <div>
                    <div class='contact-label'>Working Hours</div>
                    <div class='contact-text'>Monday – Sunday<br>8:00 AM – 9:00 PM</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Action Buttons
        st.markdown(f"""
        <div class='btn-row' style='justify-content:flex-start;'>
            <a class='btn-call' href='{CALL_LINK}'>📞 Call Now</a>
            <a class='btn-whatsapp' href='{WHATSAPP}' target='_blank'>💬 WhatsApp</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Contact Form
        st.markdown("""<div class='info-card'><h3>📝 Send Us a Message</h3>""", unsafe_allow_html=True)

        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("👤 Your Name", placeholder="e.g. Rahul Sharma")
            phone = st.text_input("📞 Phone Number", placeholder="e.g. 98XXXXXXXX")
            message = st.text_area(
                "💬 Your Message",
                placeholder="e.g. I need help with Aadhaar update...",
                height=130,
            )
            submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)

            if submitted:
                if name.strip() and phone.strip() and message.strip():
                    st.success(f"✅ Thank you, **{name}**! We'll contact you on **{phone}** shortly.")
                    st.balloons()
                else:
                    st.warning("⚠️ Please fill in all fields before submitting.")

        st.markdown("</div>", unsafe_allow_html=True)

    # Google Maps
    st.markdown("""
    <div class='section-heading' style='margin-top:2.5rem;'>
        <h2>📍 Our Location</h2>
        <div class='divider'></div>
        <p>Gali No. 67B, Swatantra Nagar, Narela, Delhi – 110040</p>
    </div>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div style='border-radius:16px; overflow:hidden; box-shadow:0 8px 30px rgba(0,0,0,0.12); margin-bottom:1rem;'>
        <iframe
            src="{MAPS_EMBED}"
            width="100%"
            height="380"
            style="border:0; display:block;"
            allowfullscreen=""
            loading="lazy">
        </iframe>
    </div>""", unsafe_allow_html=True)


# ── Footer (always visible) ──────────────────────────────────
st.markdown(f"""
<div class='footer'>
    <strong>📡 {SHOP_NAME}</strong><br>
    Gali No. 67B, Near Bharat Mata Mandir, Swatantra Nagar, Narela, Delhi – 110040<br>
    📞 {PHONE} &nbsp;|&nbsp; 📧 {EMAIL} &nbsp;|&nbsp; 💬 WhatsApp Available<br><br>
    <span style='opacity:0.65; font-size:0.8rem;'>
        © {datetime.now().year} {SHOP_NAME}. All rights reserved. &nbsp;|&nbsp;
        Made with ❤️ for our valued customers.
    </span>
</div>
""", unsafe_allow_html=True)
