# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

__all__ = [
    "SettingUpdateParams",
    "DesktopNotificationPreferences",
    "AppearancePreferences",
    "AppearancePreferencesAccentTheme",
    "AppSidebarPreferences",
    "AppSidebarPreferencesRightSidebar",
    "DiffPreferences",
    "DashboardPreferences",
    "DashboardPreferencesTaskFilters",
    "ComposerPreferences",
    "ComposerPreferencesLastSelectedRepository",
    "ReviewPreferences",
    "ReviewPreferencesLayout",
]


class SettingUpdateParams(TypedDict, total=False):
    auto_restart_vm: Annotated[bool, PropertyInfo(alias="autoRestartVm")]
    """Automatically restart a session VM when needed."""

    default_project_id: Annotated[Optional[str], PropertyInfo(alias="defaultProjectId")]
    """Default project environment for new sessions, or null to clear the preference."""

    gpg_key: Annotated[str, PropertyInfo(alias="gpgKey")]
    """GPG signing key configuration. This value is returned by retrieveUserSettings."""

    include_tembo_commit_attribution: Annotated[bool, PropertyInfo(alias="includeTemboCommitAttribution")]
    """Include Tembo attribution in agent-created commits."""

    desktop_notifications_enabled: Annotated[bool, PropertyInfo(alias="desktopNotificationsEnabled")]
    """Enable or disable desktop notifications."""

    desktop_notification_preferences: Annotated[
        DesktopNotificationPreferences, PropertyInfo(alias="desktopNotificationPreferences")
    ]
    """Notification types to show on the desktop."""

    has_desktop_app: Annotated[bool, PropertyInfo(alias="hasDesktopApp")]
    """Whether the user has signed in to the Tembo desktop app."""

    open_links_in_desktop_app: Annotated[bool, PropertyInfo(alias="openLinksInDesktopApp")]
    """Open Tembo links from the browser in the desktop app when it is installed."""

    appearance_preferences: Annotated[AppearancePreferences, PropertyInfo(alias="appearancePreferences")]
    """Theme, accent, and appearance preferences. Nested updates preserve unrelated preferences."""

    app_sidebar_preferences: Annotated[AppSidebarPreferences, PropertyInfo(alias="appSidebarPreferences")]
    """Application sidebar layout preferences."""

    diff_preferences: Annotated[DiffPreferences, PropertyInfo(alias="diffPreferences")]
    """Diff display and comparison preferences."""

    dashboard_preferences: Annotated[DashboardPreferences, PropertyInfo(alias="dashboardPreferences")]
    """Dashboard task-filter preferences."""

    composer_preferences: Annotated[ComposerPreferences, PropertyInfo(alias="composerPreferences")]
    """Message composer preferences, including selected repositories."""

    review_preferences: Annotated[ReviewPreferences, PropertyInfo(alias="reviewPreferences")]
    """Code review file sorting, exclusions, bot comment visibility, and layout preferences."""

    diff_light_theme: Annotated[str, PropertyInfo(alias="diffLightTheme")]
    """Diff syntax theme for light mode."""

    diff_dark_theme: Annotated[str, PropertyInfo(alias="diffDarkTheme")]
    """Diff syntax theme for dark mode."""

    default_agent: Annotated[Optional[str], PropertyInfo(alias="defaultAgent")]
    """Default coding agent and model key. Null clears the preference."""

    follow_up_behavior: Annotated[Literal["queue", "steer"], PropertyInfo(alias="followUpBehavior")]
    """Default follow-up delivery: queue a new turn or steer an active turn."""

    custom_system_prompt: Annotated[str, PropertyInfo(alias="customSystemPrompt")]
    """Personal system instructions supplied to agents."""


class ReviewPreferencesLayout(TypedDict, total=False):
    focus_chat_height: Annotated[float, PropertyInfo(alias="focusChatHeight")]

    active_tab: Annotated[str, PropertyInfo(alias="activeTab")]

    active_view_mode: Annotated[str, PropertyInfo(alias="activeViewMode")]

    focus_chat_open: Annotated[bool, PropertyInfo(alias="focusChatOpen")]

    focus_mode: Annotated[bool, PropertyInfo(alias="focusMode")]

    left_desktop_sidebar_open: Annotated[bool, PropertyInfo(alias="leftDesktopSidebarOpen")]

    left_desktop_sidebar_width: Annotated[float, PropertyInfo(alias="leftDesktopSidebarWidth")]

    right_desktop_sidebar_open: Annotated[bool, PropertyInfo(alias="rightDesktopSidebarOpen")]

    right_desktop_sidebar_width: Annotated[float, PropertyInfo(alias="rightDesktopSidebarWidth")]


