from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.merge_input_set_request import MergeInputSetRequest
from ...models.response_dto_merge_input_set_response import ResponseDTOMergeInputSetResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MergeInputSetRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    pipeline_branch: str | Unset = UNSET,
    pipeline_repo_id: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_cache: str | Unset = "false",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(load_from_cache, Unset):
        headers["Load-From-Cache"] = load_from_cache

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["pipelineIdentifier"] = pipeline_identifier

    params["pipelineBranch"] = pipeline_branch

    params["pipelineRepoID"] = pipeline_repo_id

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["getDefaultFromOtherRepo"] = get_default_from_other_repo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inputSets/merge",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOMergeInputSetResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOMergeInputSetResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOMergeInputSetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MergeInputSetRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    pipeline_branch: str | Unset = UNSET,
    pipeline_repo_id: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_cache: str | Unset = "false",
) -> Response[Error | Failure | ResponseDTOMergeInputSetResponse]:
    """Merge given Input Sets into a single Runtime Input YAML

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        pipeline_branch (str | Unset):
        pipeline_repo_id (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_cache (str | Unset):  Default: 'false'.
        body (MergeInputSetRequest): Contains list of Input Set references and Stage Ids

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOMergeInputSetResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        pipeline_branch=pipeline_branch,
        pipeline_repo_id=pipeline_repo_id,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        load_from_cache=load_from_cache,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: MergeInputSetRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    pipeline_branch: str | Unset = UNSET,
    pipeline_repo_id: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_cache: str | Unset = "false",
) -> Error | Failure | ResponseDTOMergeInputSetResponse | None:
    """Merge given Input Sets into a single Runtime Input YAML

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        pipeline_branch (str | Unset):
        pipeline_repo_id (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_cache (str | Unset):  Default: 'false'.
        body (MergeInputSetRequest): Contains list of Input Set references and Stage Ids

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOMergeInputSetResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        pipeline_branch=pipeline_branch,
        pipeline_repo_id=pipeline_repo_id,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        load_from_cache=load_from_cache,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MergeInputSetRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    pipeline_branch: str | Unset = UNSET,
    pipeline_repo_id: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_cache: str | Unset = "false",
) -> Response[Error | Failure | ResponseDTOMergeInputSetResponse]:
    """Merge given Input Sets into a single Runtime Input YAML

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        pipeline_branch (str | Unset):
        pipeline_repo_id (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_cache (str | Unset):  Default: 'false'.
        body (MergeInputSetRequest): Contains list of Input Set references and Stage Ids

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOMergeInputSetResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        pipeline_branch=pipeline_branch,
        pipeline_repo_id=pipeline_repo_id,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        load_from_cache=load_from_cache,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MergeInputSetRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    pipeline_branch: str | Unset = UNSET,
    pipeline_repo_id: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_cache: str | Unset = "false",
) -> Error | Failure | ResponseDTOMergeInputSetResponse | None:
    """Merge given Input Sets into a single Runtime Input YAML

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        pipeline_branch (str | Unset):
        pipeline_repo_id (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_cache (str | Unset):  Default: 'false'.
        body (MergeInputSetRequest): Contains list of Input Set references and Stage Ids

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOMergeInputSetResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
            pipeline_branch=pipeline_branch,
            pipeline_repo_id=pipeline_repo_id,
            branch=branch,
            repo_identifier=repo_identifier,
            get_default_from_other_repo=get_default_from_other_repo,
            load_from_cache=load_from_cache,
        )
    ).parsed
