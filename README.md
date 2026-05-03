# Hilti Online Marketing Dashboard

An interactive portfolio project demonstrating online marketing analytics,
SEO auditing, keyword research, newsletter A/B testing, and editorial
planning. Built specifically to support an application for the
**Working Student Online Marketing (m/f/d)** role at Hilti Deutschland AG.

**Live demo:** https://hilti-marketing-dashboard-zgbevrqzomsnujzaskke3i.streamlit.app/

---

## What this dashboard contains

Five interactive sections, navigated from the sidebar:

1. **Channel Performance** - 12 months of multi-channel KPIs (Organic
   Search, Google Ads, Email Newsletter, LinkedIn Organic, LinkedIn Ads,
   Direct), with cost-per-lead and conversion-rate views.
2. **SEO Audit (Hilti.de)** - A hands-on technical SEO audit of 10 real
   Hilti.de pages, scored on content depth, on-page elements, mobile
   speed, and image alt coverage, with a recommended priority fix per page.
3. **Keyword Research** - Opportunity mapping for the Heavy-Duty kabellos
   and Nuron product clusters, with a difficulty-vs-opportunity scatter
   and a quick-win priority table.
4. **Newsletter A/B Tests** - Subject line A/B test results across four
   customer segments (Tiefbau, Elektroinstallation, Bau, Site Manager),
   with open rates calibrated to the 36-43% B2B benchmark range.
5. **Content Calendar** - A 10-week editorial plan tied to Hilti's active
   campaigns: Heavy-Duty kabellos, Winterwochen 2026, ON!Track.

---

## Why these five sections

The Working Student Online Marketing JD lists, almost verbatim:

> "creation and distribution of newsletters, content creation,
> implementation of SEO measures, conception, planning, implementation
> and evaluation of campaigns"

Each section maps to one of those activities. The dashboard is the
smallest honest version of that work, end to end.

---

## Data sources

**What is real:**

- **Hilti.de page URLs and product/campaign names**  Nuron, Heavy-Duty
  kabellos, ON!Track, Winterwochen, SSM 22, Diamantbohrer,  pulled from
  the public Hilti Germany website.
- **B2B email benchmark ranges** used to calibrate the newsletter data:
  open rates 36-43% (HubSpot, MailerLite, Brevo 2024-2025), CTR 2-4%,
  unsubscribe under 0.5%.

**What is illustrative:**

- Specific traffic, cost, conversion, and SEO score numbers. Real
  internal Hilti analytics are confidential. Numbers are calibrated so
  they fall inside the published B2B benchmark ranges.

The dashboard flags this clearly in its **Methodology** expander and in
the footer.

---

## Local setup

Tested on Python 3.10+. If you don't have Python, install it from
[python.org](https://www.python.org/downloads/) and tick "Add Python to PATH".

```bash
git clone https://github.com/<your-username>/hilti-marketing-dashboard.git
cd hilti-marketing-dashboard

python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

The dashboard opens in your browser at `http://localhost:8501`.

---

## Project structure

```
hilti-marketing-dashboard/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Three dependencies
├── README.md                       # This file
├── .gitignore
└── data/
    ├── channel_kpis.csv            # 72 rows, 6 channels x 12 months
    ├── seo_audit.csv               # 10 real Hilti.de pages, scored
    ├── keyword_research.csv        # 15 keywords, difficulty + opportunity
    ├── newsletter_ab_tests.csv     # 16 A/B test variants
    └── content_calendar.csv        # 10-week editorial plan
```

---

## Honest limitations

- **The SEO audit numbers are illustrative.** A real audit would use
  Screaming Frog, Google PageSpeed Insights, and Search Console data.
  The audit logic and prioritisation framework are real; the specific
  scores are not. Mentioning this openly is the only honest way to
  present this work.
- **Hilti's actual traffic and conversion data is confidential.** This
  dashboard does not claim to know it. The ranges are calibrated to
  public B2B benchmarks so a recruiter can sanity-check that the
  framework is sound.
- **Subject line variants in the A/B test data are realistic guesses,
  not actual Hilti newsletters.** They draw on Hilti's known German
  campaign language ("Heavy-Duty ist jetzt kabellos", "Jetzt
  Winterangebot sichern") to feel authentic.

---

## About the author

Built by **Arqam Faiz Siddiqui**, M.Sc. International Information Systems
candidate at FAU Erlangen-Nürnberg, with a Business Administration
background and prior marketing experience including SEO work at
Qist Bazaar (50+ web pages, 25% organic traffic growth) and KPI
dashboarding at GSK across 55,000+ outlets.

Not affiliated with or endorsed by Hilti AG.
