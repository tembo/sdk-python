# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import os
import threading
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, is_mapping_t, get_async_library
from ._compat import cached_property
from ._exceptions import APIStatusError, TemboError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._version import __version__

if TYPE_CHECKING:
    from .resources import (
        api_keys,
        skills,
        insights,
        organizations,
        mcp_connections,
        artifacts,
        messages,
        models,
        runtimes,
        users,
        sessions,
        projects,
        pins,
        pull_requests,
        agents,
        repositories,
        integrations,
        billing,
        live,
    )
    from .resources.api_keys import APIKeysResource, AsyncAPIKeysResource
    from .resources.skills import SkillsResource, AsyncSkillsResource
    from .resources.insights import InsightsResource, AsyncInsightsResource
    from .resources.organizations import OrganizationsResource, AsyncOrganizationsResource
    from .resources.mcp_connections import McpConnectionsResource, AsyncMcpConnectionsResource
    from .resources.artifacts import ArtifactsResource, AsyncArtifactsResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.models import ModelsResource, AsyncModelsResource
    from .resources.runtimes import RuntimesResource, AsyncRuntimesResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.sessions import SessionsResource, AsyncSessionsResource
    from .resources.projects import ProjectsResource, AsyncProjectsResource
    from .resources.pins import PinsResource, AsyncPinsResource
    from .resources.pull_requests import PullRequestsResource, AsyncPullRequestsResource
    from .resources.agents import AgentsResource, AsyncAgentsResource
    from .resources.repositories import RepositoriesResource, AsyncRepositoriesResource
    from .resources.integrations import IntegrationsResource, AsyncIntegrationsResource
    from .resources.billing import BillingResource, AsyncBillingResource
    from .resources.live import LiveResource, AsyncLiveResource

# Serializes lazy resource imports so concurrent cold access from multiple
# threads cannot deadlock on CPython import locks (see CPython 3.14).
_RESOURCE_IMPORT_LOCK = threading.RLock()

__all__ = ["Tembo", "AsyncTembo", "Client", "AsyncClient", "Timeout", "Transport", "ProxiesTypes", "RequestOptions"]


