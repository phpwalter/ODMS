# 🙋 FAQ

**Q: Can I add a new stage to the pipeline?**

A: No. The 7-stage pipeline is fixed by design to ensure determinism.

**Q: Where do I define new validation logic?**

A: Inside `validators/business_rules/` using the `x-validations` interface.

**Q: Does ODMS support OpenAPI 3.0?**

A: No. It supports **OpenAPI 3.1+** only, using modern `$ref` resolution and schema standards.
