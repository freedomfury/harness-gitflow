from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.types_webhook_execution import TypesWebhookExecution
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    webhook_identifier: str,
    webhook_execution_id: int,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhooks/{webhook_identifier}/executions/{webhook_execution_id}".format(
            webhook_identifier=quote(str(webhook_identifier), safe=""),
            webhook_execution_id=quote(str(webhook_execution_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TypesWebhookExecution | UsererrorError | None:
    if response.status_code == 200:
        response_200 = TypesWebhookExecution.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UsererrorError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsererrorError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsererrorError.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = UsererrorError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TypesWebhookExecution | UsererrorError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_identifier: str,
    webhook_execution_id: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
) -> Response[TypesWebhookExecution | UsererrorError]:
    """Get acc, org or proj webhook execution

    Args:
        webhook_identifier (str):
        webhook_execution_id (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesWebhookExecution | UsererrorError]
    """

    kwargs = _get_kwargs(
        webhook_identifier=webhook_identifier,
        webhook_execution_id=webhook_execution_id,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_identifier: str,
    webhook_execution_id: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
) -> TypesWebhookExecution | UsererrorError | None:
    """Get acc, org or proj webhook execution

    Args:
        webhook_identifier (str):
        webhook_execution_id (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesWebhookExecution | UsererrorError
    """

    return sync_detailed(
        webhook_identifier=webhook_identifier,
        webhook_execution_id=webhook_execution_id,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    webhook_identifier: str,
    webhook_execution_id: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
) -> Response[TypesWebhookExecution | UsererrorError]:
    """Get acc, org or proj webhook execution

    Args:
        webhook_identifier (str):
        webhook_execution_id (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesWebhookExecution | UsererrorError]
    """

    kwargs = _get_kwargs(
        webhook_identifier=webhook_identifier,
        webhook_execution_id=webhook_execution_id,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_identifier: str,
    webhook_execution_id: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
) -> TypesWebhookExecution | UsererrorError | None:
    """Get acc, org or proj webhook execution

    Args:
        webhook_identifier (str):
        webhook_execution_id (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesWebhookExecution | UsererrorError
    """

    return (
        await asyncio_detailed(
            webhook_identifier=webhook_identifier,
            webhook_execution_id=webhook_execution_id,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            page=page,
            limit=limit,
        )
    ).parsed
