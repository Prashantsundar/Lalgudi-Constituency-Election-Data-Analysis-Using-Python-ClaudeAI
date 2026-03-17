Lalgudi Constituency Election Data Analysis  This project analyzes voter demographic data from the Lalgudi Assembly Constituency electoral roll published by the Election Commission of India.
The project demonstrates a complete data analytics workflow, transforming unstructured electoral roll PDFs into interactive analytical dashboard
# 🗳️ Lalgudi Constituency 2021 Election Dashboard

An interactive, offline-ready election results dashboard and printable report
for the **143 — Lalgudi Assembly Constituency**, Tamil Nadu Legislative Assembly
Election 2021 (TNLA-2021).

---

## 📌 About This Project

This project transforms raw Election Commission of India polling data for the
Lalgudi constituency into two deliverables:

- **Interactive HTML Dashboard** — fully offline, works in any browser
- **Printable PDF Report** — professional hard-copy document for circulation

Built entirely using open data from the Election Commission of India.

---

## 🏛️ Constituency Overview

| Detail | Info |
|---|---|
| Constituency No. | 143 |
| Name | Lalgudi |
| District | Tiruchirappalli, Tamil Nadu |
| Election | TNLA 2021 — April 6, 2021 |
| Total Electors | 2,18,131 |
| Polling Stations | 300 |
| Candidates | 14 |
| Voter Turnout | 79.1% |

---

## 🏆 Key Results

| Party | Candidate | Votes | Vote Share |
|---|---|---|---|
| **DMK** ✅ | A. Soundarapandian | **83,264** | **48.3%** |
| AIADMK | D.R. Dharmaraj | 67,612 | 39.2% |
| NTK | I. Malar Tamil Prabha | 16,134 | 9.4% |
| AMMK | M. Vijayamurthy | 2,913 | 1.7% |
| Others | — | 2,666 | 1.4% |

**Win Margin: 15,652 votes (DMK over AIADMK)**

---

## 📁 Repository Structure
```
lalgudi-2021-election/
│
├── data/
│   └── lalgudi_2021_poll.xlsx        # Raw polling station data (ECI)
│
├── dashboard/
│   └── lalgudi_2021_dashboard_v5.html  # Interactive offline dashboard
│
├── report/
│   └── lalgudi_2021_report.pdf       # Printable hard-copy report
│
├── assets/
│   ├── LALGUDI_map.png               # Constituency map
│   ├── DMK.png                       # DMK party flag
│   ├── AIADMK_FLAG.png               # AIADMK party flag
│   ├── NTK_FLAG.jpg                  # NTK party flag
│   └── AMMK_FLAG.jpg                 # AMMK party flag
│
└── README.md
```

---

## 🖥️ Dashboard Features

- 🗺️ **Lalgudi constituency map** as background watermark
- 🏳️ **Real party flags** for DMK, AIADMK, NTK, AMMK
- 📊 **Party-wise vote share** bar chart
- 🍩 **Station-level winners** donut chart
- 📈 **DMK vs AIADMK** votes across all stations
- 🔍 **Polling station explorer** — search and filter all 300 stations
- 📋 **All party columns** — DMK, AIADMK, NTK, AMMK, SMNK, others
- 🏆 **Closest contests** — top 20 stations by smallest margin
- 📊 **Highest turnout** stations — stacked bar chart
- 👥 **All 14 candidates** results chart
- ✅ Works **100% offline** — no internet required after download
- 📱 **Mobile friendly** — works on phones, tablets, and desktops

---

## 📄 PDF Report Contents

| Page | Content |
|---|---|
| 1 | Cover page with constituency map and key results |
| 2 | Preface — about Lalgudi, key facts table |
| 3 | Full candidate results table + party flags with votes |
| 4–N | All 300 polling station data (station-wise breakdown) |
| Last | Conclusion and political analysis |

---

## 🚀 How to Use

### Interactive Dashboard
1. Download `lalgudi_2021_dashboard_v5.html`
2. Open in any browser — Chrome, Firefox, Safari, Edge
3. No installation or internet required
4. Share via WhatsApp, email, USB drive, or Google Drive

### Printable Report
1. Download `lalgudi_2021_report.pdf`
2. Open in any PDF viewer
3. Print at A4 size for best results
4. Recommended: print double-sided to save paper

---

## 🛠️ Built With

- **Python** — data processing and PDF generation
- **Pandas** — Excel data extraction and analysis
- **ReportLab** — PDF report generation
- **Chart.js** — interactive charts in the dashboard
- **HTML / CSS / JavaScript** — dashboard frontend
- **Claude (Anthropic)** — AI-assisted development

---

## 📊 Data Source

- **Election Commission of India** — official polling station results
- Constituency: 143 — Lalgudi, Tiruchirappalli District
- Election: 17th Tamil Nadu Legislative Assembly, 2021
- Data verified against official ECI published results

---

## 📜 License

This project uses publicly available election data from the Election Commission
of India. The code, dashboard, and report are free to use for research,
education, and public awareness purposes.

---

## 🙏 Acknowledgements

- Election Commission of India for transparent public data
- The voters of Lalgudi constituency
- Open source libraries: Chart.js, ReportLab, Pandas

---

*Prepared for public circulation · March 2026*
*143 — Lalgudi Assembly Constituency · TNLA 2021*
