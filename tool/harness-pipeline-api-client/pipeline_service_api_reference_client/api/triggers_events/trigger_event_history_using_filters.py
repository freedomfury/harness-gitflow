from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_page_ng_trigger_events_api_response import ResponseDTOPageNGTriggerEventsApiResponse
from ...models.trigger_event_history_using_filters_trigger_type import (
    TriggerEventHistoryUsingFiltersTriggerType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    trigger_identifier: str | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    trigger_type: TriggerEventHistoryUsingFiltersTriggerType | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["targetIdentifier"] = target_identifier

    params["triggerIdentifier"] = trigger_identifier

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_trigger_type: str | Unset = UNSET
    if not isinstance(trigger_type, Unset):
        json_trigger_type = trigger_type

    params["triggerType"] = json_trigger_type

    params["page"] = page

    params["size"] = size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/triggers/eventHistory/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageNGTriggerEventsApiResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageNGTriggerEventsApiResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageNGTriggerEventsApiResponse]:
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
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    trigger_identifier: str | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    trigger_type: TriggerEventHistoryUsingFiltersTriggerType | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
) -> Response[Error | Failure | ResponseDTOPageNGTriggerEventsApiResponse]:
    """Get event history for a trigger using filters.

     Get event history for a trigger using filters.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        trigger_identifier (str | Unset):
        status (list[str] | Unset):
        trigger_type (TriggerEventHistoryUsingFiltersTriggerType | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageNGTriggerEventsApiResponse]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        trigger_identifier=trigger_identifier,
        status=status,
        trigger_type=trigger_type,
        page=page,
        size=size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    trigger_identifier: str | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    trigger_type: TriggerEventHistoryUsingFiltersTriggerType | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
) -> Error | Failure | ResponseDTOPageNGTriggerEventsApiResponse | None:
    """Get event history for a trigger using filters.

     Get event history for a trigger using filters.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        trigger_identifier (str | Unset):
        status (list[str] | Unset):
        trigger_type (TriggerEventHistoryUsingFiltersTriggerType | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageNGTriggerEventsApiResponse
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        trigger_identifier=trigger_identifier,
        status=status,
        trigger_type=trigger_type,
        page=page,
        size=size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    trigger_identifier: str | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    trigger_type: TriggerEventHistoryUsingFiltersTriggerType | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
) -> Response[Error | Failure | ResponseDTOPageNGTriggerEventsApiResponse]:
    """Get event history for a trigger using filters.

     Get event history for a trigger using filters.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        trigger_identifier (str | Unset):
        status (list[str] | Unset):
        trigger_type (TriggerEventHistoryUsingFiltersTriggerType | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageNGTriggerEventsApiResponse]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        trigger_identifier=trigger_identifier,
        status=status,
        trigger_type=trigger_type,
        page=page,
        size=size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    trigger_identifier: str | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    trigger_type: TriggerEventHistoryUsingFiltersTriggerType | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 10,
) -> Error | Failure | ResponseDTOPageNGTriggerEventsApiResponse | None:
    """Get event history for a trigger using filters.

     Get event history for a trigger using filters.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        trigger_identifier (str | Unset):
        status (list[str] | Unset):
        trigger_type (TriggerEventHistoryUsingFiltersTriggerType | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageNGTriggerEventsApiResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            target_identifier=target_identifier,
            trigger_identifier=trigger_identifier,
            status=status,
            trigger_type=trigger_type,
            page=page,
            size=size,
        )
    ).parsed
