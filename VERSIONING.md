# Versioning Policy – ODMS

ODMS follows **Semantic Versioning (SemVer)**:

MAJOR.MINOR.PATCH

---

## MAJOR Version (X.0.0)

Increment when:
- Pipeline order changes
- Validation semantics change
- Determinism guarantees change
- Spec interpretation rules change
- Backward compatibility is broken

Examples:
- Reordering pipeline stages
- Changing response selection priority

---

## MINOR Version (0.Y.0)

Increment when:
- New features are added
- New x‑validations are introduced
- New state backends are added
- Backward compatibility is preserved

Examples:
- New CLI command
- New validation rule

---

## PATCH Version (0.0.Z)

Increment when:
- Bugs are fixed
- Internal refactors occur
- Performance improvements are made
- No user‑visible behavior changes

---

## Pre‑Releases

Pre‑releases use the format:

- `vX.Y.Z-alpha.N`
- `vX.Y.Z-beta.N`
- `vX.Y.Z-rc.N`

Rules:
- Alpha: experimental, unstable
- Beta: feature complete, stabilizing
- RC: no new features allowed

---

## Release Authority

- The Project Owner is the final authority on version assignment.
- Any MAJOR release must be explicitly documented in:
    - CHANGELOG.md
    - GitHub Release Notes
