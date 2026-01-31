---
name: 🧩 x-Validation Rule
about: Define a custom business logic simulation rule.
title: 'RULE: [Rule Name]'
labels: 'type:logic'
---

### 🎯 Objective
**Rule Name:** `x-`
**Target Collection:** [e.g., users, orders]
**Validation Logic:** [Clearly describe the business logic, e.g., "Field 'email' must be unique in collection 'users'"]

### 🧬 Integration
- [ ] Added to `docs/x-validation-catalog.md`
- [ ] Implemented in `xValidations` Stage (Stage 3)

### ✅ Acceptance Criteria
- [ ] Returns `400 Bad Request` on failure.
- [ ] Includes `subCode: BUSINESS_RULE_VIOLATION`.
- [ ] Does not modify the request payload.
