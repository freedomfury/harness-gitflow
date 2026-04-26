from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_environment_access_list_type import (
    GetEnvironmentAccessListType,
)
from ...models.response_dto_list_environment_response import ResponseDTOListEnvironmentResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    env_identifiers: list[str] | Unset = UNSET,
    env_group_identifier: str | Unset = UNSET,
    type_: GetEnvironmentAccessListType | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["searchTerm"] = search_term

    json_env_identifiers: list[str] | Unset = UNSET
    if not isinstance(env_identifiers, Unset):
        json_env_identifiers = env_identifiers

    params["envIdentifiers"] = json_env_identifiers

    params["envGroupIdentifier"] = env_group_identifier

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/environmentsV2/list/access",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOListEnvironmentResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOListEnvironmentResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOListEnvironmentResponse]:
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
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    env_identifiers: list[str] | Unset = UNSET,
    env_group_identifier: str | Unset = UNSET,
    type_: GetEnvironmentAccessListType | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOListEnvironmentResponse]:
    """Gets Environment Access list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        env_identifiers (list[str] | Unset):
        env_group_identifier (str | Unset):
        type_ (GetEnvironmentAccessListType | Unset):
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOListEnvironmentResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        env_identifiers=env_identifiers,
        env_group_identifier=env_group_identifier,
        type_=type_,
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
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    env_identifiers: list[str] | Unset = UNSET,
    env_group_identifier: str | Unset = UNSET,
    type_: GetEnvironmentAccessListType | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
) -> Error | Failure | ResponseDTOListEnvironmentResponse | None:
    """Gets Environment Access list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        env_identifiers (list[str] | Unset):
        env_group_identifier (str | Unset):
        type_ (GetEnvironmentAccessListType | Unset):
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOListEnvironmentResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        env_identifiers=env_identifiers,
        env_group_identifier=env_group_identifier,
        type_=type_,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    env_identifiers: list[str] | Unset = UNSET,
    env_group_identifier: str | Unset = UNSET,
    type_: GetEnvironmentAccessListType | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOListEnvironmentResponse]:
    """Gets Environment Access list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        env_identifiers (list[str] | Unset):
        env_group_identifier (str | Unset):
        type_ (GetEnvironmentAccessListType | Unset):
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOListEnvironmentResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        env_identifiers=env_identifiers,
        env_group_identifier=env_group_identifier,
        type_=type_,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    env_identifiers: list[str] | Unset = UNSET,
    env_group_identifier: str | Unset = UNSET,
    type_: GetEnvironmentAccessListType | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
) -> Error | Failure | ResponseDTOListEnvironmentResponse | None:
    """Gets Environment Access list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        env_identifiers (list[str] | Unset):
        env_group_identifier (str | Unset):
        type_ (GetEnvironmentAccessListType | Unset):
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOListEnvironmentResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            search_term=search_term,
            env_identifiers=env_identifiers,
            env_group_identifier=env_group_identifier,
            type_=type_,
            sort=sort,
        )
    ).parsed
