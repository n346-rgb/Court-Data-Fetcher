# 🏛️ Court-Data Fetcher & Mini-Dashboard

A lightweight web app that lets users query case metadata and recent orders from the **Faridabad District Court** by entering basic case details.

---

## 🎯 Target Court
- **Court**: Faridabad District Court (India)
- **URL**: [https://districts.ecourts.gov.in/faridabad](https://districts.ecourts.gov.in/faridabad)

---

## ⚙️ Features

- 🔍 Search by **Case Type**, **Case Number**, and **Filing Year**
- 📑 Fetches:
  - Party Names (Petitioner/Respondent)
  - Filing Date and Next Hearing Date
  - Latest PDF Order/Judgment link
- 🗃️ Stores query logs and raw responses in **SQLite**
- 🖥️ Minimal, mobile-friendly UI (HTML + Tailwind/Bootstrap)
- ❗ Graceful error handling for invalid case numbers or connection issues

---

## 🔐 CAPTCHA Handling

- ❌ The selected **district court portal currently does not enforce CAPTCHA**.
- 🧠 If introduced later:
  - The app can be extended using `Playwright` or `Selenium` for automated input.
  - Manual cookie injection or CAPTCHA-solving plugins may be required.

---

## 💻 Technologies Used

| Layer         | Stack                       |
|---------------|-----------------------------|
| Frontend      | HTML + Tailwind CSS (or Bootstrap) |
| Backend       | Python + Flask              |
| Scraping      | Playwright (headless browser) |
| Database      | SQLite                      |
| Rendering     | Jinja2 Templates             |

---

## 📦 Project Structure

