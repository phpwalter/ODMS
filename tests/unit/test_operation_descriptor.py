"""
tests/unit/test_operation_descriptor.py
Version: 0.1.0-alpha.1
Date: 2026-01-31
Issue ID: [#2](https://github.com/YOUR_USERNAME/YOUR_REPO/issues/2)

Full test suite for OperationDescriptor ensuring it meets all
Issue #2 architectural requirements.
"""

import pytest
from pydantic import ValidationError
from odms.models.registry import OperationDescriptor

def test_descriptor_missing_required_fields():
    """Requirement: Initializing without path or method raises ValidationError."""
    with pytest.raises(ValidationError):
        # Path and Method are required; empty init must fail.
        OperationDescriptor()

def test_descriptor_immutability():
    """Requirement: Attempting to mutate a field raises TypeError (Frozen)."""
    descriptor = OperationDescriptor(path="/health", method="GET")
    with pytest.raises((ValidationError, TypeError)):
        # Model is frozen; this must raise an error.
        descriptor.path = "/new-path"

def test_descriptor_json_schema_compatibility():
    """Requirement: Model accepts standard JSON Schema 2020-12 dictionary."""
    schema_2020_12 = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "properties": {"id": {"type": "string"}}
    }
    descriptor = OperationDescriptor(
        path="/test",
        method="POST",
        request_body_schema=schema_2020_12
    )
    assert descriptor.request_body_schema["type"] == "object"
