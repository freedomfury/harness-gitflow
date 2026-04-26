from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_string import ResponseDTOString
from ...types import UNSET, Response, Unset


def _get_kwargs(
    scoped_file_path: str,
    *,
    account_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/file-store/files/{scoped_file_path}/content".format(
            scoped_file_path=quote(str(scoped_file_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOString:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOString.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOString]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scoped_file_path: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOString]:
    """Get file content of scopedFilePath

    Args:
        scoped_file_path (str):
        account_identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOString]
    """

    kwargs = _get_kwargs(
        scoped_file_path=scoped_file_path,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scoped_file_path: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOString | None:
    """Get file content of scopedFilePath

    Args:
        scoped_file_path (str):
        account_identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOString
    """

    return sync_detailed(
        scoped_file_path=scoped_file_path,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    scoped_file_path: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOString]:
    """Get file content of scopedFilePath

    Args:
        scoped_file_path (str):
        account_identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOString]
    """

    kwargs = _get_kwargs(
        scoped_file_path=scoped_file_path,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scoped_file_path: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOString | None:
    """Get file content of scopedFilePath

    Args:
        scoped_file_path (str):
        account_identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOString
    """

    return (
        await asyncio_detailed(
            scoped_file_path=scoped_file_path,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
        )
    ).parsed
