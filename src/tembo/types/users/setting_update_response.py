# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SettingUpdateResponse",
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


class ReviewPreferencesLayout(BaseModel):
    focus_chat_height: Optional[float] = FieldInfo(alias="focusChatHeight", default=None)

    active_tab: Optional[str] = FieldInfo(alias="activeTab", default=None)

    active_view_mode: Optional[str] = FieldInfo(alias="activeViewMode", default=None)

    focus_chat_open: Optional[bool] = FieldInfo(alias="focusChatOpen", default=None)

    focus_mode: Optional[bool] = FieldInfo(alias="focusMode", default=None)

    left_desktop_sidebar_open: Optional[bool] = FieldInfo(alias="leftDesktopSidebarOpen", default=None)

    left_desktop_sidebar_width: Optional[float] = FieldInfo(alias="leftDesktopSidebarWidth", default=None)

    right_desktop_sidebar_open: Optional[bool] = FieldInfo(alias="rightDesktopSidebarOpen", default=None)

    right_desktop_sidebar_width: Optional[float] = FieldInfo(alias="rightDesktopSidebarWidth", default=None)


class ReviewPreferences(BaseModel):
    file_sort_mode: Optional[Literal["tree", "path-asc", "path-desc", "largest", "smallest"]] = FieldInfo(
        alias="fileSortMode", default=None
    )

    excluded_file_patterns: Optional[List[str]] = FieldInfo(alias="excludedFilePatterns", default=None)

    sections: Optional[Dict[str, bool]] = None

    hide_bot_comments: Optional[bool] = FieldInfo(alias="hideBotComments", default=None)

    layout: Optional[ReviewPreferencesLayout] = None


class ComposerPreferencesLastSelectedRepository(BaseModel):
    id: str

    name: Optional[str] = None

    type: Optional[str] = None


class ComposerPreferences(BaseModel):
    last_selected_repositories: Optional[List[ComposerPreferencesLastSelectedRepository]] = FieldInfo(
        alias="lastSelectedRepositories", default=None
    )


