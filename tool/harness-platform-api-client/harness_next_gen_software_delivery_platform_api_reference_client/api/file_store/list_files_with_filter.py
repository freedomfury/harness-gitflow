from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.files_filter_properties_dto import FilesFilterPropertiesDTO
from ...models.response_dto_page_file import ResponseDTOPageFile
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: FilesFilterPropertiesDTO | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
    account_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["pageIndex"] = page_index

    params["pageSize"] = page_size

    json_sort_orders: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(sort_orders, Unset):
        json_sort_orders = []
        for sort_orders_item_data in sort_orders:
            sort_orders_item = sort_orders_item_data.to_dict()
            json_sort_orders.append(sort_orders_item)

    params["sortOrders"] = json_sort_orders

    params["pageToken"] = page_token

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["filterIdentifier"] = filter_identifier

    params["searchTerm"] = search_term

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/file-store/files/filter",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageFile:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageFile.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageFile]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FilesFilterPropertiesDTO | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
    account_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageFile]:
    """Get filtered list of Files or Folders

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        account_identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        filter_identifier (str | Unset):
        search_term (str | Unset):
        body (FilesFilterPropertiesDTO | Unset): Properties of the Files Filter defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageFile]
    """

    kwargs = _get_kwargs(
        body=body,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        filter_identifier=filter_identifier,
        search_term=search_term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: FilesFilterPropertiesDTO | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
    account_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageFile | None:
    """Get filtered list of Files or Folders

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        account_identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        filter_identifier (str | Unset):
        search_term (str | Unset):
        body (FilesFilterPropertiesDTO | Unset): Properties of the Files Filter defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageFile
    """

    return sync_detailed(
        client=client,
        body=body,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        filter_identifier=filter_identifier,
        search_term=search_term,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FilesFilterPropertiesDTO | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
    account_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageFile]:
    """Get filtered list of Files or Folders

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        account_identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        filter_identifier (str | Unset):
        search_term (str | Unset):
        body (FilesFilterPropertiesDTO | Unset): Properties of the Files Filter defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageFile]
    """

    kwargs = _get_kwargs(
        body=body,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        filter_identifier=filter_identifier,
        search_term=search_term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FilesFilterPropertiesDTO | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
    account_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageFile | None:
    """Get filtered list of Files or Folders

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        account_identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        filter_identifier (str | Unset):
        search_term (str | Unset):
        body (FilesFilterPropertiesDTO | Unset): Properties of the Files Filter defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageFile
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            page_index=page_index,
            page_size=page_size,
            sort_orders=sort_orders,
            page_token=page_token,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            filter_identifier=filter_identifier,
            search_term=search_term,
        )
    ).parsed
