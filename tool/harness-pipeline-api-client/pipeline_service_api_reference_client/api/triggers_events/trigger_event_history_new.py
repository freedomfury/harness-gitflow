from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_page_ng_trigger_event_history_dto import ResponseDTOPageNGTriggerEventHistoryDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    trigger_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
    should_send_trigger_payload: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["targetIdentifier"] = target_identifier

    params["searchTerm"] = search_term

    params["page"] = page

    params["size"] = size

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["shouldSendTriggerPayload"] = should_send_trigger_payload

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/triggers/eventHistory/{trigger_identifier}".format(
            trigger_identifier=quote(str(trigger_identifier), safe=""),
        ),
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
    trigger_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
    should_send_trigger_payload: bool | Unset = True,
) -> Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO]:
    """Get event history for a trigger

     Get event history for a trigger

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):
        should_send_trigger_payload (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO]
    """

    kwargs = _get_kwargs(
        trigger_identifier=trigger_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        search_term=search_term,
        page=page,
        size=size,
        sort=sort,
        should_send_trigger_payload=should_send_trigger_payload,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    trigger_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
    should_send_trigger_payload: bool | Unset = True,
) -> Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO | None:
    """Get event history for a trigger

     Get event history for a trigger

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):
        should_send_trigger_payload (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO
    """

    return sync_detailed(
        trigger_identifier=trigger_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        search_term=search_term,
        page=page,
        size=size,
        sort=sort,
        should_send_trigger_payload=should_send_trigger_payload,
    ).parsed


async def asyncio_detailed(
    trigger_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
    should_send_trigger_payload: bool | Unset = True,
) -> Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO]:
    """Get event history for a trigger

     Get event history for a trigger

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):
        should_send_trigger_payload (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO]
    """

    kwargs = _get_kwargs(
        trigger_identifier=trigger_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        search_term=search_term,
        page=page,
        size=size,
        sort=sort,
        should_send_trigger_payload=should_send_trigger_payload,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trigger_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
    sort: list[str] | Unset = UNSET,
    should_send_trigger_payload: bool | Unset = True,
) -> Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO | None:
    """Get event history for a trigger

     Get event history for a trigger

    Args:
        trigger_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (list[str] | Unset):
        should_send_trigger_payload (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageNGTriggerEventHistoryDTO
    """

    return (
        await asyncio_detailed(
            trigger_identifier=trigger_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            target_identifier=target_identifier,
            search_term=search_term,
            page=page,
            size=size,
            sort=sort,
            should_send_trigger_payload=should_send_trigger_payload,
        )
    ).parsed
