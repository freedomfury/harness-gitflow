from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_set_service_hook_action import ResponseDTOSetServiceHookAction
from ...types import UNSET, Response


def _get_kwargs(
    *,
    service_spec_type: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["serviceSpecType"] = service_spec_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/servicesV2/hooks/actions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOSetServiceHookAction:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOSetServiceHookAction.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOSetServiceHookAction]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    service_spec_type: str,
) -> Response[Error | Failure | ResponseDTOSetServiceHookAction]:
    """Retrieving the list of actions available for service hooks

    Args:
        service_spec_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOSetServiceHookAction]
    """

    kwargs = _get_kwargs(
        service_spec_type=service_spec_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    service_spec_type: str,
) -> Error | Failure | ResponseDTOSetServiceHookAction | None:
    """Retrieving the list of actions available for service hooks

    Args:
        service_spec_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOSetServiceHookAction
    """

    return sync_detailed(
        client=client,
        service_spec_type=service_spec_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    service_spec_type: str,
) -> Response[Error | Failure | ResponseDTOSetServiceHookAction]:
    """Retrieving the list of actions available for service hooks

    Args:
        service_spec_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOSetServiceHookAction]
    """

    kwargs = _get_kwargs(
        service_spec_type=service_spec_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    service_spec_type: str,
) -> Error | Failure | ResponseDTOSetServiceHookAction | None:
    """Retrieving the list of actions available for service hooks

    Args:
        service_spec_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOSetServiceHookAction
    """

    return (
        await asyncio_detailed(
            client=client,
            service_spec_type=service_spec_type,
        )
    ).parsed
