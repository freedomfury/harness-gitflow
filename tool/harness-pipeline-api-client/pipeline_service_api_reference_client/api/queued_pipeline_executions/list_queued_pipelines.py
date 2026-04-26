from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.queued_pipeline_filter import QueuedPipelineFilter
from ...models.response_dto_queued_pipeline_list_response import ResponseDTOQueuedPipelineListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: QueuedPipelineFilter | Unset = UNSET,
    account_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 20,
    search_term: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["page"] = page

    params["size"] = size

    params["searchTerm"] = search_term

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pipelines/queue-management/queued-pipelines",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOQueuedPipelineListResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOQueuedPipelineListResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOQueuedPipelineListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QueuedPipelineFilter | Unset = UNSET,
    account_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 20,
    search_term: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOQueuedPipelineListResponse]:
    """List Queued Pipelines

     Lists all queued pipeline executions at account level with global queue positions

    Args:
        account_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 20.
        search_term (str | Unset):
        body (QueuedPipelineFilter | Unset): Filter criteria for listing queued pipeline
            executions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOQueuedPipelineListResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        page=page,
        size=size,
        search_term=search_term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QueuedPipelineFilter | Unset = UNSET,
    account_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 20,
    search_term: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOQueuedPipelineListResponse | None:
    """List Queued Pipelines

     Lists all queued pipeline executions at account level with global queue positions

    Args:
        account_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 20.
        search_term (str | Unset):
        body (QueuedPipelineFilter | Unset): Filter criteria for listing queued pipeline
            executions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOQueuedPipelineListResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        page=page,
        size=size,
        search_term=search_term,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QueuedPipelineFilter | Unset = UNSET,
    account_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 20,
    search_term: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOQueuedPipelineListResponse]:
    """List Queued Pipelines

     Lists all queued pipeline executions at account level with global queue positions

    Args:
        account_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 20.
        search_term (str | Unset):
        body (QueuedPipelineFilter | Unset): Filter criteria for listing queued pipeline
            executions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOQueuedPipelineListResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        page=page,
        size=size,
        search_term=search_term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QueuedPipelineFilter | Unset = UNSET,
    account_identifier: str,
    page: int | Unset = 0,
    size: int | Unset = 20,
    search_term: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOQueuedPipelineListResponse | None:
    """List Queued Pipelines

     Lists all queued pipeline executions at account level with global queue positions

    Args:
        account_identifier (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 20.
        search_term (str | Unset):
        body (QueuedPipelineFilter | Unset): Filter criteria for listing queued pipeline
            executions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOQueuedPipelineListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            page=page,
            size=size,
            search_term=search_term,
        )
    ).parsed
