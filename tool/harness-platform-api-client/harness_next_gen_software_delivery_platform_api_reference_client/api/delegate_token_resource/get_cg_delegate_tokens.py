from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delegate_token_details import DelegateTokenDetails
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_cg_delegate_tokens_status import GetCgDelegateTokensStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    status: GetCgDelegateTokensStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/delegate-token-ng",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DelegateTokenDetails | Error | Failure | None:
    if response.status_code == 200:
        response_200 = DelegateTokenDetails.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DelegateTokenDetails | Error | Failure]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    status: GetCgDelegateTokensStatus | Unset = UNSET,
) -> Response[DelegateTokenDetails | Error | Failure]:
    """Retrieves Delegate Tokens by Account, Organization, Project and status.

    Args:
        name (str | Unset):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        status (GetCgDelegateTokensStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DelegateTokenDetails | Error | Failure]
    """

    kwargs = _get_kwargs(
        name=name,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    status: GetCgDelegateTokensStatus | Unset = UNSET,
) -> DelegateTokenDetails | Error | Failure | None:
    """Retrieves Delegate Tokens by Account, Organization, Project and status.

    Args:
        name (str | Unset):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        status (GetCgDelegateTokensStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DelegateTokenDetails | Error | Failure
    """

    return sync_detailed(
        client=client,
        name=name,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    status: GetCgDelegateTokensStatus | Unset = UNSET,
) -> Response[DelegateTokenDetails | Error | Failure]:
    """Retrieves Delegate Tokens by Account, Organization, Project and status.

    Args:
        name (str | Unset):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        status (GetCgDelegateTokensStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DelegateTokenDetails | Error | Failure]
    """

    kwargs = _get_kwargs(
        name=name,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    status: GetCgDelegateTokensStatus | Unset = UNSET,
) -> DelegateTokenDetails | Error | Failure | None:
    """Retrieves Delegate Tokens by Account, Organization, Project and status.

    Args:
        name (str | Unset):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        status (GetCgDelegateTokensStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DelegateTokenDetails | Error | Failure
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            status=status,
        )
    ).parsed
