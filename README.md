# Warehouse Stock Availability Dashboard

A lightweight, browser-based dashboard that enables store teams to check warehouse stock availability with simple, visual indicators.

This project is designed to support **read-only, real-time updates** using a public GitHub-hosted `.csv` file, making it ideal for SharePoint embedding, kiosk use, or desktop reference.

---

## ✅ Key Features

- 🔍 **Live search** by Product Name, Code, or Barcode
- 🟢🟡🔴 **Visual stock status** using coloured indicator icons
- 🚚 **On Order icon** shown if stock is expected
- 🧾 CSV-driven data (auto-parsed with [PapaParse](https://www.papaparse.com/))
- 📄 **No database or login required**
- 🌐 Designed to be embedded in SharePoint or hosted via GitHub Pages

---

## 📁 Folder Structure
.
├── index.html # Main dashboard interface
├── StockDashboardData.csv # Current live stock data
├── logo.jpg # Business logo displayed at top of page
└── README.md # Project documentation (this file)

---

## 🛠 How to Update Stock Data

1. Open the GitHub repository
2. Replace `StockDashboardData.csv` with a newly exported file from your warehouse system
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