class DashboardPreferencesTaskFilters(BaseModel):
    status_filter: Optional[List[str]] = FieldInfo(alias="statusFilter", default=None)

    sort_by: Optional[Literal["createdAt", "updatedAt"]] = FieldInfo(alias="sortBy", default=None)

    search_query: Optional[str] = FieldInfo(alias="searchQuery", default=None)

    integration_type: Optional[List[str]] = FieldInfo(alias="integrationType", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    project_filter: Optional[List[str]] = FieldInfo(alias="projectFilter", default=None)

    author_filter: Optional[List[str]] = FieldInfo(alias="authorFilter", default=None)

    pr_status_filter: Optional[List[str]] = FieldInfo(alias="prStatusFilter", default=None)

    automation_filter: Optional[List[str]] = FieldInfo(alias="automationFilter", default=None)


class DashboardPreferences(BaseModel):
    task_filters: Optional[DashboardPreferencesTaskFilters] = FieldInfo(alias="taskFilters", default=None)


class DiffPreferences(BaseModel):
    style: Optional[Literal["unified", "split"]] = None

    indicators: Optional[Literal["classic", "bars", "none"]] = None

    overflow: Optional[Literal["scroll", "wrap"]] = None

    show_line_numbers: Optional[bool] = FieldInfo(alias="showLineNumbers", default=None)

    expand_unchanged: Optional[bool] = FieldInfo(alias="expandUnchanged", default=None)

    show_file_tree: Optional[bool] = FieldInfo(alias="showFileTree", default=None)

    file_tree_position: Optional[Literal["left", "right"]] = FieldInfo(alias="fileTreePosition", default=None)

    file_tree_view: Optional[Literal["list", "tree"]] = FieldInfo(alias="fileTreeView", default=None)

    light_theme: Optional[str] = FieldInfo(alias="lightTheme", default=None)

    dark_theme: Optional[str] = FieldInfo(alias="darkTheme", default=None)


class AppSidebarPreferencesRightSidebar(BaseModel):
    open: Optional[bool] = None

    width: Optional[str] = None


class AppSidebarPreferences(BaseModel):
    open: Optional[bool] = None

    session_owner_scope: Optional[Literal["mine", "team"]] = FieldInfo(alias="sessionOwnerScope", default=None)

    session_sort_by: Optional[Literal["createdAt", "updatedAt"]] = FieldInfo(alias="sessionSortBy", default=None)

    session_organization: Optional[Literal["list", "project"]] = FieldInfo(alias="sessionOrganization", default=None)

    show_archived_sessions: Optional[bool] = FieldInfo(alias="showArchivedSessions", default=None)

    width: Optional[float] = None

    right_sidebar: Optional[Dict[str, AppSidebarPreferencesRightSidebar]] = FieldInfo(
        alias="rightSidebar", default=None
    )


class AppearancePreferencesAccentTheme(BaseModel):
    theme_id: Optional[str] = FieldInfo(alias="themeId", default=None)

    custom_surface: Optional[str] = FieldInfo(alias="customSurface", default=None)

    custom_accent: Optional[str] = FieldInfo(alias="customAccent", default=None)

    custom_intensity: Optional[float] = FieldInfo(alias="customIntensity", default=None)

    system_light: Optional[str] = FieldInfo(alias="systemLight", default=None)

    system_dark: Optional[str] = FieldInfo(alias="systemDark", default=None)


class AppearancePreferences(BaseModel):
    app_theme: Optional[Literal["light", "dark", "system"]] = FieldInfo(alias="appTheme", default=None)

    accent_theme: Optional[AppearancePreferencesAccentTheme] = FieldInfo(alias="accentTheme", default=None)


class DesktopNotificationPreferences(BaseModel):
    awaiting_approval: Optional[bool] = FieldInfo(alias="awaitingApproval", default=None)

    pull_request_opened: Optional[bool] = FieldInfo(alias="pullRequestOpened", default=None)

    pull_request_review_requested: Optional[bool] = FieldInfo(alias="pullRequestReviewRequested", default=None)


class SettingUpdateResponse(BaseModel):
    auto_restart_vm: Optional[bool] = FieldInfo(alias="autoRestartVm", default=None)

    default_project_id: Optional[str] = FieldInfo(alias="defaultProjectId", default=None)

    gpg_key: Optional[str] = FieldInfo(alias="gpgKey", default=None)

    include_tembo_commit_attribution: Optional[bool] = FieldInfo(alias="includeTemboCommitAttribution", default=None)

    desktop_notifications_enabled: Optional[bool] = FieldInfo(alias="desktopNotificationsEnabled", default=None)

    desktop_notification_preferences: Optional[DesktopNotificationPreferences] = FieldInfo(
        alias="desktopNotificationPreferences", default=None
    )

    has_desktop_app: Optional[bool] = FieldInfo(alias="hasDesktopApp", default=None)

    open_links_in_desktop_app: Optional[bool] = FieldInfo(alias="openLinksInDesktopApp", default=None)

    appearance_preferences: Optional[AppearancePreferences] = FieldInfo(alias="appearancePreferences", default=None)

    app_sidebar_preferences: Optional[AppSidebarPreferences] = FieldInfo(alias="appSidebarPreferences", default=None)

    diff_preferences: Optional[DiffPreferences] = FieldInfo(alias="diffPreferences", default=None)

    dashboard_preferences: Optional[DashboardPreferences] = FieldInfo(alias="dashboardPreferences", default=None)

    composer_preferences: Optional[ComposerPreferences] = FieldInfo(alias="composerPreferences", default=None)

    review_preferences: Optional[ReviewPreferences] = FieldInfo(alias="reviewPreferences", default=None)

    diff_light_theme: Optional[str] = FieldInfo(alias="diffLightTheme", default=None)

    diff_dark_theme: Optional[str] = FieldInfo(alias="diffDarkTheme", default=None)

    default_agent: Optional[str] = FieldInfo(alias="defaultAgent", default=None)

    follow_up_behavior: Optional[Literal["queue", "steer"]] = FieldInfo(alias="followUpBehavior", default=None)

    custom_system_prompt: Optional[str] = FieldInfo(alias="customSystemPrompt", default=None)
