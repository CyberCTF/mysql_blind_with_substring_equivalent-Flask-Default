# MySQL Blind Injection Using SUBSTRING and ASCII Functions

## Description
In this CTF challenge, you will identify and exploit a blind SQL injection in a book search feature to extract the database’s name using timing-based attacks and substring functions. Direct data output is blocked; you must infer information one byte at a time.

## Objectives
- Identify a blind SQL injection point.
- Use timing-based payloads to prove SQL injection.
- Craft payloads with SUBSTRING and ASCII.
- Automate extraction of information with scripted or manual character-by-character attacks.

## Difficulty
Intermediate

## Estimated Time
45-60 minutes

## Prerequisites
- Knowledge of SQL injection (especially blind techniques)
- Basic SQL syntax
- Familiarity with HTTP requests (e.g., curl, Burp Suite, browser dev tools)
- Understanding of ASCII codes

## Skills Learned
- Detecting blind SQL injection via timing analysis
- Crafting conditional SQL queries for data extraction
- Efficient enumeration via substring/ASCII methods

## Project Structure
- folder : src (web app code)
- folder : setup (lab setup scripts, sample DB dump)
- file : readme.md
- file : .gitignore

## Quick Start
**Prerequisites:** Docker and Docker Compose installed on your system.

**Installation:**
1. Clone the repository.
2. Run `docker-compose up --build`.
3. Access the app at http://localhost:5000.
4. Reset with `docker-compose down -v` and rerun as needed.

## Issue Tracker
https://github.com/YourCTFOrg/acmebooks-blindsql-lab/issues

---
*This is a deliberately vulnerable lab designed solely for educational purposes.* 