class ReviewPreferences(TypedDict, total=False):
    file_sort_mode: Annotated[
        Literal["tree", "path-asc", "path-desc", "largest", "smallest"], PropertyInfo(alias="fileSortMode")
    ]

    excluded_file_patterns: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludedFilePatterns")]

    sections: Dict[str, bool]

    hide_bot_comments: Annotated[bool, PropertyInfo(alias="hideBotComments")]

    layout: ReviewPreferencesLayout


class ComposerPreferencesLastSelectedRepository(TypedDict, total=False):
    id: Required[str]

    name: str

    type: str


class ComposerPreferences(TypedDict, total=False):
    last_selected_repositories: Annotated[
        Iterable[ComposerPreferencesLastSelectedRepository], PropertyInfo(alias="lastSelectedRepositories")
    ]


class DashboardPreferencesTaskFilters(TypedDict, total=False):
    status_filter: Annotated[SequenceNotStr[str], PropertyInfo(alias="statusFilter")]

    sort_by: Annotated[Literal["createdAt", "updatedAt"], PropertyInfo(alias="sortBy")]

    search_query: Annotated[str, PropertyInfo(alias="searchQuery")]

    integration_type: Annotated[SequenceNotStr[str], PropertyInfo(alias="integrationType")]

    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    project_filter: Annotated[SequenceNotStr[str], PropertyInfo(alias="projectFilter")]

    author_filter: Annotated[SequenceNotStr[str], PropertyInfo(alias="authorFilter")]

    pr_status_filter: Annotated[SequenceNotStr[str], PropertyInfo(alias="prStatusFilter")]

    automation_filter: Annotated[SequenceNotStr[str], PropertyInfo(alias="automationFilter")]


class DashboardPreferences(TypedDict, total=False):
    task_filters: Annotated[DashboardPreferencesTaskFilters, PropertyInfo(alias="taskFilters")]


class DiffPreferences(TypedDict, total=False):
    style: Literal["unified", "split"]

    indicators: Literal["classic", "bars", "none"]

    overflow: Literal["scroll", "wrap"]

    show_line_numbers: Annotated[bool, PropertyInfo(alias="showLineNumbers")]

    expand_unchanged: Annotated[bool, PropertyInfo(alias="expandUnchanged")]

    show_file_tree: Annotated[bool, PropertyInfo(alias="showFileTree")]

    file_tree_position: Annotated[Literal["left", "right"], PropertyInfo(alias="fileTreePosition")]

    file_tree_view: Annotated[Literal["list", "tree"], PropertyInfo(alias="fileTreeView")]

    light_theme: Annotated[str, PropertyInfo(alias="lightTheme")]

    dark_theme: Annotated[str, PropertyInfo(alias="darkTheme")]


class AppSidebarPreferencesRightSidebar(TypedDict, total=False):
    open: bool

    width: str


class AppSidebarPreferences(TypedDict, total=False):
    open: bool

    session_owner_scope: Annotated[Literal["mine", "team"], PropertyInfo(alias="sessionOwnerScope")]

    session_sort_by: Annotated[Literal["createdAt", "updatedAt"], PropertyInfo(alias="sessionSortBy")]

    session_organization: Annotated[Literal["list", "project"], PropertyInfo(alias="sessionOrganization")]

    show_archived_sessions: Annotated[bool, PropertyInfo(alias="showArchivedSessions")]

    width: float

    right_sidebar: Annotated[Dict[str, AppSidebarPreferencesRightSidebar], PropertyInfo(alias="rightSidebar")]


class AppearancePreferencesAccentTheme(TypedDict, total=False):
    theme_id: Annotated[str, PropertyInfo(alias="themeId")]

    custom_surface: Annotated[Optional[str], PropertyInfo(alias="customSurface")]

    custom_accent: Annotated[Optional[str], PropertyInfo(alias="customAccent")]

    custom_intensity: Annotated[float, PropertyInfo(alias="customIntensity")]

    system_light: Annotated[str, PropertyInfo(alias="systemLight")]

    system_dark: Annotated[str, PropertyInfo(alias="systemDark")]


class AppearancePreferences(TypedDict, total=False):
    app_theme: Annotated[Literal["light", "dark", "system"], PropertyInfo(alias="appTheme")]

    accent_theme: Annotated[AppearancePreferencesAccentTheme, PropertyInfo(alias="accentTheme")]


class DesktopNotificationPreferences(TypedDict, total=False):
    awaiting_approval: Annotated[bool, PropertyInfo(alias="awaitingApproval")]

    pull_request_opened: Annotated[bool, PropertyInfo(alias="pullRequestOpened")]

    pull_request_review_requested: Annotated[bool, PropertyInfo(alias="pullRequestReviewRequested")]
