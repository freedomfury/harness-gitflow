from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.batch_input_sets_api_request import BatchInputSetsAPIRequest
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_page_response_input_set_list_response import ResponseDTOPageResponseInputSetListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BatchInputSetsAPIRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    page_index: int | Unset = 0,
    page_size: int | Unset = 20,
    search_term: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["pageIndex"] = page_index

    params["pageSize"] = page_size

    params["searchTerm"] = search_term

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inputSets/get/batch-input-sets-metadata",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseInputSetListResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseInputSetListResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseInputSetListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchInputSetsAPIRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    page_index: int | Unset = 0,
    page_size: int | Unset = 20,
    search_term: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseInputSetListResponse]:
    """List regular Input Sets for multiple pipelines (excludes overlay input sets)

     Lists regular Input Sets for multiple pipelines (excludes overlay input sets). If pipeline
    identifiers are not provided, fetches all accessible input sets based on RBAC permissions.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        search_term (str | Unset):
        body (BatchInputSetsAPIRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseInputSetListResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page_index=page_index,
        page_size=page_size,
        search_term=search_term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BatchInputSetsAPIRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    page_index: int | Unset = 0,
    page_size: int | Unset = 20,
    search_term: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseInputSetListResponse | None:
    """List regular Input Sets for multiple pipelines (excludes overlay input sets)

     Lists regular Input Sets for multiple pipelines (excludes overlay input sets). If pipeline
    identifiers are not provided, fetches all accessible input sets based on RBAC permissions.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        search_term (str | Unset):
        body (BatchInputSetsAPIRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseInputSetListResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page_index=page_index,
        page_size=page_size,
        search_term=search_term,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchInputSetsAPIRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    page_index: int | Unset = 0,
    page_size: int | Unset = 20,
    search_term: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseInputSetListResponse]:
    """List regular Input Sets for multiple pipelines (excludes overlay input sets)

     Lists regular Input Sets for multiple pipelines (excludes overlay input sets). If pipeline
    identifiers are not provided, fetches all accessible input sets based on RBAC permissions.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        search_term (str | Unset):
        body (BatchInputSetsAPIRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseInputSetListResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page_index=page_index,
        page_size=page_size,
        search_term=search_term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BatchInputSetsAPIRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    page_index: int | Unset = 0,
    page_size: int | Unset = 20,
    search_term: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseInputSetListResponse | None:
    """List regular Input Sets for multiple pipelines (excludes overlay input sets)

     Lists regular Input Sets for multiple pipelines (excludes overlay input sets). If pipeline
    identifiers are not provided, fetches all accessible input sets based on RBAC permissions.

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        page_index (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        search_term (str | Unset):
        body (BatchInputSetsAPIRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseInputSetListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            page_index=page_index,
            page_size=page_size,
            search_term=search_term,
        )
    ).parsed
