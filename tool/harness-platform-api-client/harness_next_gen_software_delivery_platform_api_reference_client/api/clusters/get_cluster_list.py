from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_cluster_list_scope import GetClusterListScope
from ...models.response_dto_page_response_cluster_response import ResponseDTOPageResponseClusterResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    search_term: str | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    scope: GetClusterListScope | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["environmentIdentifier"] = environment_identifier

    params["searchTerm"] = search_term

    json_identifiers: list[str] | Unset = UNSET
    if not isinstance(identifiers, Unset):
        json_identifiers = identifiers

    params["identifiers"] = json_identifiers

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_scope: str | Unset = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope

    params["scope"] = json_scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gitops/clusters",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseClusterResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseClusterResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseClusterResponse]:
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
    environment_identifier: str,
    search_term: str | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    scope: GetClusterListScope | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseClusterResponse]:
    """Gets cluster list

     Gets a list of GitOps clusters linked to an environment

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        search_term (str | Unset):
        identifiers (list[str] | Unset):
        sort (list[str] | Unset):
        scope (GetClusterListScope | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseClusterResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        search_term=search_term,
        identifiers=identifiers,
        sort=sort,
        scope=scope,
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
    environment_identifier: str,
    search_term: str | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    scope: GetClusterListScope | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseClusterResponse | None:
    """Gets cluster list

     Gets a list of GitOps clusters linked to an environment

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        search_term (str | Unset):
        identifiers (list[str] | Unset):
        sort (list[str] | Unset):
        scope (GetClusterListScope | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseClusterResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        search_term=search_term,
        identifiers=identifiers,
        sort=sort,
        scope=scope,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    search_term: str | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    scope: GetClusterListScope | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseClusterResponse]:
    """Gets cluster list

     Gets a list of GitOps clusters linked to an environment

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        search_term (str | Unset):
        identifiers (list[str] | Unset):
        sort (list[str] | Unset):
        scope (GetClusterListScope | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseClusterResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        search_term=search_term,
        identifiers=identifiers,
        sort=sort,
        scope=scope,
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
    environment_identifier: str,
    search_term: str | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    scope: GetClusterListScope | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseClusterResponse | None:
    """Gets cluster list

     Gets a list of GitOps clusters linked to an environment

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        search_term (str | Unset):
        identifiers (list[str] | Unset):
        sort (list[str] | Unset):
        scope (GetClusterListScope | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseClusterResponse
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
            search_term=search_term,
            identifiers=identifiers,
            sort=sort,
            scope=scope,
        )
    ).parsed
