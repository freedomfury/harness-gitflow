from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_aggregated_api_key_api_key_type import (
    GetAggregatedApiKeyApiKeyType,
)
from ...models.response_dto_api_key_aggregate import ResponseDTOApiKeyAggregate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    api_key_type: GetAggregatedApiKeyApiKeyType,
    parent_identifier: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    json_api_key_type: str = api_key_type
    params["apiKeyType"] = json_api_key_type

    params["parentIdentifier"] = parent_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apikey/aggregate/{identifier}".format(
            identifier=quote(str(identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOApiKeyAggregate:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOApiKeyAggregate.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOApiKeyAggregate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    api_key_type: GetAggregatedApiKeyApiKeyType,
    parent_identifier: str,
) -> Response[Error | Failure | ResponseDTOApiKeyAggregate]:
    """Fetches the API Keys details corresponding to the provided ID and Scope.

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        api_key_type (GetAggregatedApiKeyApiKeyType):
        parent_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOApiKeyAggregate]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        api_key_type=api_key_type,
        parent_identifier=parent_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    api_key_type: GetAggregatedApiKeyApiKeyType,
    parent_identifier: str,
) -> Error | Failure | ResponseDTOApiKeyAggregate | None:
    """Fetches the API Keys details corresponding to the provided ID and Scope.

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        api_key_type (GetAggregatedApiKeyApiKeyType):
        parent_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOApiKeyAggregate
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        api_key_type=api_key_type,
        parent_identifier=parent_identifier,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    api_key_type: GetAggregatedApiKeyApiKeyType,
    parent_identifier: str,
) -> Response[Error | Failure | ResponseDTOApiKeyAggregate]:
    """Fetches the API Keys details corresponding to the provided ID and Scope.

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        api_key_type (GetAggregatedApiKeyApiKeyType):
        parent_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOApiKeyAggregate]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        api_key_type=api_key_type,
        parent_identifier=parent_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    api_key_type: GetAggregatedApiKeyApiKeyType,
    parent_identifier: str,
) -> Error | Failure | ResponseDTOApiKeyAggregate | None:
    """Fetches the API Keys details corresponding to the provided ID and Scope.

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        api_key_type (GetAggregatedApiKeyApiKeyType):
        parent_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOApiKeyAggregate
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            api_key_type=api_key_type,
            parent_identifier=parent_identifier,
        )
    ).parsed
