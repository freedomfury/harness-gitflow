from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dtong_trigger_response import ResponseDTONGTriggerResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: str,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    ignore_error: bool | Unset = False,
    with_service_v2: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["targetIdentifier"] = target_identifier

    params["ignoreError"] = ignore_error

    params["withServiceV2"] = with_service_v2

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/triggers",
        "params": params,
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTONGTriggerResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTONGTriggerResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTONGTriggerResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: str,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    ignore_error: bool | Unset = False,
    with_service_v2: bool | Unset = False,
) -> Response[Error | Failure | ResponseDTONGTriggerResponse]:
    """Creates Trigger for triggering target pipeline identifier.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        ignore_error (bool | Unset):  Default: False.
        with_service_v2 (bool | Unset):  Default: False.
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTONGTriggerResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        ignore_error=ignore_error,
        with_service_v2=with_service_v2,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: str,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    ignore_error: bool | Unset = False,
    with_service_v2: bool | Unset = False,
) -> Error | Failure | ResponseDTONGTriggerResponse | None:
    """Creates Trigger for triggering target pipeline identifier.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        ignore_error (bool | Unset):  Default: False.
        with_service_v2 (bool | Unset):  Default: False.
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTONGTriggerResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        ignore_error=ignore_error,
        with_service_v2=with_service_v2,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: str,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    ignore_error: bool | Unset = False,
    with_service_v2: bool | Unset = False,
) -> Response[Error | Failure | ResponseDTONGTriggerResponse]:
    """Creates Trigger for triggering target pipeline identifier.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        ignore_error (bool | Unset):  Default: False.
        with_service_v2 (bool | Unset):  Default: False.
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTONGTriggerResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        target_identifier=target_identifier,
        ignore_error=ignore_error,
        with_service_v2=with_service_v2,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: str,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    target_identifier: str,
    ignore_error: bool | Unset = False,
    with_service_v2: bool | Unset = False,
) -> Error | Failure | ResponseDTONGTriggerResponse | None:
    """Creates Trigger for triggering target pipeline identifier.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        target_identifier (str):
        ignore_error (bool | Unset):  Default: False.
        with_service_v2 (bool | Unset):  Default: False.
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTONGTriggerResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            target_identifier=target_identifier,
            ignore_error=ignore_error,
            with_service_v2=with_service_v2,
        )
    ).parsed
