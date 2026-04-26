from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_list_of_executions_status_item import (
    GetListOfExecutionsStatusItem,
)
from ...models.pipeline_execution_filter_properties import PipelineExecutionFilterProperties
from ...models.response_dto_page_pipeline_execution_summary import ResponseDTOPagePipelineExecutionSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PipelineExecutionFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    search_term: str | Unset = UNSET,
    pipeline_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    show_all_executions: bool | Unset = False,
    module: str | Unset = UNSET,
    status: list[GetListOfExecutionsStatusItem] | Unset = UNSET,
    my_deployments: bool | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["searchTerm"] = search_term

    params["pipelineIdentifier"] = pipeline_identifier

    params["page"] = page

    params["size"] = size

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["filterIdentifier"] = filter_identifier

    params["showAllExecutions"] = show_all_executions

    params["module"] = module

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item: str = status_item_data
            json_status.append(status_item)

    params["status"] = json_status

    params["myDeployments"] = my_deployments

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["getDefaultFromOtherRepo"] = get_default_from_other_repo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pipelines/execution/summary",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPagePipelineExecutionSummary:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPagePipelineExecutionSummary.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPagePipelineExecutionSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineExecutionFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    search_term: str | Unset = UNSET,
    pipeline_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    show_all_executions: bool | Unset = False,
    module: str | Unset = UNSET,
    status: list[GetListOfExecutionsStatusItem] | Unset = UNSET,
    my_deployments: bool | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPagePipelineExecutionSummary]:
    """List Executions

     Returns a List of Pipeline Executions with Specific Filter

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        search_term (str | Unset):
        pipeline_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):
        filter_identifier (str | Unset):
        show_all_executions (bool | Unset):  Default: False.
        module (str | Unset):
        status (list[GetListOfExecutionsStatusItem] | Unset):
        my_deployments (bool | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        body (PipelineExecutionFilterProperties | Unset): Filter properties for listing pipeline
            executions. The `filterType` field (inherited) is required and must be set to
            `PipelineExecution`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPagePipelineExecutionSummary]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        pipeline_identifier=pipeline_identifier,
        page=page,
        size=size,
        sort=sort,
        filter_identifier=filter_identifier,
        show_all_executions=show_all_executions,
        module=module,
        status=status,
        my_deployments=my_deployments,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineExecutionFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    search_term: str | Unset = UNSET,
    pipeline_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    show_all_executions: bool | Unset = False,
    module: str | Unset = UNSET,
    status: list[GetListOfExecutionsStatusItem] | Unset = UNSET,
    my_deployments: bool | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOPagePipelineExecutionSummary | None:
    """List Executions

     Returns a List of Pipeline Executions with Specific Filter

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        search_term (str | Unset):
        pipeline_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):
        filter_identifier (str | Unset):
        show_all_executions (bool | Unset):  Default: False.
        module (str | Unset):
        status (list[GetListOfExecutionsStatusItem] | Unset):
        my_deployments (bool | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        body (PipelineExecutionFilterProperties | Unset): Filter properties for listing pipeline
            executions. The `filterType` field (inherited) is required and must be set to
            `PipelineExecution`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPagePipelineExecutionSummary
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        pipeline_identifier=pipeline_identifier,
        page=page,
        size=size,
        sort=sort,
        filter_identifier=filter_identifier,
        show_all_executions=show_all_executions,
        module=module,
        status=status,
        my_deployments=my_deployments,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineExecutionFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    search_term: str | Unset = UNSET,
    pipeline_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    show_all_executions: bool | Unset = False,
    module: str | Unset = UNSET,
    status: list[GetListOfExecutionsStatusItem] | Unset = UNSET,
    my_deployments: bool | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPagePipelineExecutionSummary]:
    """List Executions

     Returns a List of Pipeline Executions with Specific Filter

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        search_term (str | Unset):
        pipeline_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):
        filter_identifier (str | Unset):
        show_all_executions (bool | Unset):  Default: False.
        module (str | Unset):
        status (list[GetListOfExecutionsStatusItem] | Unset):
        my_deployments (bool | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        body (PipelineExecutionFilterProperties | Unset): Filter properties for listing pipeline
            executions. The `filterType` field (inherited) is required and must be set to
            `PipelineExecution`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPagePipelineExecutionSummary]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        pipeline_identifier=pipeline_identifier,
        page=page,
        size=size,
        sort=sort,
        filter_identifier=filter_identifier,
        show_all_executions=show_all_executions,
        module=module,
        status=status,
        my_deployments=my_deployments,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineExecutionFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    search_term: str | Unset = UNSET,
    pipeline_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    show_all_executions: bool | Unset = False,
    module: str | Unset = UNSET,
    status: list[GetListOfExecutionsStatusItem] | Unset = UNSET,
    my_deployments: bool | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOPagePipelineExecutionSummary | None:
    """List Executions

     Returns a List of Pipeline Executions with Specific Filter

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        search_term (str | Unset):
        pipeline_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):
        filter_identifier (str | Unset):
        show_all_executions (bool | Unset):  Default: False.
        module (str | Unset):
        status (list[GetListOfExecutionsStatusItem] | Unset):
        my_deployments (bool | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        body (PipelineExecutionFilterProperties | Unset): Filter properties for listing pipeline
            executions. The `filterType` field (inherited) is required and must be set to
            `PipelineExecution`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPagePipelineExecutionSummary
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            search_term=search_term,
            pipeline_identifier=pipeline_identifier,
            page=page,
            size=size,
            sort=sort,
            filter_identifier=filter_identifier,
            show_all_executions=show_all_executions,
            module=module,
            status=status,
            my_deployments=my_deployments,
            branch=branch,
            repo_identifier=repo_identifier,
            get_default_from_other_repo=get_default_from_other_repo,
        )
    ).parsed
