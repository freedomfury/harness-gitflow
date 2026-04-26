from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.list_input_set_input_set_type import ListInputSetInputSetType
from ...models.response_dto_page_response_input_set_summary_response import (
    ResponseDTOPageResponseInputSetSummaryResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    input_set_type: ListInputSetInputSetType | Unset = "ALL",
    search_term: str | Unset = UNSET,
    sort_orders: list[str] | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageIndex"] = page_index

    params["pageSize"] = page_size

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["pipelineIdentifier"] = pipeline_identifier

    json_input_set_type: str | Unset = UNSET
    if not isinstance(input_set_type, Unset):
        json_input_set_type = input_set_type

    params["inputSetType"] = json_input_set_type

    params["searchTerm"] = search_term

    json_sort_orders: list[str] | Unset = UNSET
    if not isinstance(sort_orders, Unset):
        json_sort_orders = sort_orders

    params["sortOrders"] = json_sort_orders

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["getDefaultFromOtherRepo"] = get_default_from_other_repo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/inputSets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseInputSetSummaryResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseInputSetSummaryResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseInputSetSummaryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    input_set_type: ListInputSetInputSetType | Unset = "ALL",
    search_term: str | Unset = UNSET,
    sort_orders: list[str] | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseInputSetSummaryResponse]:
    """List Input Sets

     Lists all Input Sets for a Pipeline

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        input_set_type (ListInputSetInputSetType | Unset):  Default: 'ALL'.
        search_term (str | Unset):
        sort_orders (list[str] | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseInputSetSummaryResponse]
    """

    kwargs = _get_kwargs(
        page_index=page_index,
        page_size=page_size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        input_set_type=input_set_type,
        search_term=search_term,
        sort_orders=sort_orders,
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
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    input_set_type: ListInputSetInputSetType | Unset = "ALL",
    search_term: str | Unset = UNSET,
    sort_orders: list[str] | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseInputSetSummaryResponse | None:
    """List Input Sets

     Lists all Input Sets for a Pipeline

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        input_set_type (ListInputSetInputSetType | Unset):  Default: 'ALL'.
        search_term (str | Unset):
        sort_orders (list[str] | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseInputSetSummaryResponse
    """

    return sync_detailed(
        client=client,
        page_index=page_index,
        page_size=page_size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        input_set_type=input_set_type,
        search_term=search_term,
        sort_orders=sort_orders,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    input_set_type: ListInputSetInputSetType | Unset = "ALL",
    search_term: str | Unset = UNSET,
    sort_orders: list[str] | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseInputSetSummaryResponse]:
    """List Input Sets

     Lists all Input Sets for a Pipeline

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        input_set_type (ListInputSetInputSetType | Unset):  Default: 'ALL'.
        search_term (str | Unset):
        sort_orders (list[str] | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseInputSetSummaryResponse]
    """

    kwargs = _get_kwargs(
        page_index=page_index,
        page_size=page_size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        input_set_type=input_set_type,
        search_term=search_term,
        sort_orders=sort_orders,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    input_set_type: ListInputSetInputSetType | Unset = "ALL",
    search_term: str | Unset = UNSET,
    sort_orders: list[str] | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseInputSetSummaryResponse | None:
    """List Input Sets

     Lists all Input Sets for a Pipeline

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        input_set_type (ListInputSetInputSetType | Unset):  Default: 'ALL'.
        search_term (str | Unset):
        sort_orders (list[str] | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseInputSetSummaryResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_index=page_index,
            page_size=page_size,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
            input_set_type=input_set_type,
            search_term=search_term,
            sort_orders=sort_orders,
            branch=branch,
            repo_identifier=repo_identifier,
            get_default_from_other_repo=get_default_from_other_repo,
        )
    ).parsed
