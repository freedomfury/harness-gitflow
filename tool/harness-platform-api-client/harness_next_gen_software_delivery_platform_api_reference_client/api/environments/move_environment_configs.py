from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.move_environment_configs_move_config_type import (
    MoveEnvironmentConfigsMoveConfigType,
)
from ...models.response_dto_environment_move_config_response import ResponseDTOEnvironmentMoveConfigResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    base_branch: str | Unset = UNSET,
    is_harness_code_repo: bool | Unset = False,
    move_config_type: MoveEnvironmentConfigsMoveConfigType,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["connectorRef"] = connector_ref

    params["repoName"] = repo_name

    params["branch"] = branch

    params["filePath"] = file_path

    params["commitMsg"] = commit_msg

    params["isNewBranch"] = is_new_branch

    params["baseBranch"] = base_branch

    params["isHarnessCodeRepo"] = is_harness_code_repo

    json_move_config_type: str = move_config_type
    params["moveConfigType"] = json_move_config_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/environmentsV2/move-config/{environment_identifier}".format(
            environment_identifier=quote(str(environment_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOEnvironmentMoveConfigResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOEnvironmentMoveConfigResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOEnvironmentMoveConfigResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    base_branch: str | Unset = UNSET,
    is_harness_code_repo: bool | Unset = False,
    move_config_type: MoveEnvironmentConfigsMoveConfigType,
) -> Response[Error | Failure | ResponseDTOEnvironmentMoveConfigResponse]:
    """Move environment YAML from inline to remote

    Args:
        environment_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        branch (str | Unset):
        file_path (str | Unset):
        commit_msg (str | Unset):
        is_new_branch (bool | Unset):  Default: False.
        base_branch (str | Unset):
        is_harness_code_repo (bool | Unset):  Default: False.
        move_config_type (MoveEnvironmentConfigsMoveConfigType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOEnvironmentMoveConfigResponse]
    """

    kwargs = _get_kwargs(
        environment_identifier=environment_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        connector_ref=connector_ref,
        repo_name=repo_name,
        branch=branch,
        file_path=file_path,
        commit_msg=commit_msg,
        is_new_branch=is_new_branch,
        base_branch=base_branch,
        is_harness_code_repo=is_harness_code_repo,
        move_config_type=move_config_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    base_branch: str | Unset = UNSET,
    is_harness_code_repo: bool | Unset = False,
    move_config_type: MoveEnvironmentConfigsMoveConfigType,
) -> Error | Failure | ResponseDTOEnvironmentMoveConfigResponse | None:
    """Move environment YAML from inline to remote

    Args:
        environment_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        branch (str | Unset):
        file_path (str | Unset):
        commit_msg (str | Unset):
        is_new_branch (bool | Unset):  Default: False.
        base_branch (str | Unset):
        is_harness_code_repo (bool | Unset):  Default: False.
        move_config_type (MoveEnvironmentConfigsMoveConfigType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOEnvironmentMoveConfigResponse
    """

    return sync_detailed(
        environment_identifier=environment_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        connector_ref=connector_ref,
        repo_name=repo_name,
        branch=branch,
        file_path=file_path,
        commit_msg=commit_msg,
        is_new_branch=is_new_branch,
        base_branch=base_branch,
        is_harness_code_repo=is_harness_code_repo,
        move_config_type=move_config_type,
    ).parsed


async def asyncio_detailed(
    environment_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    base_branch: str | Unset = UNSET,
    is_harness_code_repo: bool | Unset = False,
    move_config_type: MoveEnvironmentConfigsMoveConfigType,
) -> Response[Error | Failure | ResponseDTOEnvironmentMoveConfigResponse]:
    """Move environment YAML from inline to remote

    Args:
        environment_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        branch (str | Unset):
        file_path (str | Unset):
        commit_msg (str | Unset):
        is_new_branch (bool | Unset):  Default: False.
        base_branch (str | Unset):
        is_harness_code_repo (bool | Unset):  Default: False.
        move_config_type (MoveEnvironmentConfigsMoveConfigType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOEnvironmentMoveConfigResponse]
    """

    kwargs = _get_kwargs(
        environment_identifier=environment_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        connector_ref=connector_ref,
        repo_name=repo_name,
        branch=branch,
        file_path=file_path,
        commit_msg=commit_msg,
        is_new_branch=is_new_branch,
        base_branch=base_branch,
        is_harness_code_repo=is_harness_code_repo,
        move_config_type=move_config_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    base_branch: str | Unset = UNSET,
    is_harness_code_repo: bool | Unset = False,
    move_config_type: MoveEnvironmentConfigsMoveConfigType,
) -> Error | Failure | ResponseDTOEnvironmentMoveConfigResponse | None:
    """Move environment YAML from inline to remote

    Args:
        environment_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        branch (str | Unset):
        file_path (str | Unset):
        commit_msg (str | Unset):
        is_new_branch (bool | Unset):  Default: False.
        base_branch (str | Unset):
        is_harness_code_repo (bool | Unset):  Default: False.
        move_config_type (MoveEnvironmentConfigsMoveConfigType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOEnvironmentMoveConfigResponse
    """

    return (
        await asyncio_detailed(
            environment_identifier=environment_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            connector_ref=connector_ref,
            repo_name=repo_name,
            branch=branch,
            file_path=file_path,
            commit_msg=commit_msg,
            is_new_branch=is_new_branch,
            base_branch=base_branch,
            is_harness_code_repo=is_harness_code_repo,
            move_config_type=move_config_type,
        )
    ).parsed
