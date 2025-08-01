# Changelog

All notable changes to this project are documented here, using [Semantic Versioning 2.0.0](https://semver.org/).

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
