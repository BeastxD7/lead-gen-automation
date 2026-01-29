# 🕵️ Zero-Cost "Blue Ocean" Lead Scraper

> **An automated intelligence engine that hunts for high-value businesses with zero online presence.**

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Automation-orange.svg)

## 📖 The Problem
Solo founders, agencies, and freelancers often struggle to find high-quality clients without paying for expensive tools like ZoomInfo or Apollo.
* **Manual searching is slow:** Copy-pasting data from Maps takes hours.
* **High competition:** Everyone contacts the businesses that *already* have websites.
* **The "Invisible" Market:** There is a massive "Blue Ocean" of profitable businesses (Roofers, Dentists, Manufacturers) that have high revenue but **no website**. These are the perfect clients, but they are invisible to standard search tools.

## 💡 The Solution
This project is a **FastAPI-based automation engine** that acts as a virtual research assistant.
* **Input:** You provide a niche (e.g., *"Bakery"*) and specific locations (e.g., *"New York, USA"*).
* **Process:** It launches a browser instance (Playwright), performs the search, scrolls results, and **clicks into each listing** to verify data accuracy.
* **Output:** A clean, de-duplicated JSON list of leads containing Name, Phone, Address, and—most importantly—**Website Status (`false`)**.

## ✨ Key Features
* **💰 Zero API Costs:** Uses Playwright to scrape data, bypassing expensive API subscriptions.
* **🌍 Anti-Geoblocking:** Automatically configures browser context to block local IP bias, allowing you to scrape global markets (e.g., searching USA from India) without getting local results.
* **🧠 Smart De-duplication:** Detects and ignores duplicate ad listings and recurring organic results.
* **⚡ Deep Verification:** "Click-and-verify" strategy ensures 100% accuracy for physical addresses and website links, rather than relying on the often-incomplete sidebar preview.
* **🛡️ Thread-Safe Execution:** Runs Playwright in Synchronous mode within FastAPI thread pools to ensure stability on Windows servers.

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Framework:** FastAPI
* **Automation:** Playwright (Chromium)
* **Package Manager:** uv (Modern, high-speed Python package manager)

## 🚀 Installation & Setup

This project uses **uv** for blazing fast dependency management.

```uv run uvicorn app.main:app --reload```