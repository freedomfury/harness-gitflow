from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_filter_list_type import GetFilterListType
from ...models.response_dto_page_response_filter import ResponseDTOPageResponseFilter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    type_: GetFilterListType,
    search_term: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageIndex"] = page_index

    params["pageSize"] = page_size

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    json_type_: str = type_
    params["type"] = json_type_

    params["searchTerm"] = search_term

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/filters",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseFilter:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseFilter.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseFilter]:
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
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    type_: GetFilterListType,
    search_term: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseFilter]:
    """List Filters

     Lists Filters for the given criteria.

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        type_ (GetFilterListType):
        search_term (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseFilter]
    """

    kwargs = _get_kwargs(
        page_index=page_index,
        page_size=page_size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        type_=type_,
        search_term=search_term,
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
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    type_: GetFilterListType,
    search_term: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseFilter | None:
    """List Filters

     Lists Filters for the given criteria.

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        type_ (GetFilterListType):
        search_term (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseFilter
    """

    return sync_detailed(
        client=client,
        page_index=page_index,
        page_size=page_size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        type_=type_,
        search_term=search_term,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    type_: GetFilterListType,
    search_term: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseFilter]:
    """List Filters

     Lists Filters for the given criteria.

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        type_ (GetFilterListType):
        search_term (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseFilter]
    """

    kwargs = _get_kwargs(
        page_index=page_index,
        page_size=page_size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        type_=type_,
        search_term=search_term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    type_: GetFilterListType,
    search_term: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseFilter | None:
    """List Filters

     Lists Filters for the given criteria.

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        type_ (GetFilterListType):
        search_term (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseFilter
    """

    return (
        await asyncio_detailed(
            client=client,
            page_index=page_index,
            page_size=page_size,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            type_=type_,
            search_term=search_term,
        )
    ).parsed
