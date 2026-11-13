from enum import StrEnum


class ErrorCode(StrEnum):
    AGENT_NOT_ALLOWED = "agent_not_allowed"
    AGENT_SPENDING_CAP = "agent_spending_cap"
    ALREADY_STOPPED = "already_stopped"
    BAD_REQUEST = "bad_request"
    CAPACITY_UNAVAILABLE = "capacity_unavailable"
    CARD_REQUIRED = "card_required"
    IDEMPOTENCY_KEY_IN_USE = "idempotency_key_in_use"
    IDEMPOTENCY_KEY_REUSED = "idempotency_key_reused"
    INTERNAL = "internal"
    INVALID_STATE = "invalid_state"
    IN_USE = "in_use"
    KEY_RESTRICTED = "key_restricted"
    LAB_ONLY = "lab_only"
    LIMIT_REACHED = "limit_reached"
    LINK_ADDRESS_CHANGED = "link_address_changed"
    MFA_REQUIRED = "mfa_required"
    MISSING_SCOPE = "missing_scope"
    NAME_TAKEN = "name_taken"
    NOT_AVAILABLE_YET = "not_available_yet"
    NOT_FOUND = "not_found"
    PANEL_SESSION_REQUIRED = "panel_session_required"
    PAYMENT_DISPUTED = "payment_disputed"
    PLAN_CHANGED = "plan_changed"
    RATE_LIMITED = "rate_limited"
    SIGNUPS_CLOSED = "signups_closed"
    SIGN_IN_AGAIN = "sign_in_again"
    SIZE_NOT_ALLOWED = "size_not_allowed"
    SSO_REQUIRED = "sso_required"
    STUDIO_CLOSED = "studio_closed"
    STUDIO_REQUIRED = "studio_required"
    STUDIO_SUSPENDED = "studio_suspended"
    TOO_LARGE = "too_large"
    UNAUTHENTICATED = "unauthenticated"
    UNAVAILABLE = "unavailable"
    UNSUPPORTED_IMAGE = "unsupported_image"
    VALIDATION_FAILED = "validation_failed"
    VERSION_NOT_READY = "version_not_ready"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "ErrorCode | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
