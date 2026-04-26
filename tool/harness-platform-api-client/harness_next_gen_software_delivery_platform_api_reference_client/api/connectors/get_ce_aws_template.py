from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_string import ResponseDTOString
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    events_enabled: bool | Unset = UNSET,
    cur_enabled: bool | Unset = UNSET,
    optimization_enabled: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["eventsEnabled"] = events_enabled

    params["curEnabled"] = cur_enabled

    params["optimizationEnabled"] = optimization_enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/connectors/getceawstemplateurl",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOString:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOString.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOString]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    events_enabled: bool | Unset = UNSET,
    cur_enabled: bool | Unset = UNSET,
    optimization_enabled: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOString]:
    """Get the Template URL of connector

    Args:
        events_enabled (bool | Unset):
        cur_enabled (bool | Unset):
        optimization_enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOString]
    """

    kwargs = _get_kwargs(
        events_enabled=events_enabled,
        cur_enabled=cur_enabled,
        optimization_enabled=optimization_enabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    events_enabled: bool | Unset = UNSET,
    cur_enabled: bool | Unset = UNSET,
    optimization_enabled: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOString | None:
    """Get the Template URL of connector

    Args:
        events_enabled (bool | Unset):
        cur_enabled (bool | Unset):
        optimization_enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOString
    """

    return sync_detailed(
        client=client,
        events_enabled=events_enabled,
        cur_enabled=cur_enabled,
        optimization_enabled=optimization_enabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    events_enabled: bool | Unset = UNSET,
    cur_enabled: bool | Unset = UNSET,
    optimization_enabled: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOString]:
    """Get the Template URL of connector

    Args:
        events_enabled (bool | Unset):
        cur_enabled (bool | Unset):
        optimization_enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOString]
    """

    kwargs = _get_kwargs(
        events_enabled=events_enabled,
        cur_enabled=cur_enabled,
        optimization_enabled=optimization_enabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    events_enabled: bool | Unset = UNSET,
    cur_enabled: bool | Unset = UNSET,
    optimization_enabled: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOString | None:
    """Get the Template URL of connector

    Args:
        events_enabled (bool | Unset):
        cur_enabled (bool | Unset):
        optimization_enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOString
    """

    return (
        await asyncio_detailed(
            client=client,
            events_enabled=events_enabled,
            cur_enabled=cur_enabled,
            optimization_enabled=optimization_enabled,
        )
    ).parsed