class Tembo(SyncAPIClient):
    # client options
    api_key: str

    websocket_base_url: str | httpx.URL | None
    """Base URL for WebSocket connections.

    If not specified, the default base URL will be used, with 'wss://' replacing the
    'http://' or 'https://' scheme. For example: 'http://example.com' becomes
    'wss://example.com'
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        websocket_base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Tembo client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `TEMBO_API_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("TEMBO_API_KEY")
        if api_key is None:
            raise TemboError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TEMBO_API_KEY environment variable"
            )
        self.api_key = api_key
        self.websocket_base_url = websocket_base_url
        if base_url is None:
            base_url = os.environ.get("TEMBO_BASE_URL")
        if base_url is None:
            base_url = "https://api.tembo.io"
        custom_headers_env = os.environ.get("TEMBO_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = Stream

    @cached_property
    def api_keys(self) -> "APIKeysResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.api_keys import APIKeysResource
        return APIKeysResource(self)

    @cached_property
    def skills(self) -> "SkillsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.skills import SkillsResource
        return SkillsResource(self)

    @cached_property
    def insights(self) -> "InsightsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.insights import InsightsResource
        return InsightsResource(self)

    @cached_property
    def organizations(self) -> "OrganizationsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import OrganizationsResource
        return OrganizationsResource(self)

    @cached_property
    def mcp_connections(self) -> "McpConnectionsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.mcp_connections import McpConnectionsResource
        return McpConnectionsResource(self)

    @cached_property
    def artifacts(self) -> "ArtifactsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.artifacts import ArtifactsResource
        return ArtifactsResource(self)

    @cached_property
    def messages(self) -> "MessagesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.messages import MessagesResource
        return MessagesResource(self)

    @cached_property
    def models(self) -> "ModelsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.models import ModelsResource
        return ModelsResource(self)

    @cached_property
    def runtimes(self) -> "RuntimesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.runtimes import RuntimesResource
        return RuntimesResource(self)

    @cached_property
    def users(self) -> "UsersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.users import UsersResource
        return UsersResource(self)

    @cached_property
    def sessions(self) -> "SessionsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sessions import SessionsResource
        return SessionsResource(self)

    @cached_property
    def projects(self) -> "ProjectsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.projects import ProjectsResource
        return ProjectsResource(self)

    @cached_property
    def pins(self) -> "PinsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pins import PinsResource
        return PinsResource(self)

    @cached_property
    def pull_requests(self) -> "PullRequestsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pull_requests import PullRequestsResource
        return PullRequestsResource(self)

    @cached_property
    def agents(self) -> "AgentsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AgentsResource
        return AgentsResource(self)

    @cached_property
    def repositories(self) -> "RepositoriesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.repositories import RepositoriesResource
        return RepositoriesResource(self)

    @cached_property
    def integrations(self) -> "IntegrationsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.integrations import IntegrationsResource
        return IntegrationsResource(self)

    @cached_property
    def billing(self) -> "BillingResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import BillingResource
        return BillingResource(self)

    @cached_property
    def live(self) -> "LiveResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live import LiveResource
        return LiveResource(self)

    @cached_property
    def with_raw_response(self) -> TemboWithRawResponse:
        return TemboWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemboWithStreamedResponse:
        return TemboWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._api_key_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _api_key_header_auth(self) -> dict[str, str]:
        value = self.api_key
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        websocket_base_url: str | httpx.URL | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            websocket_base_url=websocket_base_url or self.websocket_base_url,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTembo(AsyncAPIClient):
    # client options
    api_key: str

    websocket_base_url: str | httpx.URL | None
    """Base URL for WebSocket connections.

    If not specified, the default base URL will be used, with 'wss://' replacing the
    'http://' or 'https://' scheme. For example: 'http://example.com' becomes
    'wss://example.com'
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        websocket_base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncTembo client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `TEMBO_API_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("TEMBO_API_KEY")
        if api_key is None:
            raise TemboError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TEMBO_API_KEY environment variable"
            )
        self.api_key = api_key
        self.websocket_base_url = websocket_base_url
        if base_url is None:
            base_url = os.environ.get("TEMBO_BASE_URL")
        if base_url is None:
            base_url = "https://api.tembo.io"
        custom_headers_env = os.environ.get("TEMBO_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = AsyncStream

    @cached_property
    def api_keys(self) -> "AsyncAPIKeysResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.api_keys import AsyncAPIKeysResource
        return AsyncAPIKeysResource(self)

    @cached_property
    def skills(self) -> "AsyncSkillsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.skills import AsyncSkillsResource
        return AsyncSkillsResource(self)

    @cached_property
    def insights(self) -> "AsyncInsightsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.insights import AsyncInsightsResource
        return AsyncInsightsResource(self)

    @cached_property
    def organizations(self) -> "AsyncOrganizationsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import AsyncOrganizationsResource
        return AsyncOrganizationsResource(self)

    @cached_property
    def mcp_connections(self) -> "AsyncMcpConnectionsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.mcp_connections import AsyncMcpConnectionsResource
        return AsyncMcpConnectionsResource(self)

    @cached_property
    def artifacts(self) -> "AsyncArtifactsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.artifacts import AsyncArtifactsResource
        return AsyncArtifactsResource(self)

    @cached_property
    def messages(self) -> "AsyncMessagesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.messages import AsyncMessagesResource
        return AsyncMessagesResource(self)

    @cached_property
    def models(self) -> "AsyncModelsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.models import AsyncModelsResource
        return AsyncModelsResource(self)

    @cached_property
    def runtimes(self) -> "AsyncRuntimesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.runtimes import AsyncRuntimesResource
        return AsyncRuntimesResource(self)

    @cached_property
    def users(self) -> "AsyncUsersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.users import AsyncUsersResource
        return AsyncUsersResource(self)

    @cached_property
    def sessions(self) -> "AsyncSessionsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sessions import AsyncSessionsResource
        return AsyncSessionsResource(self)

    @cached_property
    def projects(self) -> "AsyncProjectsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.projects import AsyncProjectsResource
        return AsyncProjectsResource(self)

    @cached_property
    def pins(self) -> "AsyncPinsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pins import AsyncPinsResource
        return AsyncPinsResource(self)

    @cached_property
    def pull_requests(self) -> "AsyncPullRequestsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pull_requests import AsyncPullRequestsResource
        return AsyncPullRequestsResource(self)

    @cached_property
    def agents(self) -> "AsyncAgentsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AsyncAgentsResource
        return AsyncAgentsResource(self)

    @cached_property
    def repositories(self) -> "AsyncRepositoriesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.repositories import AsyncRepositoriesResource
        return AsyncRepositoriesResource(self)

    @cached_property
    def integrations(self) -> "AsyncIntegrationsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.integrations import AsyncIntegrationsResource
        return AsyncIntegrationsResource(self)

    @cached_property
    def billing(self) -> "AsyncBillingResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import AsyncBillingResource
        return AsyncBillingResource(self)

    @cached_property
    def live(self) -> "AsyncLiveResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live import AsyncLiveResource
        return AsyncLiveResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncTemboWithRawResponse:
        return AsyncTemboWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemboWithStreamedResponse:
        return AsyncTemboWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._api_key_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _api_key_header_auth(self) -> dict[str, str]:
        value = self.api_key
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        websocket_base_url: str | httpx.URL | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            websocket_base_url=websocket_base_url or self.websocket_base_url,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TemboWithRawResponse:
    _client: Tembo

    def __init__(self, client: Tembo) -> None:
        self._client = client

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.api_keys import APIKeysResourceWithRawResponse
        return APIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def skills(self) -> skills.SkillsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.skills import SkillsResourceWithRawResponse
        return SkillsResourceWithRawResponse(self._client.skills)

    @cached_property
    def insights(self) -> insights.InsightsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.insights import InsightsResourceWithRawResponse
        return InsightsResourceWithRawResponse(self._client.insights)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import OrganizationsResourceWithRawResponse
        return OrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def mcp_connections(self) -> mcp_connections.McpConnectionsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.mcp_connections import McpConnectionsResourceWithRawResponse
        return McpConnectionsResourceWithRawResponse(self._client.mcp_connections)

    @cached_property
    def artifacts(self) -> artifacts.ArtifactsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.artifacts import ArtifactsResourceWithRawResponse
        return ArtifactsResourceWithRawResponse(self._client.artifacts)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.messages import MessagesResourceWithRawResponse
        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.models import ModelsResourceWithRawResponse
        return ModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def runtimes(self) -> runtimes.RuntimesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.runtimes import RuntimesResourceWithRawResponse
        return RuntimesResourceWithRawResponse(self._client.runtimes)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.users import UsersResourceWithRawResponse
        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def sessions(self) -> sessions.SessionsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sessions import SessionsResourceWithRawResponse
        return SessionsResourceWithRawResponse(self._client.sessions)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.projects import ProjectsResourceWithRawResponse
        return ProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def pins(self) -> pins.PinsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pins import PinsResourceWithRawResponse
        return PinsResourceWithRawResponse(self._client.pins)

    @cached_property
    def pull_requests(self) -> pull_requests.PullRequestsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pull_requests import PullRequestsResourceWithRawResponse
        return PullRequestsResourceWithRawResponse(self._client.pull_requests)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AgentsResourceWithRawResponse
        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def repositories(self) -> repositories.RepositoriesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.repositories import RepositoriesResourceWithRawResponse
        return RepositoriesResourceWithRawResponse(self._client.repositories)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.integrations import IntegrationsResourceWithRawResponse
        return IntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def billing(self) -> billing.BillingResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import BillingResourceWithRawResponse
        return BillingResourceWithRawResponse(self._client.billing)

    @cached_property
    def live(self) -> live.LiveResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live import LiveResourceWithRawResponse
        return LiveResourceWithRawResponse(self._client.live)


class AsyncTemboWithRawResponse:
    _client: AsyncTembo

    def __init__(self, client: AsyncTembo) -> None:
        self._client = client

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.api_keys import AsyncAPIKeysResourceWithRawResponse
        return AsyncAPIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def skills(self) -> skills.AsyncSkillsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.skills import AsyncSkillsResourceWithRawResponse
        return AsyncSkillsResourceWithRawResponse(self._client.skills)

    @cached_property
    def insights(self) -> insights.AsyncInsightsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.insights import AsyncInsightsResourceWithRawResponse
        return AsyncInsightsResourceWithRawResponse(self._client.insights)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import AsyncOrganizationsResourceWithRawResponse
        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def mcp_connections(self) -> mcp_connections.AsyncMcpConnectionsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.mcp_connections import AsyncMcpConnectionsResourceWithRawResponse
        return AsyncMcpConnectionsResourceWithRawResponse(self._client.mcp_connections)

    @cached_property
    def artifacts(self) -> artifacts.AsyncArtifactsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.artifacts import AsyncArtifactsResourceWithRawResponse
        return AsyncArtifactsResourceWithRawResponse(self._client.artifacts)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.messages import AsyncMessagesResourceWithRawResponse
        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.models import AsyncModelsResourceWithRawResponse
        return AsyncModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def runtimes(self) -> runtimes.AsyncRuntimesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.runtimes import AsyncRuntimesResourceWithRawResponse
        return AsyncRuntimesResourceWithRawResponse(self._client.runtimes)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.users import AsyncUsersResourceWithRawResponse
        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def sessions(self) -> sessions.AsyncSessionsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sessions import AsyncSessionsResourceWithRawResponse
        return AsyncSessionsResourceWithRawResponse(self._client.sessions)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.projects import AsyncProjectsResourceWithRawResponse
        return AsyncProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def pins(self) -> pins.AsyncPinsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pins import AsyncPinsResourceWithRawResponse
        return AsyncPinsResourceWithRawResponse(self._client.pins)

    @cached_property
    def pull_requests(self) -> pull_requests.AsyncPullRequestsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pull_requests import AsyncPullRequestsResourceWithRawResponse
        return AsyncPullRequestsResourceWithRawResponse(self._client.pull_requests)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AsyncAgentsResourceWithRawResponse
        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def repositories(self) -> repositories.AsyncRepositoriesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.repositories import AsyncRepositoriesResourceWithRawResponse
        return AsyncRepositoriesResourceWithRawResponse(self._client.repositories)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.integrations import AsyncIntegrationsResourceWithRawResponse
        return AsyncIntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import AsyncBillingResourceWithRawResponse
        return AsyncBillingResourceWithRawResponse(self._client.billing)

    @cached_property
    def live(self) -> live.AsyncLiveResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live import AsyncLiveResourceWithRawResponse
        return AsyncLiveResourceWithRawResponse(self._client.live)


class TemboWithStreamedResponse:
    _client: Tembo

    def __init__(self, client: Tembo) -> None:
        self._client = client

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.api_keys import APIKeysResourceWithStreamingResponse
        return APIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def skills(self) -> skills.SkillsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.skills import SkillsResourceWithStreamingResponse
        return SkillsResourceWithStreamingResponse(self._client.skills)

    @cached_property
    def insights(self) -> insights.InsightsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.insights import InsightsResourceWithStreamingResponse
        return InsightsResourceWithStreamingResponse(self._client.insights)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import OrganizationsResourceWithStreamingResponse
        return OrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def mcp_connections(self) -> mcp_connections.McpConnectionsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.mcp_connections import McpConnectionsResourceWithStreamingResponse
        return McpConnectionsResourceWithStreamingResponse(self._client.mcp_connections)

    @cached_property
    def artifacts(self) -> artifacts.ArtifactsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.artifacts import ArtifactsResourceWithStreamingResponse
        return ArtifactsResourceWithStreamingResponse(self._client.artifacts)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.messages import MessagesResourceWithStreamingResponse
        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.models import ModelsResourceWithStreamingResponse
        return ModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def runtimes(self) -> runtimes.RuntimesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.runtimes import RuntimesResourceWithStreamingResponse
        return RuntimesResourceWithStreamingResponse(self._client.runtimes)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.users import UsersResourceWithStreamingResponse
        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def sessions(self) -> sessions.SessionsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sessions import SessionsResourceWithStreamingResponse
        return SessionsResourceWithStreamingResponse(self._client.sessions)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.projects import ProjectsResourceWithStreamingResponse
        return ProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def pins(self) -> pins.PinsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pins import PinsResourceWithStreamingResponse
        return PinsResourceWithStreamingResponse(self._client.pins)

    @cached_property
    def pull_requests(self) -> pull_requests.PullRequestsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pull_requests import PullRequestsResourceWithStreamingResponse
        return PullRequestsResourceWithStreamingResponse(self._client.pull_requests)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AgentsResourceWithStreamingResponse
        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def repositories(self) -> repositories.RepositoriesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.repositories import RepositoriesResourceWithStreamingResponse
        return RepositoriesResourceWithStreamingResponse(self._client.repositories)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.integrations import IntegrationsResourceWithStreamingResponse
        return IntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def billing(self) -> billing.BillingResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import BillingResourceWithStreamingResponse
        return BillingResourceWithStreamingResponse(self._client.billing)

    @cached_property
    def live(self) -> live.LiveResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live import LiveResourceWithStreamingResponse
        return LiveResourceWithStreamingResponse(self._client.live)


class AsyncTemboWithStreamedResponse:
    _client: AsyncTembo

    def __init__(self, client: AsyncTembo) -> None:
        self._client = client

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.api_keys import AsyncAPIKeysResourceWithStreamingResponse
        return AsyncAPIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def skills(self) -> skills.AsyncSkillsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.skills import AsyncSkillsResourceWithStreamingResponse
        return AsyncSkillsResourceWithStreamingResponse(self._client.skills)

    @cached_property
    def insights(self) -> insights.AsyncInsightsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.insights import AsyncInsightsResourceWithStreamingResponse
        return AsyncInsightsResourceWithStreamingResponse(self._client.insights)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse
        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def mcp_connections(self) -> mcp_connections.AsyncMcpConnectionsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.mcp_connections import AsyncMcpConnectionsResourceWithStreamingResponse
        return AsyncMcpConnectionsResourceWithStreamingResponse(self._client.mcp_connections)

    @cached_property
    def artifacts(self) -> artifacts.AsyncArtifactsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.artifacts import AsyncArtifactsResourceWithStreamingResponse
        return AsyncArtifactsResourceWithStreamingResponse(self._client.artifacts)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.messages import AsyncMessagesResourceWithStreamingResponse
        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.models import AsyncModelsResourceWithStreamingResponse
        return AsyncModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def runtimes(self) -> runtimes.AsyncRuntimesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.runtimes import AsyncRuntimesResourceWithStreamingResponse
        return AsyncRuntimesResourceWithStreamingResponse(self._client.runtimes)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.users import AsyncUsersResourceWithStreamingResponse
        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def sessions(self) -> sessions.AsyncSessionsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sessions import AsyncSessionsResourceWithStreamingResponse
        return AsyncSessionsResourceWithStreamingResponse(self._client.sessions)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.projects import AsyncProjectsResourceWithStreamingResponse
        return AsyncProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def pins(self) -> pins.AsyncPinsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pins import AsyncPinsResourceWithStreamingResponse
        return AsyncPinsResourceWithStreamingResponse(self._client.pins)

    @cached_property
    def pull_requests(self) -> pull_requests.AsyncPullRequestsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.pull_requests import AsyncPullRequestsResourceWithStreamingResponse
        return AsyncPullRequestsResourceWithStreamingResponse(self._client.pull_requests)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AsyncAgentsResourceWithStreamingResponse
        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def repositories(self) -> repositories.AsyncRepositoriesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.repositories import AsyncRepositoriesResourceWithStreamingResponse
        return AsyncRepositoriesResourceWithStreamingResponse(self._client.repositories)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.integrations import AsyncIntegrationsResourceWithStreamingResponse
        return AsyncIntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import AsyncBillingResourceWithStreamingResponse
        return AsyncBillingResourceWithStreamingResponse(self._client.billing)

    @cached_property
    def live(self) -> live.AsyncLiveResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live import AsyncLiveResourceWithStreamingResponse
        return AsyncLiveResourceWithStreamingResponse(self._client.live)


# Alias names for the documented `Client` / `AsyncClient` symbols.
Client = Tembo
AsyncClient = AsyncTembo
