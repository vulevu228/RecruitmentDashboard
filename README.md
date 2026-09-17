# 🏢 Corporate Recruitment & Job Application Analytics Dashboard

Power BI + Azure Maps dashboard over a year of raw job applications (`data/job_application.xlsx`, 32,596 rows), tracking pipeline volume, hiring rate, and application-channel friction.

## 📊 Power BI Report
*Open `dashboard/job-application-data.pbix` in Power BI Desktop for the full interactive report, including the Azure Maps geographic view.*

![Total Applications KPI Card](dashboard/total_applications.png)
![Easy Apply Rate Donut Chart](dashboard/easy_apply_rate.png)

**DAX measures:**
- `Total Applications = COUNT(raw[ID])`
- `Total Hires = CALCULATE(COUNT(raw[ID]), raw[Hired] = TRUE)`
- `Hiring Rate % = Total Hires / Total Applications * 100`

## 🗂️ Data Prep
`Job Location` strings (e.g. `"New York, NY"`) are split into city/state via Power Query for the Azure Maps visual; trailing whitespace is trimmed so the geocoder resolves cleanly.

## 🖥️ The Power BI Project (.pbip)

`job-application-data.pbip` (open with Power BI Desktop — File → Open → the
`.pbip` file; it pulls straight from `data/job_application.xlsx`). A second,
text-based Power BI project alongside the `.pbix` above — same source data,
built as a single dark purple/pink dashboard page with Bahnschrift
throughout instead of the Azure Maps view.

![Corporate Recruitment Analytics dashboard](job-application-data.png)

A static export (`job-application-data.png`) lives alongside the `.pbip` for
anyone without Power BI Desktop.

**KPI strip:** Total Applications, Hiring Rate Gap (pp) — the spread between
Easy Apply and traditional hiring rates — MoM Applications Growth %, and
Easy Apply Rate %, so the headline volume number always sits next to
comparative context instead of standing alone. Below that: applications by
month, applications by state, an Easy Apply vs. traditional applications
split, and top job titles by application count.

## 📂 Structure
```
dashboard/
  job-application-data.pbix   full interactive report (Azure Maps view)
  *.png                       Power BI chart exports
data/job_application.xlsx     raw source
job-application-data.pbip     Power BI project (open in Desktop)
job-application-data.Report/       PBIR: pages, visuals as JSON
job-application-data.SemanticModel/ TMDL: tables, measures
job-application-data.png      static export of the .pbip dashboard
```
