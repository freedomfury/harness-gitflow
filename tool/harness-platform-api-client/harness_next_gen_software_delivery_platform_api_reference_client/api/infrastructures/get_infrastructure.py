from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_infrastructure_response import ResponseDTOInfrastructureResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    infra_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    deleted: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["environmentIdentifier"] = environment_identifier

    params["deleted"] = deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/infrastructures/{infra_identifier}".format(
            infra_identifier=quote(str(infra_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOInfrastructureResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOInfrastructureResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOInfrastructureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    infra_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    deleted: bool | Unset = False,
) -> Response[Error | Failure | ResponseDTOInfrastructureResponse]:
    """Gets an Infrastructure by identifier

    Args:
        infra_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOInfrastructureResponse]
    """

    kwargs = _get_kwargs(
        infra_identifier=infra_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        deleted=deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    infra_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    deleted: bool | Unset = False,
) -> Error | Failure | ResponseDTOInfrastructureResponse | None:
    """Gets an Infrastructure by identifier

    Args:
        infra_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOInfrastructureResponse
    """

    return sync_detailed(
        infra_identifier=infra_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        deleted=deleted,
    ).parsed


async def asyncio_detailed(
    infra_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    deleted: bool | Unset = False,
) -> Response[Error | Failure | ResponseDTOInfrastructureResponse]:
    """Gets an Infrastructure by identifier

    Args:
        infra_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOInfrastructureResponse]
    """

    kwargs = _get_kwargs(
        infra_identifier=infra_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        deleted=deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    infra_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    deleted: bool | Unset = False,
) -> Error | Failure | ResponseDTOInfrastructureResponse | None:
    """Gets an Infrastructure by identifier

    Args:
        infra_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOInfrastructureResponse
    """

    return (
        await asyncio_detailed(
            infra_identifier=infra_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            environment_identifier=environment_identifier,
            deleted=deleted,
        )
    ).parsed
