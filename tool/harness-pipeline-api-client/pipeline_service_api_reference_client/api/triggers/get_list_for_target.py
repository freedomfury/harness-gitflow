from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_page_response_ng_trigger_details_response_dto import (
    ResponseDTOPageResponseNGTriggerDetailsResponseDTO,
)
from ...models.trigger_filter_properties import TriggerFilterProperties
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TriggerFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    filter_: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["targetIdentifier"] = target_identifier

    params["filter"] = filter_

    params["page"] = page

    params["size"] = size

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["searchTerm"] = search_term

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/triggers",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseNGTriggerDetailsResponseDTO:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseNGTriggerDetailsResponseDTO.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseNGTriggerDetailsResponseDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TriggerFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    filter_: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseNGTriggerDetailsResponseDTO]:
    """Gets the paginated list of triggers for accountIdentifier, orgIdentifier, projectIdentifier,
    targetIdentifier.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        filter_ (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        search_term (str | Unset):
        body (TriggerFilterProperties | Unset): This contains details of the Trigger Filter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseNGTriggerDetailsResponseDTO]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        filter_=filter_,
        page=page,
        size=size,
        sort=sort,
        search_term=search_term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: TriggerFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    filter_: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseNGTriggerDetailsResponseDTO | None:
    """Gets the paginated list of triggers for accountIdentifier, orgIdentifier, projectIdentifier,
    targetIdentifier.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        filter_ (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        search_term (str | Unset):
        body (TriggerFilterProperties | Unset): This contains details of the Trigger Filter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseNGTriggerDetailsResponseDTO
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        filter_=filter_,
        page=page,
        size=size,
        sort=sort,
        search_term=search_term,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TriggerFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    filter_: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseNGTriggerDetailsResponseDTO]:
    """Gets the paginated list of triggers for accountIdentifier, orgIdentifier, projectIdentifier,
    targetIdentifier.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        filter_ (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        search_term (str | Unset):
        body (TriggerFilterProperties | Unset): This contains details of the Trigger Filter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseNGTriggerDetailsResponseDTO]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        filter_=filter_,
        page=page,
        size=size,
        sort=sort,
        search_term=search_term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TriggerFilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    filter_: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseNGTriggerDetailsResponseDTO | None:
    """Gets the paginated list of triggers for accountIdentifier, orgIdentifier, projectIdentifier,
    targetIdentifier.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        filter_ (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        search_term (str | Unset):
        body (TriggerFilterProperties | Unset): This contains details of the Trigger Filter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseNGTriggerDetailsResponseDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            target_identifier=target_identifier,
            filter_=filter_,
            page=page,
            size=size,
            sort=sort,
            search_term=search_term,
        )
    ).parsed
