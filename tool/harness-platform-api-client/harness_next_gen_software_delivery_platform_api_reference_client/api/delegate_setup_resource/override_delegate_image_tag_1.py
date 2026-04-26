from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    delegate_tag: str,
    valid_till_next_release: bool | Unset = False,
    valid_for_days: int | Unset = 180,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    params["delegateTag"] = delegate_tag

    params["validTillNextRelease"] = valid_till_next_release

    params["validForDays"] = valid_for_days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/delegate-setup/override-delegate-tag",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Failure | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    delegate_tag: str,
    valid_till_next_release: bool | Unset = False,
    valid_for_days: int | Unset = 180,
) -> Response[Error | Failure | str]:
    """Overrides delegate image tag for account

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        tags (list[str] | Unset):
        delegate_tag (str):
        valid_till_next_release (bool | Unset):  Default: False.
        valid_for_days (int | Unset):  Default: 180.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | str]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        tags=tags,
        delegate_tag=delegate_tag,
        valid_till_next_release=valid_till_next_release,
        valid_for_days=valid_for_days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    delegate_tag: str,
    valid_till_next_release: bool | Unset = False,
    valid_for_days: int | Unset = 180,
) -> Error | Failure | str | None:
    """Overrides delegate image tag for account

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        tags (list[str] | Unset):
        delegate_tag (str):
        valid_till_next_release (bool | Unset):  Default: False.
        valid_for_days (int | Unset):  Default: 180.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | str
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        tags=tags,
        delegate_tag=delegate_tag,
        valid_till_next_release=valid_till_next_release,
        valid_for_days=valid_for_days,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    delegate_tag: str,
    valid_till_next_release: bool | Unset = False,
    valid_for_days: int | Unset = 180,
) -> Response[Error | Failure | str]:
    """Overrides delegate image tag for account

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        tags (list[str] | Unset):
        delegate_tag (str):
        valid_till_next_release (bool | Unset):  Default: False.
        valid_for_days (int | Unset):  Default: 180.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | str]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        tags=tags,
        delegate_tag=delegate_tag,
        valid_till_next_release=valid_till_next_release,
        valid_for_days=valid_for_days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    delegate_tag: str,
    valid_till_next_release: bool | Unset = False,
    valid_for_days: int | Unset = 180,
) -> Error | Failure | str | None:
    """Overrides delegate image tag for account

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        tags (list[str] | Unset):
        delegate_tag (str):
        valid_till_next_release (bool | Unset):  Default: False.
        valid_for_days (int | Unset):  Default: 180.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | str
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            tags=tags,
            delegate_tag=delegate_tag,
            valid_till_next_release=valid_till_next_release,
            valid_for_days=valid_for_days,
        )
    ).parsed
