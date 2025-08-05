# Warehouse Stock Availability Dashboard

A lightweight, browser-based stock status viewer for pharmacy store teams.

This project is designed to support **read-only, real-time updates** using a public GitHub-hosted `.csv` file, making it ideal for SharePoint embedding, kiosk use, or desktop reference.

---

## 🌟 Features
- Real-time JSON parsing from GitHub
- Color-coded stock indicators (Green, Amber, Red)
- "On Order" icon displayed as 🚚
- Search by product name, PIP code, or barcode
- Mobile and desktop friendly
- Auto-updating date + semantic versioning

---

## 🚀 Live Demo
[View the Dashboard](https://martybo.github.io/Warehouse_Dashboard/)

---

## 📦 Version
**v1.0.0** — Initial public release  
_Deployed: 01-08-2025_

---

## 📁 Folder Structure
.
├── index.html # Main dashboard interface
├── StockDashboardData.json # Current live stock data
├── logo.jpg # Business logo displayed at top of page
└── README.md # Project documentation (this file)

---

## 🛠 How to Update Stock Data

1. Open the GitHub repository
2. Replace `StockDashboardData.json` with a newly exported file from your warehouse system
3. Commit the change — the dashboard will reflect the update immediately

---

## 📦 Requirements

- A web browser (desktop or tablet)
- Optional: SharePoint page with iframe/embed support

---

## 🚀 Deploying to GitHub Pages

1. In your GitHub repo, go to **Settings → Pages**
2. Choose the branch (`main`) and folder (`/root`) to publish from
3. Save — GitHub will provide a live public link (e.g., `https://yourname.github.io/Warehouse_Dashboard/`)

---

## 📄 License

Internal use only — © Medicare Pharmacy Group, 2025. All rights reserved.

