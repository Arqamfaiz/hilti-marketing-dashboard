"""
Hilti Online Marketing Dashboard
================================
A portfolio project demonstrating online marketing analytics, SEO auditing,
and campaign planning skills relevant to the Working Student Online
Marketing role at Hilti Deutschland AG.

Author: Arqam Faiz Siddiqui
Built: 2026
Stack: Python, Streamlit, Plotly, pandas

This dashboard combines:
  1. Marketing channel KPIs (12 months, 6 channels) calibrated to public
     B2B benchmarks (e.g. 36-43% open rate range for B2B email).
  2. A hands-on SEO audit of 10 real Hilti.de pages, with prioritised fixes.
  3. A keyword research view tied to Hilti's Nuron / Heavy-Duty launch.
  4. Newsletter A/B test results across customer segments
     (Tiefbau, Elektroinstallation, Bau, Site Manager).
  5. A content calendar mapped to active Hilti campaigns (Winterwochen,
     Heavy-Duty kabellos, ON!Track).

The KPI numbers are illustrative but plausibility-tested against published
B2B email benchmarks (HubSpot, MailerLite, Brevo 2024-2025). The SEO audit
metrics are illustrative; the page URLs are real Hilti.de paths.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ---------- Page configuration ----------
st.set_page_config(
    page_title="Hilti Online Marketing Dashboard",
    page_icon="HM",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a cleaner, marketing-flavoured look
st.markdown(
    """
    <style>
    .main-header {
        color: #D2051E;
        font-weight: 700;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #D2051E;
        margin-bottom: 1.5rem;
    }
    .insight-box {
        background-color: #FFF5F5;
        border-left: 4px solid #D2051E;
        padding: 1rem;
        border-radius: 0.3rem;
        margin: 1rem 0;
    }
    div[data-testid="metric-container"] {
        background-color: #FAFAFA;
        border-radius: 0.5rem;
        padding: 0.75rem;
        border: 1px solid #E5E5E5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Data loading ----------
DATA_DIR = Path(__file__).parent / "data"


@st.cache_data
def load_channel_kpis():
    df = pd.read_csv(DATA_DIR / "channel_kpis.csv")
    df["month"] = pd.to_datetime(df["month"])
    return df


@st.cache_data
def load_seo_audit():
    return pd.read_csv(DATA_DIR / "seo_audit.csv")


@st.cache_data
def load_keywords():
    return pd.read_csv(DATA_DIR / "keyword_research.csv")


@st.cache_data
def load_ab_tests():
    return pd.read_csv(DATA_DIR / "newsletter_ab_tests.csv")


@st.cache_data
def load_calendar():
    return pd.read_csv(DATA_DIR / "content_calendar.csv")


# ---------- Sidebar navigation ----------
with st.sidebar:
    st.markdown("### Navigation")
    section = st.radio(
        "Section",
        [
            "Channel Performance",
            "SEO Audit (Hilti.de)",
            "Keyword Research",
            "Newsletter A/B Tests",
            "Content Calendar",
        ],
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown("**About this project**")
    st.caption(
        "A portfolio dashboard built to demonstrate the day-to-day "
        "skills behind a Working Student Online Marketing role: "
        "SEO auditing, campaign analytics, newsletter testing, "
        "and editorial planning."
    )
    st.caption("Built by Arqam Faiz Siddiqui")

# ---------- Header ----------
st.markdown(
    "<h1 class='main-header'>Hilti Online Marketing Dashboard</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "An end-to-end view of digital marketing performance, SEO health, "
    "keyword opportunities, newsletter A/B testing, and content planning, "
    "framed around Hilti's active campaigns: the **Nuron Heavy-Duty kabellos** "
    "platform, **Winterwochen 2026**, and the **ON!Track** fleet management service."
)

with st.expander("Methodology and data sources"):
    st.markdown(
        """
        **What is real:**
        - Hilti.de page URLs and product/campaign names (Nuron, Heavy-Duty
          kabellos, ON!Track, Winterwochen) are pulled from the public
          Hilti Deutschland website.
        - Email benchmark ranges used to calibrate the newsletter data
          (open rates 22-43%, CTR 2-4%, unsubscribe under 0.5%) come from
          published 2024-2025 B2B email reports (HubSpot, MailerLite,
          Brevo, SalesHive).

        **What is illustrative:**
        - Specific traffic, conversion, A/B, and SEO score numbers are
          plausible illustrations, not real Hilti analytics. Real internal
          Hilti data is confidential.
        - Calibration target: numbers stay inside the ranges that public
          B2B email and SEO benchmarks consider normal-to-strong.

        **Why this exists:** The Working Student Online Marketing JD asks
        for exactly this combination of skills. This dashboard is the
        smallest honest version of that work I could ship in one weekend.
        """
    )

st.divider()

# ====================================================================
# SECTION 1: CHANNEL PERFORMANCE
# ====================================================================
if section == "Channel Performance":
    st.subheader("Channel Performance (12 months)")
    st.caption(
        "Multi-channel digital marketing performance. Useful for spotting "
        "which channels drive efficient traffic versus efficient leads."
    )

    df_kpi = load_channel_kpis()

    # Filters
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        all_channels = df_kpi["channel"].unique().tolist()
        selected_channels = st.multiselect(
            "Channels", options=all_channels, default=all_channels
        )
    with col_f2:
        date_range = st.select_slider(
            "Period",
            options=df_kpi["month"].dt.strftime("%Y-%m").unique().tolist(),
            value=(
                df_kpi["month"].dt.strftime("%Y-%m").min(),
                df_kpi["month"].dt.strftime("%Y-%m").max(),
            ),
        )

    df_view = df_kpi[
        (df_kpi["channel"].isin(selected_channels))
        & (df_kpi["month"] >= pd.to_datetime(date_range[0]))
        & (df_kpi["month"] <= pd.to_datetime(date_range[1]))
    ]

    # KPI strip
    total_sessions = df_view["sessions"].sum()
    total_leads = df_view["leads"].sum()
    total_cost = df_view["cost_eur"].sum()
    cost_per_lead = total_cost / total_leads if total_leads else 0
    avg_cvr = (total_leads / total_sessions * 100) if total_sessions else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Sessions", f"{total_sessions:,.0f}")
    c2.metric("Total Leads", f"{total_leads:,.0f}")
    c3.metric("Avg Conversion", f"{avg_cvr:.2f}%")
    c4.metric("Cost per Lead", f"€{cost_per_lead:.2f}" if total_cost else "Organic")

    # Sessions trend
    st.markdown("##### Sessions over time, by channel")
    fig_sessions = px.area(
        df_view,
        x="month",
        y="sessions",
        color="channel",
        template="plotly_white",
        labels={"month": "Month", "sessions": "Sessions", "channel": "Channel"},
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig_sessions.update_layout(
        height=380,
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=-0.3),
    )
    st.plotly_chart(fig_sessions, use_container_width=True)

    # Cost vs leads scatter
    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("##### Cost efficiency by channel")
        df_eff = (
            df_view.groupby("channel")
            .agg(
                sessions=("sessions", "sum"),
                leads=("leads", "sum"),
                cost=("cost_eur", "sum"),
            )
            .reset_index()
        )
        df_eff["cost_per_lead"] = df_eff.apply(
            lambda r: r["cost"] / r["leads"] if r["leads"] else 0, axis=1
        )
        fig_eff = px.bar(
            df_eff.sort_values("cost_per_lead"),
            x="cost_per_lead",
            y="channel",
            orientation="h",
            template="plotly_white",
            labels={"cost_per_lead": "Cost per Lead (EUR)", "channel": ""},
            color="cost_per_lead",
            color_continuous_scale="Reds",
        )
        fig_eff.update_layout(
            height=350, margin=dict(l=20, r=20, t=20, b=20), showlegend=False
        )
        st.plotly_chart(fig_eff, use_container_width=True)

    with col_right:
        st.markdown("##### Conversion rate by channel")
        df_cvr = (
            df_view.groupby("channel")
            .agg(cvr=("conversion_rate_pct", "mean"))
            .reset_index()
            .sort_values("cvr", ascending=True)
        )
        fig_cvr = px.bar(
            df_cvr,
            x="cvr",
            y="channel",
            orientation="h",
            template="plotly_white",
            labels={"cvr": "Conversion Rate (%)", "channel": ""},
            color="cvr",
            color_continuous_scale="Greens",
        )
        fig_cvr.update_layout(
            height=350, margin=dict(l=20, r=20, t=20, b=20), showlegend=False
        )
        st.plotly_chart(fig_cvr, use_container_width=True)

    st.markdown(
        """
        <div class='insight-box'>
        <b>Insight:</b> Email Newsletter delivers the highest conversion rate
        in the dataset (around 4% on average). Organic Search is the volume
        leader and zero-cost. Paid channels (Google Ads, LinkedIn Ads) drive
        leads at a comparable cost per lead, suggesting room to test
        reallocating budget toward whichever has stronger downstream pipeline
        impact, which CRM data would clarify.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ====================================================================
# SECTION 2: SEO AUDIT
# ====================================================================
elif section == "SEO Audit (Hilti.de)":
    st.subheader("SEO Audit: Hilti Deutschland Pages")
    st.caption(
        "A hands-on technical SEO audit of 10 real Hilti.de pages. "
        "Each page is scored on content, on-page elements, and Core Web "
        "Vitals, with a recommended priority fix."
    )

    df_seo = load_seo_audit()

    # KPI strip
    avg_score = df_seo["seo_score"].mean()
    pages_below_70 = (df_seo["seo_score"] < 70).sum()
    avg_mobile_speed = df_seo["page_speed_mobile"].mean()
    pages_no_h1 = (df_seo["h1_present"] == "No").sum()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Avg SEO Score", f"{avg_score:.1f}/100")
    c2.metric("Pages Below 70", f"{pages_below_70}", delta_color="inverse")
    c3.metric("Avg Mobile Speed", f"{avg_mobile_speed:.0f}/100")
    c4.metric("Missing H1 Tags", f"{pages_no_h1}", delta_color="inverse")

    # Score distribution
    st.markdown("##### SEO score by page (sorted)")
    df_seo_sorted = df_seo.sort_values("seo_score", ascending=True)
    fig_scores = go.Figure()
    fig_scores.add_trace(
        go.Bar(
            y=df_seo_sorted["page_url"].str.replace("/de/de", ""),
            x=df_seo_sorted["seo_score"],
            orientation="h",
            marker=dict(
                color=df_seo_sorted["seo_score"],
                colorscale="RdYlGn",
                cmin=50,
                cmax=100,
            ),
            text=df_seo_sorted["seo_score"],
            textposition="outside",
            hovertemplate=(
                "<b>%{y}</b><br>SEO Score: %{x}<br>"
                "<extra></extra>"
            ),
        )
    )
    fig_scores.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis_title="SEO Score (0-100)",
        yaxis_title="",
    )
    st.plotly_chart(fig_scores, use_container_width=True)

    # Performance scatter
    st.markdown("##### Page speed vs SEO score")
    st.caption(
        "Top-right quadrant is the goal. Bottom-left pages need work on "
        "both technical performance and content."
    )
    fig_speed = px.scatter(
        df_seo,
        x="page_speed_mobile",
        y="seo_score",
        size="word_count",
        color="seo_score",
        color_continuous_scale="RdYlGn",
        hover_data=["page_url", "target_keyword", "priority_fix"],
        labels={
            "page_speed_mobile": "Mobile PageSpeed (0-100)",
            "seo_score": "SEO Score (0-100)",
        },
        template="plotly_white",
    )
    fig_speed.add_hline(y=75, line_dash="dash", line_color="grey", opacity=0.5)
    fig_speed.add_vline(x=70, line_dash="dash", line_color="grey", opacity=0.5)
    fig_speed.update_layout(
        height=420, margin=dict(l=20, r=20, t=20, b=20), showlegend=False
    )
    st.plotly_chart(fig_speed, use_container_width=True)

    # Detailed audit table
    st.markdown("##### Page-by-page audit findings")
    display_cols = [
        "page_url",
        "target_keyword",
        "word_count",
        "page_speed_mobile",
        "images_with_alt_pct",
        "seo_score",
        "priority_fix",
    ]
    st.dataframe(
        df_seo[display_cols].sort_values("seo_score", ascending=True),
        use_container_width=True,
        hide_index=True,
        column_config={
            "page_url": "URL Path",
            "target_keyword": "Target Keyword",
            "word_count": st.column_config.NumberColumn("Words", format="%d"),
            "page_speed_mobile": st.column_config.ProgressColumn(
                "Mobile Speed", min_value=0, max_value=100, format="%d"
            ),
            "images_with_alt_pct": st.column_config.NumberColumn(
                "Alt Tags %", format="%d%%"
            ),
            "seo_score": st.column_config.ProgressColumn(
                "SEO Score", min_value=0, max_value=100, format="%d"
            ),
            "priority_fix": "Recommended Fix",
        },
    )

    st.markdown(
        """
        <div class='insight-box'>
        <b>Top 3 priority fixes:</b><br>
        1. <b>SSM 22 product page</b> is missing an H1 tag, the single
        easiest on-page win to ship.<br>
        2. <b>Akku Abbruchhammer page</b> has thin content (690 words) on a
        commercial keyword with 3,600 monthly searches; expanding the page
        to 1,400+ words and adding internal links from the Heavy-Duty hub
        is the highest-ROI content move.<br>
        3. <b>Nuron Akku-Plattform page</b> mobile speed is at 68; image
        compression and lazy-loading would push this above the 75 threshold.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ====================================================================
# SECTION 3: KEYWORD RESEARCH
# ====================================================================
elif section == "Keyword Research":
    st.subheader("Keyword Research: Heavy-Duty kabellos Cluster")
    st.caption(
        "Keyword opportunities for Hilti's Nuron and Heavy-Duty product "
        "lines, scored by search volume, current rank, and competition."
    )

    df_kw = load_keywords()

    # KPI strip
    total_volume = df_kw["monthly_search_volume"].sum()
    avg_rank = df_kw["current_rank"].mean()
    quick_wins = df_kw[
        (df_kw["current_rank"] <= 10) & (df_kw["current_rank"] > df_kw["target_rank"])
    ].shape[0]

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Monthly Volume", f"{total_volume:,}")
    c2.metric("Avg Current Rank", f"{avg_rank:.1f}")
    c3.metric("Quick-Win Keywords", f"{quick_wins}")

    # Opportunity scatter
    st.markdown("##### Keyword opportunity map")
    st.caption(
        "Bigger dots = higher search volume. Top-left quadrant (low difficulty, "
        "high opportunity) is where to focus first."
    )
    fig_kw = px.scatter(
        df_kw,
        x="keyword_difficulty",
        y="opportunity_score",
        size="monthly_search_volume",
        color="intent",
        hover_data=["keyword", "current_rank", "target_rank"],
        labels={
            "keyword_difficulty": "Keyword Difficulty (0-100)",
            "opportunity_score": "Opportunity Score (0-100)",
            "intent": "Intent",
        },
        template="plotly_white",
    )
    fig_kw.update_layout(
        height=420,
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=-0.25),
    )
    st.plotly_chart(fig_kw, use_container_width=True)

    # Keyword table
    st.markdown("##### Keyword priority table")
    st.dataframe(
        df_kw.sort_values("opportunity_score", ascending=False),
        use_container_width=True,
        hide_index=True,
        column_config={
            "keyword": "Keyword",
            "monthly_search_volume": st.column_config.NumberColumn(
                "Volume / mo", format="%d"
            ),
            "keyword_difficulty": st.column_config.ProgressColumn(
                "Difficulty", min_value=0, max_value=100, format="%d"
            ),
            "current_rank": "Current Rank",
            "target_rank": "Target Rank",
            "intent": "Intent",
            "opportunity_score": st.column_config.ProgressColumn(
                "Opportunity", min_value=0, max_value=100, format="%d"
            ),
        },
    )

# ====================================================================
# SECTION 4: NEWSLETTER A/B TESTS
# ====================================================================
elif section == "Newsletter A/B Tests":
    st.subheader("Newsletter A/B Test Results")
    st.caption(
        "A/B test outcomes across customer segments. Open rates, CTR, and "
        "unsubscribe rates calibrated against published 2024-2025 B2B email "
        "benchmarks (open ~36-43%, CTR ~2-4%, unsubscribe under 0.5%)."
    )

    df_ab = load_ab_tests()
    df_ab["open_rate"] = (df_ab["opens"] / df_ab["sent"] * 100).round(2)
    df_ab["ctr"] = (df_ab["clicks"] / df_ab["sent"] * 100).round(2)
    df_ab["unsub_rate"] = (df_ab["unsubscribes"] / df_ab["sent"] * 100).round(3)

    # KPI strip
    avg_open = df_ab["open_rate"].mean()
    avg_ctr = df_ab["ctr"].mean()
    avg_unsub = df_ab["unsub_rate"].mean()
    total_sent = df_ab["sent"].sum()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Avg Open Rate", f"{avg_open:.1f}%", help="B2B benchmark: 36-43%")
    c2.metric("Avg CTR", f"{avg_ctr:.2f}%", help="B2B benchmark: 2-4%")
    c3.metric("Avg Unsub Rate", f"{avg_unsub:.2f}%", help="Healthy: under 0.5%")
    c4.metric("Total Emails Sent", f"{total_sent:,}")

    # Subject line winners
    st.markdown("##### Subject line winners by campaign")
    df_winners = (
        df_ab.groupby(["campaign_name", "subject_line_variant"])
        .agg(open_rate=("open_rate", "mean"), ctr=("ctr", "mean"))
        .reset_index()
    )
    fig_subj = px.bar(
        df_winners,
        x="campaign_name",
        y="open_rate",
        color="subject_line_variant",
        barmode="group",
        template="plotly_white",
        labels={
            "campaign_name": "Campaign",
            "open_rate": "Open Rate (%)",
            "subject_line_variant": "Subject Line",
        },
        color_discrete_sequence=["#D2051E", "#666666"],
    )
    fig_subj.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis_tickangle=-25,
        legend=dict(orientation="h", yanchor="bottom", y=-0.5),
    )
    st.plotly_chart(fig_subj, use_container_width=True)

    # Segment heatmap
    st.markdown("##### Open rate by segment and campaign")
    pivot = df_ab.pivot_table(
        index="campaign_name", columns="segment", values="open_rate", aggfunc="mean"
    )
    fig_heat = go.Figure(
        data=go.Heatmap(
            z=pivot.values,
            x=pivot.columns,
            y=pivot.index,
            colorscale="Reds",
            text=pivot.values.round(1),
            texttemplate="%{text}%",
            colorbar=dict(title="Open %"),
        )
    )
    fig_heat.update_layout(
        height=380, margin=dict(l=20, r=20, t=20, b=20), template="plotly_white"
    )
    st.plotly_chart(fig_heat, use_container_width=True)

    st.markdown(
        """
        <div class='insight-box'>
        <b>What the data says:</b><br>
        - Specific, value-led subject lines (<i>"Bis zu 30 Prozent sparen"</i>,
        <i>"5 Werkzeuge die Ihre Baustelle veraendern"</i>) outperform generic
        announcements on click-through.<br>
        - The <i>Elektroinstallation</i> segment responds better to product-
        discovery framing; <i>Tiefbau</i> responds better to direct value/saving
        messages.<br>
        - Unsubscribe rates stay under 0.4% across all campaigns, well within
        the healthy B2B range.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ====================================================================
# SECTION 5: CONTENT CALENDAR
# ====================================================================
elif section == "Content Calendar":
    st.subheader("Content Calendar: Q1-Q2 2026")
    st.caption(
        "10-week editorial plan tied to Hilti's active campaigns: "
        "Heavy-Duty kabellos, Winterwochen 2026, ON!Track."
    )

    df_cal = load_calendar()

    # Status overview
    status_counts = df_cal["status"].value_counts()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Articles Live", status_counts.get("Live", 0))
    c2.metric("In Draft", status_counts.get("Draft", 0))
    c3.metric("In Planning", status_counts.get("Planning", 0))
    c4.metric("Critical Priority", (df_cal["priority"] == "Critical").sum())

    # Calendar table
    st.markdown("##### 10-week editorial plan")
    st.dataframe(
        df_cal,
        use_container_width=True,
        hide_index=True,
        column_config={
            "week": "Week",
            "article_title_de": "Article Title (DE)",
            "target_keyword": "Target Keyword",
            "channel": "Channel",
            "status": st.column_config.SelectboxColumn(
                "Status", options=["Live", "Draft", "Planning"]
            ),
            "word_count_target": st.column_config.NumberColumn(
                "Target Words", format="%d"
            ),
            "priority": st.column_config.SelectboxColumn(
                "Priority", options=["Critical", "High", "Medium", "Low"]
            ),
        },
    )

    # Status by priority chart
    st.markdown("##### Editorial pipeline by status and priority")
    df_pipeline = df_cal.groupby(["status", "priority"]).size().reset_index(name="count")
    fig_pipe = px.bar(
        df_pipeline,
        x="status",
        y="count",
        color="priority",
        template="plotly_white",
        labels={"status": "Status", "count": "Articles", "priority": "Priority"},
        color_discrete_sequence=["#D2051E", "#FF6B6B", "#FFA94D", "#A0A0A0"],
        barmode="stack",
    )
    fig_pipe.update_layout(
        height=380,
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=-0.3),
    )
    st.plotly_chart(fig_pipe, use_container_width=True)

# ---------- Footer ----------
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: #888; font-size: 0.85em; padding-top: 1em;'>
    Built by Arqam Faiz Siddiqui as a portfolio project for the Hilti Working
    Student Online Marketing application. <br>
    Not affiliated with or endorsed by Hilti AG. KPI ranges calibrated to
    public B2B benchmarks; Hilti.de page paths are real, audit metrics are illustrative.
    </div>
    """,
    unsafe_allow_html=True,
)
