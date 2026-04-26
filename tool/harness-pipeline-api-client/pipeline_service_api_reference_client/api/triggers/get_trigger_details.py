from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dtong_trigger_details_response_dto import ResponseDTONGTriggerDetailsResponseDTO
from ...types import UNSET, Response


def _get_kwargs(
    trigger_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["targetIdentifier"] = target_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/triggers/{trigger_identifier}/details".format(
            trigger_identifier=quote(str(trigger_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTONGTriggerDetailsResponseDTO:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTONGTriggerDetailsResponseDTO.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTONGTriggerDetailsResponseDTO]:
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
) -> Response[Error | Failure | ResponseDTONGTriggerDetailsResponseDTO]:
    """Fetches Trigger details for a specific accountIdentifier, orgIdentifier, projectIdentifier,
    targetIdentifier, triggerIdentifier.

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTONGTriggerDetailsResponseDTO]
    """

    kwargs = _get_kwargs(
        trigger_identifier=trigger_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
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
) -> Error | Failure | ResponseDTONGTriggerDetailsResponseDTO | None:
    """Fetches Trigger details for a specific accountIdentifier, orgIdentifier, projectIdentifier,
    targetIdentifier, triggerIdentifier.

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTONGTriggerDetailsResponseDTO
    """

    return sync_detailed(
        trigger_identifier=trigger_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
    ).parsed


async def asyncio_detailed(
    trigger_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
) -> Response[Error | Failure | ResponseDTONGTriggerDetailsResponseDTO]:
    """Fetches Trigger details for a specific accountIdentifier, orgIdentifier, projectIdentifier,
    targetIdentifier, triggerIdentifier.

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTONGTriggerDetailsResponseDTO]
    """

    kwargs = _get_kwargs(
        trigger_identifier=trigger_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
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
) -> Error | Failure | ResponseDTONGTriggerDetailsResponseDTO | None:
    """Fetches Trigger details for a specific accountIdentifier, orgIdentifier, projectIdentifier,
    targetIdentifier, triggerIdentifier.

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTONGTriggerDetailsResponseDTO
    """

    return (
        await asyncio_detailed(
            trigger_identifier=trigger_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            target_identifier=target_identifier,
        )
    ).parsed
