from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_list_string import ResponseDTOListString
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    connector_ref: str,
    organization: str,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["connectorRef"] = connector_ref

    params["organization"] = organization

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tas/space",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOListString:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOListString.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOListString]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    connector_ref: str,
    organization: str,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOListString]:
    """Return the Tas spaces

    Args:
        connector_ref (str):
        organization (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOListString]
    """

    kwargs = _get_kwargs(
        connector_ref=connector_ref,
        organization=organization,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    connector_ref: str,
    organization: str,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOListString | None:
    """Return the Tas spaces

    Args:
        connector_ref (str):
        organization (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOListString
    """

    return sync_detailed(
        client=client,
        connector_ref=connector_ref,
        organization=organization,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    connector_ref: str,
    organization: str,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOListString]:
    """Return the Tas spaces

    Args:
        connector_ref (str):
        organization (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOListString]
    """

    kwargs = _get_kwargs(
        connector_ref=connector_ref,
        organization=organization,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    connector_ref: str,
    organization: str,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOListString | None:
    """Return the Tas spaces

    Args:
        connector_ref (str):
        organization (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOListString
    """

    return (
        await asyncio_detailed(
            client=client,
            connector_ref=connector_ref,
            organization=organization,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
        )
    ).parsed
