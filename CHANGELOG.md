# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

---

## [1.0.1] - 2025-08-03
### Added
- GitHub API integration to dynamically display the **Last Updated** date of the `StockDashboardData.json` file based on latest commit timestamp
- Refined search input handling:
  - Search is only activated when **3 or more characters** are entered
  - Input is split by `/` for **compound search filtering** (e.g., `levoth/tab/50`)
- Explanatory hint text below search bar

### Changed
- Hardcoded **Deployed** date shown in footer as `03-08-2025` (previously showed current local date)

---

### v1.0.0 (Public Release)
- First production release
- Includes:
  - Delivery van emoji for "On Order"
  - Refined search with row hiding until 3+ characters
  - Last updated & deployed date display
  - Responsive layout and barcode display improvements

---

## [1.0.0-rc3] - 2025-08-01
### Fixed
- Reverted to full row rendering on page load
- Ensured reliable search after load
- Removed "In Stock" column
- Reordered columns to match user priorities

### Added
- Business logo support via `logo.jpg`
- Last updated and deployed timestamps

---

## [1.0.0-rc2] - 2025-08-01
### Fixed
- Trimmed CSV headers for reliable matching
- Improved parsing for “On Order” field

### Issue
- Search still failed due to delayed DOM population

---

## [1.0.0-rc1] - 2025-08-01
### Added
- Filter-first rendering concept (hide table until 3+ characters typed)
- Visual enhancements: status icons, delivery van, modern input

### Issue
- Data failed to render due to header mismatch or async issues
