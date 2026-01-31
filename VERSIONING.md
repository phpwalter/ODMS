Here is the completely rebuilt **VERSIONING.md**, upgraded to reflect the **7-stage "Iron Gate" pipeline**, the **Stage 0 Registry**, and the **TDD rigor** of the project.

---

# Versioning Policy – ODMS

ODMS follows **Semantic Versioning (SemVer)** (MAJOR.MINOR.PATCH) to ensure that the "Digital Twin" remains a reliable, deterministic authority for frontend and backend teams.

---

## 🔴 MAJOR Version (X.0.0)

Increment a MAJOR version when **Contract Authority** or **Pipeline Integrity** is fundamentally altered. Any change that requires developers to rethink their integration or breaks backward compatibility is a MAJOR bump.

**Increment when:**

* **Pipeline Reordering**: Any change to the sequence of the **7-stage "Iron Gate" pipeline**.
* **Registry Evolution**: Changes to the **Stage 0 Registry** logic that alter how OpenAPI 3.1 specs are resolved or interpreted.
* **Error Model Breaking Changes**: Structural changes to the **Universal Error Model** (e.g., renaming `subCode` or `trace`).
* **Determinism Shifts**: Any modification that changes the "Same Input + Same State = Same Output" guarantee.
* **Spec Support**: Dropping support for specific OpenAPI or JSON Schema versions.

---

## 🟡 MINOR Version (0.Y.0)

Increment a MINOR version when new capabilities are added to the "Validation Factory" without breaking existing contracts.

**Increment when:**

* **New x-Validations**: Adding new rules to the **Stage 3: x-Validation** catalog.
* **New State Backends**: Adding new deterministic adapters to **Stage 5** (e.g., adding PostgreSQL to SQLite/Memory).
* **CLI Enhancements**: Adding new commands or flags to the `odms` toolkit.
* **New Artifacts**: Adding new exporters (e.g., a new SDK generator or a different test collection format).

---

## 🟢 PATCH Version (0.0.Z)

Increment a PATCH version for internal hardening that does not affect the external "Contract."

**Increment when:**

* **Bug Fixes**: Resolving failures in the pipeline or CLI that do not change the intended behavior.
* **Test Scaffolding**: Updates to the **TDD Pytest suite** or fixture files.
* **Documentation**: Updates to READMEs, the `x-validation-catalog.md`, or inline code comments.
* **Performance**: Internal refactors to improve speed within a pipeline stage.

---

## 🧪 Pre-Releases & TDD Gates

To maintain high quality, pre-releases are used during milestone transitions:

* **Alpha (`-alpha.N`)**: Experimental builds during **M1 and M2**.
* **Beta (`-beta.N`)**: Feature complete builds during **M3 and M4**.
* **RC (`-rc.N`)**: Release Candidates undergoing final **M5 Hard Gate** verification.

---

## ⚖️ Release Authority & Governance

* **Integrity Lock**: No version shall be bumped until the **92% Test Pass Rate** gate is cleared.
* **Changelog**: All MAJOR and MINOR versions must be accompanied by an entry in `CHANGELOG.md` detailing which pipeline stages were affected.
* **Authority**: The Project Owner is the final arbiter of version assignments.
