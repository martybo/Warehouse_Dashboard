# Warehouse Stock Availability Dashboard

A lightweight, browser-based stock status viewer for pharmacy teams.

This tool supports **read-only, real-time updates** using a public GitHub-hosted `.json` file, ideal for SharePoint embedding, kiosk use, or local web access via browser.

---

## 🌟 Features (v1.1.1)
- ✅ Real-time JSON parsing from GitHub
- ✅ Color-coded stock indicators (Green, Amber, Red)
- ✅ "On Order" detection with 🚚 icon
- ✅ Multi-field search using `/` separator (e.g., `amox/tab/500`)
- ✅ Sortable columns (Product, PIP Code, Barcode, etc.)
- ✅ Responsive design (mobile and desktop)
- ✅ Intelligent filtering (results hidden until 3+ characters entered)
- ✅ Auto-updating “Last Updated” date from file contents
- ✅ Deployment-ready for SharePoint, intranet, or kiosk use

---

## 🚀 Live Demo
[🔗 View the Dashboard](https://martybo.github.io/Warehouse_Dashboard/)

---

## 📦 Version
**v1.1.1** — Improved filtering, formatting, and On Order detection  
_Deployed: 05-08-2025_

---

## 📁 Folder Structure
├── index.html # Main dashboard interface (UI logic + styles)
├── StockDashboardData.json # Live warehouse stock data
├── logo.jpg # Business logo shown at top of page
└── README.md # Project documentation (this file)


---

## 🔄 How to Update Stock Data

This dashboard reads directly from the `StockDashboardData.json` file hosted on GitHub.

To update:

1. Run the `auto_convert_and_push.py` script to regenerate the JSON from `.csv` and `.txt` inputs
2. Automatically commits the new JSON to GitHub
3. The dashboard reflects updates instantly upon page load

_The script can be run on Mac or Windows using a local Python environment or GUI launcher._

---

## 🛠 Requirements

- A modern web browser (Chrome, Edge, Safari, Firefox)
- Optional: SharePoint or internal intranet support for iframe/web embedding

---

## 🧰 Deploying to GitHub Pages

1. Go to **Settings → Pages** in your GitHub repository
2. Set:
   - **Branch**: `main`
   - **Folder**: `/ (root)`
3. Save to generate a live site URL

---

## 🛡 License

**Internal use only** — © Medicare Pharmacy Group, 2025. All rights reserved.
