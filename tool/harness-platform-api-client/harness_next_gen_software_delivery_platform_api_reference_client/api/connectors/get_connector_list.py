from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_connector_list_category import GetConnectorListCategory
from ...models.get_connector_list_source_category import (
    GetConnectorListSourceCategory,
)
from ...models.get_connector_list_type import GetConnectorListType
from ...models.response_dto_page_response_connector_response import ResponseDTOPageResponseConnectorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    type_: GetConnectorListType | Unset = UNSET,
    category: GetConnectorListCategory | Unset = UNSET,
    source_category: GetConnectorListSourceCategory | Unset = UNSET,
    version: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageIndex"] = page_index

    params["pageSize"] = page_size

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["searchTerm"] = search_term

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category

    params["category"] = json_category

    json_source_category: str | Unset = UNSET
    if not isinstance(source_category, Unset):
        json_source_category = source_category

    params["source_category"] = json_source_category

    params["version"] = version

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["getDefaultFromOtherRepo"] = get_default_from_other_repo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/connectors",
        "params": params,
    }

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
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    type_: GetConnectorListType | Unset = UNSET,
    category: GetConnectorListCategory | Unset = UNSET,
    source_category: GetConnectorListSourceCategory | Unset = UNSET,
    version: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseConnectorResponse]:
    """List all Connectors using filters

     Lists all the Connectors matching the specified filters.

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        type_ (GetConnectorListType | Unset):
        category (GetConnectorListCategory | Unset):
        source_category (GetConnectorListSourceCategory | Unset):
        version (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseConnectorResponse]
    """

    kwargs = _get_kwargs(
        page_index=page_index,
        page_size=page_size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        type_=type_,
        category=category,
        source_category=source_category,
        version=version,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    type_: GetConnectorListType | Unset = UNSET,
    category: GetConnectorListCategory | Unset = UNSET,
    source_category: GetConnectorListSourceCategory | Unset = UNSET,
    version: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseConnectorResponse | None:
    """List all Connectors using filters

     Lists all the Connectors matching the specified filters.

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        type_ (GetConnectorListType | Unset):
        category (GetConnectorListCategory | Unset):
        source_category (GetConnectorListSourceCategory | Unset):
        version (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseConnectorResponse
    """

    return sync_detailed(
        client=client,
        page_index=page_index,
        page_size=page_size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        type_=type_,
        category=category,
        source_category=source_category,
        version=version,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    type_: GetConnectorListType | Unset = UNSET,
    category: GetConnectorListCategory | Unset = UNSET,
    source_category: GetConnectorListSourceCategory | Unset = UNSET,
    version: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseConnectorResponse]:
    """List all Connectors using filters

     Lists all the Connectors matching the specified filters.

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        type_ (GetConnectorListType | Unset):
        category (GetConnectorListCategory | Unset):
        source_category (GetConnectorListSourceCategory | Unset):
        version (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseConnectorResponse]
    """

    kwargs = _get_kwargs(
        page_index=page_index,
        page_size=page_size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        type_=type_,
        category=category,
        source_category=source_category,
        version=version,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_index: int | Unset = 0,
    page_size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    type_: GetConnectorListType | Unset = UNSET,
    category: GetConnectorListCategory | Unset = UNSET,
    source_category: GetConnectorListSourceCategory | Unset = UNSET,
    version: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseConnectorResponse | None:
    """List all Connectors using filters

     Lists all the Connectors matching the specified filters.

    Args:
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        type_ (GetConnectorListType | Unset):
        category (GetConnectorListCategory | Unset):
        source_category (GetConnectorListSourceCategory | Unset):
        version (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseConnectorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_index=page_index,
            page_size=page_size,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            search_term=search_term,
            type_=type_,
            category=category,
            source_category=source_category,
            version=version,
            branch=branch,
            repo_identifier=repo_identifier,
            get_default_from_other_repo=get_default_from_other_repo,
        )
    ).parsed
