from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_input_sets_api_request import BulkInputSetsAPIRequest
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_bulk_input_sets_api_response import ResponseDTOBulkInputSetsAPIResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: BulkInputSetsAPIRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["pipelineIdentifier"] = pipeline_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inputSets/get/bulk",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOBulkInputSetsAPIResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOBulkInputSetsAPIResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOBulkInputSetsAPIResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkInputSetsAPIRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
) -> Response[Error | Failure | ResponseDTOBulkInputSetsAPIResponse]:
    """Get multiple input sets by identifiers (non-deleted only)

     Gets multiple input sets by their identifiers for a specific pipeline. Only returns non-deleted
    input sets.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        body (BulkInputSetsAPIRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBulkInputSetsAPIResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BulkInputSetsAPIRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
) -> Error | Failure | ResponseDTOBulkInputSetsAPIResponse | None:
    """Get multiple input sets by identifiers (non-deleted only)

     Gets multiple input sets by their identifiers for a specific pipeline. Only returns non-deleted
    input sets.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        body (BulkInputSetsAPIRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBulkInputSetsAPIResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkInputSetsAPIRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
) -> Response[Error | Failure | ResponseDTOBulkInputSetsAPIResponse]:
    """Get multiple input sets by identifiers (non-deleted only)

     Gets multiple input sets by their identifiers for a specific pipeline. Only returns non-deleted
    input sets.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        body (BulkInputSetsAPIRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBulkInputSetsAPIResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BulkInputSetsAPIRequest,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
) -> Error | Failure | ResponseDTOBulkInputSetsAPIResponse | None:
    """Get multiple input sets by identifiers (non-deleted only)

     Gets multiple input sets by their identifiers for a specific pipeline. Only returns non-deleted
    input sets.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        body (BulkInputSetsAPIRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBulkInputSetsAPIResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
        )
    ).parsed
