# 🗺️ ODMS 30-Day Solo Roadmap

This roadmap defines the **Linear Execution Path** for the OpenAPI-Driven Mock Server (ODMS). We move strictly from **Spec Authority** to **Ecosystem Tools** through a series of five technical Hard Gates.

---

## 📑 Milestone 1: Spec Resolution & Registry (Days 1–7)

**Objective:** Transform passive YAML into executable intent.

* **Hard Gate:** A CLI tool that prints every route and its validation rules from a YAML.
* **Focus:** `OperationDescriptor` models, recursive `$ref` resolution (Prance), and the Stage 0 Registry.
* **TDD Requirement:** 100% coverage on resolution failure scenarios (circular refs, missing files).

## 🛡️ Milestone 2: The Iron Gate (Days 8–15)

**Objective:** Implement the first half of the request pipeline (Stages 1-4).

* **Hard Gate:** FastAPI server rejecting any request not matching the spec or security protocols.
* **Focus:** SecurityGate (JWT), RequestExtraction, x-Validations, and Schema Validation.
* **TDD Requirement:** "Red-Green" verification of every validation error code.

## 🧠 Milestone 3: Deterministic State & Logic (Days 16–23)

**Objective:** Create the "Digital Twin" memory and response selection (Stages 5-6).

* **Hard Gate:** Proving same input + same state = same output across restarts.
* **Focus:** SQLite/Memory backends, StateInteraction, and deterministic ResponseSelection.
* **TDD Requirement:** Fixture-based regression tests for state persistence.

## 📡 Milestone 4: Serialization & Transparency (Days 24–27)

**Objective:** Finalize output delivery and observability (Stage 7).

* **Hard Gate:** All responses and errors strictly follow the Universal Error Model and OpenAPI content-types.
* **Focus:** Stage 7 Serialization, Trace support, and Swagger UI integration.
* **TDD Requirement:** Content-type header verification and error schema compliance.

## 🧰 Milestone 5: CLI & Ecosystem Tools (Days 28–30)

**Objective:** Enable user interaction, seeding, and final hardening.

* **Hard Gate:** 92% Test Pass Rate and 80% Code Coverage via GitHub Actions.
* **Focus:** `odms` CLI (`start`, `seed`, `reset`), and Postman collection exports.
* **TDD Requirement:** End-to-end (E2E) scenario tests for all CLI commands.

---

## 🛠️ Roadmap Governance

1. **Linearity:** No issue from a future Milestone may be started until the current Milestone's **Gatekeeper Issue** is closed.
2. **TDD First:** Every feature issue must be preceded or accompanied by a Test Scaffold issue.
3. **Versioning:** Milestone transitions trigger a MINOR or MAJOR version bump per the `VERSIONING.md` policy.
