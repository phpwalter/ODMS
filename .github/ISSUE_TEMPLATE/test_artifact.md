---
name: 🧪 Test Artifact
about: Create or update testing artifacts (Postman, Fixtures, etc.).
title: 'TEST: [Artifact Name]'
labels: 'type:testing'
---

### 🎯 Artifact Type
- [ ] Postman Collection
- [ ] CLI Fixture (Input + State JSON)
- [ ] Scenario Test Script (HTTPX)

### 🧬 Target Endpoint/Version
- **Endpoint:** [e.g., /user/login]
- **API Version:**

### ✅ Acceptance Criteria
- [ ] Artifact strictly follows the OpenAPI YAML schema.
- [ ] [cite_start]Includes validation for the `X-API-Version` header[cite: 4].
- [ ] Successfully executes against the current ODMS build.
