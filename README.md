# First Layer Overview: Top-Level `wordplay`

This is the root directory of the `wordplay` project. The project provides a complete Cambridge curriculum-aligned interactive website for learning English from Beginner to Mastery levels. Users can interactively progress across six CEFR levels (A1–C2), with added resources for exam preparation and tracking progress.

### Project Structure
Here is an overview of project files and folders found at this top layer:

- **404.html**: Custom error page displayed when users access a non-existent URL.
- **AI_HANDOVER.md**: Document describing AI-driven handover practices for regenerating code assets using AI tools.
- **AUTH_PROPOSAL.md**: Proposal for long-term implementation of user authorization systems (e.g., login, accounts).
- **README.md**: You are reading this file!
- **SESSION_CONTEXT.md**: Technical reference for AI workflows during site generation.
- **SYLLABUS.md**: Reference material for mapping Cambridge syllabus topics into site structure.
- **_headers/**: Configuration for HTTP response headers on the live-hosted site.
- **a/**: Beginner level modules (A1 and A2), part of the first official CEFR levels.
- **b/**: Intermediate CEFR levels (B1 and B2), including FCE (exam-specific).
- **c/**: Advanced CEFR levels (C1 and C2), including integration for exams like CAE and CPE.
- **es/**: Localization resources for Spanish curriculum expansions.
- **shared/**: Shared assets like CSS and JavaScript powering site-wide components.

---

## Purpose of This Project
Wordplay is designed for educators and English learners alike. The static site format ensures privacy and accessibility, storing user progress locally without backend dependencies—future updates may add login and external persistence solutions.

---
_Last Updated: May 2026_