from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.harness_approval_activity_request import HarnessApprovalActivityRequest
from ...models.response_dto_approval_instance_response import ResponseDTOApprovalInstanceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    approval_instance_id: str,
    *,
    body: HarnessApprovalActivityRequest,
    account_identifier: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/approvals/{approval_instance_id}/harness/activity".format(
            approval_instance_id=quote(str(approval_instance_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOApprovalInstanceResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOApprovalInstanceResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOApprovalInstanceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    approval_instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: HarnessApprovalActivityRequest,
    account_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOApprovalInstanceResponse]:
    """Approve or Reject a Pipeline Execution

    Args:
        approval_instance_id (str):
        account_identifier (str | Unset):
        body (HarnessApprovalActivityRequest): Details of approval activity requested

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOApprovalInstanceResponse]
    """

    kwargs = _get_kwargs(
        approval_instance_id=approval_instance_id,
        body=body,
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    approval_instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: HarnessApprovalActivityRequest,
    account_identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOApprovalInstanceResponse | None:
    """Approve or Reject a Pipeline Execution

    Args:
        approval_instance_id (str):
        account_identifier (str | Unset):
        body (HarnessApprovalActivityRequest): Details of approval activity requested

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOApprovalInstanceResponse
    """

    return sync_detailed(
        approval_instance_id=approval_instance_id,
        client=client,
        body=body,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    approval_instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: HarnessApprovalActivityRequest,
    account_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOApprovalInstanceResponse]:
    """Approve or Reject a Pipeline Execution

    Args:
        approval_instance_id (str):
        account_identifier (str | Unset):
        body (HarnessApprovalActivityRequest): Details of approval activity requested

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOApprovalInstanceResponse]
    """

    kwargs = _get_kwargs(
        approval_instance_id=approval_instance_id,
        body=body,
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    approval_instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: HarnessApprovalActivityRequest,
    account_identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOApprovalInstanceResponse | None:
    """Approve or Reject a Pipeline Execution

    Args:
        approval_instance_id (str):
        account_identifier (str | Unset):
        body (HarnessApprovalActivityRequest): Details of approval activity requested

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOApprovalInstanceResponse
    """

    return (
        await asyncio_detailed(
            approval_instance_id=approval_instance_id,
            client=client,
            body=body,
            account_identifier=account_identifier,
        )
    ).parsed
