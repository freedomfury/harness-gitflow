from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_list_user_group import ResponseDTOListUserGroup
from ...models.user_group_filter import UserGroupFilter
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: UserGroupFilter,
    account_identifier: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/user-groups/batch",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOListUserGroup:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOListUserGroup.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOListUserGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserGroupFilter,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOListUserGroup]:
    """List User Groups by filter

     List the User Groups selected by a filter in an account/org/project. This api supports maximum of
    10K User Group in response.

    Args:
        account_identifier (str):
        body (UserGroupFilter): This is the view of the UserGroupFilter entity defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOListUserGroup]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UserGroupFilter,
    account_identifier: str,
) -> Error | Failure | ResponseDTOListUserGroup | None:
    """List User Groups by filter

     List the User Groups selected by a filter in an account/org/project. This api supports maximum of
    10K User Group in response.

    Args:
        account_identifier (str):
        body (UserGroupFilter): This is the view of the UserGroupFilter entity defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOListUserGroup
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserGroupFilter,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOListUserGroup]:
    """List User Groups by filter

     List the User Groups selected by a filter in an account/org/project. This api supports maximum of
    10K User Group in response.

    Args:
        account_identifier (str):
        body (UserGroupFilter): This is the view of the UserGroupFilter entity defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOListUserGroup]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UserGroupFilter,
    account_identifier: str,
) -> Error | Failure | ResponseDTOListUserGroup | None:
    """List User Groups by filter

     List the User Groups selected by a filter in an account/org/project. This api supports maximum of
    10K User Group in response.

    Args:
        account_identifier (str):
        body (UserGroupFilter): This is the view of the UserGroupFilter entity defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOListUserGroup
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
        )
    ).parsed
