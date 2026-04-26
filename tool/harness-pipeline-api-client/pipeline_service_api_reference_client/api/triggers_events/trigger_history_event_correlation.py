from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_page_ng_trigger_event_history_base_dto import ResponseDTOPageNGTriggerEventHistoryBaseDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_correlation_id: str,
    *,
    account_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["page"] = page

    params["size"] = size

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/triggers/eventHistory/eventCorrelation/{event_correlation_id}".format(
            event_correlation_id=quote(str(event_correlation_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageNGTriggerEventHistoryBaseDTO:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageNGTriggerEventHistoryBaseDTO.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryBaseDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_correlation_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryBaseDTO]:
    """Get Trigger history event correlation

     Get Trigger history event correlation

    Args:
        event_correlation_id (str):
        account_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryBaseDTO]
    """

    kwargs = _get_kwargs(
        event_correlation_id=event_correlation_id,
        account_identifier=account_identifier,
        page=page,
        size=size,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_correlation_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageNGTriggerEventHistoryBaseDTO | None:
    """Get Trigger history event correlation

     Get Trigger history event correlation

    Args:
        event_correlation_id (str):
        account_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageNGTriggerEventHistoryBaseDTO
    """

    return sync_detailed(
        event_correlation_id=event_correlation_id,
        client=client,
        account_identifier=account_identifier,
        page=page,
        size=size,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    event_correlation_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryBaseDTO]:
    """Get Trigger history event correlation

     Get Trigger history event correlation

    Args:
        event_correlation_id (str):
        account_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryBaseDTO]
    """

    kwargs = _get_kwargs(
        event_correlation_id=event_correlation_id,
        account_identifier=account_identifier,
        page=page,
        size=size,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_correlation_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageNGTriggerEventHistoryBaseDTO | None:
    """Get Trigger history event correlation

     Get Trigger history event correlation

    Args:
        event_correlation_id (str):
        account_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageNGTriggerEventHistoryBaseDTO
    """

    return (
        await asyncio_detailed(
            event_correlation_id=event_correlation_id,
            client=client,
            account_identifier=account_identifier,
            page=page,
            size=size,
            sort=sort,
        )
    ).parsed
