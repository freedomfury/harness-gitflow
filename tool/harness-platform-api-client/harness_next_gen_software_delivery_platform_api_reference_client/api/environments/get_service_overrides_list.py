from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_page_response_service_override_response import (
    ResponseDTOPageResponseServiceOverrideResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    size: int | Unset = 500,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    service_identifier: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["environmentIdentifier"] = environment_identifier

    params["serviceIdentifier"] = service_identifier

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/environmentsV2/serviceOverrides",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseServiceOverrideResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseServiceOverrideResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseServiceOverrideResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 500,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    service_identifier: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseServiceOverrideResponse]:
    """Gets Service Overrides list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 500.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        service_identifier (str | Unset):
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseServiceOverrideResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        service_identifier=service_identifier,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 500,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    service_identifier: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseServiceOverrideResponse | None:
    """Gets Service Overrides list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 500.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        service_identifier (str | Unset):
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseServiceOverrideResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        service_identifier=service_identifier,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 500,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    service_identifier: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseServiceOverrideResponse]:
    """Gets Service Overrides list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 500.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        service_identifier (str | Unset):
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseServiceOverrideResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        service_identifier=service_identifier,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 500,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    service_identifier: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseServiceOverrideResponse | None:
    """Gets Service Overrides list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 500.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        service_identifier (str | Unset):
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseServiceOverrideResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            environment_identifier=environment_identifier,
            service_identifier=service_identifier,
            sort=sort,
        )
    ).parsed
