---
name: 📘 User Story
about: Define a new feature from a user's perspective.
title: 'US: [Title]'
labels: ["type:feature", "priority:medium"]
---

### 🔰 User Role
**As a** [Frontend Developer | QA Engineer | Backend Developer | Project Owner]
**I want** [description of the capability]
**so that** [benefit or value to the project, e.g., BR-02 Deterministic Execution]

### ✅ Acceptance Criteria
- [ ] Criterion 1 (e.g., Must enforce Header Versioning #3)
- [ ] Criterion 2 (e.g., Must return trace metadata identifying the failed stage)
- [ ] Criterion 3 (e.g., Output must strictly match YAML schema)

### 🧬 Related Pipeline Stage
*Target stage as defined in TSD 5.4:*
- [ ] Stage 1: Security Gate (JWT & Versioning)
- [ ] Stage 2: Request Extraction
- [ ] Stage 3: x-Validations (Business Logic)
- [ ] Stage 4: Schema Validation (JSON Schema 2020-12)
- [ ] Stage 5: State Interaction (Deterministic CRUD)
- [ ] Stage 6: Response Selection (Example/Fixture/State/Schema)
- [ ] Stage 7: Serialization

### 🧪 Validation Plan
- [ ] Unit Test (Pytest)
- [ ] Fixture Test (Same input + same state = same output)
- [ ] Scenario Test (Multi-step flow)
