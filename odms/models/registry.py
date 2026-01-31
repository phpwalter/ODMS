"""
odms/models/registry.py
Version: 0.1.0-alpha.1
Date: 2026-01-31
Issue ID: [#2](https://github.com/YOUR_USERNAME/YOUR_REPO/issues/2)

Defines the immutable OperationDescriptor model, acting as the
authoritative blueprint for all API routes.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field


class OperationDescriptor(BaseModel):
    """
    An immutable representation of an OpenAPI operation.

    This model serves as the Stage 0 'Blueprint' for the ODMS
    execution pipeline.
    """

    # Enforce immutability to prevent runtime contract drift
    model_config = ConfigDict(frozen=True)

    path: str = Field(
        ...,
        description="The API endpoint path (e.g., '/users')"
    )
    method: str = Field(
        ...,
        description="The HTTP verb in uppercase (e.g., 'POST')"
    )
    security_schemes: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="List of security protocols enforced on this route"
    )
    request_body_schema: Optional[Dict[str, Any]] = Field(
        default=None,
        description="JSON Schema 2020-12 defining the valid request body"
    )
    x_validations: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Custom business logic rules (Stage 3)"
    )
