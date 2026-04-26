from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.handle_stage_interrupt_interrupt_type import (
    HandleStageInterruptInterruptType,
)
from ...models.response_dto_interrupt_response import ResponseDTOInterruptResponse
from ...types import UNSET, Response


def _get_kwargs(
    plan_execution_id: str,
    node_execution_id: str,
    *,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    interrupt_type: HandleStageInterruptInterruptType,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    json_interrupt_type: str = interrupt_type
    params["interruptType"] = json_interrupt_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/pipeline/execute/interrupt/{plan_execution_id}/{node_execution_id}".format(
            plan_execution_id=quote(str(plan_execution_id), safe=""),
            node_execution_id=quote(str(node_execution_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOInterruptResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOInterruptResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOInterruptResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plan_execution_id: str,
    node_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    interrupt_type: HandleStageInterruptInterruptType,
) -> Response[Error | Failure | ResponseDTOInterruptResponse]:
    """Handles the interrupt for a given stage in a pipeline

    Args:
        plan_execution_id (str):
        node_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        interrupt_type (HandleStageInterruptInterruptType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOInterruptResponse]
    """

    kwargs = _get_kwargs(
        plan_execution_id=plan_execution_id,
        node_execution_id=node_execution_id,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        interrupt_type=interrupt_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    plan_execution_id: str,
    node_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    interrupt_type: HandleStageInterruptInterruptType,
) -> Error | Failure | ResponseDTOInterruptResponse | None:
    """Handles the interrupt for a given stage in a pipeline

    Args:
        plan_execution_id (str):
        node_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        interrupt_type (HandleStageInterruptInterruptType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOInterruptResponse
    """

    return sync_detailed(
        plan_execution_id=plan_execution_id,
        node_execution_id=node_execution_id,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        interrupt_type=interrupt_type,
    ).parsed


async def asyncio_detailed(
    plan_execution_id: str,
    node_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    interrupt_type: HandleStageInterruptInterruptType,
) -> Response[Error | Failure | ResponseDTOInterruptResponse]:
    """Handles the interrupt for a given stage in a pipeline

    Args:
        plan_execution_id (str):
        node_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        interrupt_type (HandleStageInterruptInterruptType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOInterruptResponse]
    """

    kwargs = _get_kwargs(
        plan_execution_id=plan_execution_id,
        node_execution_id=node_execution_id,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        interrupt_type=interrupt_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plan_execution_id: str,
    node_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    interrupt_type: HandleStageInterruptInterruptType,
) -> Error | Failure | ResponseDTOInterruptResponse | None:
    """Handles the interrupt for a given stage in a pipeline

    Args:
        plan_execution_id (str):
        node_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        interrupt_type (HandleStageInterruptInterruptType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOInterruptResponse
    """

    return (
        await asyncio_detailed(
            plan_execution_id=plan_execution_id,
            node_execution_id=node_execution_id,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            interrupt_type=interrupt_type,
        )
    ).parsed
