from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_boolean import ResponseDTOBoolean
from ...types import UNSET, Response, Unset


def _get_kwargs(
    trigger_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["targetIdentifier"] = target_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/triggers/{trigger_identifier}".format(
            trigger_identifier=quote(str(trigger_identifier), safe=""),
        ),
        "params": params,
    }

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
    trigger_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOBoolean]:
    """Deletes Trigger by identifier.

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBoolean]
    """

    kwargs = _get_kwargs(
        trigger_identifier=trigger_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    trigger_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOBoolean | None:
    """Deletes Trigger by identifier.

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBoolean
    """

    return sync_detailed(
        trigger_identifier=trigger_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    trigger_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOBoolean]:
    """Deletes Trigger by identifier.

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBoolean]
    """

    kwargs = _get_kwargs(
        trigger_identifier=trigger_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trigger_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOBoolean | None:
    """Deletes Trigger by identifier.

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBoolean
    """

    return (
        await asyncio_detailed(
            trigger_identifier=trigger_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            target_identifier=target_identifier,
            if_match=if_match,
        )
    ).parsed
