from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.list_aggregated_keys_schemes_item import (
    ListAggregatedKeysSchemesItem,
)
from ...models.list_aggregated_keys_usages_item import (
    ListAggregatedKeysUsagesItem,
)
from ...models.response_dto_page_response_key import ResponseDTOPageResponseKey
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    parent_identifier: str | Unset = UNSET,
    key_scheme: str | Unset = UNSET,
    fingerprint: str | Unset = UNSET,
    sub_key_id: str | Unset = UNSET,
    usages: list[ListAggregatedKeysUsagesItem] | Unset = UNSET,
    schemes: list[ListAggregatedKeysSchemesItem] | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["parentIdentifier"] = parent_identifier

    params["keyScheme"] = key_scheme

    params["fingerprint"] = fingerprint

    params["subKeyId"] = sub_key_id

    json_usages: list[str] | Unset = UNSET
    if not isinstance(usages, Unset):
        json_usages = []
        for usages_item_data in usages:
            usages_item: str = usages_item_data
            json_usages.append(usages_item)

    params["usages"] = json_usages

    json_schemes: list[str] | Unset = UNSET
    if not isinstance(schemes, Unset):
        json_schemes = []
        for schemes_item_data in schemes:
            schemes_item: str = schemes_item_data
            json_schemes.append(schemes_item)

    params["schemes"] = json_schemes

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/keys",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseKey:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseKey.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseKey]:
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
    parent_identifier: str | Unset = UNSET,
    key_scheme: str | Unset = UNSET,
    fingerprint: str | Unset = UNSET,
    sub_key_id: str | Unset = UNSET,
    usages: list[ListAggregatedKeysUsagesItem] | Unset = UNSET,
    schemes: list[ListAggregatedKeysSchemesItem] | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseKey]:
    """List Keys

     Lists SSH, PGP, or all Keys based on keyScheme parameter. Supports filtering by fingerprint,
    subKeyId, usages, and schemes.

    Args:
        account_identifier (str):
        parent_identifier (str | Unset):
        key_scheme (str | Unset):
        fingerprint (str | Unset):
        sub_key_id (str | Unset):
        usages (list[ListAggregatedKeysUsagesItem] | Unset):
        schemes (list[ListAggregatedKeysSchemesItem] | Unset):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseKey]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        parent_identifier=parent_identifier,
        key_scheme=key_scheme,
        fingerprint=fingerprint,
        sub_key_id=sub_key_id,
        usages=usages,
        schemes=schemes,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    parent_identifier: str | Unset = UNSET,
    key_scheme: str | Unset = UNSET,
    fingerprint: str | Unset = UNSET,
    sub_key_id: str | Unset = UNSET,
    usages: list[ListAggregatedKeysUsagesItem] | Unset = UNSET,
    schemes: list[ListAggregatedKeysSchemesItem] | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseKey | None:
    """List Keys

     Lists SSH, PGP, or all Keys based on keyScheme parameter. Supports filtering by fingerprint,
    subKeyId, usages, and schemes.

    Args:
        account_identifier (str):
        parent_identifier (str | Unset):
        key_scheme (str | Unset):
        fingerprint (str | Unset):
        sub_key_id (str | Unset):
        usages (list[ListAggregatedKeysUsagesItem] | Unset):
        schemes (list[ListAggregatedKeysSchemesItem] | Unset):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseKey
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        parent_identifier=parent_identifier,
        key_scheme=key_scheme,
        fingerprint=fingerprint,
        sub_key_id=sub_key_id,
        usages=usages,
        schemes=schemes,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    parent_identifier: str | Unset = UNSET,
    key_scheme: str | Unset = UNSET,
    fingerprint: str | Unset = UNSET,
    sub_key_id: str | Unset = UNSET,
    usages: list[ListAggregatedKeysUsagesItem] | Unset = UNSET,
    schemes: list[ListAggregatedKeysSchemesItem] | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseKey]:
    """List Keys

     Lists SSH, PGP, or all Keys based on keyScheme parameter. Supports filtering by fingerprint,
    subKeyId, usages, and schemes.

    Args:
        account_identifier (str):
        parent_identifier (str | Unset):
        key_scheme (str | Unset):
        fingerprint (str | Unset):
        sub_key_id (str | Unset):
        usages (list[ListAggregatedKeysUsagesItem] | Unset):
        schemes (list[ListAggregatedKeysSchemesItem] | Unset):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseKey]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        parent_identifier=parent_identifier,
        key_scheme=key_scheme,
        fingerprint=fingerprint,
        sub_key_id=sub_key_id,
        usages=usages,
        schemes=schemes,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    parent_identifier: str | Unset = UNSET,
    key_scheme: str | Unset = UNSET,
    fingerprint: str | Unset = UNSET,
    sub_key_id: str | Unset = UNSET,
    usages: list[ListAggregatedKeysUsagesItem] | Unset = UNSET,
    schemes: list[ListAggregatedKeysSchemesItem] | Unset = UNSET,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseKey | None:
    """List Keys

     Lists SSH, PGP, or all Keys based on keyScheme parameter. Supports filtering by fingerprint,
    subKeyId, usages, and schemes.

    Args:
        account_identifier (str):
        parent_identifier (str | Unset):
        key_scheme (str | Unset):
        fingerprint (str | Unset):
        sub_key_id (str | Unset):
        usages (list[ListAggregatedKeysUsagesItem] | Unset):
        schemes (list[ListAggregatedKeysSchemesItem] | Unset):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseKey
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            parent_identifier=parent_identifier,
            key_scheme=key_scheme,
            fingerprint=fingerprint,
            sub_key_id=sub_key_id,
            usages=usages,
            schemes=schemes,
            page_index=page_index,
            page_size=page_size,
            sort_orders=sort_orders,
            page_token=page_token,
        )
    ).parsed
