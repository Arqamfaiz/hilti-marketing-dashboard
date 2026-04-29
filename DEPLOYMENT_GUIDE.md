# Quick Deployment Guide (Hilti Dashboard)

You have already deployed the Infineon dashboard, so this is the same
workflow with a fresh repo. Estimated time: **20-30 minutes**, much faster
than the first one.

---

## Step 1: Upload to GitHub (10 min)

1. Go to <https://github.com/new>
2. Repository name: `hilti-marketing-dashboard`
3. Description: `Online marketing analytics, SEO audit, and content planning dashboard for Hilti Germany`
4. **Public**, no extra files (README/license/gitignore unchecked)
5. Click **Create repository**

### Upload the files

On the new repo page, click the **"uploading an existing file"** link.

1. Open File Explorer to your unzipped `hilti_dashboard` folder.
2. Select `app.py`, `requirements.txt`, `README.md`, and `.gitignore`
   (skip the `data` folder for now).
3. Drag them into the GitHub upload box.
4. Scroll down, type `Initial upload`, click **Commit changes**.

### Add the data folder (one file at a time)

For each of the 5 CSV files, repeat:

1. **Add file → Create new file**
2. Filename: `data/channel_kpis.csv` (then `data/seo_audit.csv`, etc.)
   — type just **one** `data/`, not `data/data/`
3. Open the matching file in **Notepad**, `Ctrl+A`, `Ctrl+C`
4. Paste into the GitHub editor with `Ctrl+V`
5. Scroll down, click **Commit changes**

The 5 CSV files to upload:
- `channel_kpis.csv`
- `seo_audit.csv`
- `keyword_research.csv`
- `newsletter_ab_tests.csv`
- `content_calendar.csv`

### Verify

Go to `https://github.com/YOUR-USERNAME/hilti-marketing-dashboard/tree/main/data`

You should see exactly 5 CSV files inside one `data` folder.

---

## Step 2: Deploy to Streamlit Cloud (5 min)

1. Go to <https://share.streamlit.io>
2. Click **Create app** → **Deploy a public app from GitHub**
3. Repository: `YOUR-USERNAME/hilti-marketing-dashboard`
4. Branch: `main`
5. Main file path: `app.py`
6. Click **Deploy**

Wait 2-4 minutes for the "in the oven" build. Done.

---

## Step 3: Update your CV

In your CV's PROJECTS section, **replace** the Infineon project entry with:

```latex
\resumeOneRowHeading{Hilti Online Marketing Dashboard \;|\; \href{YOUR-STREAMLIT-URL}{\underline{Dashboard}} \;|\; \href{https://github.com/YOUR-USERNAME/hilti-marketing-dashboard}{\underline{GitHub}}}{\textit{2026 | Self-initiated}}
\resumeItemListStart
\resumeItem{Built an interactive Python and Streamlit marketing dashboard covering channel KPIs, on-page SEO audit of 10 real Hilti.de pages, and editorial planning around the Heavy-Duty kabellos and Winterwochen campaigns.}
\resumeItem{Designed newsletter A/B tests across customer segments (Tiefbau, Elektroinstallation) with open rates calibrated to published 2024-2025 B2B email benchmarks.}
\resumeItemListEnd
```

Replace `YOUR-STREAMLIT-URL` and `YOUR-USERNAME` with the actual values.

---

## What to say in the interview

> "Hilti's job description listed five things: SEO measures, content
> creation, newsletters, campaign planning, and campaign evaluation. I
> wanted to show I could do all five, so I built a dashboard with one
> section for each. The Hilti.de URLs in the SEO audit are real, and the
> email benchmark ranges come from public 2024-2025 reports. The
> internal Hilti numbers are obviously not real, and I labelled that
> clearly. It took an evening, and the goal was to give you something
> to react to in an interview, not a finished consulting deliverable."

That's the honest answer. It tends to land well.
