from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.list_aggregated_service_accounts_filter_type import (
    ListAggregatedServiceAccountsFilterType,
)
from ...models.response_dto_page_response_service_account_aggregate import (
    ResponseDTOPageResponseServiceAccountAggregate,
)
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    filter_type: ListAggregatedServiceAccountsFilterType | Unset = "EXCLUDE_INHERITED_SERVICE_ACCOUNTS",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    json_identifiers: list[str] | Unset = UNSET
    if not isinstance(identifiers, Unset):
        json_identifiers = identifiers

    params["identifiers"] = json_identifiers

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

    params["searchTerm"] = search_term

    json_filter_type: str | Unset = UNSET
    if not isinstance(filter_type, Unset):
        json_filter_type = filter_type

    params["filterType"] = json_filter_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/serviceaccount/aggregate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseServiceAccountAggregate:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseServiceAccountAggregate.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseServiceAccountAggregate]:
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
    identifiers: list[str] | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    filter_type: ListAggregatedServiceAccountsFilterType | Unset = "EXCLUDE_INHERITED_SERVICE_ACCOUNTS",
) -> Response[Error | Failure | ResponseDTOPageResponseServiceAccountAggregate]:
    """List aggregated Service Accounts

     Fetches the list of Aggregated Service Accounts corresponding to the request's filter criteria.

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        identifiers (list[str] | Unset):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        search_term (str | Unset):
        filter_type (ListAggregatedServiceAccountsFilterType | Unset):  Default:
            'EXCLUDE_INHERITED_SERVICE_ACCOUNTS'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseServiceAccountAggregate]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        identifiers=identifiers,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
        search_term=search_term,
        filter_type=filter_type,
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
    identifiers: list[str] | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    filter_type: ListAggregatedServiceAccountsFilterType | Unset = "EXCLUDE_INHERITED_SERVICE_ACCOUNTS",
) -> Error | Failure | ResponseDTOPageResponseServiceAccountAggregate | None:
    """List aggregated Service Accounts

     Fetches the list of Aggregated Service Accounts corresponding to the request's filter criteria.

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        identifiers (list[str] | Unset):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        search_term (str | Unset):
        filter_type (ListAggregatedServiceAccountsFilterType | Unset):  Default:
            'EXCLUDE_INHERITED_SERVICE_ACCOUNTS'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseServiceAccountAggregate
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        identifiers=identifiers,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
        search_term=search_term,
        filter_type=filter_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    filter_type: ListAggregatedServiceAccountsFilterType | Unset = "EXCLUDE_INHERITED_SERVICE_ACCOUNTS",
) -> Response[Error | Failure | ResponseDTOPageResponseServiceAccountAggregate]:
    """List aggregated Service Accounts

     Fetches the list of Aggregated Service Accounts corresponding to the request's filter criteria.

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        identifiers (list[str] | Unset):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        search_term (str | Unset):
        filter_type (ListAggregatedServiceAccountsFilterType | Unset):  Default:
            'EXCLUDE_INHERITED_SERVICE_ACCOUNTS'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseServiceAccountAggregate]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        identifiers=identifiers,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
        search_term=search_term,
        filter_type=filter_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    filter_type: ListAggregatedServiceAccountsFilterType | Unset = "EXCLUDE_INHERITED_SERVICE_ACCOUNTS",
) -> Error | Failure | ResponseDTOPageResponseServiceAccountAggregate | None:
    """List aggregated Service Accounts

     Fetches the list of Aggregated Service Accounts corresponding to the request's filter criteria.

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        identifiers (list[str] | Unset):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        search_term (str | Unset):
        filter_type (ListAggregatedServiceAccountsFilterType | Unset):  Default:
            'EXCLUDE_INHERITED_SERVICE_ACCOUNTS'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseServiceAccountAggregate
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            identifiers=identifiers,
            page_index=page_index,
            page_size=page_size,
            sort_orders=sort_orders,
            page_token=page_token,
            search_term=search_term,
            filter_type=filter_type,
        )
    ).parsed
