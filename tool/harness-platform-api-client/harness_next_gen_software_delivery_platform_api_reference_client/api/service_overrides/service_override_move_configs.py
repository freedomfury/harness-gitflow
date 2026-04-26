from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_service_override_move_config_response import ResponseDTOServiceOverrideMoveConfigResponse
from ...models.service_override_move_configs_move_config_type import (
    ServiceOverrideMoveConfigsMoveConfigType,
)
from ...models.service_override_move_configs_service_overrides_type import (
    ServiceOverrideMoveConfigsServiceOverridesType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
    move_config_type: ServiceOverrideMoveConfigsMoveConfigType | Unset = UNSET,
    environment_ref: str | Unset = UNSET,
    service_ref: str | Unset = UNSET,
    infra_identifier: str | Unset = UNSET,
    service_overrides_type: ServiceOverrideMoveConfigsServiceOverridesType | Unset = UNSET,
    identifier: str | Unset = UNSET,
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

    params["environmentRef"] = environment_ref

    params["serviceRef"] = service_ref

    params["infraIdentifier"] = infra_identifier

    json_service_overrides_type: str | Unset = UNSET
    if not isinstance(service_overrides_type, Unset):
        json_service_overrides_type = service_overrides_type

    params["serviceOverridesType"] = json_service_overrides_type

    params["identifier"] = identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/serviceOverrides/move-config",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOServiceOverrideMoveConfigResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOServiceOverrideMoveConfigResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOServiceOverrideMoveConfigResponse]:
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
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    base_branch: str | Unset = UNSET,
    is_harness_code_repo: bool | Unset = False,
    move_config_type: ServiceOverrideMoveConfigsMoveConfigType | Unset = UNSET,
    environment_ref: str | Unset = UNSET,
    service_ref: str | Unset = UNSET,
    infra_identifier: str | Unset = UNSET,
    service_overrides_type: ServiceOverrideMoveConfigsServiceOverridesType | Unset = UNSET,
    identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOServiceOverrideMoveConfigResponse]:
    """Move ServiceOverride YAML from inline to remote or remote to inline

    Args:
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
        move_config_type (ServiceOverrideMoveConfigsMoveConfigType | Unset):
        environment_ref (str | Unset):
        service_ref (str | Unset):
        infra_identifier (str | Unset):
        service_overrides_type (ServiceOverrideMoveConfigsServiceOverridesType | Unset):
        identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOServiceOverrideMoveConfigResponse]
    """

    kwargs = _get_kwargs(
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
        environment_ref=environment_ref,
        service_ref=service_ref,
        infra_identifier=infra_identifier,
        service_overrides_type=service_overrides_type,
        identifier=identifier,
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
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    base_branch: str | Unset = UNSET,
    is_harness_code_repo: bool | Unset = False,
    move_config_type: ServiceOverrideMoveConfigsMoveConfigType | Unset = UNSET,
    environment_ref: str | Unset = UNSET,
    service_ref: str | Unset = UNSET,
    infra_identifier: str | Unset = UNSET,
    service_overrides_type: ServiceOverrideMoveConfigsServiceOverridesType | Unset = UNSET,
    identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOServiceOverrideMoveConfigResponse | None:
    """Move ServiceOverride YAML from inline to remote or remote to inline

    Args:
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
        move_config_type (ServiceOverrideMoveConfigsMoveConfigType | Unset):
        environment_ref (str | Unset):
        service_ref (str | Unset):
        infra_identifier (str | Unset):
        service_overrides_type (ServiceOverrideMoveConfigsServiceOverridesType | Unset):
        identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOServiceOverrideMoveConfigResponse
    """

    return sync_detailed(
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
        environment_ref=environment_ref,
        service_ref=service_ref,
        infra_identifier=infra_identifier,
        service_overrides_type=service_overrides_type,
        identifier=identifier,
    ).parsed


async def asyncio_detailed(
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
    move_config_type: ServiceOverrideMoveConfigsMoveConfigType | Unset = UNSET,
    environment_ref: str | Unset = UNSET,
    service_ref: str | Unset = UNSET,
    infra_identifier: str | Unset = UNSET,
    service_overrides_type: ServiceOverrideMoveConfigsServiceOverridesType | Unset = UNSET,
    identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOServiceOverrideMoveConfigResponse]:
    """Move ServiceOverride YAML from inline to remote or remote to inline

    Args:
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
        move_config_type (ServiceOverrideMoveConfigsMoveConfigType | Unset):
        environment_ref (str | Unset):
        service_ref (str | Unset):
        infra_identifier (str | Unset):
        service_overrides_type (ServiceOverrideMoveConfigsServiceOverridesType | Unset):
        identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOServiceOverrideMoveConfigResponse]
    """

    kwargs = _get_kwargs(
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
        environment_ref=environment_ref,
        service_ref=service_ref,
        infra_identifier=infra_identifier,
        service_overrides_type=service_overrides_type,
        identifier=identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
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
    move_config_type: ServiceOverrideMoveConfigsMoveConfigType | Unset = UNSET,
    environment_ref: str | Unset = UNSET,
    service_ref: str | Unset = UNSET,
    infra_identifier: str | Unset = UNSET,
    service_overrides_type: ServiceOverrideMoveConfigsServiceOverridesType | Unset = UNSET,
    identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOServiceOverrideMoveConfigResponse | None:
    """Move ServiceOverride YAML from inline to remote or remote to inline

    Args:
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
        move_config_type (ServiceOverrideMoveConfigsMoveConfigType | Unset):
        environment_ref (str | Unset):
        service_ref (str | Unset):
        infra_identifier (str | Unset):
        service_overrides_type (ServiceOverrideMoveConfigsServiceOverridesType | Unset):
        identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOServiceOverrideMoveConfigResponse
    """

    return (
        await asyncio_detailed(
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
            environment_ref=environment_ref,
            service_ref=service_ref,
            infra_identifier=infra_identifier,
            service_overrides_type=service_overrides_type,
            identifier=identifier,
        )
    ).parsed
