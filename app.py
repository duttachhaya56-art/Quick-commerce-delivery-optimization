import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="DeliverX - Quick-Commerce Intelligence",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for Professional SaaS Look & Perfect Spacing
st.markdown("""
    <style>
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    .metric-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    .metric-title {
        color: #94A3B8;
        font-size: 13px;
        font-weight: 500;
    }
    .metric-value {
        color: #F8FAFC;
        font-size: 24px;
        font-weight: 700;
        margin-top: 4px;
    }
    .card-container {
        background-color: #1E293B;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #334155;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 2. Sidebar Navigation (SaaS Style)
with st.sidebar:
    st.markdown("### 🚀 DeliverX")
    st.markdown("---")
    st.markdown("🏠 **Dashboard**")
    st.markdown("📦 Orders")
    st.markdown("🚚 Dispatch")
    st.markdown("👥 Drivers")
    st.markdown("🛍️ Customers")
    st.markdown("📈 Analytics")
    st.markdown("📋 Reports")
    st.markdown("💰 Finance")
    st.markdown("🔌 Integrations")
    st.markdown("⚙️ Settings")
    st.markdown("---")
    st.info("System Status: Operational 🟢")

# 3. Top Header Bar
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("## Good morning, Chhaya! 👋")
    st.caption("Here's what's happening with your quick-commerce operations today.")
with col_h2:
    st.markdown("<div style='text-align: right; color: #38BDF8; font-size: 14px; padding-top: 10px;'>📅 May 20, 2026 &nbsp;|&nbsp; 🟢 Live</div>", unsafe_allow_html=True)

st.markdown("<hr style='border-color: #334155; margin: 10px 0 20px 0;'>", unsafe_allow_html=True)

# 4. Top 5 Glowing KPI Metric Cards
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Total Orders</div>
            <div class="metric-value">12,548</div>
            <span style="color: #38BDF8; font-size: 12px;">+100% vs yesterday</span>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Delivered</div>
            <div class="metric-value">9,842</div>
            <span style="color: #4ADE80; font-size: 12px;">+21.5% vs yesterday</span>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-title">In Transit</div>
            <div class="metric-value">2,168</div>
            <span style="color: #FB923C; font-size: 12px;">-4.2% optimized</span>
        </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-title">On-Time Delivery</div>
            <div class="metric-value">96.8%</div>
            <span style="color: #C084FC; font-size: 12px;">+1.2% vs yesterday</span>
        </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Revenue</div>
            <div class="metric-value">₹24.8L</div>
            <span style="color: #F472B6; font-size: 12px;">+14.0% vs yesterday</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 5. Middle Section: Operational Overview & Live Map Tracking & Live Operations Stream
col_mid1, col_mid2, col_mid3 = st.columns([1.3, 1.1, 0.9])

with col_mid1:
    st.markdown("### 📈 Operational Overview")
    chart_data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Orders": [4200, 5800, 7500, 9200, 8800, 11000, 12548],
        "Delivered": [3900, 5200, 6800, 8500, 8100, 10200, 9842]
    })
    fig = px.area(chart_data, x="Day", y=["Orders", "Delivered"], color_discrete_sequence=["#38BDF8", "#4ADE80"])
    fig.update_layout(
        paper_bgcolor="#1E293B", plot_bgcolor="#1E293B",
        font=dict(color="#F8FAFC", size=11),
        margin=dict(l=10, r=10, t=10, b=10), height=240,
        legend=dict(orientation="h", y=1.1, x=0.5)
    )
    st.plotly_chart(fig, use_container_width=True)

with col_mid2:
    st.markdown("### 🗺️ Live Map Tracking")
    st.markdown("""
        <div class="card-container" style="height: 240px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <p style="color: #38BDF8; font-weight: 600; margin: 0 0 8px 0;">📍 Dark Store #DS-Delhi-04 Active</p>
                <p style="color: #4ADE80; font-size: 13px; margin: 0 0 6px 0;">🛵 Rider #4387 en route (ETA: 4m)</p>
                <p style="color: #FB923C; font-size: 13px; margin: 0 0 6px 0;">⚡ Batch Routing Optimized: ON</p>
            </div>
            <div style="background: #0F172A; padding: 8px; border-radius: 8px; text-align: center; color: #94A3B8; font-size: 12px;">
                Network Load: Optimal &nbsp;|&nbsp; Latency: 18ms
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_mid3:
    st.markdown("### ⚡ Live Operations")
    st.markdown("""
        <div class="card-container" style="height: 240px; font-size: 12.5px; overflow-y: auto;">
            <p style="color: #4ADE80; margin: 0 0 10px 0;">● Order #4387 Delivered <br><small style="color:#94A3B8;">2 mins ago</small></p>
            <p style="color: #38BDF8; margin: 0 0 10px 0;">● Order #4388 Dispatched <br><small style="color:#94A3B8;">5 mins ago</small></p>
            <p style="color: #FB923C; margin: 0 0 10px 0;">● Driver Rerouted (Traffic)</p>
            <p style="color: #C084FC; margin: 0;">● Stock Refilled SKU-99</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Bottom Section: Donut Distribution, Top Drivers & Revenue Trend
b1, b2, b3 = st.columns(3)

with b1:
    st.markdown("### 🍩 Order Status Distribution")
    status_df = pd.DataFrame({
        "Status": ["Delivered", "In Transit", "Delayed", "Failed"],
        "Count": [9842, 2168, 450, 88]
    })
    fig_donut = px.pie(status_df, names="Status", values="Count", hole=0.6, color_discrete_sequence=["#4ADE80", "#38BDF8", "#FB923C", "#F43F5E"])
    fig_donut.update_layout(
        paper_bgcolor="#1E293B", plot_bgcolor="#1E293B",
        font=dict(color="#F8FAFC", size=11),
        margin=dict(l=10, r=10, t=10, b=10), height=220,
        legend=dict(orientation="h", y=-0.1, x=0.1)
    )
    st.plotly_chart(fig_donut, use_container_width=True)

with b2:
    st.markdown("### ⭐ Top Performing Drivers")
    st.markdown("""
        <div class="card-container" style="height: 220px; font-size: 13px;">
            <div style="display:flex; justify-content:space-between; margin-bottom:12px; padding-bottom:6px; border-bottom:1px solid #334155;"><span>👤 Amit Sharma</span><span style="color:#4ADE80; font-weight:600;">142 deliveries</span></div>
            <div style="display:flex; justify-content:space-between; margin-bottom:12px; padding-bottom:6px; border-bottom:1px solid #334155;"><span>👤 Rahul Singh</span><span style="color:#38BDF8; font-weight:600;">135 deliveries</span></div>
            <div style="display:flex; justify-content:space-between; margin-bottom:12px; padding-bottom:6px; border-bottom:1px solid #334155;"><span>👤 Rakesh Kumar</span><span style="color:#C084FC; font-weight:600;">128 deliveries</span></div>
            <div style="display:flex; justify-content:space-between;"><span>👤 Sunita Patel</span><span style="color:#F472B6; font-weight:600;">120 deliveries</span></div>
        </div>
    """, unsafe_allow_html=True)

with b3:
    st.markdown("### 📊 Revenue Analytics Trend")
    rev_data = pd.DataFrame({
        "Date": [f"May {i}" for i in range(1, 9)],
        "Revenue": [1.2, 1.5, 1.8, 2.4, 3.1, 3.8, 4.5, 5.2]
    })
    fig_bar = px.bar(rev_data, x="Date", y="Revenue", color_discrete_sequence=["#C084FC"])
    fig_bar.update_layout(
        paper_bgcolor="#1E293B", plot_bgcolor="#1E293B",
        font=dict(color="#F8FAFC", size=11),
        margin=dict(l=10, r=10, t=10, b=10), height=220
    )
    st.plotly_chart(fig_bar, use_container_width=True)