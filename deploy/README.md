# MySQL Blind Injection Using SUBSTRING and ASCII Functions

## Description
In this CTF challenge, you will identify and exploit a blind SQL injection in a book search feature to extract the database’s name using timing-based attacks and substring functions. Direct data output is blocked; you must infer information one byte at a time.

## Quick Start
**Docker Pull & Run:**

```
docker pull cyberctf/acmebooks-blindsql-lab:latest
docker run -p 5000:5000 cyberctf/acmebooks-blindsql-lab:latest
```

Or use Docker Compose:

```
docker-compose up --build
```

Access the app at http://localhost:5000

## Issue Tracker
https://github.com/YourCTFOrg/acmebooks-blindsql-lab/issues

---
*This is a deliberately vulnerable lab designed solely for educational purposes.* 