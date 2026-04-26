from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.connector_filter_properties import ConnectorFilterProperties
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_page_response_connector_response import ResponseDTOPageResponseConnectorResponse
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ConnectorFilterProperties,
    account_identifier: str,
    search_term: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    include_all_connectors_available_at_scope: bool | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    get_distinct_from_branches: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    only_favorites: bool | Unset = False,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["searchTerm"] = search_term

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["filterIdentifier"] = filter_identifier

    params["includeAllConnectorsAvailableAtScope"] = include_all_connectors_available_at_scope

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["getDefaultFromOtherRepo"] = get_default_from_other_repo

    params["getDistinctFromBranches"] = get_distinct_from_branches

    params["version"] = version

    params["onlyFavorites"] = only_favorites

    params["pageIndex"] = page_index

    params["pageSize"] = page_size

    json_sort_orders: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(sort_orders, Unset):
        json_sort_orders = []
        for sort_orders_item_data in sort_orders:
            sort_orders_item = sort_orders_item_data.to_dict()
            json_sort_orders.append(sort_orders_item)

    params["sortOrders"] = json_sort_orders

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/connectors/listV2",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseConnectorResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseConnectorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseConnectorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConnectorFilterProperties,
    account_identifier: str,
    search_term: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    include_all_connectors_available_at_scope: bool | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    get_distinct_from_branches: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    only_favorites: bool | Unset = False,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseConnectorResponse]:
    """Fetches the list of Connectors corresponding to the request's filter criteria.

    Args:
        account_identifier (str):
        search_term (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        filter_identifier (str | Unset):
        include_all_connectors_available_at_scope (bool | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        get_distinct_from_branches (bool | Unset):
        version (str | Unset):
        only_favorites (bool | Unset):  Default: False.
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        body (ConnectorFilterProperties): Properties of the Connector Filter defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseConnectorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        search_term=search_term,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        filter_identifier=filter_identifier,
        include_all_connectors_available_at_scope=include_all_connectors_available_at_scope,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        get_distinct_from_branches=get_distinct_from_branches,
        version=version,
        only_favorites=only_favorites,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ConnectorFilterProperties,
    account_identifier: str,
    search_term: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    include_all_connectors_available_at_scope: bool | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    get_distinct_from_branches: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    only_favorites: bool | Unset = False,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseConnectorResponse | None:
    """Fetches the list of Connectors corresponding to the request's filter criteria.

    Args:
        account_identifier (str):
        search_term (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        filter_identifier (str | Unset):
        include_all_connectors_available_at_scope (bool | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        get_distinct_from_branches (bool | Unset):
        version (str | Unset):
        only_favorites (bool | Unset):  Default: False.
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        body (ConnectorFilterProperties): Properties of the Connector Filter defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseConnectorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        search_term=search_term,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        filter_identifier=filter_identifier,
        include_all_connectors_available_at_scope=include_all_connectors_available_at_scope,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        get_distinct_from_branches=get_distinct_from_branches,
        version=version,
        only_favorites=only_favorites,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConnectorFilterProperties,
    account_identifier: str,
    search_term: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    include_all_connectors_available_at_scope: bool | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    get_distinct_from_branches: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    only_favorites: bool | Unset = False,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseConnectorResponse]:
    """Fetches the list of Connectors corresponding to the request's filter criteria.

    Args:
        account_identifier (str):
        search_term (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        filter_identifier (str | Unset):
        include_all_connectors_available_at_scope (bool | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        get_distinct_from_branches (bool | Unset):
        version (str | Unset):
        only_favorites (bool | Unset):  Default: False.
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        body (ConnectorFilterProperties): Properties of the Connector Filter defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseConnectorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        search_term=search_term,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        filter_identifier=filter_identifier,
        include_all_connectors_available_at_scope=include_all_connectors_available_at_scope,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        get_distinct_from_branches=get_distinct_from_branches,
        version=version,
        only_favorites=only_favorites,
        page_index=page_index,
        page_size=page_size,
        sort_orders=sort_orders,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ConnectorFilterProperties,
    account_identifier: str,
    search_term: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    include_all_connectors_available_at_scope: bool | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    get_distinct_from_branches: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    only_favorites: bool | Unset = False,
    page_index: int | Unset = 0,
    page_size: int | Unset = 50,
    sort_orders: list[SortOrder] | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseConnectorResponse | None:
    """Fetches the list of Connectors corresponding to the request's filter criteria.

    Args:
        account_identifier (str):
        search_term (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        filter_identifier (str | Unset):
        include_all_connectors_available_at_scope (bool | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        get_distinct_from_branches (bool | Unset):
        version (str | Unset):
        only_favorites (bool | Unset):  Default: False.
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.
        sort_orders (list[SortOrder] | Unset):
        page_token (str | Unset):
        body (ConnectorFilterProperties): Properties of the Connector Filter defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseConnectorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            search_term=search_term,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            filter_identifier=filter_identifier,
            include_all_connectors_available_at_scope=include_all_connectors_available_at_scope,
            branch=branch,
            repo_identifier=repo_identifier,
            get_default_from_other_repo=get_default_from_other_repo,
            get_distinct_from_branches=get_distinct_from_branches,
            version=version,
            only_favorites=only_favorites,
            page_index=page_index,
            page_size=page_size,
            sort_orders=sort_orders,
            page_token=page_token,
        )
    ).parsed
