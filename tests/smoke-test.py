# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke test: calls every generated operation once to confirm the SDK can reach each endpoint.
# Run it from this repo with `python tests/smoke-test.py`. The generator also runs this file
# against a mock server and reads the JSON report produced via SCALAR_SMOKE_REPORT.
from __future__ import annotations

import json
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, TypedDict

from tembo import Tembo

# The shared smoke-test runner injects base URL and credentials through the same
# environment variables the generated client reads in normal use.
client = Tembo(max_retries=2, timeout=10)


class SmokeResult(TypedDict, total=False):
    operation: str
    method: str
    path: str
    label: str
    status: str
    durationMs: int
    error: str


class _SmokeCaseBase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


# `label` says which of an operation's two calls this is — "required params" or "all params".
# It sits in a total=False extension because it is absent when the operation contributed a
# single case, while the fields above are always present.
class SmokeCase(_SmokeCaseBase, total=False):
    label: str


def _smoke_case_0() -> None:
    api_key = client.api_keys.list(
        limit=50,
    )


def _smoke_case_1() -> None:
    api_key = client.api_keys.list(
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_2() -> None:
    api_key = client.api_keys.create()


def _smoke_case_3() -> None:
    api_key = client.api_keys.create(
        expires_at="2024-01-01T00:00:00.000Z",
        name="x",
    )


def _smoke_case_4() -> None:
    api_key = client.api_keys.retrieve(
        api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_5() -> None:
    api_key = client.api_keys.update(
        api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
    )


def _smoke_case_6() -> None:
    api_key = client.api_keys.delete(
        api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_7() -> None:
    skill = client.skills.list(
        limit=50,
        source="organization",
    )


def _smoke_case_8() -> None:
    skill = client.skills.list(
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        names=["name"],
        repository_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        project_id="project_id",
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        search="search",
        source="organization",
    )


def _smoke_case_9() -> None:
    skill = client.skills.create(
        description="",
        name="x",
        files=[{"content": "", "filename": "x"}],
    )


def _smoke_case_10() -> None:
    skill = client.skills.retrieve(
        skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_11() -> None:
    skill = client.skills.update(
        skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_12() -> None:
    skill = client.skills.update(
        skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        description="",
        name="x",
        files=[{"content": "", "filename": "x"}],
    )


def _smoke_case_13() -> None:
    skill = client.skills.delete(
        skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_14() -> None:
    marketplace = client.skills.marketplace.list(
        limit=50,
    )


def _smoke_case_15() -> None:
    marketplace = client.skills.marketplace.list(
        cursor="",
        limit=50,
        search="search",
    )


def _smoke_case_16() -> None:
    marketplace = client.skills.marketplace.retrieve(
        skill_id="skillId",
        source="source",
    )


def _smoke_case_17() -> None:
    insight = client.insights.retrieve(
        range="1y",
    )


def _smoke_case_18() -> None:
    insight = client.insights.update(
        enabled=False,
    )


def _smoke_case_19() -> None:
    insight = client.insights.list_members(
        limit=50,
        range="1y",
    )


def _smoke_case_20() -> None:
    insight = client.insights.list_members(
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        range="1y",
    )


def _smoke_case_21() -> None:
    insight = client.insights.list_repositories(
        limit=50,
        range="1y",
    )


def _smoke_case_22() -> None:
    insight = client.insights.list_repositories(
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        range="1y",
    )


def _smoke_case_23() -> None:
    organization = client.organizations.create(
        name="x",
    )


def _smoke_case_24() -> None:
    organization = client.organizations.create(
        name="x",
        slug="x",
    )


def _smoke_case_25() -> None:
    organization = client.organizations.retrieve(
        organization_id="organizationId",
    )


def _smoke_case_26() -> None:
    organization = client.organizations.update(
        organization_id="organizationId",
    )


def _smoke_case_27() -> None:
    organization = client.organizations.update(
        organization_id="organizationId",
        name="x",
        slug="x",
        onboarding_completed=False,
    )


def _smoke_case_28() -> None:
    organization = client.organizations.delete(
        organization_id="organizationId",
    )


def _smoke_case_29() -> None:
    member = client.organizations.members.list(
        organization_id="organizationId",
        limit=50,
        status="active",
    )


def _smoke_case_30() -> None:
    member = client.organizations.members.list(
        organization_id="organizationId",
        cursor="cursor",
        limit=50,
        search="search",
        status="active",
    )


def _smoke_case_31() -> None:
    member = client.organizations.members.create(
        organization_id="organizationId",
        email_address="user@example.com",
        role="org:member",
    )


def _smoke_case_32() -> None:
    member = client.organizations.members.retrieve(
        organization_id="organizationId",
        member_id="memberId",
    )


def _smoke_case_33() -> None:
    member = client.organizations.members.update(
        organization_id="organizationId",
        member_id="memberId",
        role="org:admin",
    )


def _smoke_case_34() -> None:
    member = client.organizations.members.delete(
        organization_id="organizationId",
        member_id="memberId",
    )


def _smoke_case_35() -> None:
    secret = client.organizations.secrets.list(
        organization_id="organizationId",
        limit=50,
    )


def _smoke_case_36() -> None:
    secret = client.organizations.secrets.list(
        organization_id="organizationId",
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        search="search",
    )


def _smoke_case_37() -> None:
    secret = client.organizations.secrets.create(
        organization_id="organizationId",
        key="x",
        value="x",
    )


def _smoke_case_38() -> None:
    secret = client.organizations.secrets.retrieve(
        organization_id="organizationId",
        secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_39() -> None:
    secret = client.organizations.secrets.update(
        organization_id="organizationId",
        secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_40() -> None:
    secret = client.organizations.secrets.update(
        organization_id="organizationId",
        secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        key="x",
        value="x",
    )


def _smoke_case_41() -> None:
    secret = client.organizations.secrets.delete(
        organization_id="organizationId",
        secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_42() -> None:
    setting = client.organizations.settings.retrieve(
        organization_id="organizationId",
    )


def _smoke_case_43() -> None:
    setting = client.organizations.settings.update(
        organization_id="organizationId",
    )


def _smoke_case_44() -> None:
    setting = client.organizations.settings.update(
        organization_id="organizationId",
        amp_api_key="",
        anthropic_api_key="",
        aws_bedrock_access_key_id="",
        aws_bedrock_region="",
        aws_bedrock_secret_access_key="",
        clone_depth=1,
        commit_instructions="",
        cursor_api_key="",
        custom_system_prompt="",
        default_agent="",
        default_keep_alive_minutes=0,
        default_sandbox_size="nano",
        delete_branch_when_pr_closed=False,
        draft_prs=False,
        enable_coderabbit_bot=False,
        enable_cursor_bot=False,
        enable_gemini_code_assist_bot=False,
        enable_github_actions_bot=False,
        enable_graphite_bot=False,
        enable_greptile_bot=False,
        experimental_mcp=False,
        feature_mention_author=False,
        gcp_vertex_ai_location="",
        gcp_vertex_ai_project="",
        gcp_vertex_ai_service_account_json="",
        kernel_api_key="",
        max_bot_reviews=0,
        max_solutions=0,
        openai_api_key="",
        xai_api_key="",
        openrouter_api_key="",
        pg_stat_statements_reset_frequency="",
        pm_system_prompt="",
        pr_title_instructions="",
        pull_request_insights_enabled=False,
        should_sign_commits=False,
        slack_review_on_tembo=False,
        slow_query_threshold_ms=0,
        ssh_public_keys="",
        weekly_report_enabled=False,
    )


def _smoke_case_45() -> None:
    setting = client.organizations.settings.validate_credentials(
        organization_id="organizationId",
        provider="anthropic",
        api_key="",
    )


def _smoke_case_46() -> None:
    subscription = client.organizations.subscriptions.retrieve(
        organization_id="organizationId",
    )


def _smoke_case_47() -> None:
    mcp_connection = client.mcp_connections.list(
        limit=50,
    )


def _smoke_case_48() -> None:
    mcp_connection = client.mcp_connections.list(
        connected=True,
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        search="search",
    )


def _smoke_case_49() -> None:
    mcp_connection = client.mcp_connections.create(
        name="x",
        args=[],
        command="x",
        type="stdio",
        visibility="shared",
    )


def _smoke_case_50() -> None:
    mcp_connection = client.mcp_connections.create(
        name="x",
        args=[],
        command="x",
        env={},
        type="stdio",
        visibility="shared",
    )


def _smoke_case_51() -> None:
    mcp_connection = client.mcp_connections.retrieve(
        mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_52() -> None:
    mcp_connection = client.mcp_connections.update(
        mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        type="remote",
    )


def _smoke_case_53() -> None:
    mcp_connection = client.mcp_connections.update(
        mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        server_url="https://example.com",
        type="remote",
        auth_type="oauth",
        client_id="x",
        client_secret="x",
        headers={},
        oauth_registration="automatic",
        scope="x",
    )


def _smoke_case_54() -> None:
    mcp_connection = client.mcp_connections.delete(
        mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_55() -> None:
    mcp_connection = client.mcp_connections.authorize(
        mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_56() -> None:
    mcp_connection = client.mcp_connections.test(
        mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_57() -> None:
    artifact = client.artifacts.list(
        limit=50,
    )


def _smoke_case_58() -> None:
    artifact = client.artifacts.list(
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        job_id="job_id",
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        types=["PullRequest"],
    )


def _smoke_case_59() -> None:
    artifact = client.artifacts.create(
        title="x",
        output={"type": "html", "content": "x"},
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_60() -> None:
    artifact = client.artifacts.create(
        title="x",
        description="x",
        category="code_walkthrough",
        output={"type": "html", "content": "x", "file_name": "x"},
        related_pull_request_urls=["https://example.com"],
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_61() -> None:
    artifact = client.artifacts.retrieve(
        artifact_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_62() -> None:
    artifact = client.artifacts.delete(
        artifact_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_63() -> None:
    message = client.messages.list(
        limit=50,
    )


def _smoke_case_64() -> None:
    message = client.messages.list(
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        thread_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_65() -> None:
    message = client.messages.create(
        content="x",
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_66() -> None:
    message = client.messages.create(
        artifact_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        content="x",
        mcp_servers=["x"],
        pull_request_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        agent_options={"reasoning_level": "x", "mode": "normal", "speed": "normal", "goal": {}, "ultracode": False},
        delivery_mode="queue",
        rich_content={
            "type": "doc",
            "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Hello"}]}],
        },
        slash_command={"command": "x", "arguments": ""},
    )


def _smoke_case_67() -> None:
    message = client.messages.retrieve(
        message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_68() -> None:
    message = client.messages.update(
        message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_69() -> None:
    message = client.messages.update(
        message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        content="x",
        rich_content={
            "type": "doc",
            "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Hello"}]}],
        },
    )


def _smoke_case_70() -> None:
    message = client.messages.delete(
        message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_71() -> None:
    model = client.models.list(
        limit=50,
    )


def _smoke_case_72() -> None:
    model = client.models.list(
        cursor="claude-opus-5-5",
        limit=50,
    )


def _smoke_case_73() -> None:
    model = client.models.update(
        model_name="claude-opus-5-5",
    )


def _smoke_case_74() -> None:
    model = client.models.update(
        model_name="claude-opus-5-5",
        enabled=False,
        inference_provider="TemboManagedInference",
    )


def _smoke_case_75() -> None:
    runtime = client.runtimes.list(
        limit=50,
    )


def _smoke_case_76() -> None:
    runtime = client.runtimes.list(
        cursor="claudeCode",
        limit=50,
    )


def _smoke_case_77() -> None:
    user = client.users.me()


def _smoke_case_78() -> None:
    user = client.users.retrieve(
        user_id="userId",
    )


def _smoke_case_79() -> None:
    setting = client.users.settings.retrieve(
        user_id="userId",
    )


def _smoke_case_80() -> None:
    setting = client.users.settings.update(
        user_id="userId",
    )


def _smoke_case_81() -> None:
    setting = client.users.settings.update(
        user_id="userId",
        auto_restart_vm=False,
        default_project_id="x",
        gpg_key="",
        include_tembo_commit_attribution=False,
        desktop_notifications_enabled=False,
        desktop_notification_preferences={
            "awaiting_approval": False,
            "pull_request_opened": False,
            "pull_request_review_requested": False,
        },
        has_desktop_app=False,
        open_links_in_desktop_app=False,
        appearance_preferences={"app_theme": "light", "accent_theme": {}},
        app_sidebar_preferences={
            "open": False,
            "session_owner_scope": "mine",
            "session_sort_by": "createdAt",
            "session_organization": "list",
            "show_archived_sessions": False,
            "width": 0,
            "right_sidebar": {},
        },
        diff_preferences={
            "style": "unified",
            "indicators": "classic",
            "overflow": "scroll",
            "show_line_numbers": False,
            "expand_unchanged": False,
            "show_file_tree": False,
            "file_tree_position": "left",
            "file_tree_view": "list",
            "light_theme": "",
            "dark_theme": "",
        },
        dashboard_preferences={"task_filters": {}},
        composer_preferences={"last_selected_repositories": [{"id": ""}]},
        review_preferences={
            "file_sort_mode": "tree",
            "excluded_file_patterns": ["x"],
            "sections": {},
            "hide_bot_comments": False,
            "layout": {},
        },
        diff_light_theme="",
        diff_dark_theme="",
        default_agent="",
        follow_up_behavior="queue",
        custom_system_prompt="",
    )


def _smoke_case_82() -> None:
    connected_account = client.users.connected_accounts.list(
        user_id="userId",
        limit=50,
    )


def _smoke_case_83() -> None:
    connected_account = client.users.connected_accounts.list(
        user_id="userId",
        cursor="cursor",
        limit=50,
    )


def _smoke_case_84() -> None:
    connected_account = client.users.connected_accounts.retrieve(
        user_id="userId",
        connected_account_id="connectedAccountId",
    )


def _smoke_case_85() -> None:
    subscription = client.users.subscriptions.retrieve(
        user_id="userId",
    )


def _smoke_case_86() -> None:
    environment_variable = client.users.environment_variables.list(
        user_id="userId",
    )


def _smoke_case_87() -> None:
    environment_variable = client.users.environment_variables.create(
        user_id="userId",
        key="x",
        value="x",
    )


def _smoke_case_88() -> None:
    environment_variable = client.users.environment_variables.delete(
        user_id="userId",
        environment_variable_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_89() -> None:
    client.users.profile_picture.retrieve(
        user_id="userId",
    )


def _smoke_case_90() -> None:
    profile_picture = client.users.profile_picture.update(
        user_id="userId",
        file=b"file",
    )


def _smoke_case_91() -> None:
    profile_picture = client.users.profile_picture.delete(
        user_id="userId",
    )


def _smoke_case_92() -> None:
    session = client.sessions.list(
        limit=50,
        include_archived=True,
        include_total=False,
        sort_by="lastQueuedAt",
        state="all",
    )


def _smoke_case_93() -> None:
    session = client.sessions.list(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        created_by=["created_by"],
        created_after="2024-01-01T00:00:00.000Z",
        cursor="cursor",
        limit=50,
        exclude_pinned=True,
        external_ids=["external_id"],
        has_project=True,
        include_archived=True,
        include_total=False,
        participant=["participant"],
        pending_reviewer_keys=["pending_reviewer_key"],
        project_ids=["project_id"],
        pull_request_statuses=["open"],
        repository_ids=["repository_id"],
        search="search",
        sort_by="lastQueuedAt",
        source_ids=["source_id"],
        source_types=["source_type"],
        state="all",
    )


def _smoke_case_94() -> None:
    session = client.sessions.create(
        agent="claudeCode:claude-fable-5-1",
        base_branch="main",
        mcp_servers=[],
        project_id="your-project-id",
        target_branch="main",
        visibility="private",
        code_repository_ids=["123e4567-e89b-12d3-a456-426614174000"],
        description="Fix the authentication bug in the login component",
    )


def _smoke_case_95() -> None:
    session = client.sessions.create(
        agent="claudeCode:claude-fable-5-1",
        base_branch="main",
        mcp_servers=[],
        project_id="your-project-id",
        sandbox_size="nano",
        target_branch="main",
        visibility="private",
        agent_options={"reasoning_level": "x", "mode": "normal", "speed": "normal", "goal": {}, "ultracode": False},
        branch_name="x",
        code_repository_ids=["123e4567-e89b-12d3-a456-426614174000"],
        description="Fix the authentication bug in the login component",
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        rich_content={"type": "x", "text": "", "attrs": {}, "marks": [{"type": "x"}], "content": []},
        pull_request_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        queue_right_away=False,
        automatic_sizing=False,
        session_mode="chat",
        startup_agent="claudeCode",
    )


def _smoke_case_96() -> None:
    session = client.sessions.retrieve(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_97() -> None:
    session = client.sessions.update(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_98() -> None:
    session = client.sessions.update(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        memory_mb=1024,
        agent="x",
        agent_options={"reasoning_level": "x", "mode": "normal", "speed": "normal", "goal": {}, "ultracode": False},
        base_branch="x",
        branch_name="x",
        description="x",
        rich_content={"type": "x", "text": "", "attrs": {}, "marks": [{"type": "x"}], "content": []},
        level=0,
        mcp_servers=["x"],
        mode="normal",
        project_id="",
        sandbox_size="nano",
        target_branch="x",
        title="x",
        visibility="private",
    )


def _smoke_case_99() -> None:
    session = client.sessions.delete(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_100() -> None:
    session = client.sessions.fork(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        queue_right_away=True,
    )


def _smoke_case_101() -> None:
    session = client.sessions.fork(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        prompt="x",
        title="x",
        queue_right_away=True,
    )


def _smoke_case_102() -> None:
    session = client.sessions.stop(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_103() -> None:
    session = client.sessions.stop(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cancel_queued=True,
    )


def _smoke_case_104() -> None:
    session = client.sessions.list_events(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_105() -> None:
    session = client.sessions.list_events(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cursor="cursor",
        limit=50,
        message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        after="after",
    )


def _smoke_case_106() -> None:
    source = client.sessions.sources.list(
        limit=50,
        include_total=False,
    )


def _smoke_case_107() -> None:
    source = client.sessions.sources.list(
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        enabled=True,
        include_total=False,
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        search="search",
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        types=["type"],
    )


def _smoke_case_108() -> None:
    source = client.sessions.sources.retrieve(
        source_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_109() -> None:
    diff = client.sessions.diffs.list(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_110() -> None:
    diff = client.sessions.diffs.list(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        has_changes=True,
    )


def _smoke_case_111() -> None:
    diff = client.sessions.diffs.retrieve(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        diff_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_112() -> None:
    input = client.sessions.inputs.list(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_113() -> None:
    input = client.sessions.inputs.update(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        input_id="inputId",
        answers={},
    )


def _smoke_case_114() -> None:
    queue = client.sessions.queue.update(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        message_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
    )


def _smoke_case_115() -> None:
    command = client.sessions.commands.list(
        session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_116() -> None:
    project = client.projects.update_defaults(
        project_id="x",
        sandbox_size="nano",
    )


def _smoke_case_117() -> None:
    project = client.projects.list(
        limit=50,
    )


def _smoke_case_118() -> None:
    project = client.projects.list(
        cursor="cursor",
        limit=50,
        default_only="true",
        search="search",
    )


def _smoke_case_119() -> None:
    project = client.projects.create(
        name="x",
        sizes=["medium"],
        resource_settings={"automaticSizing": False},
    )


def _smoke_case_120() -> None:
    project = client.projects.create(
        description="",
        name="x",
        setup_script="",
        code_repository_ids=["x"],
        agent_instructions="",
        color="neutral",
        icon="folder",
        include_deps=False,
        include_skills=False,
        onboarding_default=False,
        run_now=False,
        schedule={"cron": "x", "timezone": "x"},
        sizes=["medium"],
        resource_settings={"automaticSizing": False},
    )


def _smoke_case_121() -> None:
    project = client.projects.retrieve(
        project_id="projectId",
    )


def _smoke_case_122() -> None:
    project = client.projects.update(
        project_id="projectId",
        resource_settings={"automaticSizing": False},
    )


def _smoke_case_123() -> None:
    project = client.projects.update(
        project_id="projectId",
        description="",
        name="x",
        setup_script="",
        code_repository_ids=["x"],
        agent_instructions="",
        color="neutral",
        icon="folder",
        include_deps=False,
        include_skills=False,
        resource_settings={"automaticSizing": False},
        default_for_sizes=["nano"],
        environment_variables={},
        schedule={"cron": "x", "enabled": False, "timezone": "x"},
        sizes=["nano"],
        warm_pool_schedule={"timezone": "x", "days": [0], "start_time": "", "end_time": ""},
        warm_pool_enabled=False,
    )


def _smoke_case_124() -> None:
    project = client.projects.delete(
        project_id="projectId",
    )


def _smoke_case_125() -> None:
    project = client.projects.duplicate(
        project_id="projectId",
    )


def _smoke_case_126() -> None:
    environment_variable = client.projects.environment_variables.list(
        project_id="projectId",
    )


def _smoke_case_127() -> None:
    environment_variable = client.projects.environment_variables.create(
        project_id="projectId",
        secrets=[{"key": "", "value": "x"}],
    )


def _smoke_case_128() -> None:
    environment_variable = client.projects.environment_variables.delete(
        project_id="projectId",
        key="key",
    )


def _smoke_case_129() -> None:
    snapshot = client.projects.snapshots.list(
        project_id="projectId",
        limit=50,
    )


def _smoke_case_130() -> None:
    snapshot = client.projects.snapshots.list(
        project_id="projectId",
        cursor="cursor",
        limit=50,
    )


def _smoke_case_131() -> None:
    snapshot = client.projects.snapshots.retrieve(
        project_id="projectId",
        snapshot_id="snapshotId",
    )


def _smoke_case_132() -> None:
    snapshot = client.projects.snapshots.update(
        project_id="projectId",
        snapshot_id="snapshotId",
    )


def _smoke_case_133() -> None:
    snapshot = client.projects.snapshots.update(
        project_id="projectId",
        snapshot_id="snapshotId",
        name="",
        pinned=False,
    )


def _smoke_case_134() -> None:
    snapshot = client.projects.snapshots.delete(
        project_id="projectId",
        snapshot_id="snapshotId",
    )


def _smoke_case_135() -> None:
    build = client.projects.builds.list(
        project_id="projectId",
        limit=50,
    )


def _smoke_case_136() -> None:
    build = client.projects.builds.list(
        project_id="projectId",
        cursor="cursor",
        limit=50,
    )


def _smoke_case_137() -> None:
    build = client.projects.builds.create(
        project_id="projectId",
    )


def _smoke_case_138() -> None:
    build = client.projects.builds.create(
        project_id="projectId",
        sizes=["nano"],
        snapshot_id="x",
    )


def _smoke_case_139() -> None:
    build = client.projects.builds.retrieve(
        project_id="projectId",
        build_id="buildId",
    )


def _smoke_case_140() -> None:
    build = client.projects.builds.cancel(
        project_id="projectId",
        build_id="buildId",
    )


def _smoke_case_141() -> None:
    schedule = client.projects.schedules.list(
        project_id="projectId",
        limit=50,
    )


def _smoke_case_142() -> None:
    schedule = client.projects.schedules.list(
        project_id="projectId",
        cursor="cursor",
        limit=50,
    )


def _smoke_case_143() -> None:
    schedule = client.projects.schedules.create(
        project_id="projectId",
        cron="x",
    )


def _smoke_case_144() -> None:
    schedule = client.projects.schedules.create(
        project_id="projectId",
        cron="x",
        timezone="x",
    )


def _smoke_case_145() -> None:
    schedule = client.projects.schedules.retrieve(
        project_id="projectId",
        schedule_id="scheduleId",
    )


def _smoke_case_146() -> None:
    schedule = client.projects.schedules.update(
        project_id="projectId",
        schedule_id="scheduleId",
    )


def _smoke_case_147() -> None:
    schedule = client.projects.schedules.update(
        project_id="projectId",
        schedule_id="scheduleId",
        cron="x",
        enabled=False,
        timezone="x",
    )


def _smoke_case_148() -> None:
    schedule = client.projects.schedules.delete(
        project_id="projectId",
        schedule_id="scheduleId",
    )


def _smoke_case_149() -> None:
    pin = client.pins.list(
        limit=50,
    )


def _smoke_case_150() -> None:
    pin = client.pins.list(
        cursor="cursor",
        limit=50,
    )


def _smoke_case_151() -> None:
    pin = client.pins.create(
        type="session",
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_152() -> None:
    pin = client.pins.create(
        type="session",
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        placement={"target": {"type": "session", "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}, "position": "before"},
    )


def _smoke_case_153() -> None:
    pin = client.pins.update(
        resource_type="session",
        resource_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        placement={"target": {"type": "session", "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}, "position": "before"},
    )


def _smoke_case_154() -> None:
    pin = client.pins.delete(
        resource_type="session",
        resource_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_155() -> None:
    pull_request = client.pull_requests.list(
        limit=50,
    )


def _smoke_case_156() -> None:
    pull_request = client.pull_requests.list(
        author_ids=["author_id"],
        created_after="2024-01-01T00:00:00.000Z",
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        exclude_author_ids=["exclude_author_id"],
        exclude_organization_name="exclude_organization_name",
        exclude_returned_author_ids=["exclude_returned_author_id"],
        exclude_reviewer_ids=["exclude_reviewer_id"],
        has_tembo_session=True,
        include_authors=True,
        include_total=True,
        include_stacks=True,
        repository_ids=["repository_id"],
        reviewer_ids=["reviewer_id"],
        merged_after="2024-01-01T00:00:00.000Z",
        search="search",
        sort_by="createdAt",
        state="open",
        updated_after="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_157() -> None:
    pull_request = client.pull_requests.retrieve(
        pull_request_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_158() -> None:
    agent = client.agents.list(
        limit=50,
    )


def _smoke_case_159() -> None:
    agent = client.agents.list(
        cursor="cursor",
        limit=50,
        ids="ids",
        search="search",
        archived=True,
        sort="latestRun",
        status="status",
        integration="integration",
        author="author",
    )


def _smoke_case_160() -> None:
    agent = client.agents.create()


def _smoke_case_161() -> None:
    agent = client.agents.create(
        name="x",
        instructions={
            "type": "doc",
            "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Hello"}]}],
        },
        mcp_servers=["x"],
        agent="x",
        agent_options={"reasoning_level": "x", "mode": "normal", "speed": "normal", "goal": {}, "ultracode": False},
        sandbox_size="nano",
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        artifact_type="PullRequest",
        repository_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        triggers=[{"name": "x"}],
        schedules=[{"cron": "x"}],
        template_name="addTestCoverage",
        source_agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_162() -> None:
    agent = client.agents.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_163() -> None:
    agent = client.agents.update(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_164() -> None:
    agent = client.agents.update(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        expected_updated_at="2024-01-01T00:00:00.000Z",
        name="x",
        key="x",
        instructions={
            "type": "doc",
            "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Hello"}]}],
        },
        mcp_servers=["x"],
        agent="x",
        agent_options={"reasoning_level": "x", "mode": "normal", "speed": "normal", "goal": {}, "ultracode": False},
        user_state={},
        sandbox_size="nano",
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        template_id="",
        script="",
        artifact_type="PullRequest",
        repository_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        enabled=False,
        archived=False,
    )


def _smoke_case_165() -> None:
    agent = client.agents.delete(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_166() -> None:
    template = client.agents.templates.list(
        limit=50,
    )


def _smoke_case_167() -> None:
    template = client.agents.templates.list(
        cursor="addTestCoverage",
        limit=50,
    )


def _smoke_case_168() -> None:
    template = client.agents.templates.retrieve(
        template_name="templateName",
    )


def _smoke_case_169() -> None:
    schedule = client.agents.schedules.list(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_170() -> None:
    schedule = client.agents.schedules.list(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_171() -> None:
    schedule = client.agents.schedules.create(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cron="x",
    )


def _smoke_case_172() -> None:
    schedule = client.agents.schedules.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_173() -> None:
    schedule = client.agents.schedules.update(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cron="x",
    )


def _smoke_case_174() -> None:
    schedule = client.agents.schedules.delete(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_175() -> None:
    trigger = client.agents.triggers.list(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_176() -> None:
    trigger = client.agents.triggers.list(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_177() -> None:
    trigger = client.agents.triggers.create(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
    )


def _smoke_case_178() -> None:
    trigger = client.agents.triggers.create(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        integration_type="x",
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        filters={
            "projects": [""],
            "boards": [""],
            "statuses": [""],
            "assigned_to": [""],
            "labels": [""],
            "include_new_issues": False,
        },
    )


def _smoke_case_179() -> None:
    trigger = client.agents.triggers.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_180() -> None:
    trigger = client.agents.triggers.update(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
    )


def _smoke_case_181() -> None:
    trigger = client.agents.triggers.update(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        filters={
            "projects": [""],
            "boards": [""],
            "statuses": [""],
            "assigned_to": [""],
            "labels": [""],
            "include_new_issues": False,
        },
    )


def _smoke_case_182() -> None:
    trigger = client.agents.triggers.delete(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_183() -> None:
    run = client.agents.runs.list(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_184() -> None:
    run = client.agents.runs.list(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_185() -> None:
    run = client.agents.runs.create(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_186() -> None:
    run = client.agents.runs.create(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        body={},
    )


def _smoke_case_187() -> None:
    run = client.agents.runs.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_188() -> None:
    content_revision = client.agents.content_revisions.list(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_189() -> None:
    content_revision = client.agents.content_revisions.list(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cursor="cursor",
        limit=50,
    )


def _smoke_case_190() -> None:
    content_revision = client.agents.content_revisions.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        version=1,
    )


def _smoke_case_191() -> None:
    content_revision = client.agents.content_revisions.restore(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        version=1,
        expected_content_version=1,
    )


def _smoke_case_192() -> None:
    repository = client.repositories.list(
        limit=50,
        enabled="all",
        order="desc",
        sort="pullRequests",
    )


def _smoke_case_193() -> None:
    repository = client.repositories.list(
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        enabled="all",
        ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        order="desc",
        search="search",
        sort="pullRequests",
    )


def _smoke_case_194() -> None:
    repository = client.repositories.retrieve(
        repository_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_195() -> None:
    repository = client.repositories.update(
        repository_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        enabled=False,
    )


def _smoke_case_196() -> None:
    repository = client.repositories.update(
        repository_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        enabled=False,
        base_branch="x",
        target_branch="x",
    )


def _smoke_case_197() -> None:
    integration = client.integrations.list(
        limit=50,
        include_total=False,
    )


def _smoke_case_198() -> None:
    integration = client.integrations.list(
        cursor="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
        enabled=True,
        has_enabled_repositories=True,
        ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        search="search",
        type=["type"],
        created_after="2024-01-01T00:00:00.000Z",
        exclude_organization_name="exclude_organization_name",
        include_total=False,
    )


def _smoke_case_199() -> None:
    integration = client.integrations.create(
        environment="x",
        role_arn="x",
        type="aws",
    )


def _smoke_case_200() -> None:
    integration = client.integrations.retrieve(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_201() -> None:
    integration = client.integrations.update(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        settings={},
    )


def _smoke_case_202() -> None:
    integration = client.integrations.update(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        settings={
            "default_repository_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
            "disallowed_slack_channel_ids": ["x"],
            "instant_solve": False,
            "sentry_environments": ["x"],
        },
    )


def _smoke_case_203() -> None:
    integration = client.integrations.delete(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_204() -> None:
    integration = client.integrations.authorize(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_205() -> None:
    integration = client.integrations.authorize(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        return_url="https://example.com",
        capability="confluenceTriggers",
    )


def _smoke_case_206() -> None:
    integration = client.integrations.test(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_207() -> None:
    integration = client.integrations.sync(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        mode="queued",
    )


def _smoke_case_208() -> None:
    integration = client.integrations.sync_all()


def _smoke_case_209() -> None:
    integration = client.integrations.retrieve_sync_status()


def _smoke_case_210() -> None:
    integration = client.integrations.retrieve_sync_status(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_211() -> None:
    integration = client.integrations.retrieve_rate_limit(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_212() -> None:
    integration = client.integrations.list_sentry_environments(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_213() -> None:
    integration = client.integrations.list_sentry_environments(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cursor="cursor",
        limit=50,
    )


def _smoke_case_214() -> None:
    integration = client.integrations.list_slack_channels(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=50,
    )


def _smoke_case_215() -> None:
    integration = client.integrations.list_slack_channels(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cursor="cursor",
        limit=50,
        search="search",
    )


def _smoke_case_216() -> None:
    provider = client.integrations.providers.list(
        limit=50,
    )


def _smoke_case_217() -> None:
    provider = client.integrations.providers.list(
        cursor="cursor",
        limit=50,
        return_url="https://example.com",
    )


def _smoke_case_218() -> None:
    provider = client.integrations.providers.discover_snyk_organizations(
        client_id="x",
        client_secret="x",
        limit=50,
    )


def _smoke_case_219() -> None:
    provider = client.integrations.providers.discover_snyk_organizations(
        client_id="x",
        client_secret="x",
        cursor="x",
        limit=50,
    )


def _smoke_case_220() -> None:
    trigger = client.integrations.triggers.list(
        limit=50,
    )


def _smoke_case_221() -> None:
    trigger = client.integrations.triggers.list(
        cursor="cursor",
        limit=50,
    )


def _smoke_case_222() -> None:
    trigger = client.integrations.triggers.retrieve(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        trigger_name="triggerName",
    )


def _smoke_case_223() -> None:
    trigger = client.integrations.triggers.list_filter_options(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        trigger_name="triggerName",
        field="field",
        limit=50,
    )


def _smoke_case_224() -> None:
    trigger = client.integrations.triggers.list_filter_options(
        integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        trigger_name="triggerName",
        field="field",
        cursor="cursor",
        limit=50,
        search="search",
    )


def _smoke_case_225() -> None:
    billing = client.billing.retrieve()


def _smoke_case_226() -> None:
    billing = client.billing.list_usage(
        limit=50,
    )


def _smoke_case_227() -> None:
    billing = client.billing.list_usage(
        cursor="cursor",
        limit=50,
        type="all",
        session_id="session_id",
        created_after="2024-01-01T00:00:00.000Z",
        created_before="2024-01-01T00:00:00.000Z",
        created_by=["created_by"],
        models=["model"],
    )


def _smoke_case_228() -> None:
    live = client.live.authorize()


def _smoke_case_229() -> None:
    def _probe() -> None:
        with client.live.connect() as socket:
            try:
                socket.recv()
            finally:
                socket.close(code=1000, reason="smoke-test")

    _probe()


cases: list[SmokeCase] = [
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/api-keys",
        "label": "required params",
        "run": _smoke_case_0,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/api-keys",
        "label": "all params",
        "run": _smoke_case_1,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/api-keys",
        "label": "required params",
        "run": _smoke_case_2,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/api-keys",
        "label": "all params",
        "run": _smoke_case_3,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/api-keys/{apiKeyId}",
        "run": _smoke_case_4,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/api-keys/{apiKeyId}",
        "run": _smoke_case_5,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/api-keys/{apiKeyId}",
        "run": _smoke_case_6,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/skills",
        "label": "required params",
        "run": _smoke_case_7,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/skills",
        "label": "all params",
        "run": _smoke_case_8,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/skills",
        "run": _smoke_case_9,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/skills/{skillId}",
        "run": _smoke_case_10,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/skills/{skillId}",
        "label": "required params",
        "run": _smoke_case_11,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/skills/{skillId}",
        "label": "all params",
        "run": _smoke_case_12,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/skills/{skillId}",
        "run": _smoke_case_13,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/skills/marketplace",
        "label": "required params",
        "run": _smoke_case_14,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/skills/marketplace",
        "label": "all params",
        "run": _smoke_case_15,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/skills/marketplace/{skillId}",
        "run": _smoke_case_16,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/insights",
        "run": _smoke_case_17,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/insights",
        "run": _smoke_case_18,
    },
    {
        "operation": "listMembers",
        "method": "GET",
        "path": "/v1/insights/members",
        "label": "required params",
        "run": _smoke_case_19,
    },
    {
        "operation": "listMembers",
        "method": "GET",
        "path": "/v1/insights/members",
        "label": "all params",
        "run": _smoke_case_20,
    },
    {
        "operation": "listRepositories",
        "method": "GET",
        "path": "/v1/insights/repositories",
        "label": "required params",
        "run": _smoke_case_21,
    },
    {
        "operation": "listRepositories",
        "method": "GET",
        "path": "/v1/insights/repositories",
        "label": "all params",
        "run": _smoke_case_22,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/organizations",
        "label": "required params",
        "run": _smoke_case_23,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/organizations",
        "label": "all params",
        "run": _smoke_case_24,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/organizations/{organizationId}",
        "run": _smoke_case_25,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/organizations/{organizationId}",
        "label": "required params",
        "run": _smoke_case_26,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/organizations/{organizationId}",
        "label": "all params",
        "run": _smoke_case_27,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/organizations/{organizationId}",
        "run": _smoke_case_28,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/organizations/{organizationId}/members",
        "label": "required params",
        "run": _smoke_case_29,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/organizations/{organizationId}/members",
        "label": "all params",
        "run": _smoke_case_30,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/organizations/{organizationId}/members",
        "run": _smoke_case_31,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/organizations/{organizationId}/members/{memberId}",
        "run": _smoke_case_32,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/organizations/{organizationId}/members/{memberId}",
        "run": _smoke_case_33,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/organizations/{organizationId}/members/{memberId}",
        "run": _smoke_case_34,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/organizations/{organizationId}/secrets",
        "label": "required params",
        "run": _smoke_case_35,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/organizations/{organizationId}/secrets",
        "label": "all params",
        "run": _smoke_case_36,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/organizations/{organizationId}/secrets",
        "run": _smoke_case_37,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/organizations/{organizationId}/secrets/{secretId}",
        "run": _smoke_case_38,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/organizations/{organizationId}/secrets/{secretId}",
        "label": "required params",
        "run": _smoke_case_39,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/organizations/{organizationId}/secrets/{secretId}",
        "label": "all params",
        "run": _smoke_case_40,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/organizations/{organizationId}/secrets/{secretId}",
        "run": _smoke_case_41,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/organizations/{organizationId}/settings",
        "run": _smoke_case_42,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/organizations/{organizationId}/settings",
        "label": "required params",
        "run": _smoke_case_43,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/organizations/{organizationId}/settings",
        "label": "all params",
        "run": _smoke_case_44,
    },
    {
        "operation": "validateCredentials",
        "method": "POST",
        "path": "/v1/organizations/{organizationId}/settings/validate-credentials",
        "run": _smoke_case_45,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/organizations/{organizationId}/subscriptions",
        "run": _smoke_case_46,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/mcp-connections",
        "label": "required params",
        "run": _smoke_case_47,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/mcp-connections",
        "label": "all params",
        "run": _smoke_case_48,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/mcp-connections",
        "label": "required params",
        "run": _smoke_case_49,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/mcp-connections",
        "label": "all params",
        "run": _smoke_case_50,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/mcp-connections/{mcpConnectionId}",
        "run": _smoke_case_51,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/mcp-connections/{mcpConnectionId}",
        "label": "required params",
        "run": _smoke_case_52,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/mcp-connections/{mcpConnectionId}",
        "label": "all params",
        "run": _smoke_case_53,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/mcp-connections/{mcpConnectionId}",
        "run": _smoke_case_54,
    },
    {
        "operation": "authorize",
        "method": "POST",
        "path": "/v1/mcp-connections/{mcpConnectionId}/authorize",
        "run": _smoke_case_55,
    },
    {
        "operation": "test",
        "method": "POST",
        "path": "/v1/mcp-connections/{mcpConnectionId}/test",
        "run": _smoke_case_56,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/artifacts",
        "label": "required params",
        "run": _smoke_case_57,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/artifacts",
        "label": "all params",
        "run": _smoke_case_58,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/artifacts",
        "label": "required params",
        "run": _smoke_case_59,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/artifacts",
        "label": "all params",
        "run": _smoke_case_60,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/artifacts/{artifactId}",
        "run": _smoke_case_61,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/artifacts/{artifactId}",
        "run": _smoke_case_62,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/messages",
        "label": "required params",
        "run": _smoke_case_63,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/messages",
        "label": "all params",
        "run": _smoke_case_64,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/messages",
        "label": "required params",
        "run": _smoke_case_65,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/messages",
        "label": "all params",
        "run": _smoke_case_66,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/messages/{messageId}",
        "run": _smoke_case_67,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/messages/{messageId}",
        "label": "required params",
        "run": _smoke_case_68,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/messages/{messageId}",
        "label": "all params",
        "run": _smoke_case_69,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/messages/{messageId}",
        "run": _smoke_case_70,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/models",
        "label": "required params",
        "run": _smoke_case_71,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/models",
        "label": "all params",
        "run": _smoke_case_72,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/models/{modelName}",
        "label": "required params",
        "run": _smoke_case_73,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/models/{modelName}",
        "label": "all params",
        "run": _smoke_case_74,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/runtimes",
        "label": "required params",
        "run": _smoke_case_75,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/runtimes",
        "label": "all params",
        "run": _smoke_case_76,
    },
    {
        "operation": "me",
        "method": "GET",
        "path": "/v1/users/me",
        "run": _smoke_case_77,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/users/{userId}",
        "run": _smoke_case_78,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/users/{userId}/settings",
        "run": _smoke_case_79,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/users/{userId}/settings",
        "label": "required params",
        "run": _smoke_case_80,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/users/{userId}/settings",
        "label": "all params",
        "run": _smoke_case_81,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/users/{userId}/connected-accounts",
        "label": "required params",
        "run": _smoke_case_82,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/users/{userId}/connected-accounts",
        "label": "all params",
        "run": _smoke_case_83,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/users/{userId}/connected-accounts/{connectedAccountId}",
        "run": _smoke_case_84,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/users/{userId}/subscriptions",
        "run": _smoke_case_85,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/users/{userId}/environment-variables",
        "run": _smoke_case_86,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/users/{userId}/environment-variables",
        "run": _smoke_case_87,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/users/{userId}/environment-variables/{environmentVariableId}",
        "run": _smoke_case_88,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/users/{userId}/profile-picture",
        "run": _smoke_case_89,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/users/{userId}/profile-picture",
        "run": _smoke_case_90,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/users/{userId}/profile-picture",
        "run": _smoke_case_91,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/sessions",
        "label": "required params",
        "run": _smoke_case_92,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/sessions",
        "label": "all params",
        "run": _smoke_case_93,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/sessions",
        "label": "required params",
        "run": _smoke_case_94,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/sessions",
        "label": "all params",
        "run": _smoke_case_95,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/sessions/{sessionId}",
        "run": _smoke_case_96,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/sessions/{sessionId}",
        "label": "required params",
        "run": _smoke_case_97,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/sessions/{sessionId}",
        "label": "all params",
        "run": _smoke_case_98,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/sessions/{sessionId}",
        "run": _smoke_case_99,
    },
    {
        "operation": "fork",
        "method": "POST",
        "path": "/v1/sessions/{sessionId}/fork",
        "label": "required params",
        "run": _smoke_case_100,
    },
    {
        "operation": "fork",
        "method": "POST",
        "path": "/v1/sessions/{sessionId}/fork",
        "label": "all params",
        "run": _smoke_case_101,
    },
    {
        "operation": "stop",
        "method": "POST",
        "path": "/v1/sessions/{sessionId}/stop",
        "label": "required params",
        "run": _smoke_case_102,
    },
    {
        "operation": "stop",
        "method": "POST",
        "path": "/v1/sessions/{sessionId}/stop",
        "label": "all params",
        "run": _smoke_case_103,
    },
    {
        "operation": "listEvents",
        "method": "GET",
        "path": "/v1/sessions/{sessionId}/events",
        "label": "required params",
        "run": _smoke_case_104,
    },
    {
        "operation": "listEvents",
        "method": "GET",
        "path": "/v1/sessions/{sessionId}/events",
        "label": "all params",
        "run": _smoke_case_105,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/sessions/sources",
        "label": "required params",
        "run": _smoke_case_106,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/sessions/sources",
        "label": "all params",
        "run": _smoke_case_107,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/sessions/sources/{sourceId}",
        "run": _smoke_case_108,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/sessions/{sessionId}/diffs",
        "label": "required params",
        "run": _smoke_case_109,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/sessions/{sessionId}/diffs",
        "label": "all params",
        "run": _smoke_case_110,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/sessions/{sessionId}/diffs/{diffId}",
        "run": _smoke_case_111,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/sessions/{sessionId}/inputs",
        "run": _smoke_case_112,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/sessions/{sessionId}/inputs/{inputId}",
        "run": _smoke_case_113,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/sessions/{sessionId}/queue",
        "run": _smoke_case_114,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/sessions/{sessionId}/commands",
        "run": _smoke_case_115,
    },
    {
        "operation": "updateDefaults",
        "method": "PUT",
        "path": "/v1/projects/defaults",
        "run": _smoke_case_116,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects",
        "label": "required params",
        "run": _smoke_case_117,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects",
        "label": "all params",
        "run": _smoke_case_118,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects",
        "label": "required params",
        "run": _smoke_case_119,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects",
        "label": "all params",
        "run": _smoke_case_120,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/projects/{projectId}",
        "run": _smoke_case_121,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/projects/{projectId}",
        "label": "required params",
        "run": _smoke_case_122,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/projects/{projectId}",
        "label": "all params",
        "run": _smoke_case_123,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/projects/{projectId}",
        "run": _smoke_case_124,
    },
    {
        "operation": "duplicate",
        "method": "POST",
        "path": "/v1/projects/{projectId}/duplicate",
        "run": _smoke_case_125,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/{projectId}/environment-variables",
        "run": _smoke_case_126,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects/{projectId}/environment-variables",
        "run": _smoke_case_127,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/projects/{projectId}/environment-variables/{key}",
        "run": _smoke_case_128,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/{projectId}/snapshots",
        "label": "required params",
        "run": _smoke_case_129,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/{projectId}/snapshots",
        "label": "all params",
        "run": _smoke_case_130,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/projects/{projectId}/snapshots/{snapshotId}",
        "run": _smoke_case_131,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/projects/{projectId}/snapshots/{snapshotId}",
        "label": "required params",
        "run": _smoke_case_132,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/projects/{projectId}/snapshots/{snapshotId}",
        "label": "all params",
        "run": _smoke_case_133,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/projects/{projectId}/snapshots/{snapshotId}",
        "run": _smoke_case_134,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/{projectId}/builds",
        "label": "required params",
        "run": _smoke_case_135,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/{projectId}/builds",
        "label": "all params",
        "run": _smoke_case_136,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects/{projectId}/builds",
        "label": "required params",
        "run": _smoke_case_137,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects/{projectId}/builds",
        "label": "all params",
        "run": _smoke_case_138,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/projects/{projectId}/builds/{buildId}",
        "run": _smoke_case_139,
    },
    {
        "operation": "cancel",
        "method": "POST",
        "path": "/v1/projects/{projectId}/builds/{buildId}/cancel",
        "run": _smoke_case_140,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/{projectId}/schedules",
        "label": "required params",
        "run": _smoke_case_141,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/{projectId}/schedules",
        "label": "all params",
        "run": _smoke_case_142,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects/{projectId}/schedules",
        "label": "required params",
        "run": _smoke_case_143,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects/{projectId}/schedules",
        "label": "all params",
        "run": _smoke_case_144,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/projects/{projectId}/schedules/{scheduleId}",
        "run": _smoke_case_145,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/projects/{projectId}/schedules/{scheduleId}",
        "label": "required params",
        "run": _smoke_case_146,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/projects/{projectId}/schedules/{scheduleId}",
        "label": "all params",
        "run": _smoke_case_147,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/projects/{projectId}/schedules/{scheduleId}",
        "run": _smoke_case_148,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/pins",
        "label": "required params",
        "run": _smoke_case_149,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/pins",
        "label": "all params",
        "run": _smoke_case_150,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/pins",
        "label": "required params",
        "run": _smoke_case_151,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/pins",
        "label": "all params",
        "run": _smoke_case_152,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/pins/{resourceType}/{resourceId}",
        "run": _smoke_case_153,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/pins/{resourceType}/{resourceId}",
        "run": _smoke_case_154,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/pull-requests",
        "label": "required params",
        "run": _smoke_case_155,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/pull-requests",
        "label": "all params",
        "run": _smoke_case_156,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/pull-requests/{pullRequestId}",
        "run": _smoke_case_157,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents",
        "label": "required params",
        "run": _smoke_case_158,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents",
        "label": "all params",
        "run": _smoke_case_159,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents",
        "label": "required params",
        "run": _smoke_case_160,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents",
        "label": "all params",
        "run": _smoke_case_161,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agentId}",
        "run": _smoke_case_162,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/agents/{agentId}",
        "label": "required params",
        "run": _smoke_case_163,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/agents/{agentId}",
        "label": "all params",
        "run": _smoke_case_164,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/agents/{agentId}",
        "run": _smoke_case_165,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/templates",
        "label": "required params",
        "run": _smoke_case_166,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/templates",
        "label": "all params",
        "run": _smoke_case_167,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/templates/{templateName}",
        "run": _smoke_case_168,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/{agentId}/schedules",
        "label": "required params",
        "run": _smoke_case_169,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/{agentId}/schedules",
        "label": "all params",
        "run": _smoke_case_170,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents/{agentId}/schedules",
        "run": _smoke_case_171,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agentId}/schedules/{scheduleId}",
        "run": _smoke_case_172,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/agents/{agentId}/schedules/{scheduleId}",
        "run": _smoke_case_173,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/agents/{agentId}/schedules/{scheduleId}",
        "run": _smoke_case_174,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/{agentId}/triggers",
        "label": "required params",
        "run": _smoke_case_175,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/{agentId}/triggers",
        "label": "all params",
        "run": _smoke_case_176,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents/{agentId}/triggers",
        "label": "required params",
        "run": _smoke_case_177,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents/{agentId}/triggers",
        "label": "all params",
        "run": _smoke_case_178,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agentId}/triggers/{triggerId}",
        "run": _smoke_case_179,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/agents/{agentId}/triggers/{triggerId}",
        "label": "required params",
        "run": _smoke_case_180,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/agents/{agentId}/triggers/{triggerId}",
        "label": "all params",
        "run": _smoke_case_181,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/agents/{agentId}/triggers/{triggerId}",
        "run": _smoke_case_182,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/{agentId}/runs",
        "label": "required params",
        "run": _smoke_case_183,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/{agentId}/runs",
        "label": "all params",
        "run": _smoke_case_184,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents/{agentId}/runs",
        "label": "required params",
        "run": _smoke_case_185,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents/{agentId}/runs",
        "label": "all params",
        "run": _smoke_case_186,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agentId}/runs/{runId}",
        "run": _smoke_case_187,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/{agentId}/content-revisions",
        "label": "required params",
        "run": _smoke_case_188,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/{agentId}/content-revisions",
        "label": "all params",
        "run": _smoke_case_189,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agentId}/content-revisions/{version}",
        "run": _smoke_case_190,
    },
    {
        "operation": "restore",
        "method": "POST",
        "path": "/v1/agents/{agentId}/content-revisions/{version}/restore",
        "run": _smoke_case_191,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/repositories",
        "label": "required params",
        "run": _smoke_case_192,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/repositories",
        "label": "all params",
        "run": _smoke_case_193,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/repositories/{repositoryId}",
        "run": _smoke_case_194,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/repositories/{repositoryId}",
        "label": "required params",
        "run": _smoke_case_195,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/repositories/{repositoryId}",
        "label": "all params",
        "run": _smoke_case_196,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/integrations",
        "label": "required params",
        "run": _smoke_case_197,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/integrations",
        "label": "all params",
        "run": _smoke_case_198,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/integrations",
        "run": _smoke_case_199,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/integrations/{integrationId}",
        "run": _smoke_case_200,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/integrations/{integrationId}",
        "label": "required params",
        "run": _smoke_case_201,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/integrations/{integrationId}",
        "label": "all params",
        "run": _smoke_case_202,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/integrations/{integrationId}",
        "run": _smoke_case_203,
    },
    {
        "operation": "authorize",
        "method": "POST",
        "path": "/v1/integrations/{integrationId}/authorize",
        "label": "required params",
        "run": _smoke_case_204,
    },
    {
        "operation": "authorize",
        "method": "POST",
        "path": "/v1/integrations/{integrationId}/authorize",
        "label": "all params",
        "run": _smoke_case_205,
    },
    {
        "operation": "test",
        "method": "POST",
        "path": "/v1/integrations/{integrationId}/test",
        "run": _smoke_case_206,
    },
    {
        "operation": "sync",
        "method": "POST",
        "path": "/v1/integrations/{integrationId}/sync",
        "run": _smoke_case_207,
    },
    {
        "operation": "syncAll",
        "method": "POST",
        "path": "/v1/integrations/sync",
        "run": _smoke_case_208,
    },
    {
        "operation": "retrieveSyncStatus",
        "method": "GET",
        "path": "/v1/integrations/sync/status",
        "label": "required params",
        "run": _smoke_case_209,
    },
    {
        "operation": "retrieveSyncStatus",
        "method": "GET",
        "path": "/v1/integrations/sync/status",
        "label": "all params",
        "run": _smoke_case_210,
    },
    {
        "operation": "retrieveRateLimit",
        "method": "GET",
        "path": "/v1/integrations/{integrationId}/rate-limit",
        "run": _smoke_case_211,
    },
    {
        "operation": "listSentryEnvironments",
        "method": "GET",
        "path": "/v1/integrations/{integrationId}/sentry-environments",
        "label": "required params",
        "run": _smoke_case_212,
    },
    {
        "operation": "listSentryEnvironments",
        "method": "GET",
        "path": "/v1/integrations/{integrationId}/sentry-environments",
        "label": "all params",
        "run": _smoke_case_213,
    },
    {
        "operation": "listSlackChannels",
        "method": "GET",
        "path": "/v1/integrations/{integrationId}/slack-channels",
        "label": "required params",
        "run": _smoke_case_214,
    },
    {
        "operation": "listSlackChannels",
        "method": "GET",
        "path": "/v1/integrations/{integrationId}/slack-channels",
        "label": "all params",
        "run": _smoke_case_215,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/integrations/providers",
        "label": "required params",
        "run": _smoke_case_216,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/integrations/providers",
        "label": "all params",
        "run": _smoke_case_217,
    },
    {
        "operation": "discoverSnykOrganizations",
        "method": "POST",
        "path": "/v1/integrations/providers/snyk/organizations",
        "label": "required params",
        "run": _smoke_case_218,
    },
    {
        "operation": "discoverSnykOrganizations",
        "method": "POST",
        "path": "/v1/integrations/providers/snyk/organizations",
        "label": "all params",
        "run": _smoke_case_219,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/integrations/triggers",
        "label": "required params",
        "run": _smoke_case_220,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/integrations/triggers",
        "label": "all params",
        "run": _smoke_case_221,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/integrations/{integrationId}/triggers/{triggerName}",
        "run": _smoke_case_222,
    },
    {
        "operation": "listFilterOptions",
        "method": "GET",
        "path": "/v1/integrations/{integrationId}/triggers/{triggerName}/filter-options/{field}",
        "label": "required params",
        "run": _smoke_case_223,
    },
    {
        "operation": "listFilterOptions",
        "method": "GET",
        "path": "/v1/integrations/{integrationId}/triggers/{triggerName}/filter-options/{field}",
        "label": "all params",
        "run": _smoke_case_224,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/billing",
        "run": _smoke_case_225,
    },
    {
        "operation": "listUsage",
        "method": "GET",
        "path": "/v1/billing/usage",
        "label": "required params",
        "run": _smoke_case_226,
    },
    {
        "operation": "listUsage",
        "method": "GET",
        "path": "/v1/billing/usage",
        "label": "all params",
        "run": _smoke_case_227,
    },
    {
        "operation": "authorize",
        "method": "POST",
        "path": "/v1/live",
        "run": _smoke_case_228,
    },
    {
        "operation": "connect",
        "method": "GET",
        "path": "/v1/live",
        "run": _smoke_case_229,
    },
]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [case for case in cases if any(needle in case["operation"] or needle in case["path"] for needle in needles)]


def _smoke_concurrency(case_count: int) -> int:
    override = os.environ.get("SCALAR_SMOKE_CONCURRENCY")
    if override:
        try:
            parsed = int(override)
            if parsed > 0:
                return min(parsed, case_count)
        except ValueError:
            pass
    return min(DEFAULT_SMOKE_CONCURRENCY, case_count)


def _case_identity(case: SmokeCase) -> SmokeResult:
    # `label` is carried through only when the operation contributed both of its calls, so a
    # single-case operation reports exactly as it did before there were two.
    identity: SmokeResult = {
        "operation": case["operation"],
        "method": case["method"],
        "path": case["path"],
    }
    label = case.get("label")
    if label:
        identity["label"] = label
    return identity


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    identity = _case_identity(case)
    try:
        case["run"]()
        return {
            **identity,
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            **identity,
            "status": "failed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
            "error": traceback.format_exc(),
        }


def main() -> None:
    selected = _selected_cases()
    if selected:
        # Keep enough parallelism to catch generated SDK concurrency bugs without overwhelming
        # CI runners or the in-process mock server for large SDKs.
        with ThreadPoolExecutor(max_workers=_smoke_concurrency(len(selected))) as executor:
            results = list(executor.map(_run_case, selected))
    else:
        results = []
    failed = [result for result in results if result["status"] == "failed"]

    report_path = os.environ.get("SCALAR_SMOKE_REPORT")
    if report_path:
        Path(report_path).write_text(
            json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8"
        )
    else:
        for result in results:
            suffix = f" [{result['label']}]" if result.get("label") else ""
            if result["status"] == "passed":
                print(
                    f"PASS {result['operation']}{suffix} ({result['method']} {result['path']}) {result['durationMs']}ms"
                )
            else:
                print(
                    f"FAIL {result['operation']}{suffix} ({result['method']} {result['path']})\n{result.get('error', '')}",
                    file=sys.stderr,
                )
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
