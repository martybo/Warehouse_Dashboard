# Changelog

All notable changes to this project are documented here, using [Semantic Versioning 2.0.0](https://semver.org/).

---

## [1.1.1] - 2025-08-05
### Fixed
- Corrected broken data source path that prevented stock data from loading and search results from appearing.
- Repaired missing `"On Order"` logic — now detects non-zero values accurately and displays 🚚.
- Sanitized field data and ensured robust null handling.

### Added
- Left-justified text alignment for key columns (`Product Name`, `PIPCode`, `Barcode`)
- Centered alignment for icon columns (`Stock Status`, `On Order`)
- Multi-segment search using `/` separators (e.g. `levoth/tab/100`)
- “Last Updated” date based on JSON content, not GitHub API

---

## [1.1.0] - 2025-08-04
### Changed
- Switched from CSV to JSON data source for improved integrity and compatibility.
- Removed download CSV button temporarily.
- Updated UI layout: cleaner table design, flexible styling.

### Added
- "On Order" logic in UI (initial implementation)
- Column sorting on all headers
- Version and copyright footer

---

## [1.0.1] - 2025-08-02
### Fixed
- Adjusted GitHub fetch logic to display correct "Last Updated" timestamp
- Improved JSON escaping to avoid display issues in product names

### Added
- Initial JSON build script (`auto_convert_and_push.py`)
- Support for direct GitHub API commit via GitHub token
- Basic `.env` support for local development security

---

## [1.0.0] - 2025-08-01
### Public Release
- First stable production release

### Features
- Responsive layout for desktop/tablet
- Live CSV parsing using PapaParse
- Color-coded stock status (green/amber/red)
- Search with filter logic and emoji 🚚 indicator
- Last updated & deployed timestamp

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
