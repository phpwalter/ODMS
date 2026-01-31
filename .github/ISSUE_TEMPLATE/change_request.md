---
name: 🔄 Change Request
about: Propose a change to existing logic, architecture, or scope.
title: 'CR: [Title]'
labels: 'type:change'
---

### 🔧 Description of Change
[Clearly describe the proposed change.]

### 📈 Justification
[Explain why the change is necessary or valuable (e.g., mitigating Risk R-003 or addressing a BRD Success Metric).]

### 🔍 Impact Assessment
- **Affects Contract?** (Does this change the OpenAPI YAML?)
- **Affects Determinism?** (Will same input + state still = same output?)
- **Affects Milestone?** (Which Milestone in the Dependency Map is impacted?)
- **Requires Architectural Change?** (Does this modify the Immutable Pipeline?)

### 🧬 Pipeline Stage Alignment
*Indicate which of the 7 stages require modification:*
- [ ] Stage 1: Security Gate
- [ ] Stage 3: x-Validations
- [ ] Stage 5: State Interaction
- [ ] Other: _________

### 🧪 Acceptance Criteria
- [ ] [cite_start][Criterion 1: e.g., Must maintain compliance with Walters Guideline #3] [cite: 4]
- [ ] [Criterion 2: e.g., All existing Fixture Tests must pass]

### 📝 Approval (Internal Use)
- **Approved by Systems Architect:** [ ]
- **Approval Date:** YYYY-MM-DD
