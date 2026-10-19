# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "BillingRetrieveResponse",
    "Access",
    "Trial",
    "AvailablePlan",
    "Balance",
    "BalanceLastTransaction",
    "OnDemand",
    "Subscription",
    "SubscriptionPlan",
    "SubscriptionUpgradablePlan",
]


class SubscriptionUpgradablePlan(BaseModel):
    id: str

    title: str

    tier: int

    description: str

    included_credits: float = FieldInfo(alias="includedCredits")

    monthly_price: float = FieldInfo(alias="monthlyPrice")

    yearly_price: Optional[float] = FieldInfo(alias="yearlyPrice", default=None)


class SubscriptionPlan(BaseModel):
    id: str

    title: str

    tier: int

    description: str

    included_credits: float = FieldInfo(alias="includedCredits")

    monthly_price: float = FieldInfo(alias="monthlyPrice")

    yearly_price: Optional[float] = FieldInfo(alias="yearlyPrice", default=None)


class Subscription(BaseModel):
    status: Literal["Active", "PastDue", "Unpaid", "Canceled", "Trialing", "Incomplete", "IncompleteExpired"]

    canceled_at: Optional[datetime] = FieldInfo(alias="canceledAt", default=None)

    period_end: Optional[datetime] = FieldInfo(alias="periodEnd", default=None)

    type: Literal["paid"]

    plan: Optional[SubscriptionPlan] = None

    current_tier: int = FieldInfo(alias="currentTier")

    upgradable_plans: List[SubscriptionUpgradablePlan] = FieldInfo(alias="upgradablePlans")


class OnDemand(BaseModel):
    enabled: bool

    current_usage: float = FieldInfo(alias="currentUsage")

    max_credit_usage: float = FieldInfo(alias="maxCreditUsage")


class BalanceLastTransaction(BaseModel):
    amount: int

    created_at: datetime = FieldInfo(alias="createdAt")


class Balance(BaseModel):
    calculated_balance: float = FieldInfo(alias="calculatedBalance")

    available_balance: float = FieldInfo(alias="availableBalance")

    available_on_demand_usage: float = FieldInfo(alias="availableOnDemandUsage")

    last_transaction: Optional[BalanceLastTransaction] = FieldInfo(alias="lastTransaction", default=None)

    unlimited_credits: bool = FieldInfo(alias="unlimitedCredits")


class AvailablePlan(BaseModel):
    id: str

    title: str

    tier: int

    description: str

    included_credits: float = FieldInfo(alias="includedCredits")

    monthly_price: float = FieldInfo(alias="monthlyPrice")

    yearly_price: Optional[float] = FieldInfo(alias="yearlyPrice", default=None)


class Trial(BaseModel):
    status: Literal["Trialing"]

    started_at: datetime = FieldInfo(alias="startedAt")

    ends_at: datetime = FieldInfo(alias="endsAt")

    allowance: float

    remaining_allowance: float = FieldInfo(alias="remainingAllowance")

    exhausted: bool


class Access(BaseModel):
    state: Literal["blocked", "trial", "paid"]

    can_execute: bool = FieldInfo(alias="canExecute")

    blocked_reason: Optional[
        Literal["awaiting_demo", "trial_expired", "trial_allowance_exhausted", "subscription_ended"]
    ] = FieldInfo(alias="blockedReason", default=None)


class BillingRetrieveResponse(BaseModel):
    access: Access

    trial: Optional[Trial] = None

    billing_enabled: bool = FieldInfo(alias="billingEnabled")

    available_plans: List[AvailablePlan] = FieldInfo(alias="availablePlans")

    balance: Balance

    on_demand: OnDemand = FieldInfo(alias="onDemand")

    subscription: Optional[Subscription] = None
