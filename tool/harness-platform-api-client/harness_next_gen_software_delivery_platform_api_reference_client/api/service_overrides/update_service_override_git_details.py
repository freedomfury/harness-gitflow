from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.git_metadata_update_request_info import GitMetadataUpdateRequestInfo
from ...models.response_dto_service_override_git_update_response import ResponseDTOServiceOverrideGitUpdateResponse
from ...models.update_service_override_git_details_service_overrides_type import (
    UpdateServiceOverrideGitDetailsServiceOverridesType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    identifier: str | Unset = UNSET,
    environment_ref: str | Unset = UNSET,
    service_ref: str | Unset = UNSET,
    infra_identifier: str | Unset = UNSET,
    service_overrides_type: UpdateServiceOverrideGitDetailsServiceOverridesType | Unset = UNSET,
    connector_ref: GitMetadataUpdateRequestInfo | Unset = UNSET,
    repo_name: GitMetadataUpdateRequestInfo | Unset = UNSET,
    file_path: GitMetadataUpdateRequestInfo | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["identifier"] = identifier

    params["environmentRef"] = environment_ref

    params["serviceRef"] = service_ref

    params["infraIdentifier"] = infra_identifier

    json_service_overrides_type: str | Unset = UNSET
    if not isinstance(service_overrides_type, Unset):
        json_service_overrides_type = service_overrides_type

    params["serviceOverridesType"] = json_service_overrides_type

    json_connector_ref: dict[str, Any] | Unset = UNSET
    if not isinstance(connector_ref, Unset):
        json_connector_ref = connector_ref.to_dict()
    if not isinstance(json_connector_ref, Unset):
        params.update(json_connector_ref)

    json_repo_name: dict[str, Any] | Unset = UNSET
    if not isinstance(repo_name, Unset):
        json_repo_name = repo_name.to_dict()
    if not isinstance(json_repo_name, Unset):
        params.update(json_repo_name)

    json_file_path: dict[str, Any] | Unset = UNSET
    if not isinstance(file_path, Unset):
        json_file_path = file_path.to_dict()
    if not isinstance(json_file_path, Unset):
        params.update(json_file_path)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/serviceOverrides/update-git-metadata",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOServiceOverrideGitUpdateResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOServiceOverrideGitUpdateResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOServiceOverrideGitUpdateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    identifier: str | Unset = UNSET,
    environment_ref: str | Unset = UNSET,
    service_ref: str | Unset = UNSET,
    infra_identifier: str | Unset = UNSET,
    service_overrides_type: UpdateServiceOverrideGitDetailsServiceOverridesType | Unset = UNSET,
    connector_ref: GitMetadataUpdateRequestInfo | Unset = UNSET,
    repo_name: GitMetadataUpdateRequestInfo | Unset = UNSET,
    file_path: GitMetadataUpdateRequestInfo | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOServiceOverrideGitUpdateResponse]:
    """Update git-metadata in remote ServiceOverride Entity

     Update git-metadata in remote ServiceOverride and returns the identifier of updated ServiceOverride

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        identifier (str | Unset):
        environment_ref (str | Unset):
        service_ref (str | Unset):
        infra_identifier (str | Unset):
        service_overrides_type (UpdateServiceOverrideGitDetailsServiceOverridesType | Unset):
        connector_ref (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params
            that can be updated for given entity
        repo_name (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params that
            can be updated for given entity
        file_path (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params that
            can be updated for given entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOServiceOverrideGitUpdateResponse]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        identifier=identifier,
        environment_ref=environment_ref,
        service_ref=service_ref,
        infra_identifier=infra_identifier,
        service_overrides_type=service_overrides_type,
        connector_ref=connector_ref,
        repo_name=repo_name,
        file_path=file_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    identifier: str | Unset = UNSET,
    environment_ref: str | Unset = UNSET,
    service_ref: str | Unset = UNSET,
    infra_identifier: str | Unset = UNSET,
    service_overrides_type: UpdateServiceOverrideGitDetailsServiceOverridesType | Unset = UNSET,
    connector_ref: GitMetadataUpdateRequestInfo | Unset = UNSET,
    repo_name: GitMetadataUpdateRequestInfo | Unset = UNSET,
    file_path: GitMetadataUpdateRequestInfo | Unset = UNSET,
) -> Error | Failure | ResponseDTOServiceOverrideGitUpdateResponse | None:
    """Update git-metadata in remote ServiceOverride Entity

     Update git-metadata in remote ServiceOverride and returns the identifier of updated ServiceOverride

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        identifier (str | Unset):
        environment_ref (str | Unset):
        service_ref (str | Unset):
        infra_identifier (str | Unset):
        service_overrides_type (UpdateServiceOverrideGitDetailsServiceOverridesType | Unset):
        connector_ref (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params
            that can be updated for given entity
        repo_name (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params that
            can be updated for given entity
        file_path (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params that
            can be updated for given entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOServiceOverrideGitUpdateResponse
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        identifier=identifier,
        environment_ref=environment_ref,
        service_ref=service_ref,
        infra_identifier=infra_identifier,
        service_overrides_type=service_overrides_type,
        connector_ref=connector_ref,
        repo_name=repo_name,
        file_path=file_path,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    identifier: str | Unset = UNSET,
    environment_ref: str | Unset = UNSET,
    service_ref: str | Unset = UNSET,
    infra_identifier: str | Unset = UNSET,
    service_overrides_type: UpdateServiceOverrideGitDetailsServiceOverridesType | Unset = UNSET,
    connector_ref: GitMetadataUpdateRequestInfo | Unset = UNSET,
    repo_name: GitMetadataUpdateRequestInfo | Unset = UNSET,
    file_path: GitMetadataUpdateRequestInfo | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOServiceOverrideGitUpdateResponse]:
    """Update git-metadata in remote ServiceOverride Entity

     Update git-metadata in remote ServiceOverride and returns the identifier of updated ServiceOverride

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        identifier (str | Unset):
        environment_ref (str | Unset):
        service_ref (str | Unset):
        infra_identifier (str | Unset):
        service_overrides_type (UpdateServiceOverrideGitDetailsServiceOverridesType | Unset):
        connector_ref (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params
            that can be updated for given entity
        repo_name (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params that
            can be updated for given entity
        file_path (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params that
            can be updated for given entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOServiceOverrideGitUpdateResponse]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        identifier=identifier,
        environment_ref=environment_ref,
        service_ref=service_ref,
        infra_identifier=infra_identifier,
        service_overrides_type=service_overrides_type,
        connector_ref=connector_ref,
        repo_name=repo_name,
        file_path=file_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    identifier: str | Unset = UNSET,
    environment_ref: str | Unset = UNSET,
    service_ref: str | Unset = UNSET,
    infra_identifier: str | Unset = UNSET,
    service_overrides_type: UpdateServiceOverrideGitDetailsServiceOverridesType | Unset = UNSET,
    connector_ref: GitMetadataUpdateRequestInfo | Unset = UNSET,
    repo_name: GitMetadataUpdateRequestInfo | Unset = UNSET,
    file_path: GitMetadataUpdateRequestInfo | Unset = UNSET,
) -> Error | Failure | ResponseDTOServiceOverrideGitUpdateResponse | None:
    """Update git-metadata in remote ServiceOverride Entity

     Update git-metadata in remote ServiceOverride and returns the identifier of updated ServiceOverride

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        identifier (str | Unset):
        environment_ref (str | Unset):
        service_ref (str | Unset):
        infra_identifier (str | Unset):
        service_overrides_type (UpdateServiceOverrideGitDetailsServiceOverridesType | Unset):
        connector_ref (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params
            that can be updated for given entity
        repo_name (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params that
            can be updated for given entity
        file_path (GitMetadataUpdateRequestInfo | Unset): This lists down GIT metadata params that
            can be updated for given entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOServiceOverrideGitUpdateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            identifier=identifier,
            environment_ref=environment_ref,
            service_ref=service_ref,
            infra_identifier=infra_identifier,
            service_overrides_type=service_overrides_type,
            connector_ref=connector_ref,
            repo_name=repo_name,
            file_path=file_path,
        )
    ).parsed
