from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.move_service_configs_move_config_type import (
    MoveServiceConfigsMoveConfigType,
)
from ...models.response_dto_service_move_config_response import ResponseDTOServiceMoveConfigResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_identifier: str,
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
    move_config_type: MoveServiceConfigsMoveConfigType | Unset = UNSET,
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

    json_move_config_type: str | Unset = UNSET
    if not isinstance(move_config_type, Unset):
        json_move_config_type = move_config_type

    params["moveConfigType"] = json_move_config_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/servicesV2/move-config/{service_identifier}".format(
            service_identifier=quote(str(service_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOServiceMoveConfigResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOServiceMoveConfigResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOServiceMoveConfigResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_identifier: str,
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
    move_config_type: MoveServiceConfigsMoveConfigType | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOServiceMoveConfigResponse]:
    """Move Service YAML from inline to remote

    Args:
        service_identifier (str):
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
        move_config_type (MoveServiceConfigsMoveConfigType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOServiceMoveConfigResponse]
    """

    kwargs = _get_kwargs(
        service_identifier=service_identifier,
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
    service_identifier: str,
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
    move_config_type: MoveServiceConfigsMoveConfigType | Unset = UNSET,
) -> Error | Failure | ResponseDTOServiceMoveConfigResponse | None:
    """Move Service YAML from inline to remote

    Args:
        service_identifier (str):
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
        move_config_type (MoveServiceConfigsMoveConfigType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOServiceMoveConfigResponse
    """

    return sync_detailed(
        service_identifier=service_identifier,
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
    service_identifier: str,
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
    move_config_type: MoveServiceConfigsMoveConfigType | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOServiceMoveConfigResponse]:
    """Move Service YAML from inline to remote

    Args:
        service_identifier (str):
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
        move_config_type (MoveServiceConfigsMoveConfigType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOServiceMoveConfigResponse]
    """

    kwargs = _get_kwargs(
        service_identifier=service_identifier,
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
    service_identifier: str,
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
    move_config_type: MoveServiceConfigsMoveConfigType | Unset = UNSET,
) -> Error | Failure | ResponseDTOServiceMoveConfigResponse | None:
    """Move Service YAML from inline to remote

    Args:
        service_identifier (str):
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
        move_config_type (MoveServiceConfigsMoveConfigType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOServiceMoveConfigResponse
    """

    return (
        await asyncio_detailed(
            service_identifier=service_identifier,
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
