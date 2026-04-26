from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_list_user_setting_response_dto import ResponseDTOListUserSettingResponseDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    group: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["group"] = group

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user-settings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOListUserSettingResponseDTO:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOListUserSettingResponseDTO.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOListUserSettingResponseDTO]:
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
    group: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOListUserSettingResponseDTO]:
    """Get list of user settings under the specified category

    Args:
        account_identifier (str):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOListUserSettingResponseDTO]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        group=group,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    group: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOListUserSettingResponseDTO | None:
    """Get list of user settings under the specified category

    Args:
        account_identifier (str):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOListUserSettingResponseDTO
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        group=group,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    group: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOListUserSettingResponseDTO]:
    """Get list of user settings under the specified category

    Args:
        account_identifier (str):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOListUserSettingResponseDTO]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        group=group,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    group: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOListUserSettingResponseDTO | None:
    """Get list of user settings under the specified category

    Args:
        account_identifier (str):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOListUserSettingResponseDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            group=group,
        )
    ).parsed
