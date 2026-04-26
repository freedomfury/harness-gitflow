from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.manual_execution_request import ManualExecutionRequest
from ...models.response_dto_manual_execution_response import ResponseDTOManualExecutionResponse
from ...types import UNSET, Response


def _get_kwargs(
    node_execution_id: str,
    *,
    body: ManualExecutionRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pipeline/execute/manual-execution/{node_execution_id}".format(
            node_execution_id=quote(str(node_execution_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOManualExecutionResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOManualExecutionResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOManualExecutionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ManualExecutionRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
) -> Response[Error | Failure | ResponseDTOManualExecutionResponse]:
    """Marks the Manual Execution as fail or resume

    Args:
        node_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        body (ManualExecutionRequest): Request for marking manual execution as fail or resume

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOManualExecutionResponse]
    """

    kwargs = _get_kwargs(
        node_execution_id=node_execution_id,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ManualExecutionRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
) -> Error | Failure | ResponseDTOManualExecutionResponse | None:
    """Marks the Manual Execution as fail or resume

    Args:
        node_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        body (ManualExecutionRequest): Request for marking manual execution as fail or resume

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOManualExecutionResponse
    """

    return sync_detailed(
        node_execution_id=node_execution_id,
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    node_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ManualExecutionRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
) -> Response[Error | Failure | ResponseDTOManualExecutionResponse]:
    """Marks the Manual Execution as fail or resume

    Args:
        node_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        body (ManualExecutionRequest): Request for marking manual execution as fail or resume

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOManualExecutionResponse]
    """

    kwargs = _get_kwargs(
        node_execution_id=node_execution_id,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ManualExecutionRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
) -> Error | Failure | ResponseDTOManualExecutionResponse | None:
    """Marks the Manual Execution as fail or resume

    Args:
        node_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        body (ManualExecutionRequest): Request for marking manual execution as fail or resume

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOManualExecutionResponse
    """

    return (
        await asyncio_detailed(
            node_execution_id=node_execution_id,
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
        )
    ).parsed
