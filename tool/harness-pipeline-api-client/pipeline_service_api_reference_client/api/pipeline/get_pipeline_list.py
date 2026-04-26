from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.pipeline_filter_properties import PipelineFilterProperties
from ...models.response_dto_page_pms_pipeline_summary_response import ResponseDTOPagePMSPipelineSummaryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PipelineFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
    module: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    get_distinct_from_branches: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["page"] = page

    params["size"] = size

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["searchTerm"] = search_term

    params["module"] = module

    params["filterIdentifier"] = filter_identifier

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["getDefaultFromOtherRepo"] = get_default_from_other_repo

    params["getDistinctFromBranches"] = get_distinct_from_branches

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pipelines/list",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPagePMSPipelineSummaryResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPagePMSPipelineSummaryResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPagePMSPipelineSummaryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
    module: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    get_distinct_from_branches: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPagePMSPipelineSummaryResponse]:
    """List Pipelines

     Returns List of Pipelines in the Given Project

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        search_term (str | Unset):
        module (str | Unset):
        filter_identifier (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        get_distinct_from_branches (bool | Unset):
        body (PipelineFilterProperties | Unset): Properties of the Pipelines Filter defined in
            Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPagePMSPipelineSummaryResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        size=size,
        sort=sort,
        search_term=search_term,
        module=module,
        filter_identifier=filter_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        get_distinct_from_branches=get_distinct_from_branches,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
    module: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    get_distinct_from_branches: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOPagePMSPipelineSummaryResponse | None:
    """List Pipelines

     Returns List of Pipelines in the Given Project

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        search_term (str | Unset):
        module (str | Unset):
        filter_identifier (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        get_distinct_from_branches (bool | Unset):
        body (PipelineFilterProperties | Unset): Properties of the Pipelines Filter defined in
            Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPagePMSPipelineSummaryResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        size=size,
        sort=sort,
        search_term=search_term,
        module=module,
        filter_identifier=filter_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        get_distinct_from_branches=get_distinct_from_branches,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
    module: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    get_distinct_from_branches: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPagePMSPipelineSummaryResponse]:
    """List Pipelines

     Returns List of Pipelines in the Given Project

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        search_term (str | Unset):
        module (str | Unset):
        filter_identifier (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        get_distinct_from_branches (bool | Unset):
        body (PipelineFilterProperties | Unset): Properties of the Pipelines Filter defined in
            Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPagePMSPipelineSummaryResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        size=size,
        sort=sort,
        search_term=search_term,
        module=module,
        filter_identifier=filter_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        get_distinct_from_branches=get_distinct_from_branches,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
    module: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    get_distinct_from_branches: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOPagePMSPipelineSummaryResponse | None:
    """List Pipelines

     Returns List of Pipelines in the Given Project

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        search_term (str | Unset):
        module (str | Unset):
        filter_identifier (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        get_distinct_from_branches (bool | Unset):
        body (PipelineFilterProperties | Unset): Properties of the Pipelines Filter defined in
            Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPagePMSPipelineSummaryResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            page=page,
            size=size,
            sort=sort,
            search_term=search_term,
            module=module,
            filter_identifier=filter_identifier,
            branch=branch,
            repo_identifier=repo_identifier,
            get_default_from_other_repo=get_default_from_other_repo,
            get_distinct_from_branches=get_distinct_from_branches,
        )
    ).parsed
