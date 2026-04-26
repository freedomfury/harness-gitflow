from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_page_ng_trigger_event_history_dto import ResponseDTOPageNGTriggerEventHistoryDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    target_identifier: str | Unset = UNSET,
    artifact_type: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["targetIdentifier"] = target_identifier

    params["artifactType"] = artifact_type

    params["searchTerm"] = search_term

    params["page"] = page

    params["size"] = size

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/triggers/eventHistory/artifact-manifest-info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageNGTriggerEventHistoryDTO.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    target_identifier: str | Unset = UNSET,
    artifact_type: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO]:
    """Get artifact and manifest trigger event history based on build source type

     Get artifact and manifest trigger event history based on build source type

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        target_identifier (str | Unset):
        artifact_type (str | Unset):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        artifact_type=artifact_type,
        search_term=search_term,
        page=page,
        size=size,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    target_identifier: str | Unset = UNSET,
    artifact_type: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO | None:
    """Get artifact and manifest trigger event history based on build source type

     Get artifact and manifest trigger event history based on build source type

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        target_identifier (str | Unset):
        artifact_type (str | Unset):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        artifact_type=artifact_type,
        search_term=search_term,
        page=page,
        size=size,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    target_identifier: str | Unset = UNSET,
    artifact_type: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO]:
    """Get artifact and manifest trigger event history based on build source type

     Get artifact and manifest trigger event history based on build source type

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        target_identifier (str | Unset):
        artifact_type (str | Unset):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        artifact_type=artifact_type,
        search_term=search_term,
        page=page,
        size=size,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    target_identifier: str | Unset = UNSET,
    artifact_type: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO | None:
    """Get artifact and manifest trigger event history based on build source type

     Get artifact and manifest trigger event history based on build source type

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        target_identifier (str | Unset):
        artifact_type (str | Unset):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            target_identifier=target_identifier,
            artifact_type=artifact_type,
            search_term=search_term,
            page=page,
            size=size,
            sort=sort,
        )
    ).parsed
