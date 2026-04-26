from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...types import UNSET, Response, Unset


def _get_kwargs(
    plan_execution_id: str,
    *,
    account_identifier: str,
    node_execution_id: str | Unset = UNSET,
    depth: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["nodeExecutionId"] = node_execution_id

    params["depth"] = depth

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pipelines/execution/{plan_execution_id}/workflow-graph".format(
            plan_execution_id=quote(str(plan_execution_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Failure | None:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Failure]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plan_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    node_execution_id: str | Unset = UNSET,
    depth: int | Unset = 10,
) -> Response[Error | Failure]:
    """Get workflow graph for visualization

     Returns the workflow graph for visualization

    Args:
        plan_execution_id (str):
        account_identifier (str):
        node_execution_id (str | Unset):
        depth (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure]
    """

    kwargs = _get_kwargs(
        plan_execution_id=plan_execution_id,
        account_identifier=account_identifier,
        node_execution_id=node_execution_id,
        depth=depth,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    plan_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    node_execution_id: str | Unset = UNSET,
    depth: int | Unset = 10,
) -> Error | Failure | None:
    """Get workflow graph for visualization

     Returns the workflow graph for visualization

    Args:
        plan_execution_id (str):
        account_identifier (str):
        node_execution_id (str | Unset):
        depth (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure
    """

    return sync_detailed(
        plan_execution_id=plan_execution_id,
        client=client,
        account_identifier=account_identifier,
        node_execution_id=node_execution_id,
        depth=depth,
    ).parsed


async def asyncio_detailed(
    plan_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    node_execution_id: str | Unset = UNSET,
    depth: int | Unset = 10,
) -> Response[Error | Failure]:
    """Get workflow graph for visualization

     Returns the workflow graph for visualization

    Args:
        plan_execution_id (str):
        account_identifier (str):
        node_execution_id (str | Unset):
        depth (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure]
    """

    kwargs = _get_kwargs(
        plan_execution_id=plan_execution_id,
        account_identifier=account_identifier,
        node_execution_id=node_execution_id,
        depth=depth,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plan_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    node_execution_id: str | Unset = UNSET,
    depth: int | Unset = 10,
) -> Error | Failure | None:
    """Get workflow graph for visualization

     Returns the workflow graph for visualization

    Args:
        plan_execution_id (str):
        account_identifier (str):
        node_execution_id (str | Unset):
        depth (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure
    """

    return (
        await asyncio_detailed(
            plan_execution_id=plan_execution_id,
            client=client,
            account_identifier=account_identifier,
            node_execution_id=node_execution_id,
            depth=depth,
        )
    ).parsed
