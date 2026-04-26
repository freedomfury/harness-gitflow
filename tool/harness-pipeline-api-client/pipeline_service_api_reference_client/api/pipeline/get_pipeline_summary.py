from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dtopms_pipeline_summary_response import ResponseDTOPMSPipelineSummaryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pipeline_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_fallback_branch: bool | Unset = False,
    load_from_cache: str | Unset = "false",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(load_from_cache, Unset):
        headers["Load-From-Cache"] = load_from_cache

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["getDefaultFromOtherRepo"] = get_default_from_other_repo

    params["loadFromFallbackBranch"] = load_from_fallback_branch

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pipelines/summary/{pipeline_identifier}".format(
            pipeline_identifier=quote(str(pipeline_identifier), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPMSPipelineSummaryResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPMSPipelineSummaryResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPMSPipelineSummaryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pipeline_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_fallback_branch: bool | Unset = False,
    load_from_cache: str | Unset = "false",
) -> Response[Error | Failure | ResponseDTOPMSPipelineSummaryResponse]:
    """Fetch Pipeline Summary

     Returns Pipeline Summary by Identifier

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_fallback_branch (bool | Unset):  Default: False.
        load_from_cache (str | Unset):  Default: 'false'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPMSPipelineSummaryResponse]
    """

    kwargs = _get_kwargs(
        pipeline_identifier=pipeline_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        load_from_fallback_branch=load_from_fallback_branch,
        load_from_cache=load_from_cache,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pipeline_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_fallback_branch: bool | Unset = False,
    load_from_cache: str | Unset = "false",
) -> Error | Failure | ResponseDTOPMSPipelineSummaryResponse | None:
    """Fetch Pipeline Summary

     Returns Pipeline Summary by Identifier

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_fallback_branch (bool | Unset):  Default: False.
        load_from_cache (str | Unset):  Default: 'false'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPMSPipelineSummaryResponse
    """

    return sync_detailed(
        pipeline_identifier=pipeline_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        load_from_fallback_branch=load_from_fallback_branch,
        load_from_cache=load_from_cache,
    ).parsed


async def asyncio_detailed(
    pipeline_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_fallback_branch: bool | Unset = False,
    load_from_cache: str | Unset = "false",
) -> Response[Error | Failure | ResponseDTOPMSPipelineSummaryResponse]:
    """Fetch Pipeline Summary

     Returns Pipeline Summary by Identifier

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_fallback_branch (bool | Unset):  Default: False.
        load_from_cache (str | Unset):  Default: 'false'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPMSPipelineSummaryResponse]
    """

    kwargs = _get_kwargs(
        pipeline_identifier=pipeline_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        load_from_fallback_branch=load_from_fallback_branch,
        load_from_cache=load_from_cache,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pipeline_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_fallback_branch: bool | Unset = False,
    load_from_cache: str | Unset = "false",
) -> Error | Failure | ResponseDTOPMSPipelineSummaryResponse | None:
    """Fetch Pipeline Summary

     Returns Pipeline Summary by Identifier

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_fallback_branch (bool | Unset):  Default: False.
        load_from_cache (str | Unset):  Default: 'false'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPMSPipelineSummaryResponse
    """

    return (
        await asyncio_detailed(
            pipeline_identifier=pipeline_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            branch=branch,
            repo_identifier=repo_identifier,
            get_default_from_other_repo=get_default_from_other_repo,
            load_from_fallback_branch=load_from_fallback_branch,
            load_from_cache=load_from_cache,
        )
    ).parsed
