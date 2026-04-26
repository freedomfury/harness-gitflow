from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.types_branch_extended import TypesBranchExtended
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_identifier: str,
    branch_name: str,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    include_checks: bool | Unset = False,
    include_rules: bool | Unset = False,
    include_pullreqs: bool | Unset = False,
    max_divergence: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["include_checks"] = include_checks

    params["include_rules"] = include_rules

    params["include_pullreqs"] = include_pullreqs

    params["max_divergence"] = max_divergence

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repos/{repo_identifier}/branches/{branch_name}".format(
            repo_identifier=quote(str(repo_identifier), safe=""),
            branch_name=quote(str(branch_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TypesBranchExtended | UsererrorError | None:
    if response.status_code == 200:
        response_200 = TypesBranchExtended.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UsererrorError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsererrorError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsererrorError.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UsererrorError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TypesBranchExtended | UsererrorError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repo_identifier: str,
    branch_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    include_checks: bool | Unset = False,
    include_rules: bool | Unset = False,
    include_pullreqs: bool | Unset = False,
    max_divergence: int | Unset = 0,
) -> Response[TypesBranchExtended | UsererrorError]:
    """Get branch

    Args:
        repo_identifier (str):
        branch_name (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        include_checks (bool | Unset):  Default: False.
        include_rules (bool | Unset):  Default: False.
        include_pullreqs (bool | Unset):  Default: False.
        max_divergence (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesBranchExtended | UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        branch_name=branch_name,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        include_checks=include_checks,
        include_rules=include_rules,
        include_pullreqs=include_pullreqs,
        max_divergence=max_divergence,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repo_identifier: str,
    branch_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    include_checks: bool | Unset = False,
    include_rules: bool | Unset = False,
    include_pullreqs: bool | Unset = False,
    max_divergence: int | Unset = 0,
) -> TypesBranchExtended | UsererrorError | None:
    """Get branch

    Args:
        repo_identifier (str):
        branch_name (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        include_checks (bool | Unset):  Default: False.
        include_rules (bool | Unset):  Default: False.
        include_pullreqs (bool | Unset):  Default: False.
        max_divergence (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesBranchExtended | UsererrorError
    """

    return sync_detailed(
        repo_identifier=repo_identifier,
        branch_name=branch_name,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        include_checks=include_checks,
        include_rules=include_rules,
        include_pullreqs=include_pullreqs,
        max_divergence=max_divergence,
    ).parsed


async def asyncio_detailed(
    repo_identifier: str,
    branch_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    include_checks: bool | Unset = False,
    include_rules: bool | Unset = False,
    include_pullreqs: bool | Unset = False,
    max_divergence: int | Unset = 0,
) -> Response[TypesBranchExtended | UsererrorError]:
    """Get branch

    Args:
        repo_identifier (str):
        branch_name (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        include_checks (bool | Unset):  Default: False.
        include_rules (bool | Unset):  Default: False.
        include_pullreqs (bool | Unset):  Default: False.
        max_divergence (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesBranchExtended | UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        branch_name=branch_name,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        include_checks=include_checks,
        include_rules=include_rules,
        include_pullreqs=include_pullreqs,
        max_divergence=max_divergence,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repo_identifier: str,
    branch_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    include_checks: bool | Unset = False,
    include_rules: bool | Unset = False,
    include_pullreqs: bool | Unset = False,
    max_divergence: int | Unset = 0,
) -> TypesBranchExtended | UsererrorError | None:
    """Get branch

    Args:
        repo_identifier (str):
        branch_name (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        include_checks (bool | Unset):  Default: False.
        include_rules (bool | Unset):  Default: False.
        include_pullreqs (bool | Unset):  Default: False.
        max_divergence (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesBranchExtended | UsererrorError
    """

    return (
        await asyncio_detailed(
            repo_identifier=repo_identifier,
            branch_name=branch_name,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            include_checks=include_checks,
            include_rules=include_rules,
            include_pullreqs=include_pullreqs,
            max_divergence=max_divergence,
        )
    ).parsed
