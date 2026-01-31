---
name: 🐛 Bug Report
about: Report a failure in the pipeline or CLI.
title: 'BUG: [Title]'
labels: 'type:bug'
---

### 🚨 Description
[Describe the bug.]

### 📋 Error Metadata (Universal Error Model)
*Mandatory fields from TSD 8:*
- **Code:** [e.g., VALIDATION_FAILED]
- **SubCode:** [e.g., SCHEMA_MISMATCH]
- **RequestID:** - **Trace Stage:** [Identify which of the 7 stages failed]

### 🔄 Steps to Reproduce
1. Start ODMS with `odms start --spec [file] --backend [memory|file|sqlite]`
2. Send request with header `X-API-Version: 1`
3. Observe error output

### ✅ Expected Behavior
[What should have happened according to the OpenAPI YAML?]
