from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.filter_properties import FilterProperties
from ...models.response_dto_page_pipeline_execution_identifier_summary import (
    ResponseDTOPagePipelineExecutionIdentifierSummary,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: FilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["pipelineIdentifier"] = pipeline_identifier

    params["page"] = page

    params["size"] = size

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["getDefaultFromOtherRepo"] = get_default_from_other_repo

    params["filterIdentifier"] = filter_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pipelines/execution/executionSummary",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPagePipelineExecutionIdentifierSummary:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPagePipelineExecutionIdentifierSummary.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPagePipelineExecutionIdentifierSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPagePipelineExecutionIdentifierSummary]:
    """List Execution Identifier

     Returns a List of Pipeline Executions Identifier with Specific Filter

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        filter_identifier (str | Unset):
        body (FilterProperties | Unset): Properties of the Filter entity defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPagePipelineExecutionIdentifierSummary]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        page=page,
        size=size,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        filter_identifier=filter_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: FilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPagePipelineExecutionIdentifierSummary | None:
    """List Execution Identifier

     Returns a List of Pipeline Executions Identifier with Specific Filter

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        filter_identifier (str | Unset):
        body (FilterProperties | Unset): Properties of the Filter entity defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPagePipelineExecutionIdentifierSummary
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        page=page,
        size=size,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        filter_identifier=filter_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPagePipelineExecutionIdentifierSummary]:
    """List Execution Identifier

     Returns a List of Pipeline Executions Identifier with Specific Filter

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        filter_identifier (str | Unset):
        body (FilterProperties | Unset): Properties of the Filter entity defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPagePipelineExecutionIdentifierSummary]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        page=page,
        size=size,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        filter_identifier=filter_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPagePipelineExecutionIdentifierSummary | None:
    """List Execution Identifier

     Returns a List of Pipeline Executions Identifier with Specific Filter

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        filter_identifier (str | Unset):
        body (FilterProperties | Unset): Properties of the Filter entity defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPagePipelineExecutionIdentifierSummary
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
            page=page,
            size=size,
            branch=branch,
            repo_identifier=repo_identifier,
            get_default_from_other_repo=get_default_from_other_repo,
            filter_identifier=filter_identifier,
        )
    ).parsed
