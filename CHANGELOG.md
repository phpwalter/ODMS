# Changelog
All notable changes to **OpenAPI‑Driven Mock Server (ODMS)** are documented in this file.

This project follows **Semantic Versioning (SemVer)**:
`MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes to pipeline, contract enforcement, or execution model
- **MINOR**: Backward‑compatible feature additions
- **PATCH**: Bug fixes and internal improvements

---

## [Unreleased]

### 🚀 Added
- 

### 🛠️ Changed
- 

### 🐛 Fixed
- 

### ⚠️ Breaking Changes
- 

---

## [1.0.0] - 2026-01-28

### 🚀 Added
- Spec‑driven mock server treating OpenAPI 3.1 as executable intent
- Immutable 7‑stage request execution pipeline ("Iron Gate")
- Recursive `$ref` resolution with frozen in‑memory spec registry
- Deterministic state backends: Memory, File, SQLite
- Business logic execution via `x‑validations`
- Fixed response selection strategy: Examples → Fixtures → State → Schema
- Universal error model with trace support
- CLI commands: `start`, `seed`, `reset`
- Optional Swagger UI and resolved `/openapi.json`
- Postman collections and CLI fixture tests

### 🛠️ Changed
- N/A (Initial release)

### 🐛 Fixed
- N/A (Initial release)

### ⚠️ Breaking Changes
- N/A (Initial release)

---

## Versioning Rules

- Any change affecting **pipeline order**, **validation semantics**, or **determinism** requires a **MAJOR** version bump.
- Any change adding new capabilities without altering behavior requires a **MINOR** version bump.
- Bug fixes and refactors without behavior change require a **PATCH** version bump.
