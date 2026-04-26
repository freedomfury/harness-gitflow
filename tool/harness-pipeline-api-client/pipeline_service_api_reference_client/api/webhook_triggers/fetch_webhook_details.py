from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_webhook_event_processing_details import ResponseDTOWebhookEventProcessingDetails
from ...types import UNSET, Response


def _get_kwargs(
    *,
    account_identifier: str,
    event_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["eventId"] = event_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhook/triggerProcessingDetails",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOWebhookEventProcessingDetails:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOWebhookEventProcessingDetails.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOWebhookEventProcessingDetails]:
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
    event_id: str,
) -> Response[Error | Failure | ResponseDTOWebhookEventProcessingDetails]:
    """Gets webhook event processing details for input eventId.

    Args:
        account_identifier (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOWebhookEventProcessingDetails]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        event_id=event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    event_id: str,
) -> Error | Failure | ResponseDTOWebhookEventProcessingDetails | None:
    """Gets webhook event processing details for input eventId.

    Args:
        account_identifier (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOWebhookEventProcessingDetails
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        event_id=event_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    event_id: str,
) -> Response[Error | Failure | ResponseDTOWebhookEventProcessingDetails]:
    """Gets webhook event processing details for input eventId.

    Args:
        account_identifier (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOWebhookEventProcessingDetails]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        event_id=event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    event_id: str,
) -> Error | Failure | ResponseDTOWebhookEventProcessingDetails | None:
    """Gets webhook event processing details for input eventId.

    Args:
        account_identifier (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOWebhookEventProcessingDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            event_id=event_id,
        )
    ).parsed
