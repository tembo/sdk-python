# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from datetime import date, datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SubscriptionRetrieveResponse",
    "Chatgpt",
    "ChatgptUsage",
    "ChatgptUsageRateLimit",
    "ChatgptUsageRateLimitPrimary",
    "ChatgptUsageRateLimitSecondary",
    "ChatgptUsageRateLimitCredits",
    "ChatgptUsageRateLimitIndividualLimit",
    "ChatgptUsageRateLimitResetCredits",
    "ChatgptUsageRateLimitResetCreditsCredit",
    "ChatgptUsageTokenUsage",
    "ChatgptUsageTokenUsageSummary",
    "ChatgptUsageTokenUsageDailyUsageBucket",
    "ChatgptUsageError",
    "Claude",
    "ClaudeUsage",
    "ClaudeUsageRateLimit",
    "ClaudeUsageRateLimit2",
    "ClaudeUsageRateLimit3",
    "ClaudeUsageRateLimit4",
    "ClaudeUsageRateLimit5",
    "ClaudeUsageRateLimit6",
    "ClaudeUsageRateLimit7",
    "ClaudeUsageError",
    "Supergrok",
]


class Supergrok(BaseModel):
    connected: bool


class ClaudeUsageError(BaseModel):
    code: Literal["reconnectRequired", "rateLimited", "unavailable"]

    message: str

    retry_after: Optional[str] = FieldInfo(alias="retryAfter", default=None)


class ClaudeUsageRateLimit7(BaseModel):
    key: Literal["seven_day_cowork"]

    label: Literal["Weekly limit · Cowork"]

    detail: None = None

    remaining_percent: int = FieldInfo(alias="remainingPercent")

    resets_at: Optional[float] = FieldInfo(alias="resetsAt", default=None)


class ClaudeUsageRateLimit6(BaseModel):
    key: Literal["seven_day_sonnet"]

    label: Literal["Weekly limit · Sonnet"]

    detail: None = None

    remaining_percent: int = FieldInfo(alias="remainingPercent")

    resets_at: Optional[float] = FieldInfo(alias="resetsAt", default=None)


class ClaudeUsageRateLimit5(BaseModel):
    key: Literal["seven_day_opus"]

    label: Literal["Weekly limit · Opus"]

    detail: None = None

    remaining_percent: int = FieldInfo(alias="remainingPercent")

    resets_at: Optional[float] = FieldInfo(alias="resetsAt", default=None)


class ClaudeUsageRateLimit4(BaseModel):
    key: Literal["seven_day_oauth_apps"]

    label: Literal["Weekly limit · OAuth apps"]

    detail: None = None

    remaining_percent: int = FieldInfo(alias="remainingPercent")

    resets_at: Optional[float] = FieldInfo(alias="resetsAt", default=None)


class ClaudeUsageRateLimit3(BaseModel):
    key: Literal["seven_day"]

    label: Literal["Weekly limit"]

    detail: None = None

    remaining_percent: int = FieldInfo(alias="remainingPercent")

    resets_at: Optional[float] = FieldInfo(alias="resetsAt", default=None)


class ClaudeUsageRateLimit2(BaseModel):
    key: Literal["five_hour"]

    label: Literal["5-hour limit"]

    detail: None = None

    remaining_percent: int = FieldInfo(alias="remainingPercent")

    resets_at: Optional[float] = FieldInfo(alias="resetsAt", default=None)


ClaudeUsageRateLimit: TypeAlias = Union[
    ClaudeUsageRateLimit2,
    ClaudeUsageRateLimit3,
    ClaudeUsageRateLimit4,
    ClaudeUsageRateLimit5,
    ClaudeUsageRateLimit6,
    ClaudeUsageRateLimit7,
]


class ClaudeUsage(BaseModel):
    rate_limits: List[ClaudeUsageRateLimit] = FieldInfo(alias="rateLimits")


class Claude(BaseModel):
    connected: bool

    reconnect_required: bool = FieldInfo(alias="reconnectRequired")

    usage: Optional[ClaudeUsage] = None

    usage_error: Optional[ClaudeUsageError] = FieldInfo(alias="usageError", default=None)


class ChatgptUsageError(BaseModel):
    code: Literal["reconnectRequired", "rateLimited", "unavailable"]

    message: str

    retry_after: Optional[str] = FieldInfo(alias="retryAfter", default=None)


class ChatgptUsageTokenUsageDailyUsageBucket(BaseModel):
    start_date: date = FieldInfo(alias="startDate")

    tokens: int


class ChatgptUsageTokenUsageSummary(BaseModel):
    lifetime_tokens: Optional[int] = FieldInfo(alias="lifetimeTokens", default=None)

    peak_daily_tokens: Optional[int] = FieldInfo(alias="peakDailyTokens", default=None)

    longest_running_turn_sec: Optional[int] = FieldInfo(alias="longestRunningTurnSec", default=None)

    current_streak_days: Optional[int] = FieldInfo(alias="currentStreakDays", default=None)

    longest_streak_days: Optional[int] = FieldInfo(alias="longestStreakDays", default=None)


