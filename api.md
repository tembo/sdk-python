# Tembo SDK Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`ApiKeys`](#apikeys)
  - [List API keys](#list-api-keys)
  - [Create an API key](#create-an-api-key)
  - [Retrieve an API key](#retrieve-an-api-key)
  - [Update an API key](#update-an-api-key)
  - [Delete an API key](#delete-an-api-key)
- [`Skills`](#skills)
  - [List skills](#list-skills)
  - [Create a skill](#create-a-skill)
  - [Retrieve a skill](#retrieve-a-skill)
  - [Update a skill](#update-a-skill)
  - [Delete a skill](#delete-a-skill)
  - [`Skills Marketplace`](#skills-marketplace)
    - [List marketplace skills](#list-marketplace-skills)
    - [Retrieve a marketplace skill](#retrieve-a-marketplace-skill)
- [`Insights`](#insights)
  - [Retrieve insights](#retrieve-insights)
  - [Update insights](#update-insights)
  - [List insight members](#list-insight-members)
  - [List insight repositories](#list-insight-repositories)
- [`Organizations`](#organizations)
  - [Create an organization](#create-an-organization)
  - [Retrieve an organization](#retrieve-an-organization)
  - [Update an organization](#update-an-organization)
  - [Delete an organization](#delete-an-organization)
  - [`Organizations Members`](#organizations-members)
    - [List organization members](#list-organization-members)
    - [Create an organization member](#create-an-organization-member)
    - [Retrieve an organization member](#retrieve-an-organization-member)
    - [Update an organization member](#update-an-organization-member)
    - [Remove an organization member](#remove-an-organization-member)
  - [`Organizations Secrets`](#organizations-secrets)
    - [List organization secrets](#list-organization-secrets)
    - [Create an organization secret](#create-an-organization-secret)
    - [Retrieve an organization secret](#retrieve-an-organization-secret)
    - [Update an organization secret](#update-an-organization-secret)
    - [Delete an organization secret](#delete-an-organization-secret)
  - [`Organizations Settings`](#organizations-settings)
    - [Retrieve organization settings](#retrieve-organization-settings)
    - [Update organization settings](#update-organization-settings)
    - [Validate organization provider credentials](#validate-organization-provider-credentials)
  - [`Organizations Subscriptions`](#organizations-subscriptions)
    - [Retrieve organization subscriptions](#retrieve-organization-subscriptions)
    - [Reset organization subscription usage](#reset-organization-subscription-usage)
- [`McpConnections`](#mcpconnections)
  - [List MCP connections](#list-mcp-connections)
  - [Create an MCP connection](#create-an-mcp-connection)
  - [Retrieve an MCP connection](#retrieve-an-mcp-connection)
  - [Update an MCP connection](#update-an-mcp-connection)
  - [Delete an MCP connection](#delete-an-mcp-connection)
  - [Authorize an MCP connection](#authorize-an-mcp-connection)
  - [Test an MCP connection](#test-an-mcp-connection)
- [`Artifacts`](#artifacts)
  - [List artifacts](#list-artifacts)
  - [Create an artifact](#create-an-artifact)
  - [Retrieve an artifact](#retrieve-an-artifact)
  - [Delete an artifact](#delete-an-artifact)
- [`Messages`](#messages)
  - [List messages](#list-messages)
  - [Create a message](#create-a-message)
  - [Retrieve a message](#retrieve-a-message)
  - [Update a message](#update-a-message)
  - [Delete a message](#delete-a-message)
- [`Models`](#models)
  - [List models](#list-models)
  - [Update a model](#update-a-model)
- [`Runtimes`](#runtimes)
  - [List runtimes](#list-runtimes)
- [`Users`](#users)
  - [Retrieve the current user](#retrieve-the-current-user)
  - [Retrieve a user](#retrieve-a-user)
  - [Delete a user](#delete-a-user)
  - [`Users Settings`](#users-settings)
    - [Retrieve user settings](#retrieve-user-settings)
    - [Update user settings](#update-user-settings)
  - [`Users ConnectedAccounts`](#users-connectedaccounts)
    - [List user connected accounts](#list-user-connected-accounts)
    - [Retrieve a user connected account](#retrieve-a-user-connected-account)
  - [`Users Subscriptions`](#users-subscriptions)
    - [Retrieve user subscriptions](#retrieve-user-subscriptions)
    - [Reset user subscription usage](#reset-user-subscription-usage)
  - [`Users ProfilePicture`](#users-profilepicture)
    - [Retrieve a user profile picture](#retrieve-a-user-profile-picture)
    - [Update your profile picture](#update-your-profile-picture)
    - [Delete your profile picture](#delete-your-profile-picture)
- [`Sessions`](#sessions)
  - [List sessions](#list-sessions)
  - [Create a session](#create-a-session)
  - [Retrieve a session](#retrieve-a-session)
  - [Update a session](#update-a-session)
  - [Delete a session](#delete-a-session)
  - [Fork a session](#fork-a-session)
  - [Stop a session](#stop-a-session)
  - [List session events](#list-session-events)
  - [`Sessions Sources`](#sessions-sources)
    - [List session sources](#list-session-sources)
    - [Retrieve a session source](#retrieve-a-session-source)
  - [`Sessions Diffs`](#sessions-diffs)
    - [List session diffs](#list-session-diffs)
    - [Retrieve a session diff](#retrieve-a-session-diff)
- [`Projects`](#projects)
  - [Update project defaults](#update-project-defaults)
  - [List projects](#list-projects)
  - [Create a project](#create-a-project)
  - [Retrieve a project](#retrieve-a-project)
  - [Update a project](#update-a-project)
  - [Delete a project](#delete-a-project)
  - [Duplicate a project](#duplicate-a-project)
  - [`Projects EnvironmentVariables`](#projects-environmentvariables)
    - [List project environment variables](#list-project-environment-variables)
    - [Create project environment variables](#create-project-environment-variables)
    - [Delete a project environment variable](#delete-a-project-environment-variable)
  - [`Projects Snapshots`](#projects-snapshots)
    - [List project snapshots](#list-project-snapshots)
    - [Retrieve a project snapshot](#retrieve-a-project-snapshot)
    - [Update a project snapshot](#update-a-project-snapshot)
    - [Delete a project snapshot](#delete-a-project-snapshot)
  - [`Projects Builds`](#projects-builds)
    - [List project builds](#list-project-builds)
    - [Create a project build](#create-a-project-build)
    - [Retrieve a project build](#retrieve-a-project-build)
    - [Cancel a project build](#cancel-a-project-build)
  - [`Projects Schedules`](#projects-schedules)
    - [List project schedules](#list-project-schedules)
    - [Create a project schedule](#create-a-project-schedule)
    - [Retrieve a project schedule](#retrieve-a-project-schedule)
    - [Update a project schedule](#update-a-project-schedule)
    - [Delete a project schedule](#delete-a-project-schedule)
- [`Pins`](#pins)
  - [List pins](#list-pins)
  - [Create a pin](#create-a-pin)
  - [Update a pin](#update-a-pin)
  - [Delete a pin](#delete-a-pin)
- [`PullRequests`](#pullrequests)
  - [List pull requests](#list-pull-requests)
  - [Retrieve a pull request](#retrieve-a-pull-request)
- [`Agents`](#agents)
  - [List agents](#list-agents)
  - [Create an agent](#create-an-agent)
  - [Retrieve an agent](#retrieve-an-agent)
  - [Update an agent](#update-an-agent)
  - [Delete an agent](#delete-an-agent)
  - [`Agents Templates`](#agents-templates)
    - [List agent templates](#list-agent-templates)
    - [Retrieve an agent template](#retrieve-an-agent-template)
  - [`Agents Schedules`](#agents-schedules)
    - [List agent schedules](#list-agent-schedules)
    - [Create an agent schedule](#create-an-agent-schedule)
    - [Retrieve an agent schedule](#retrieve-an-agent-schedule)
    - [Update an agent schedule](#update-an-agent-schedule)
    - [Delete an agent schedule](#delete-an-agent-schedule)
  - [`Agents Triggers`](#agents-triggers)
    - [List agent triggers](#list-agent-triggers)
    - [Create an agent trigger](#create-an-agent-trigger)
    - [Retrieve an agent trigger](#retrieve-an-agent-trigger)
    - [Update an agent trigger](#update-an-agent-trigger)
    - [Delete an agent trigger](#delete-an-agent-trigger)
  - [`Agents Runs`](#agents-runs)
    - [List agent runs](#list-agent-runs)
    - [Create an agent run](#create-an-agent-run)
    - [Retrieve an agent run](#retrieve-an-agent-run)
  - [`Agents ContentRevisions`](#agents-contentrevisions)
    - [List agent instruction revisions](#list-agent-instruction-revisions)
    - [Retrieve an agent instruction revision](#retrieve-an-agent-instruction-revision)
    - [Restore agent instructions](#restore-agent-instructions)
- [`Repositories`](#repositories)
  - [List repositories](#list-repositories)
  - [Retrieve a repository](#retrieve-a-repository)
  - [Update a repository](#update-a-repository)
- [`Integrations`](#integrations)
  - [List integrations](#list-integrations)
  - [Create an integration](#create-an-integration)
  - [Retrieve an integration](#retrieve-an-integration)
  - [Update an integration](#update-an-integration)
  - [Delete an integration](#delete-an-integration)
  - [Authorize an integration](#authorize-an-integration)
  - [Test an integration](#test-an-integration)
  - [Sync an integration](#sync-an-integration)
  - [Sync eligible integrations](#sync-eligible-integrations)
  - [Retrieve integration sync status](#retrieve-integration-sync-status)
  - [Retrieve an integration rate limit](#retrieve-an-integration-rate-limit)
  - [List Sentry environments](#list-sentry-environments)
  - [List Slack channels](#list-slack-channels)
  - [`Integrations Providers`](#integrations-providers)
    - [List integration providers](#list-integration-providers)
    - [Discover Snyk organizations](#discover-snyk-organizations)
  - [`Integrations Triggers`](#integrations-triggers)
    - [List integration triggers](#list-integration-triggers)
    - [Retrieve an integration trigger](#retrieve-an-integration-trigger)
    - [List integration trigger filter options](#list-integration-trigger-filter-options)
- [`Billing`](#billing)
  - [Retrieve billing](#retrieve-billing)
  - [List billing usage](#list-billing-usage)
- [`Live`](#live)
  - [Authorize a live connection](#authorize-a-live-connection)
  - [Live resource subscriptions](#live-resource-subscriptions)

## Setup

```python
import os

from tembo import Tembo

client = Tembo(
    api_key=os.environ.get("TEMBO_API_KEY"),
)
```

## `ApiKeys`

### List API keys

List active API keys for the current organization.

| Direction | Type |
| --- | --- |
| Request | [`APIKeyListParams`](./src/tembo/types/api_key_list_params.py) |
| Response | [`APIKeyListResponse`](./src/tembo/types/api_key_list_response.py) |

```python
api_key = client.api_keys.list(
    limit=50,
)
```

### Create an API key

Create an API key for the current organization. Optionally set `expiresAt` to a future timestamp after which the key stops authenticating requests. The complete token is returned only by this operation.

| Direction | Type |
| --- | --- |
| Request | [`APIKeyCreateParams`](./src/tembo/types/api_key_create_params.py) |
| Response | [`APIKeyCreateResponse`](./src/tembo/types/api_key_create_response.py) |

```python
api_key = client.api_keys.create()
```

### Retrieve an API key

Retrieve an active API key without exposing its complete token.

| Direction | Type |
| --- | --- |
| Response | [`APIKeyRetrieveResponse`](./src/tembo/types/api_key_retrieve_response.py) |

```python
api_key = client.api_keys.retrieve(
    api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update an API key

Rename an active API key.

| Direction | Type |
| --- | --- |
| Request | [`APIKeyUpdateParams`](./src/tembo/types/api_key_update_params.py) |
| Response | [`APIKeyUpdateResponse`](./src/tembo/types/api_key_update_response.py) |

```python
api_key = client.api_keys.update(
    api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
)
```

### Delete an API key

Revoke an active API key so it can no longer authenticate requests.

| Direction | Type |
| --- | --- |
| Response | [`APIKeyDeleteResponse`](./src/tembo/types/api_key_delete_response.py) |

```python
api_key = client.api_keys.delete(
    api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Skills`

### List skills

List organization skills or skills checked into a repository.

| Direction | Type |
| --- | --- |
| Request | [`SkillListParams`](./src/tembo/types/skill_list_params.py) |
| Response | [`SkillListResponse`](./src/tembo/types/skill_list_response.py) |

```python
skill = client.skills.list(
    limit=50,
    source="organization",
)
```

### Create a skill

Create an organization skill with its files.

| Direction | Type |
| --- | --- |
| Request | [`SkillCreateParams`](./src/tembo/types/skill_create_params.py) |
| Response | [`SkillCreateResponse`](./src/tembo/types/skill_create_response.py) |

```python
skill = client.skills.create(
    description="",
    name="x",
    files=[{"content": "", "filename": "x"}],
)
```

### Retrieve a skill

Retrieve an organization skill and all of its files.

| Direction | Type |
| --- | --- |
| Response | [`SkillRetrieveResponse`](./src/tembo/types/skill_retrieve_response.py) |

```python
skill = client.skills.retrieve(
    skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update a skill

Update an organization skill. When files are provided, they replace the complete file set.

| Direction | Type |
| --- | --- |
| Request | [`SkillUpdateParams`](./src/tembo/types/skill_update_params.py) |
| Response | [`SkillUpdateResponse`](./src/tembo/types/skill_update_response.py) |

```python
skill = client.skills.update(
    skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Delete a skill

Delete an organization skill.

| Direction | Type |
| --- | --- |
| Response | [`SkillDeleteResponse`](./src/tembo/types/skill_delete_response.py) |

```python
skill = client.skills.delete(
    skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Skills Marketplace`

#### List marketplace skills

List popular marketplace skills or search the catalog. Results have no continuation cursor.

| Direction | Type |
| --- | --- |
| Request | [`MarketplaceListParams`](./src/tembo/types/skills/marketplace_list_params.py) |
| Response | [`MarketplaceListResponse`](./src/tembo/types/skills/marketplace_list_response.py) |

```python
marketplace = client.skills.marketplace.list(
    limit=50,
)
```

#### Retrieve a marketplace skill

Retrieve the files and content hash for a marketplace skill. This does not install the skill.

| Direction | Type |
| --- | --- |
| Request | [`MarketplaceRetrieveParams`](./src/tembo/types/skills/marketplace_retrieve_params.py) |
| Response | [`MarketplaceRetrieveResponse`](./src/tembo/types/skills/marketplace_retrieve_response.py) |

```python
marketplace = client.skills.marketplace.retrieve(
    skill_id="skillId",
    source="source",
)
```

## `Insights`

### Retrieve insights

Retrieve pull request contribution insights and their collection status for the current organization.

| Direction | Type |
| --- | --- |
| Request | [`InsightRetrieveParams`](./src/tembo/types/insight_retrieve_params.py) |
| Response | [`InsightRetrieveResponse`](./src/tembo/types/insight_retrieve_response.py) |

```python
insight = client.insights.retrieve(
    range="1y",
)
```

### Update insights

Enable or disable pull request insight collection. Enabling starts the initial refresh when needed.

| Direction | Type |
| --- | --- |
| Request | [`InsightUpdateParams`](./src/tembo/types/insight_update_params.py) |
| Response | [`InsightUpdateResponse`](./src/tembo/types/insight_update_response.py) |

```python
insight = client.insights.update(
    enabled=False,
)
```

### List insight members

List organization members included in pull request insights.

| Direction | Type |
| --- | --- |
| Request | [`InsightListMembersParams`](./src/tembo/types/insight_list_members_params.py) |
| Response | [`InsightListMembersResponse`](./src/tembo/types/insight_list_members_response.py) |

```python
insight = client.insights.list_members(
    limit=50,
    range="1y",
)
```

### List insight repositories

List repositories included in pull request insights for the current organization.

| Direction | Type |
| --- | --- |
| Request | [`InsightListRepositoriesParams`](./src/tembo/types/insight_list_repositories_params.py) |
| Response | [`InsightListRepositoriesResponse`](./src/tembo/types/insight_list_repositories_response.py) |

```python
insight = client.insights.list_repositories(
    limit=50,
    range="1y",
)
```

## `Organizations`

### Create an organization

Create an organization and make the authenticated user its administrator.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationCreateParams`](./src/tembo/types/organization_create_params.py) |
| Response | [`OrganizationCreateResponse`](./src/tembo/types/organization_create_response.py) |

```python
organization = client.organizations.create(
    name="x",
)
```

### Retrieve an organization

Retrieve an organization profile.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationRetrieveResponse`](./src/tembo/types/organization_retrieve_response.py) |

```python
organization = client.organizations.retrieve(
    organization_id="organizationId",
)
```

### Update an organization

Update organization profile fields or onboarding state.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationUpdateParams`](./src/tembo/types/organization_update_params.py) |
| Response | [`OrganizationUpdateResponse`](./src/tembo/types/organization_update_response.py) |

```python
organization = client.organizations.update(
    organization_id="organizationId",
)
```

### Delete an organization

Delete the organization from the identity provider and Tembo.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationDeleteResponse`](./src/tembo/types/organization_delete_response.py) |

```python
organization = client.organizations.delete(
    organization_id="organizationId",
)
```

### `Organizations Members`

#### List organization members

List active members or pending invitations with cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`MemberListParams`](./src/tembo/types/organizations/member_list_params.py) |
| Response | [`MemberListResponse`](./src/tembo/types/organizations/member_list_response.py) |

```python
member = client.organizations.members.list(
    organization_id="organizationId",
    limit=50,
    status="active",
)
```

#### Create an organization member

Invite or add a user to an organization with a role.

| Direction | Type |
| --- | --- |
| Request | [`MemberCreateParams`](./src/tembo/types/organizations/member_create_params.py) |
| Response | [`MemberCreateResponse`](./src/tembo/types/organizations/member_create_response.py) |

```python
member = client.organizations.members.create(
    organization_id="organizationId",
    email_address="user@example.com",
    role="org:member",
)
```

#### Retrieve an organization member

Retrieve an active member or pending member invitation.

| Direction | Type |
| --- | --- |
| Response | [`MemberRetrieveResponse`](./src/tembo/types/organizations/member_retrieve_response.py) |

```python
member = client.organizations.members.retrieve(
    organization_id="organizationId",
    member_id="memberId",
)
```

#### Update an organization member

Update an organization member role.

| Direction | Type |
| --- | --- |
| Request | [`MemberUpdateParams`](./src/tembo/types/organizations/member_update_params.py) |
| Response | [`MemberUpdateResponse`](./src/tembo/types/organizations/member_update_response.py) |

```python
member = client.organizations.members.update(
    organization_id="organizationId",
    member_id="memberId",
    role="org:admin",
)
```

#### Remove an organization member

Remove an active member or revoke a pending invitation.

| Direction | Type |
| --- | --- |
| Response | [`MemberDeleteResponse`](./src/tembo/types/organizations/member_delete_response.py) |

```python
member = client.organizations.members.delete(
    organization_id="organizationId",
    member_id="memberId",
)
```

### `Organizations Secrets`

#### List organization secrets

List redacted organization secret summaries with cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`SecretListParams`](./src/tembo/types/organizations/secret_list_params.py) |
| Response | [`SecretListResponse`](./src/tembo/types/organizations/secret_list_response.py) |

```python
secret = client.organizations.secrets.list(
    organization_id="organizationId",
    limit=50,
)
```

#### Create an organization secret

Create an encrypted organization secret.

| Direction | Type |
| --- | --- |
| Request | [`SecretCreateParams`](./src/tembo/types/organizations/secret_create_params.py) |
| Response | [`SecretCreateResponse`](./src/tembo/types/organizations/secret_create_response.py) |

```python
secret = client.organizations.secrets.create(
    organization_id="organizationId",
    key="x",
    value="x",
)
```

#### Retrieve an organization secret

Retrieve a redacted organization secret summary.

| Direction | Type |
| --- | --- |
| Response | [`SecretRetrieveResponse`](./src/tembo/types/organizations/secret_retrieve_response.py) |

```python
secret = client.organizations.secrets.retrieve(
    organization_id="organizationId",
    secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Update an organization secret

Update a secret name, encrypted value, or both.

| Direction | Type |
| --- | --- |
| Request | [`SecretUpdateParams`](./src/tembo/types/organizations/secret_update_params.py) |
| Response | [`SecretUpdateResponse`](./src/tembo/types/organizations/secret_update_response.py) |

```python
secret = client.organizations.secrets.update(
    organization_id="organizationId",
    secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Delete an organization secret

Delete an organization secret.

| Direction | Type |
| --- | --- |
| Response | [`SecretDeleteResponse`](./src/tembo/types/organizations/secret_delete_response.py) |

```python
secret = client.organizations.secrets.delete(
    organization_id="organizationId",
    secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Organizations Settings`

#### Retrieve organization settings

Retrieve effective organization settings, including defaults for settings that have not been configured.

| Direction | Type |
| --- | --- |
| Response | [`SettingRetrieveResponse`](./src/tembo/types/organizations/setting_retrieve_response.py) |

```python
setting = client.organizations.settings.retrieve(
    organization_id="organizationId",
)
```

#### Update organization settings

Configure organization defaults for agent/model, VM size and keep-alive; inference credentials; agent prompts and commit/PR instructions; bot feedback, signing, reports, and insights. Only supplied settings are changed.

| Direction | Type |
| --- | --- |
| Request | [`SettingUpdateParams`](./src/tembo/types/organizations/setting_update_params.py) |
| Response | [`SettingUpdateResponse`](./src/tembo/types/organizations/setting_update_response.py) |

```python
setting = client.organizations.settings.update(
    organization_id="organizationId",
)
```

#### Validate organization provider credentials

Validate supplied inference provider credentials for an organization without saving them. The provider must be available on the organization’s plan.

| Direction | Type |
| --- | --- |
| Request | [`SettingValidateCredentialsParams`](./src/tembo/types/organizations/setting_validate_credentials_params.py) |
| Response | [`SettingValidateCredentialsResponse`](./src/tembo/types/organizations/setting_validate_credentials_response.py) |

```python
setting = client.organizations.settings.validate_credentials(
    organization_id="organizationId",
    provider="anthropic",
    api_key="",
)
```

### `Organizations Subscriptions`

#### Retrieve organization subscriptions

Retrieve connection statuses and available ChatGPT and Claude usage. Provider usage errors are reported without failing the response.

| Direction | Type |
| --- | --- |
| Response | [`SubscriptionRetrieveResponse`](./src/tembo/types/organizations/subscription_retrieve_response.py) |

```python
subscription = client.organizations.subscriptions.retrieve(
    organization_id="organizationId",
)
```

#### Reset organization subscription usage

Redeem an earned ChatGPT rate-limit reset.

| Direction | Type |
| --- | --- |
| Request | [`SubscriptionResetParams`](./src/tembo/types/organizations/subscription_reset_params.py) |
| Response | [`SubscriptionResetResponse`](./src/tembo/types/organizations/subscription_reset_response.py) |

```python
subscription = client.organizations.subscriptions.reset(
    organization_id="organizationId",
    idempotency_key="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    provider="chatgpt",
)
```

## `McpConnections`

### List MCP connections

List MCP connections for the current organization with cursor pagination and optional search by name or URL. Command arguments, headers, and environment configuration are omitted.

| Direction | Type |
| --- | --- |
| Request | [`McpConnectionListParams`](./src/tembo/types/mcp_connection_list_params.py) |
| Response | [`McpConnectionListResponse`](./src/tembo/types/mcp_connection_list_response.py) |

```python
mcp_connection = client.mcp_connections.list(
    limit=50,
)
```

### Create an MCP connection

Create a new stdio or Streamable HTTP MCP connection. Remote connections support OAuth, Client Credentials (M2M), or static headers and begin authorization when required; stdio commands are stored but never executed by this API.

| Direction | Type |
| --- | --- |
| Request | [`McpConnectionCreateParams`](./src/tembo/types/mcp_connection_create_params.py) |
| Response | [`McpConnectionCreateResponse`](./src/tembo/types/mcp_connection_create_response.py) |

```python
mcp_connection = client.mcp_connections.create(
    name="x",
    args=[],
    command="x",
    type="stdio",
    visibility="shared",
)
```

### Retrieve an MCP connection

Retrieve MCP connection configuration and authentication details. Stored header values, environment values, OAuth tokens, and client secrets are never returned.

| Direction | Type |
| --- | --- |
| Response | [`McpConnectionRetrieveResponse`](./src/tembo/types/mcp_connection_retrieve_response.py) |

```python
mcp_connection = client.mcp_connections.retrieve(
    mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update an MCP connection

Update MCP configuration, including OAuth, Client Credentials (M2M), or static-header authentication. Supplied headers merge by key only for unchanged-server static_headers authentication; otherwise they are replaced. Environment values merge by key, null values remove individual keys, and a null environment clears all variables. Hidden credentials are preserved unless explicitly changed or authentication is replaced; changing a remote server URL clears credentials for the old server. Call authorize explicitly after changing the server or authentication to reconnect.

| Direction | Type |
| --- | --- |
| Request | [`McpConnectionUpdateParams`](./src/tembo/types/mcp_connection_update_params.py) |
| Response | [`McpConnectionUpdateResponse`](./src/tembo/types/mcp_connection_update_response.py) |

```python
mcp_connection = client.mcp_connections.update(
    mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    type="remote",
)
```

### Delete an MCP connection

Delete an MCP connection in the current organization.

| Direction | Type |
| --- | --- |
| Response | [`McpConnectionDeleteResponse`](./src/tembo/types/mcp_connection_delete_response.py) |

```python
mcp_connection = client.mcp_connections.delete(
    mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Authorize an MCP connection

Connect or authorize a remote Streamable HTTP MCP connection, returning an OAuth URL when user authorization is required. Stdio connections are rejected because this action cannot authorize them.

| Direction | Type |
| --- | --- |
| Response | [`McpConnectionAuthorizeResponse`](./src/tembo/types/mcp_connection_authorize_response.py) |

```python
mcp_connection = client.mcp_connections.authorize(
    mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Test an MCP connection

Test a remote MCP connection by connecting to its server. Stdio connections are rejected because the API does not execute arbitrary local commands.

| Direction | Type |
| --- | --- |
| Response | [`McpConnectionTestResponse`](./src/tembo/types/mcp_connection_test_response.py) |

```python
mcp_connection = client.mcp_connections.test(
    mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Artifacts`

### List artifacts

List organization artifacts with optional session and type filters.

| Direction | Type |
| --- | --- |
| Request | [`ArtifactListParams`](./src/tembo/types/artifact_list_params.py) |
| Response | [`ArtifactListResponse`](./src/tembo/types/artifact_list_response.py) |

```python
artifact = client.artifacts.list(
    limit=50,
)
```

### Create an artifact

Create a file artifact for a session from inline content or an uploaded asset.

| Direction | Type |
| --- | --- |
| Request | [`ArtifactCreateParams`](./src/tembo/types/artifact_create_params.py) |
| Response | [`ArtifactCreateResponse`](./src/tembo/types/artifact_create_response.py) |

```python
artifact = client.artifacts.create(
    title="x",
    output={"type": "html", "content": "x"},
    session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Retrieve an artifact

Retrieve an organization artifact by ID.

| Direction | Type |
| --- | --- |
| Response | [`ArtifactRetrieveResponse`](./src/tembo/types/artifact_retrieve_response.py) |

```python
artifact = client.artifacts.retrieve(
    artifact_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Delete an artifact

Delete an organization artifact and its backing asset when present.

| Direction | Type |
| --- | --- |
| Response | [`ArtifactDeleteResponse`](./src/tembo/types/artifact_delete_response.py) |

```python
artifact = client.artifacts.delete(
    artifact_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Messages`

### List messages

List organization messages with optional session and thread filters.

| Direction | Type |
| --- | --- |
| Request | [`MessageListParams`](./src/tembo/types/message_list_params.py) |
| Response | [`MessageListResponse`](./src/tembo/types/message_list_response.py) |

```python
message = client.messages.list(
    limit=50,
)
```

### Create a message

Send a task or follow-up message to an existing session, resume work, or steer an active agent turn using deliveryMode.

| Direction | Type |
| --- | --- |
| Request | [`MessageCreateParams`](./src/tembo/types/message_create_params.py) |
| Response | [`MessageCreateResponse`](./src/tembo/types/message_create_response.py) |

```python
message = client.messages.create(
    content="x",
    session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Retrieve a message

Retrieve an organization message by ID.

| Direction | Type |
| --- | --- |
| Response | [`MessageRetrieveResponse`](./src/tembo/types/message_retrieve_response.py) |

```python
message = client.messages.retrieve(
    message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update a message

Update message content before its queued processing has started.

| Direction | Type |
| --- | --- |
| Request | [`MessageUpdateParams`](./src/tembo/types/message_update_params.py) |
| Response | [`MessageUpdateResponse`](./src/tembo/types/message_update_response.py) |

```python
message = client.messages.update(
    message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Delete a message

Delete a message and cancel its queued jobs, runtime turns, and active sandbox sessions.

| Direction | Type |
| --- | --- |
| Response | [`MessageDeleteResponse`](./src/tembo/types/message_delete_response.py) |

```python
message = client.messages.delete(
    message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Models`

### List models

List the models available to the current organization, including enablement and inference-provider access.

| Direction | Type |
| --- | --- |
| Request | [`ModelListParams`](./src/tembo/types/model_list_params.py) |
| Response | [`ModelListResponse`](./src/tembo/types/model_list_response.py) |

```python
model = client.models.list(
    limit=50,
)
```

### Update a model

Enable or disable an organization model, or select its inference provider.

| Direction | Type |
| --- | --- |
| Request | [`ModelUpdateParams`](./src/tembo/types/model_update_params.py) |
| Response | [`ModelUpdateResponse`](./src/tembo/types/model_update_response.py) |

```python
model = client.models.update(
    model_name="claude-opus-5-5",
)
```

## `Runtimes`

### List runtimes

List execution runtimes and their compatible model references for the current organization.

| Direction | Type |
| --- | --- |
| Request | [`RuntimeListParams`](./src/tembo/types/runtime_list_params.py) |
| Response | [`RuntimeListResponse`](./src/tembo/types/runtime_list_response.py) |

```python
runtime = client.runtimes.list(
    limit=50,
)
```

## `Users`

### Retrieve the current user

Retrieve the authenticated user.

| Direction | Type |
| --- | --- |
| Response | [`UserMeResponse`](./src/tembo/types/user_me_response.py) |

```python
user = client.users.me()
```

### Retrieve a user

Retrieve a user profile visible to the caller.

| Direction | Type |
| --- | --- |
| Response | [`UserRetrieveResponse`](./src/tembo/types/user_retrieve_response.py) |

```python
user = client.users.retrieve(
    user_id="userId",
)
```

### Delete a user

Queue permanent deletion of your user account.

| Direction | Type |
| --- | --- |
| Request | [`UserDeleteParams`](./src/tembo/types/user_delete_params.py) |
| Response | [`UserDeleteResponse`](./src/tembo/types/user_delete_response.py) |

```python
user = client.users.delete(
    user_id="userId",
)
```

### `Users Settings`

#### Retrieve user settings

Retrieve user preferences without exposing stored credentials.

| Direction | Type |
| --- | --- |
| Response | [`SettingRetrieveResponse`](./src/tembo/types/users/setting_retrieve_response.py) |

```python
setting = client.users.settings.retrieve(
    user_id="userId",
)
```

#### Update user settings

Configure personal agent/model and project defaults, system instructions, follow-up queue/steer behavior, VM restart, commit signing/attribution, notifications, themes, and review layout. Updates preserve unrelated settings.

| Direction | Type |
| --- | --- |
| Request | [`SettingUpdateParams`](./src/tembo/types/users/setting_update_params.py) |
| Response | [`SettingUpdateResponse`](./src/tembo/types/users/setting_update_response.py) |

```python
setting = client.users.settings.update(
    user_id="userId",
)
```

### `Users ConnectedAccounts`

#### List user connected accounts

List the user identity-provider accounts without returning credentials.

| Direction | Type |
| --- | --- |
| Request | [`ConnectedAccountListParams`](./src/tembo/types/users/connected_account_list_params.py) |
| Response | [`ConnectedAccountListResponse`](./src/tembo/types/users/connected_account_list_response.py) |

```python
connected_account = client.users.connected_accounts.list(
    user_id="userId",
    limit=50,
)
```

#### Retrieve a user connected account

Retrieve one identity-provider account without returning credentials.

| Direction | Type |
| --- | --- |
| Response | [`ConnectedAccountRetrieveResponse`](./src/tembo/types/users/connected_account_retrieve_response.py) |

```python
connected_account = client.users.connected_accounts.retrieve(
    user_id="userId",
    connected_account_id="connectedAccountId",
)
```

### `Users Subscriptions`

#### Retrieve user subscriptions

Retrieve connection statuses and available ChatGPT and Claude usage. Provider usage errors are reported without failing the response.

| Direction | Type |
| --- | --- |
| Response | [`SubscriptionRetrieveResponse`](./src/tembo/types/users/subscription_retrieve_response.py) |

```python
subscription = client.users.subscriptions.retrieve(
    user_id="userId",
)
```

#### Reset user subscription usage

Redeem an earned ChatGPT rate-limit reset.

| Direction | Type |
| --- | --- |
| Request | [`SubscriptionResetParams`](./src/tembo/types/users/subscription_reset_params.py) |
| Response | [`SubscriptionResetResponse`](./src/tembo/types/users/subscription_reset_response.py) |

```python
subscription = client.users.subscriptions.reset(
    user_id="userId",
    idempotency_key="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    provider="chatgpt",
)
```

### `Users ProfilePicture`

#### Retrieve a user profile picture

Redirect to a user's profile picture. Signed URLs are valid for one hour.

```python
client.users.profile_picture.retrieve(
    user_id="userId",
)
```

#### Update your profile picture

Upload a JPEG, PNG, GIF, or WebP profile picture up to 5 MB.

| Direction | Type |
| --- | --- |
| Request | [`ProfilePictureUpdateParams`](./src/tembo/types/users/profile_picture_update_params.py) |
| Response | [`ProfilePictureUpdateResponse`](./src/tembo/types/users/profile_picture_update_response.py) |

```python
profile_picture = client.users.profile_picture.update(
    user_id="userId",
    file=b"file",
)
```

#### Delete your profile picture

Delete your profile picture. This succeeds if no picture exists.

| Direction | Type |
| --- | --- |
| Response | [`ProfilePictureDeleteResponse`](./src/tembo/types/users/profile_picture_delete_response.py) |

```python
profile_picture = client.users.profile_picture.delete(
    user_id="userId",
)
```

## `Sessions`

### List sessions

List and search sessions, including active or archived sessions, with repository, project, creator, and source filters and cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`SessionListParams`](./src/tembo/types/session_list_params.py) |
| Response | [`SessionListResponse`](./src/tembo/types/session_list_response.py) |

```python
session = client.sessions.list(
    limit=50,
    include_archived=True,
    include_total=False,
    sort_by="lastQueuedAt",
    state="all",
)
```

### Create a session

Create a session for a task. Provide the initial prompt in description and optionally configure its repositories, agent, Build (normal) or Plan (planning) mode, and private or workspace visibility.

| Direction | Type |
| --- | --- |
| Request | [`SessionCreateParams`](./src/tembo/types/session_create_params.py) |
| Response | [`SessionCreateResponse`](./src/tembo/types/session_create_response.py) |

```python
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
```

### Retrieve a session

Retrieve a session you have permission to access.

| Direction | Type |
| --- | --- |
| Response | [`SessionRetrieveResponse`](./src/tembo/types/session_retrieve_response.py) |

```python
session = client.sessions.retrieve(
    session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update a session

Update a session: archive or restore it, set priority, rename it, change agent/model, switch between Build (normal) and Plan (planning) modes, configure its workspace and branches, or change visibility between private and visible to workspace (public). Archiving uses level=0; restoring archived sessions uses level=1 and does not restart work. Use pins to pin or unpin sessions.

| Direction | Type |
| --- | --- |
| Request | [`SessionUpdateParams`](./src/tembo/types/session_update_params.py) |
| Response | [`SessionUpdateResponse`](./src/tembo/types/session_update_response.py) |

```python
session = client.sessions.update(
    session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Delete a session

Archive a session and stop its VM without permanently deleting it. Equivalent to updateSession with level=0; restore with updateSession and level=1.

| Direction | Type |
| --- | --- |
| Response | [`SessionDeleteResponse`](./src/tembo/types/session_delete_response.py) |

```python
session = client.sessions.delete(
    session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Fork a session

Create an independent session from a fresh workspace snapshot, or the latest saved snapshot when stopped, without replaying messages or adding context.

| Direction | Type |
| --- | --- |
| Request | [`SessionForkParams`](./src/tembo/types/session_fork_params.py) |
| Response | [`SessionForkResponse`](./src/tembo/types/session_fork_response.py) |

```python
session = client.sessions.fork(
    session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    queue_right_away=True,
)
```

### Stop a session

Interrupt active session work without archiving it. Continue with the next queued message, or set cancelQueued=true to cancel pending messages too.

| Direction | Type |
| --- | --- |
| Request | [`SessionStopParams`](./src/tembo/types/session_stop_params.py) |
| Response | [`SessionStopResponse`](./src/tembo/types/session_stop_response.py) |

```python
session = client.sessions.stop(
    session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### List session events

List recorded session stream events with cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`SessionListEventsParams`](./src/tembo/types/session_list_events_params.py) |
| Response | [`SessionListEventsResponse`](./src/tembo/types/session_list_events_response.py) |

```python
session = client.sessions.list_events(
    session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=50,
)
```

### `Sessions Sources`

#### List session sources

List session sources in the authenticated organization.

| Direction | Type |
| --- | --- |
| Request | [`SourceListParams`](./src/tembo/types/sessions/source_list_params.py) |
| Response | [`SourceListResponse`](./src/tembo/types/sessions/source_list_response.py) |

```python
source = client.sessions.sources.list(
    limit=50,
    include_total=False,
)
```

#### Retrieve a session source

Retrieve one session source.

| Direction | Type |
| --- | --- |
| Response | [`SourceRetrieveResponse`](./src/tembo/types/sessions/source_retrieve_response.py) |

```python
source = client.sessions.sources.retrieve(
    source_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Sessions Diffs`

#### List session diffs

List recorded session diff metadata with cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`DiffListParams`](./src/tembo/types/sessions/diff_list_params.py) |
| Response | [`DiffListResponse`](./src/tembo/types/sessions/diff_list_response.py) |

```python
diff = client.sessions.diffs.list(
    session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=50,
)
```

#### Retrieve a session diff

Retrieve one recorded session diff and its content.

| Direction | Type |
| --- | --- |
| Response | [`DiffRetrieveResponse`](./src/tembo/types/sessions/diff_retrieve_response.py) |

```python
diff = client.sessions.diffs.retrieve(
    session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    diff_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Projects`

### Update project defaults

Choose the default project and sandbox size for the organization.

| Direction | Type |
| --- | --- |
| Request | [`ProjectUpdateDefaultsParams`](./src/tembo/types/project_update_defaults_params.py) |
| Response | [`ProjectUpdateDefaultsResponse`](./src/tembo/types/project_update_defaults_response.py) |

```python
project = client.projects.update_defaults(
    project_id="x",
    sandbox_size="nano",
)
```

### List projects

List projects in the authenticated organization.

| Direction | Type |
| --- | --- |
| Request | [`ProjectListParams`](./src/tembo/types/project_list_params.py) |
| Response | [`ProjectListResponse`](./src/tembo/types/project_list_response.py) |

```python
project = client.projects.list(
    limit=50,
)
```

### Create a project

Create a reusable project environment.

| Direction | Type |
| --- | --- |
| Request | [`ProjectCreateParams`](./src/tembo/types/project_create_params.py) |
| Response | [`ProjectCreateResponse`](./src/tembo/types/project_create_response.py) |

```python
project = client.projects.create(
    name="x",
    sizes=["nano"],
)
```

### Retrieve a project

Retrieve project configuration. Use the project subresources to list snapshots, builds, schedules, and environment variables.

| Direction | Type |
| --- | --- |
| Response | [`ProjectRetrieveResponse`](./src/tembo/types/project_retrieve_response.py) |

```python
project = client.projects.retrieve(
    project_id="projectId",
)
```

### Update a project

Update project repositories, setup script, agent instructions, environment variables, VM sizes and defaults; enable or pause scheduled builds or the warm pool; rename or customize its appearance.

| Direction | Type |
| --- | --- |
| Request | [`ProjectUpdateParams`](./src/tembo/types/project_update_params.py) |
| Response | [`ProjectUpdateResponse`](./src/tembo/types/project_update_response.py) |

```python
project = client.projects.update(
    project_id="projectId",
)
```

### Delete a project

Archive a project, remove its default VM-size assignments, and disable its build schedule. This does not permanently delete the project record.

| Direction | Type |
| --- | --- |
| Response | [`ProjectDeleteResponse`](./src/tembo/types/project_delete_response.py) |

```python
project = client.projects.delete(
    project_id="projectId",
)
```

### Duplicate a project

Create a new project with the same configuration, environment variables, and schedule as an existing project. Snapshots are not copied.

| Direction | Type |
| --- | --- |
| Response | [`ProjectDuplicateResponse`](./src/tembo/types/project_duplicate_response.py) |

```python
project = client.projects.duplicate(
    project_id="projectId",
)
```

### `Projects EnvironmentVariables`

#### List project environment variables

List environment-variable names without exposing values.

| Direction | Type |
| --- | --- |
| Response | [`EnvironmentVariableListResponse`](./src/tembo/types/projects/environment_variable_list_response.py) |

```python
environment_variable = client.projects.environment_variables.list(
    project_id="projectId",
)
```

#### Create project environment variables

Create one or more encrypted project environment variables.

| Direction | Type |
| --- | --- |
| Request | [`EnvironmentVariableCreateParams`](./src/tembo/types/projects/environment_variable_create_params.py) |
| Response | [`EnvironmentVariableCreateResponse`](./src/tembo/types/projects/environment_variable_create_response.py) |

```python
environment_variable = client.projects.environment_variables.create(
    project_id="projectId",
    secrets=[{"key": "", "value": "x"}],
)
```

#### Delete a project environment variable

Delete one encrypted project environment variable.

| Direction | Type |
| --- | --- |
| Response | [`EnvironmentVariableDeleteResponse`](./src/tembo/types/projects/environment_variable_delete_response.py) |

```python
environment_variable = client.projects.environment_variables.delete(
    project_id="projectId",
    key="key",
)
```

### `Projects Snapshots`

#### List project snapshots

List recent VM snapshots built for a project.

| Direction | Type |
| --- | --- |
| Request | [`SnapshotListParams`](./src/tembo/types/projects/snapshot_list_params.py) |
| Response | [`SnapshotListResponse`](./src/tembo/types/projects/snapshot_list_response.py) |

```python
snapshot = client.projects.snapshots.list(
    project_id="projectId",
    limit=50,
)
```

#### Retrieve a project snapshot

Retrieve one project snapshot.

| Direction | Type |
| --- | --- |
| Response | [`SnapshotRetrieveResponse`](./src/tembo/types/projects/snapshot_retrieve_response.py) |

```python
snapshot = client.projects.snapshots.retrieve(
    project_id="projectId",
    snapshot_id="snapshotId",
)
```

#### Update a project snapshot

Rename a snapshot or choose whether it is pinned.

| Direction | Type |
| --- | --- |
| Request | [`SnapshotUpdateParams`](./src/tembo/types/projects/snapshot_update_params.py) |
| Response | [`SnapshotUpdateResponse`](./src/tembo/types/projects/snapshot_update_response.py) |

```python
snapshot = client.projects.snapshots.update(
    project_id="projectId",
    snapshot_id="snapshotId",
)
```

#### Delete a project snapshot

Delete a project snapshot.

| Direction | Type |
| --- | --- |
| Response | [`SnapshotDeleteResponse`](./src/tembo/types/projects/snapshot_delete_response.py) |

```python
snapshot = client.projects.snapshots.delete(
    project_id="projectId",
    snapshot_id="snapshotId",
)
```

### `Projects Builds`

#### List project builds

List recent queued, running, and failed project builds.

| Direction | Type |
| --- | --- |
| Request | [`BuildListParams`](./src/tembo/types/projects/build_list_params.py) |
| Response | [`BuildListResponse`](./src/tembo/types/projects/build_list_response.py) |

```python
build = client.projects.builds.list(
    project_id="projectId",
    limit=50,
)
```

#### Create a project build

Build selected project sizes or rebuild one snapshot.

| Direction | Type |
| --- | --- |
| Request | [`BuildCreateParams`](./src/tembo/types/projects/build_create_params.py) |
| Response | [`BuildCreateResponse`](./src/tembo/types/projects/build_create_response.py) |

```python
build = client.projects.builds.create(
    project_id="projectId",
)
```

#### Retrieve a project build

Retrieve project build status.

| Direction | Type |
| --- | --- |
| Response | [`BuildRetrieveResponse`](./src/tembo/types/projects/build_retrieve_response.py) |

```python
build = client.projects.builds.retrieve(
    project_id="projectId",
    build_id="buildId",
)
```

#### Cancel a project build

Cancel an active queued or running project build.

| Direction | Type |
| --- | --- |
| Response | [`BuildCancelResponse`](./src/tembo/types/projects/build_cancel_response.py) |

```python
build = client.projects.builds.cancel(
    project_id="projectId",
    build_id="buildId",
)
```

### `Projects Schedules`

#### List project schedules

List schedules linked to a project.

| Direction | Type |
| --- | --- |
| Request | [`ScheduleListParams`](./src/tembo/types/projects/schedule_list_params.py) |
| Response | [`ScheduleListResponse`](./src/tembo/types/projects/schedule_list_response.py) |

```python
schedule = client.projects.schedules.list(
    project_id="projectId",
    limit=50,
)
```

#### Create a project schedule

Create a recurring project build schedule.

| Direction | Type |
| --- | --- |
| Request | [`ScheduleCreateParams`](./src/tembo/types/projects/schedule_create_params.py) |
| Response | [`ScheduleCreateResponse`](./src/tembo/types/projects/schedule_create_response.py) |

```python
schedule = client.projects.schedules.create(
    project_id="projectId",
    cron="x",
)
```

#### Retrieve a project schedule

Retrieve one project build schedule.

| Direction | Type |
| --- | --- |
| Response | [`ScheduleRetrieveResponse`](./src/tembo/types/projects/schedule_retrieve_response.py) |

```python
schedule = client.projects.schedules.retrieve(
    project_id="projectId",
    schedule_id="scheduleId",
)
```

#### Update a project schedule

Update timing or enabled state for a project schedule.

| Direction | Type |
| --- | --- |
| Request | [`ScheduleUpdateParams`](./src/tembo/types/projects/schedule_update_params.py) |
| Response | [`ScheduleUpdateResponse`](./src/tembo/types/projects/schedule_update_response.py) |

```python
schedule = client.projects.schedules.update(
    project_id="projectId",
    schedule_id="scheduleId",
)
```

#### Delete a project schedule

Disable a project build schedule.

| Direction | Type |
| --- | --- |
| Response | [`ScheduleDeleteResponse`](./src/tembo/types/projects/schedule_delete_response.py) |

```python
schedule = client.projects.schedules.delete(
    project_id="projectId",
    schedule_id="scheduleId",
)
```

## `Pins`

### List pins

List your pinned resources in pin order.

| Direction | Type |
| --- | --- |
| Request | [`PinListParams`](./src/tembo/types/pin_list_params.py) |
| Response | [`PinListResponse`](./src/tembo/types/pin_list_response.py) |

```python
pin = client.pins.list(
    limit=50,
)
```

### Create a pin

Pin a session, pull request, or project you have permission to access.

| Direction | Type |
| --- | --- |
| Request | [`PinCreateParams`](./src/tembo/types/pin_create_params.py) |
| Response | [`PinCreateResponse`](./src/tembo/types/pin_create_response.py) |

```python
pin = client.pins.create(
    type="session",
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update a pin

Reorder a pinned session, pull request, or project before or after another pin for the authenticated user. Use createPin to pin a resource and deletePin to unpin it.

| Direction | Type |
| --- | --- |
| Request | [`PinUpdateParams`](./src/tembo/types/pin_update_params.py) |
| Response | [`PinUpdateResponse`](./src/tembo/types/pin_update_response.py) |

```python
pin = client.pins.update(
    resource_type="session",
    resource_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    placement={"target": {"type": "session", "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}, "position": "before"},
)
```

### Delete a pin

Unpin a session, pull request, or project for the authenticated user without deleting or archiving the resource.

| Direction | Type |
| --- | --- |
| Response | [`PinDeleteResponse`](./src/tembo/types/pin_delete_response.py) |

```python
pin = client.pins.delete(
    resource_type="session",
    resource_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `PullRequests`

### List pull requests

List pull requests for the authenticated organization with cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`PullRequestListParams`](./src/tembo/types/pull_request_list_params.py) |
| Response | [`PullRequestListResponse`](./src/tembo/types/pull_request_list_response.py) |

```python
pull_request = client.pull_requests.list(
    limit=50,
)
```

### Retrieve a pull request

Retrieve a pull request for the authenticated organization.

| Direction | Type |
| --- | --- |
| Response | [`PullRequestRetrieveResponse`](./src/tembo/types/pull_request_retrieve_response.py) |

```python
pull_request = client.pull_requests.retrieve(
    pull_request_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Agents`

### List agents

List agents available in your organization, with optional search, status, integration, and author filters.

| Direction | Type |
| --- | --- |
| Request | [`AgentListParams`](./src/tembo/types/agent_list_params.py) |
| Response | [`AgentListResponse`](./src/tembo/types/agent_list_response.py) |

```python
agent = client.agents.list(
    limit=50,
)
```

### Create an agent

Create an agent from instructions, a template, or another agent. sourceAgentId cannot be combined with other fields. Template creation accepts only templateName, name, and triggers; creation from scratch requires name.

| Direction | Type |
| --- | --- |
| Request | [`AgentCreateParams`](./src/tembo/types/agent_create_params.py) |
| Response | [`AgentCreateResponse`](./src/tembo/types/agent_create_response.py) |

```python
agent = client.agents.create()
```

### Retrieve an agent

Retrieve an agent and its configuration, repository associations, and run summary.

| Direction | Type |
| --- | --- |
| Response | [`AgentRetrieveResponse`](./src/tembo/types/agent_retrieve_response.py) |

```python
agent = client.agents.retrieve(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update an agent

Update agent instructions, model, workspace, repositories, or persistent state; enable or pause the agent; archive or restore it. enabled and archived also control its schedules and triggers. Supply expectedUpdatedAt to reject concurrent changes.

| Direction | Type |
| --- | --- |
| Request | [`AgentUpdateParams`](./src/tembo/types/agent_update_params.py) |
| Response | [`AgentUpdateResponse`](./src/tembo/types/agent_update_response.py) |

```python
agent = client.agents.update(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Delete an agent

Archive an agent and disable its scheduled and triggered jobs without permanently deleting it. Restore with updateAgent and archived=false.

| Direction | Type |
| --- | --- |
| Response | [`AgentDeleteResponse`](./src/tembo/types/agent_delete_response.py) |

```python
agent = client.agents.delete(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Agents Templates`

#### List agent templates

List reusable agent templates and their configuration requirements.

| Direction | Type |
| --- | --- |
| Request | [`TemplateListParams`](./src/tembo/types/agents/template_list_params.py) |
| Response | [`TemplateListResponse`](./src/tembo/types/agents/template_list_response.py) |

```python
template = client.agents.templates.list(
    limit=50,
)
```

#### Retrieve an agent template

Retrieve a reusable agent template by name, including its instructions and required parameters.

| Direction | Type |
| --- | --- |
| Response | [`TemplateRetrieveResponse`](./src/tembo/types/agents/template_retrieve_response.py) |

```python
template = client.agents.templates.retrieve(
    template_name="templateName",
)
```

### `Agents Schedules`

#### List agent schedules

List the schedules configured for an agent.

| Direction | Type |
| --- | --- |
| Request | [`ScheduleListParams`](./src/tembo/types/agents/schedule_list_params.py) |
| Response | [`ScheduleListResponse`](./src/tembo/types/agents/schedule_list_response.py) |

```python
schedule = client.agents.schedules.list(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=50,
)
```

#### Create an agent schedule

Create a recurring schedule that starts agent runs using a cron expression.

| Direction | Type |
| --- | --- |
| Request | [`ScheduleCreateParams`](./src/tembo/types/agents/schedule_create_params.py) |
| Response | [`ScheduleCreateResponse`](./src/tembo/types/agents/schedule_create_response.py) |

```python
schedule = client.agents.schedules.create(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    cron="x",
)
```

#### Retrieve an agent schedule

Retrieve an agent schedule, including its enabled state and next execution time.

| Direction | Type |
| --- | --- |
| Response | [`ScheduleRetrieveResponse`](./src/tembo/types/agents/schedule_retrieve_response.py) |

```python
schedule = client.agents.schedules.retrieve(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Update an agent schedule

Change an agent schedule cron expression. Use updateAgent with enabled to enable or pause the agent and its schedules.

| Direction | Type |
| --- | --- |
| Request | [`ScheduleUpdateParams`](./src/tembo/types/agents/schedule_update_params.py) |
| Response | [`ScheduleUpdateResponse`](./src/tembo/types/agents/schedule_update_response.py) |

```python
schedule = client.agents.schedules.update(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    cron="x",
)
```

#### Delete an agent schedule

Delete a recurring agent schedule.

| Direction | Type |
| --- | --- |
| Response | [`ScheduleDeleteResponse`](./src/tembo/types/agents/schedule_delete_response.py) |

```python
schedule = client.agents.schedules.delete(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Agents Triggers`

#### List agent triggers

List the integration events configured to start runs of an agent.

| Direction | Type |
| --- | --- |
| Request | [`TriggerListParams`](./src/tembo/types/agents/trigger_list_params.py) |
| Response | [`TriggerListResponse`](./src/tembo/types/agents/trigger_list_response.py) |

```python
trigger = client.agents.triggers.list(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=50,
)
```

#### Create an agent trigger

Configure an integration event to start agent runs. Available filters depend on the integration and event name.

| Direction | Type |
| --- | --- |
| Request | [`TriggerCreateParams`](./src/tembo/types/agents/trigger_create_params.py) |
| Response | [`TriggerCreateResponse`](./src/tembo/types/agents/trigger_create_response.py) |

```python
trigger = client.agents.triggers.create(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
)
```

#### Retrieve an agent trigger

Retrieve an agent trigger and its integration event filters.

| Direction | Type |
| --- | --- |
| Response | [`TriggerRetrieveResponse`](./src/tembo/types/agents/trigger_retrieve_response.py) |

```python
trigger = client.agents.triggers.retrieve(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Update an agent trigger

Change an agent trigger event, integration, or filters. Use updateAgent with enabled to enable or pause the agent and its triggers.

| Direction | Type |
| --- | --- |
| Request | [`TriggerUpdateParams`](./src/tembo/types/agents/trigger_update_params.py) |
| Response | [`TriggerUpdateResponse`](./src/tembo/types/agents/trigger_update_response.py) |

```python
trigger = client.agents.triggers.update(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
)
```

#### Delete an agent trigger

Delete an integration event trigger for an agent.

| Direction | Type |
| --- | --- |
| Response | [`TriggerDeleteResponse`](./src/tembo/types/agents/trigger_delete_response.py) |

```python
trigger = client.agents.triggers.delete(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Agents Runs`

#### List agent runs

List executions of an agent, including status, linked session, measured duration, and failure summary.

| Direction | Type |
| --- | --- |
| Request | [`RunListParams`](./src/tembo/types/agents/run_list_params.py) |
| Response | [`RunListResponse`](./src/tembo/types/agents/run_list_response.py) |

```python
run = client.agents.runs.list(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=50,
)
```

#### Create an agent run

Queue an agent run. The entire JSON object body is passed to the agent as event input; no eventPayload wrapper is needed. Omit the body to run without event input. The response confirms queuing, not completed execution.

| Direction | Type |
| --- | --- |
| Request | [`RunCreateParams`](./src/tembo/types/agents/run_create_params.py) |
| Response | [`RunCreateResponse`](./src/tembo/types/agents/run_create_response.py) |

```python
run = client.agents.runs.create(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Retrieve an agent run

Retrieve the status, linked session, measured duration, and failure summary of an agent run.

| Direction | Type |
| --- | --- |
| Response | [`RunRetrieveResponse`](./src/tembo/types/agents/run_retrieve_response.py) |

```python
run = client.agents.runs.retrieve(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Agents ContentRevisions`

#### List agent instruction revisions

List saved revisions of an agent’s instruction JSON document, newest first. Revisions do not include other agent configuration. Author details are redacted from public API responses.

| Direction | Type |
| --- | --- |
| Request | [`ContentRevisionListParams`](./src/tembo/types/agents/content_revision_list_params.py) |
| Response | [`ContentRevisionListResponse`](./src/tembo/types/agents/content_revision_list_response.py) |

```python
content_revision = client.agents.content_revisions.list(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=50,
)
```

#### Retrieve an agent instruction revision

Retrieve the instruction JSON document saved in one revision. Other agent configuration is not included. Author details are redacted from public API responses.

| Direction | Type |
| --- | --- |
| Response | [`ContentRevisionRetrieveResponse`](./src/tembo/types/agents/content_revision_retrieve_response.py) |

```python
content_revision = client.agents.content_revisions.retrieve(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    version=1,
)
```

#### Restore agent instructions

Restore a saved instruction JSON document and its mentioned integrations, without reverting other agent configuration. A changed document creates a new revision attributed to the caller. Supply the agent’s current contentVersion as expectedContentVersion; a concurrent instruction change returns 409.

| Direction | Type |
| --- | --- |
| Request | [`ContentRevisionRestoreParams`](./src/tembo/types/agents/content_revision_restore_params.py) |
| Response | [`ContentRevisionRestoreResponse`](./src/tembo/types/agents/content_revision_restore_response.py) |

```python
content_revision = client.agents.content_revisions.restore(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    version=1,
    expected_content_version=1,
)
```

## `Repositories`

### List repositories

List repositories in the authenticated organization. Defaults to enabled repositories.

| Direction | Type |
| --- | --- |
| Request | [`RepositoryListParams`](./src/tembo/types/repository_list_params.py) |
| Response | [`RepositoryListResponse`](./src/tembo/types/repository_list_response.py) |

```python
repository = client.repositories.list(
    limit=50,
    enabled="all",
    order="desc",
    sort="pullRequests",
)
```

### Retrieve a repository

Retrieve a repository in the authenticated organization.

| Direction | Type |
| --- | --- |
| Response | [`RepositoryRetrieveResponse`](./src/tembo/types/repository_retrieve_response.py) |

```python
repository = client.repositories.retrieve(
    repository_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update a repository

Update repository configuration or enable or disable it.

| Direction | Type |
| --- | --- |
| Request | [`RepositoryUpdateParams`](./src/tembo/types/repository_update_params.py) |
| Response | [`RepositoryUpdateResponse`](./src/tembo/types/repository_update_response.py) |

```python
repository = client.repositories.update(
    repository_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    enabled=False,
)
```

## `Integrations`

### List integrations

List integrations visible to the current organization or authenticated admin.

| Direction | Type |
| --- | --- |
| Request | [`IntegrationListParams`](./src/tembo/types/integration_list_params.py) |
| Response | [`IntegrationListResponse`](./src/tembo/types/integration_list_response.py) |

```python
integration = client.integrations.list(
    limit=50,
    include_total=False,
)
```

### Create an integration

Connect AWS, BigQuery, GitLab, PostgreSQL, Snyk, OpenConnect VPN, or Tailscale using provider credentials. For browser-authorized providers, use listIntegrationProviders and authorizeIntegration instead.

| Direction | Type |
| --- | --- |
| Request | [`IntegrationCreateParams`](./src/tembo/types/integration_create_params.py) |
| Response | [`IntegrationCreateResponse`](./src/tembo/types/integration_create_response.py) |

```python
integration = client.integrations.create(
    environment="x",
    role_arn="x",
    type="aws",
)
```

### Retrieve an integration

Retrieve an integration and its configuration.

| Direction | Type |
| --- | --- |
| Response | [`IntegrationRetrieveResponse`](./src/tembo/types/integration_retrieve_response.py) |

```python
integration = client.integrations.retrieve(
    integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update an integration

Update integration settings such as the default repository, Slack channel restrictions, automatic solving, or Sentry environments; replace AWS or PostgreSQL configuration; set or remove Atlassian service-account credentials.

| Direction | Type |
| --- | --- |
| Request | [`IntegrationUpdateParams`](./src/tembo/types/integration_update_params.py) |
| Response | [`IntegrationUpdateResponse`](./src/tembo/types/integration_update_response.py) |

```python
integration = client.integrations.update(
    integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    settings={},
)
```

### Delete an integration

Uninstall an integration from its provider when supported, then delete it from Tembo.

| Direction | Type |
| --- | --- |
| Response | [`IntegrationDeleteResponse`](./src/tembo/types/integration_delete_response.py) |

```python
integration = client.integrations.delete(
    integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Authorize an integration

Return the provider authorization URL for an integration.

| Direction | Type |
| --- | --- |
| Request | [`IntegrationAuthorizeParams`](./src/tembo/types/integration_authorize_params.py) |
| Response | [`IntegrationAuthorizeResponse`](./src/tembo/types/integration_authorize_response.py) |

```python
integration = client.integrations.authorize(
    integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Test an integration

Test the saved provider connection.

| Direction | Type |
| --- | --- |
| Response | [`IntegrationTestResponse`](./src/tembo/types/integration_test_response.py) |

```python
integration = client.integrations.test(
    integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Sync an integration

Queue or immediately perform an integration sync.

| Direction | Type |
| --- | --- |
| Request | [`IntegrationSyncParams`](./src/tembo/types/integration_sync_params.py) |
| Response | [`IntegrationSyncResponse`](./src/tembo/types/integration_sync_response.py) |

```python
integration = client.integrations.sync(
    integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    mode="queued",
)
```

### Sync eligible integrations

Queue integration and pull-request sync jobs for integrations with enabled repositories.

| Direction | Type |
| --- | --- |
| Request | [`IntegrationSyncAllParams`](./src/tembo/types/integration_sync_all_params.py) |
| Response | [`IntegrationSyncAllResponse`](./src/tembo/types/integration_sync_all_response.py) |

```python
integration = client.integrations.sync_all()
```

### Retrieve integration sync status

Count active sync jobs for an integration or eligible integrations.

| Direction | Type |
| --- | --- |
| Request | [`IntegrationRetrieveSyncStatusParams`](./src/tembo/types/integration_retrieve_sync_status_params.py) |
| Response | [`IntegrationRetrieveSyncStatusResponse`](./src/tembo/types/integration_retrieve_sync_status_response.py) |

```python
integration = client.integrations.retrieve_sync_status()
```

### Retrieve an integration rate limit

Retrieve the GitHub installation rate-limit state.

| Direction | Type |
| --- | --- |
| Response | [`IntegrationRetrieveRateLimitResponse`](./src/tembo/types/integration_retrieve_rate_limit_response.py) |

```python
integration = client.integrations.retrieve_rate_limit(
    integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### List Sentry environments

List environments visible to a Sentry integration.

| Direction | Type |
| --- | --- |
| Request | [`IntegrationListSentryEnvironmentsParams`](./src/tembo/types/integration_list_sentry_environments_params.py) |
| Response | [`IntegrationListSentryEnvironmentsResponse`](./src/tembo/types/integration_list_sentry_environments_response.py) |

```python
integration = client.integrations.list_sentry_environments(
    integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=50,
)
```

### List Slack channels

List channels visible to a Slack integration.

| Direction | Type |
| --- | --- |
| Request | [`IntegrationListSlackChannelsParams`](./src/tembo/types/integration_list_slack_channels_params.py) |
| Response | [`IntegrationListSlackChannelsResponse`](./src/tembo/types/integration_list_slack_channels_response.py) |

```python
integration = client.integrations.list_slack_channels(
    integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=50,
)
```

### `Integrations Providers`

#### List integration providers

List providers available to the current organization.

| Direction | Type |
| --- | --- |
| Request | [`ProviderListParams`](./src/tembo/types/integrations/provider_list_params.py) |
| Response | [`ProviderListResponse`](./src/tembo/types/integrations/provider_list_response.py) |

```python
provider = client.integrations.providers.list(
    limit=50,
)
```

#### Discover Snyk organizations

Validate Snyk service-account credentials and list accessible organizations.

| Direction | Type |
| --- | --- |
| Request | [`ProviderDiscoverSnykOrganizationsParams`](./src/tembo/types/integrations/provider_discover_snyk_organizations_params.py) |
| Response | [`ProviderDiscoverSnykOrganizationsResponse`](./src/tembo/types/integrations/provider_discover_snyk_organizations_response.py) |

```python
provider = client.integrations.providers.discover_snyk_organizations(
    client_id="x",
    client_secret="x",
    limit=50,
)
```

### `Integrations Triggers`

#### List integration triggers

List visible automation triggers grouped by provider.

| Direction | Type |
| --- | --- |
| Request | [`TriggerListParams`](./src/tembo/types/integrations/trigger_list_params.py) |
| Response | [`TriggerListResponse`](./src/tembo/types/integrations/trigger_list_response.py) |

```python
trigger = client.integrations.triggers.list(
    limit=50,
)
```

#### Retrieve an integration trigger

Retrieve a trigger definition and its default filter values for an integration in the current organization.

| Direction | Type |
| --- | --- |
| Response | [`TriggerRetrieveResponse`](./src/tembo/types/integrations/trigger_retrieve_response.py) |

```python
trigger = client.integrations.triggers.retrieve(
    integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    trigger_name="triggerName",
)
```

#### List integration trigger filter options

List one cursor-page of selectable values for an integration trigger filter field, with optional search.

| Direction | Type |
| --- | --- |
| Request | [`TriggerListFilterOptionsParams`](./src/tembo/types/integrations/trigger_list_filter_options_params.py) |
| Response | [`TriggerListFilterOptionsResponse`](./src/tembo/types/integrations/trigger_list_filter_options_response.py) |

```python
trigger = client.integrations.triggers.list_filter_options(
    integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    trigger_name="triggerName",
    field="field",
    limit=50,
)
```

## `Billing`

### Retrieve billing

Retrieve billing and credit information for the organization.

| Direction | Type |
| --- | --- |
| Response | [`BillingRetrieveResponse`](./src/tembo/types/billing_retrieve_response.py) |

```python
billing = client.billing.retrieve()
```

### List billing usage

List session usage with cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`BillingListUsageParams`](./src/tembo/types/billing_list_usage_params.py) |
| Response | [`BillingListUsageResponse`](./src/tembo/types/billing_list_usage_response.py) |

```python
billing = client.billing.list_usage(
    limit=50,
)
```

## `Live`

### Authorize a live connection

Issue a 30-second WebSocket ticket for one live connection that multiplexes resource subscriptions.

| Direction | Type |
| --- | --- |
| Response | [`LiveAuthorizeResponse`](./src/tembo/types/live_authorize_response.py) |

```python
live = client.live.authorize()
```

### Live resource subscriptions

Native WebSocket. Send `{ op: "subscribe", id, resource, input }`, `{ op: "unsubscribe", id }`, or `{ op: "ping" }`; receive `{ id, type: "ready" | "event" | "error" }` or `{ type: "pong" }`.

| Direction | Type |
| --- | --- |
| Request | [`LiveConnectParams`](./src/tembo/types/live_connect_params.py) |

```python
with client.live.connect() as connection:
    message = connection.recv()
    print(message)
```
