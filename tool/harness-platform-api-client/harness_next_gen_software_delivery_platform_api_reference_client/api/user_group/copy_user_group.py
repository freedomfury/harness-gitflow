from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_boolean import ResponseDTOBoolean
from ...models.scope import Scope
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: list[Scope],
    account_identifier: str,
    group_identifier: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["groupIdentifier"] = group_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/user-groups/copy",
        "params": params,
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOBoolean:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOBoolean.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOBoolean]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[Scope],
    account_identifier: str,
    group_identifier: str,
) -> Response[Error | Failure | ResponseDTOBoolean]:
    """Copy User Group

     Copy a User Group in an account/org/project

    Args:
        account_identifier (str):
        group_identifier (str):
        body (list[Scope]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBoolean]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        group_identifier=group_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: list[Scope],
    account_identifier: str,
    group_identifier: str,
) -> Error | Failure | ResponseDTOBoolean | None:
    """Copy User Group

     Copy a User Group in an account/org/project

    Args:
        account_identifier (str):
        group_identifier (str):
        body (list[Scope]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBoolean
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        group_identifier=group_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[Scope],
    account_identifier: str,
    group_identifier: str,
) -> Response[Error | Failure | ResponseDTOBoolean]:
    """Copy User Group

     Copy a User Group in an account/org/project

    Args:
        account_identifier (str):
        group_identifier (str):
        body (list[Scope]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBoolean]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        group_identifier=group_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[Scope],
    account_identifier: str,
    group_identifier: str,
) -> Error | Failure | ResponseDTOBoolean | None:
    """Copy User Group

     Copy a User Group in an account/org/project

    Args:
        account_identifier (str):
        group_identifier (str):
        body (list[Scope]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBoolean
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            group_identifier=group_identifier,
        )
    ).parsed
