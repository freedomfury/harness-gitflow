from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.types_delete_branch_output import TypesDeleteBranchOutput
from ...models.types_rules_violations import TypesRulesViolations
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_identifier: str,
    branch_name: str,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    bypass_rules: bool | Unset = False,
    dry_run_rules: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["bypass_rules"] = bypass_rules

    params["dry_run_rules"] = dry_run_rules

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/repos/{repo_identifier}/branches/{branch_name}".format(
            repo_identifier=quote(str(repo_identifier), safe=""),
            branch_name=quote(str(branch_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TypesDeleteBranchOutput | TypesRulesViolations | UsererrorError | None:
    if response.status_code == 200:
        response_200 = TypesDeleteBranchOutput.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = TypesRulesViolations.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = UsererrorError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TypesDeleteBranchOutput | TypesRulesViolations | UsererrorError]:
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
    bypass_rules: bool | Unset = False,
    dry_run_rules: bool | Unset = False,
) -> Response[TypesDeleteBranchOutput | TypesRulesViolations | UsererrorError]:
    """Delete branch

    Args:
        repo_identifier (str):
        branch_name (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        bypass_rules (bool | Unset):  Default: False.
        dry_run_rules (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesDeleteBranchOutput | TypesRulesViolations | UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        branch_name=branch_name,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        bypass_rules=bypass_rules,
        dry_run_rules=dry_run_rules,
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
    bypass_rules: bool | Unset = False,
    dry_run_rules: bool | Unset = False,
) -> TypesDeleteBranchOutput | TypesRulesViolations | UsererrorError | None:
    """Delete branch

    Args:
        repo_identifier (str):
        branch_name (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        bypass_rules (bool | Unset):  Default: False.
        dry_run_rules (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesDeleteBranchOutput | TypesRulesViolations | UsererrorError
    """

    return sync_detailed(
        repo_identifier=repo_identifier,
        branch_name=branch_name,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        bypass_rules=bypass_rules,
        dry_run_rules=dry_run_rules,
    ).parsed


async def asyncio_detailed(
    repo_identifier: str,
    branch_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    bypass_rules: bool | Unset = False,
    dry_run_rules: bool | Unset = False,
) -> Response[TypesDeleteBranchOutput | TypesRulesViolations | UsererrorError]:
    """Delete branch

    Args:
        repo_identifier (str):
        branch_name (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        bypass_rules (bool | Unset):  Default: False.
        dry_run_rules (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesDeleteBranchOutput | TypesRulesViolations | UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        branch_name=branch_name,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        bypass_rules=bypass_rules,
        dry_run_rules=dry_run_rules,
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
    bypass_rules: bool | Unset = False,
    dry_run_rules: bool | Unset = False,
) -> TypesDeleteBranchOutput | TypesRulesViolations | UsererrorError | None:
    """Delete branch

    Args:
        repo_identifier (str):
        branch_name (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        bypass_rules (bool | Unset):  Default: False.
        dry_run_rules (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesDeleteBranchOutput | TypesRulesViolations | UsererrorError
    """

    return (
        await asyncio_detailed(
            repo_identifier=repo_identifier,
            branch_name=branch_name,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            bypass_rules=bypass_rules,
            dry_run_rules=dry_run_rules,
        )
    ).parsed