class ChatgptUsageTokenUsage(BaseModel):
    summary: ChatgptUsageTokenUsageSummary

    daily_usage_buckets: Optional[List[ChatgptUsageTokenUsageDailyUsageBucket]] = FieldInfo(
        alias="dailyUsageBuckets", default=None
    )


class ChatgptUsageRateLimitResetCreditsCredit(BaseModel):
    id: str

    reset_type: Literal["codexRateLimits", "unknown"] = FieldInfo(alias="resetType")

    status: Literal["available", "redeeming", "redeemed", "unknown"]

    granted_at: int = FieldInfo(alias="grantedAt")

    expires_at: Optional[int] = FieldInfo(alias="expiresAt", default=None)

    title: Optional[str] = None

    description: Optional[str] = None


class ChatgptUsageRateLimitResetCredits(BaseModel):
    available_count: int = FieldInfo(alias="availableCount")

    credits: Optional[List[ChatgptUsageRateLimitResetCreditsCredit]] = None


class ChatgptUsageRateLimitIndividualLimit(BaseModel):
    limit: str

    used: str

    remaining_percent: float = FieldInfo(alias="remainingPercent")

    resets_at: int = FieldInfo(alias="resetsAt")


class ChatgptUsageRateLimitCredits(BaseModel):
    has_credits: bool = FieldInfo(alias="hasCredits")

    unlimited: bool

    balance: Optional[str] = None


class ChatgptUsageRateLimitSecondary(BaseModel):
    used_percent: float = FieldInfo(alias="usedPercent")

    window_duration_mins: Optional[int] = FieldInfo(alias="windowDurationMins", default=None)

    resets_at: Optional[int] = FieldInfo(alias="resetsAt", default=None)


class ChatgptUsageRateLimitPrimary(BaseModel):
    used_percent: float = FieldInfo(alias="usedPercent")

    window_duration_mins: Optional[int] = FieldInfo(alias="windowDurationMins", default=None)

    resets_at: Optional[int] = FieldInfo(alias="resetsAt", default=None)


class ChatgptUsageRateLimit(BaseModel):
    limit_id: Optional[str] = FieldInfo(alias="limitId", default=None)

    limit_name: Optional[str] = FieldInfo(alias="limitName", default=None)

    plan_type: Optional[
        Literal[
            "free",
            "go",
            "plus",
            "pro",
            "prolite",
            "team",
            "self_serve_business_prolite",
            "self_serve_business_usage_based",
            "business",
            "ent26",
            "enterprise_cbp_automation",
            "enterprise_cbp_usage_based",
            "enterprise",
            "edu",
            "edu_plus",
            "edu_pro",
            "unknown",
        ]
    ] = FieldInfo(alias="planType", default=None)

    primary: Optional[ChatgptUsageRateLimitPrimary] = None

    secondary: Optional[ChatgptUsageRateLimitSecondary] = None

    credits: Optional[ChatgptUsageRateLimitCredits] = None

    individual_limit: Optional[ChatgptUsageRateLimitIndividualLimit] = FieldInfo(alias="individualLimit", default=None)

    spend_control_reached: Optional[bool] = FieldInfo(alias="spendControlReached", default=None)

    rate_limit_reached_type: Optional[
        Literal[
            "rate_limit_reached",
            "workspace_owner_credits_depleted",
            "workspace_member_credits_depleted",
            "workspace_owner_usage_limit_reached",
            "workspace_member_usage_limit_reached",
            "unknown",
        ]
    ] = FieldInfo(alias="rateLimitReachedType", default=None)


class ChatgptUsage(BaseModel):
    plan_type: Literal[
        "free",
        "go",
        "plus",
        "pro",
        "prolite",
        "team",
        "self_serve_business_prolite",
        "self_serve_business_usage_based",
        "business",
        "ent26",
        "enterprise_cbp_automation",
        "enterprise_cbp_usage_based",
        "enterprise",
        "edu",
        "edu_plus",
        "edu_pro",
        "unknown",
    ] = FieldInfo(alias="planType")

    rate_limits: List[ChatgptUsageRateLimit] = FieldInfo(alias="rateLimits")

    rate_limit_reset_credits: Optional[ChatgptUsageRateLimitResetCredits] = FieldInfo(
        alias="rateLimitResetCredits", default=None
    )

    token_usage: ChatgptUsageTokenUsage = FieldInfo(alias="tokenUsage")

    fetched_at: datetime = FieldInfo(alias="fetchedAt")


class Chatgpt(BaseModel):
    connected: bool

    usage: Optional[ChatgptUsage] = None

    usage_error: Optional[ChatgptUsageError] = FieldInfo(alias="usageError", default=None)


class SubscriptionRetrieveResponse(BaseModel):
    chatgpt: Chatgpt

    claude: Claude

    supergrok: Supergrok
