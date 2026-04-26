from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.pipeline_execution_outline_filter_dto import PipelineExecutionOutlineFilterDTO
from ...models.response_dto_custom_page_pipeline_execution_outline import ResponseDTOCustomPagePipelineExecutionOutline
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PipelineExecutionOutlineFilterDTO | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    last_seen_execution_id: str | Unset = UNSET,
    last_seen_start_time: int | Unset = UNSET,
    size: int | Unset = 10,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["lastSeenExecutionId"] = last_seen_execution_id

    params["lastSeenStartTime"] = last_seen_start_time

    params["size"] = size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pipelines/execution/summary/outline",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOCustomPagePipelineExecutionOutline:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOCustomPagePipelineExecutionOutline.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOCustomPagePipelineExecutionOutline]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineExecutionOutlineFilterDTO | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    last_seen_execution_id: str | Unset = UNSET,
    last_seen_start_time: int | Unset = UNSET,
    size: int | Unset = 10,
) -> Response[Error | Failure | ResponseDTOCustomPagePipelineExecutionOutline]:
    """List Executions Outline

     Returns a List of Pipeline Executions Outline given pipelineId or a list of executionIds

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        last_seen_execution_id (str | Unset):
        last_seen_start_time (int | Unset):
        size (int | Unset):  Default: 10.
        body (PipelineExecutionOutlineFilterDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOCustomPagePipelineExecutionOutline]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        last_seen_execution_id=last_seen_execution_id,
        last_seen_start_time=last_seen_start_time,
        size=size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineExecutionOutlineFilterDTO | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    last_seen_execution_id: str | Unset = UNSET,
    last_seen_start_time: int | Unset = UNSET,
    size: int | Unset = 10,
) -> Error | Failure | ResponseDTOCustomPagePipelineExecutionOutline | None:
    """List Executions Outline

     Returns a List of Pipeline Executions Outline given pipelineId or a list of executionIds

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        last_seen_execution_id (str | Unset):
        last_seen_start_time (int | Unset):
        size (int | Unset):  Default: 10.
        body (PipelineExecutionOutlineFilterDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOCustomPagePipelineExecutionOutline
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        last_seen_execution_id=last_seen_execution_id,
        last_seen_start_time=last_seen_start_time,
        size=size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineExecutionOutlineFilterDTO | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    last_seen_execution_id: str | Unset = UNSET,
    last_seen_start_time: int | Unset = UNSET,
    size: int | Unset = 10,
) -> Response[Error | Failure | ResponseDTOCustomPagePipelineExecutionOutline]:
    """List Executions Outline

     Returns a List of Pipeline Executions Outline given pipelineId or a list of executionIds

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        last_seen_execution_id (str | Unset):
        last_seen_start_time (int | Unset):
        size (int | Unset):  Default: 10.
        body (PipelineExecutionOutlineFilterDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOCustomPagePipelineExecutionOutline]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        last_seen_execution_id=last_seen_execution_id,
        last_seen_start_time=last_seen_start_time,
        size=size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineExecutionOutlineFilterDTO | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    last_seen_execution_id: str | Unset = UNSET,
    last_seen_start_time: int | Unset = UNSET,
    size: int | Unset = 10,
) -> Error | Failure | ResponseDTOCustomPagePipelineExecutionOutline | None:
    """List Executions Outline

     Returns a List of Pipeline Executions Outline given pipelineId or a list of executionIds

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        last_seen_execution_id (str | Unset):
        last_seen_start_time (int | Unset):
        size (int | Unset):  Default: 10.
        body (PipelineExecutionOutlineFilterDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOCustomPagePipelineExecutionOutline
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            last_seen_execution_id=last_seen_execution_id,
            last_seen_start_time=last_seen_start_time,
            size=size,
        )
    ).parsed
