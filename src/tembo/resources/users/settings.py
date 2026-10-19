# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from typing_extensions import Literal

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.users.setting_retrieve_response import SettingRetrieveResponse
from ...types.users.setting_update_response import SettingUpdateResponse
from ...types.users import setting_update_params

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingRetrieveResponse:
        """
        Retrieve user preferences without exposing stored credentials.

        Args:
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SettingRetrieveResponse: Retrieve user settings

        Example:
            ```python
            setting = client.users.settings.retrieve(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{userId}/settings", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingRetrieveResponse,
        )

    def update(
        self,
        user_id: str,
        *,
        auto_restart_vm: bool | Omit = omit,
        default_project_id: Optional[str] | Omit = omit,
        gpg_key: str | Omit = omit,
        include_tembo_commit_attribution: bool | Omit = omit,
        desktop_notifications_enabled: bool | Omit = omit,
        desktop_notification_preferences: setting_update_params.DesktopNotificationPreferences | Omit = omit,
        has_desktop_app: bool | Omit = omit,
        open_links_in_desktop_app: bool | Omit = omit,
        appearance_preferences: setting_update_params.AppearancePreferences | Omit = omit,
        app_sidebar_preferences: setting_update_params.AppSidebarPreferences | Omit = omit,
        diff_preferences: setting_update_params.DiffPreferences | Omit = omit,
        dashboard_preferences: setting_update_params.DashboardPreferences | Omit = omit,
        composer_preferences: setting_update_params.ComposerPreferences | Omit = omit,
        review_preferences: setting_update_params.ReviewPreferences | Omit = omit,
        diff_light_theme: str | Omit = omit,
        diff_dark_theme: str | Omit = omit,
        default_agent: Optional[str] | Omit = omit,
        follow_up_behavior: Literal["queue", "steer"] | Omit = omit,
        custom_system_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingUpdateResponse:
        """
        Configure personal agent/model and project defaults, system instructions, follow-up queue/steer behavior, VM restart, commit signing/attribution, notifications, themes, and review layout. Updates preserve unrelated settings.

        Args:
            user_id: Path parameter.
            auto_restart_vm: Automatically restart a session VM when needed.
            default_project_id: Default project environment for new sessions, or null to clear the preference.
            gpg_key: GPG signing key configuration. This value is returned by retrieveUserSettings.
            include_tembo_commit_attribution: Include Tembo attribution in agent-created commits.
            desktop_notifications_enabled: Enable or disable desktop notifications.
            desktop_notification_preferences: Notification types to show on the desktop.
            has_desktop_app: Whether the user has signed in to the Tembo desktop app.
            open_links_in_desktop_app: Open Tembo links from the browser in the desktop app when it is installed.
            appearance_preferences: Theme, accent, and appearance preferences. Nested updates preserve unrelated preferences.
            app_sidebar_preferences: Application sidebar layout preferences.
            diff_preferences: Diff display and comparison preferences.
            dashboard_preferences: Dashboard task-filter preferences.
            composer_preferences: Message composer preferences, including selected repositories.
            review_preferences: Code review file sorting, exclusions, bot comment visibility, and layout preferences.
            diff_light_theme: Diff syntax theme for light mode.
            diff_dark_theme: Diff syntax theme for dark mode.
            default_agent: Default coding agent and model key. Null clears the preference.
            follow_up_behavior: Default follow-up delivery: queue a new turn or steer an active turn.
            custom_system_prompt: Personal system instructions supplied to agents.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SettingUpdateResponse: Update user settings

        Example:
            ```python
            setting = client.users.settings.update(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            path_template("/v1/users/{userId}/settings", **{"userId": user_id}),
            body=maybe_transform(
                {
                    "auto_restart_vm": auto_restart_vm,
                    "default_project_id": default_project_id,
                    "gpg_key": gpg_key,
                    "include_tembo_commit_attribution": include_tembo_commit_attribution,
                    "desktop_notifications_enabled": desktop_notifications_enabled,
                    "desktop_notification_preferences": desktop_notification_preferences,
                    "has_desktop_app": has_desktop_app,
                    "open_links_in_desktop_app": open_links_in_desktop_app,
                    "appearance_preferences": appearance_preferences,
                    "app_sidebar_preferences": app_sidebar_preferences,
                    "diff_preferences": diff_preferences,
                    "dashboard_preferences": dashboard_preferences,
                    "composer_preferences": composer_preferences,
                    "review_preferences": review_preferences,
                    "diff_light_theme": diff_light_theme,
                    "diff_dark_theme": diff_dark_theme,
                    "default_agent": default_agent,
                    "follow_up_behavior": follow_up_behavior,
                    "custom_system_prompt": custom_system_prompt,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingUpdateResponse,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingRetrieveResponse:
        """
        Retrieve user preferences without exposing stored credentials.

        Args:
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SettingRetrieveResponse: Retrieve user settings

        Example:
            ```python
            setting = await client.users.settings.retrieve(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{userId}/settings", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingRetrieveResponse,
        )

    async def update(
        self,
        user_id: str,
        *,
        auto_restart_vm: bool | Omit = omit,
        default_project_id: Optional[str] | Omit = omit,
        gpg_key: str | Omit = omit,
        include_tembo_commit_attribution: bool | Omit = omit,
        desktop_notifications_enabled: bool | Omit = omit,
        desktop_notification_preferences: setting_update_params.DesktopNotificationPreferences | Omit = omit,
        has_desktop_app: bool | Omit = omit,
        open_links_in_desktop_app: bool | Omit = omit,
        appearance_preferences: setting_update_params.AppearancePreferences | Omit = omit,
        app_sidebar_preferences: setting_update_params.AppSidebarPreferences | Omit = omit,
        diff_preferences: setting_update_params.DiffPreferences | Omit = omit,
        dashboard_preferences: setting_update_params.DashboardPreferences | Omit = omit,
        composer_preferences: setting_update_params.ComposerPreferences | Omit = omit,
        review_preferences: setting_update_params.ReviewPreferences | Omit = omit,
        diff_light_theme: str | Omit = omit,
        diff_dark_theme: str | Omit = omit,
        default_agent: Optional[str] | Omit = omit,
        follow_up_behavior: Literal["queue", "steer"] | Omit = omit,
        custom_system_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingUpdateResponse:
        """
        Configure personal agent/model and project defaults, system instructions, follow-up queue/steer behavior, VM restart, commit signing/attribution, notifications, themes, and review layout. Updates preserve unrelated settings.

        Args:
            user_id: Path parameter.
            auto_restart_vm: Automatically restart a session VM when needed.
            default_project_id: Default project environment for new sessions, or null to clear the preference.
            gpg_key: GPG signing key configuration. This value is returned by retrieveUserSettings.
            include_tembo_commit_attribution: Include Tembo attribution in agent-created commits.
            desktop_notifications_enabled: Enable or disable desktop notifications.
            desktop_notification_preferences: Notification types to show on the desktop.
            has_desktop_app: Whether the user has signed in to the Tembo desktop app.
            open_links_in_desktop_app: Open Tembo links from the browser in the desktop app when it is installed.
            appearance_preferences: Theme, accent, and appearance preferences. Nested updates preserve unrelated preferences.
            app_sidebar_preferences: Application sidebar layout preferences.
            diff_preferences: Diff display and comparison preferences.
            dashboard_preferences: Dashboard task-filter preferences.
            composer_preferences: Message composer preferences, including selected repositories.
            review_preferences: Code review file sorting, exclusions, bot comment visibility, and layout preferences.
            diff_light_theme: Diff syntax theme for light mode.
            diff_dark_theme: Diff syntax theme for dark mode.
            default_agent: Default coding agent and model key. Null clears the preference.
            follow_up_behavior: Default follow-up delivery: queue a new turn or steer an active turn.
            custom_system_prompt: Personal system instructions supplied to agents.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SettingUpdateResponse: Update user settings

        Example:
            ```python
            setting = await client.users.settings.update(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            path_template("/v1/users/{userId}/settings", **{"userId": user_id}),
            body=await async_maybe_transform(
                {
                    "auto_restart_vm": auto_restart_vm,
                    "default_project_id": default_project_id,
                    "gpg_key": gpg_key,
                    "include_tembo_commit_attribution": include_tembo_commit_attribution,
                    "desktop_notifications_enabled": desktop_notifications_enabled,
                    "desktop_notification_preferences": desktop_notification_preferences,
                    "has_desktop_app": has_desktop_app,
                    "open_links_in_desktop_app": open_links_in_desktop_app,
                    "appearance_preferences": appearance_preferences,
                    "app_sidebar_preferences": app_sidebar_preferences,
                    "diff_preferences": diff_preferences,
                    "dashboard_preferences": dashboard_preferences,
                    "composer_preferences": composer_preferences,
                    "review_preferences": review_preferences,
                    "diff_light_theme": diff_light_theme,
                    "diff_dark_theme": diff_dark_theme,
                    "default_agent": default_agent,
                    "follow_up_behavior": follow_up_behavior,
                    "custom_system_prompt": custom_system_prompt,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingUpdateResponse,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.retrieve = to_raw_response_wrapper(
            settings.retrieve,
        )
        self.update = to_raw_response_wrapper(
            settings.update,
        )


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.retrieve = async_to_raw_response_wrapper(
            settings.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            settings.update,
        )


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.retrieve = to_streamed_response_wrapper(
            settings.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            settings.update,
        )


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.retrieve = async_to_streamed_response_wrapper(
            settings.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            settings.update,
        )
