from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...types import UNSET, Response


def _get_kwargs(
    plan_execution_id: str,
    *,
    account_identifier: str,
    node_execution_id: str,
    file_name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["nodeExecutionId"] = node_execution_id

    params["fileName"] = file_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/input-file/file/{plan_execution_id}".format(
            plan_execution_id=quote(str(plan_execution_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | Failure:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error | Failure]:
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
    node_execution_id: str,
    file_name: str,
) -> Response[Any | Error | Failure]:
    """Returns a file uploaded or filtered based on the fileIdentifier provided for a given nodeExecutionId

     Returns a file uploaded or filtered based on the fileIdentifier provided for a given nodeExecutionId

    Args:
        plan_execution_id (str):
        account_identifier (str):
        node_execution_id (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Failure]
    """

    kwargs = _get_kwargs(
        plan_execution_id=plan_execution_id,
        account_identifier=account_identifier,
        node_execution_id=node_execution_id,
        file_name=file_name,
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
    node_execution_id: str,
    file_name: str,
) -> Any | Error | Failure | None:
    """Returns a file uploaded or filtered based on the fileIdentifier provided for a given nodeExecutionId

     Returns a file uploaded or filtered based on the fileIdentifier provided for a given nodeExecutionId

    Args:
        plan_execution_id (str):
        account_identifier (str):
        node_execution_id (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | Failure
    """

    return sync_detailed(
        plan_execution_id=plan_execution_id,
        client=client,
        account_identifier=account_identifier,
        node_execution_id=node_execution_id,
        file_name=file_name,
    ).parsed


async def asyncio_detailed(
    plan_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    node_execution_id: str,
    file_name: str,
) -> Response[Any | Error | Failure]:
    """Returns a file uploaded or filtered based on the fileIdentifier provided for a given nodeExecutionId

     Returns a file uploaded or filtered based on the fileIdentifier provided for a given nodeExecutionId

    Args:
        plan_execution_id (str):
        account_identifier (str):
        node_execution_id (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Failure]
    """

    kwargs = _get_kwargs(
        plan_execution_id=plan_execution_id,
        account_identifier=account_identifier,
        node_execution_id=node_execution_id,
        file_name=file_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plan_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    node_execution_id: str,
    file_name: str,
) -> Any | Error | Failure | None:
    """Returns a file uploaded or filtered based on the fileIdentifier provided for a given nodeExecutionId

     Returns a file uploaded or filtered based on the fileIdentifier provided for a given nodeExecutionId

    Args:
        plan_execution_id (str):
        account_identifier (str):
        node_execution_id (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | Failure
    """

    return (
        await asyncio_detailed(
            plan_execution_id=plan_execution_id,
            client=client,
            account_identifier=account_identifier,
            node_execution_id=node_execution_id,
            file_name=file_name,
        )
    ).parsed
