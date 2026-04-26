from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_overlay_input_set_response import ResponseDTOOverlayInputSetResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    input_set_identifier: str,
    *,
    body: str,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    root_folder: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    last_object_id: str | Unset = UNSET,
    resolved_conflict_commit_id: str | Unset = UNSET,
    base_branch: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    last_commit_id: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    is_harness_code_repo: bool | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["pipelineIdentifier"] = pipeline_identifier

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["rootFolder"] = root_folder

    params["filePath"] = file_path

    params["commitMsg"] = commit_msg

    params["lastObjectId"] = last_object_id

    params["resolvedConflictCommitId"] = resolved_conflict_commit_id

    params["baseBranch"] = base_branch

    params["connectorRef"] = connector_ref

    params["lastCommitId"] = last_commit_id

    params["isNewBranch"] = is_new_branch

    params["isHarnessCodeRepo"] = is_harness_code_repo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/inputSets/overlay/{input_set_identifier}".format(
            input_set_identifier=quote(str(input_set_identifier), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOOverlayInputSetResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOOverlayInputSetResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOOverlayInputSetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    input_set_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: str,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    root_folder: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    last_object_id: str | Unset = UNSET,
    resolved_conflict_commit_id: str | Unset = UNSET,
    base_branch: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    last_commit_id: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    is_harness_code_repo: bool | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOOverlayInputSetResponse]:
    """Update an Overlay Input Set for a pipeline

    Args:
        input_set_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        root_folder (str | Unset):
        file_path (str | Unset):
        commit_msg (str | Unset):
        last_object_id (str | Unset):
        resolved_conflict_commit_id (str | Unset):
        base_branch (str | Unset):
        connector_ref (str | Unset):
        last_commit_id (str | Unset):
        is_new_branch (bool | Unset):  Default: False.
        is_harness_code_repo (bool | Unset):
        if_match (str | Unset):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOOverlayInputSetResponse]
    """

    kwargs = _get_kwargs(
        input_set_identifier=input_set_identifier,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        root_folder=root_folder,
        file_path=file_path,
        commit_msg=commit_msg,
        last_object_id=last_object_id,
        resolved_conflict_commit_id=resolved_conflict_commit_id,
        base_branch=base_branch,
        connector_ref=connector_ref,
        last_commit_id=last_commit_id,
        is_new_branch=is_new_branch,
        is_harness_code_repo=is_harness_code_repo,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    input_set_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: str,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    root_folder: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    last_object_id: str | Unset = UNSET,
    resolved_conflict_commit_id: str | Unset = UNSET,
    base_branch: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    last_commit_id: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    is_harness_code_repo: bool | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOOverlayInputSetResponse | None:
    """Update an Overlay Input Set for a pipeline

    Args:
        input_set_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        root_folder (str | Unset):
        file_path (str | Unset):
        commit_msg (str | Unset):
        last_object_id (str | Unset):
        resolved_conflict_commit_id (str | Unset):
        base_branch (str | Unset):
        connector_ref (str | Unset):
        last_commit_id (str | Unset):
        is_new_branch (bool | Unset):  Default: False.
        is_harness_code_repo (bool | Unset):
        if_match (str | Unset):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOOverlayInputSetResponse
    """

    return sync_detailed(
        input_set_identifier=input_set_identifier,
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        root_folder=root_folder,
        file_path=file_path,
        commit_msg=commit_msg,
        last_object_id=last_object_id,
        resolved_conflict_commit_id=resolved_conflict_commit_id,
        base_branch=base_branch,
        connector_ref=connector_ref,
        last_commit_id=last_commit_id,
        is_new_branch=is_new_branch,
        is_harness_code_repo=is_harness_code_repo,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    input_set_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: str,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    root_folder: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    last_object_id: str | Unset = UNSET,
    resolved_conflict_commit_id: str | Unset = UNSET,
    base_branch: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    last_commit_id: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    is_harness_code_repo: bool | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOOverlayInputSetResponse]:
    """Update an Overlay Input Set for a pipeline

    Args:
        input_set_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        root_folder (str | Unset):
        file_path (str | Unset):
        commit_msg (str | Unset):
        last_object_id (str | Unset):
        resolved_conflict_commit_id (str | Unset):
        base_branch (str | Unset):
        connector_ref (str | Unset):
        last_commit_id (str | Unset):
        is_new_branch (bool | Unset):  Default: False.
        is_harness_code_repo (bool | Unset):
        if_match (str | Unset):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOOverlayInputSetResponse]
    """

    kwargs = _get_kwargs(
        input_set_identifier=input_set_identifier,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        root_folder=root_folder,
        file_path=file_path,
        commit_msg=commit_msg,
        last_object_id=last_object_id,
        resolved_conflict_commit_id=resolved_conflict_commit_id,
        base_branch=base_branch,
        connector_ref=connector_ref,
        last_commit_id=last_commit_id,
        is_new_branch=is_new_branch,
        is_harness_code_repo=is_harness_code_repo,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    input_set_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: str,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    root_folder: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
    commit_msg: str | Unset = UNSET,
    last_object_id: str | Unset = UNSET,
    resolved_conflict_commit_id: str | Unset = UNSET,
    base_branch: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    last_commit_id: str | Unset = UNSET,
    is_new_branch: bool | Unset = False,
    is_harness_code_repo: bool | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOOverlayInputSetResponse | None:
    """Update an Overlay Input Set for a pipeline

    Args:
        input_set_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        root_folder (str | Unset):
        file_path (str | Unset):
        commit_msg (str | Unset):
        last_object_id (str | Unset):
        resolved_conflict_commit_id (str | Unset):
        base_branch (str | Unset):
        connector_ref (str | Unset):
        last_commit_id (str | Unset):
        is_new_branch (bool | Unset):  Default: False.
        is_harness_code_repo (bool | Unset):
        if_match (str | Unset):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOOverlayInputSetResponse
    """

    return (
        await asyncio_detailed(
            input_set_identifier=input_set_identifier,
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
            branch=branch,
            repo_identifier=repo_identifier,
            root_folder=root_folder,
            file_path=file_path,
            commit_msg=commit_msg,
            last_object_id=last_object_id,
            resolved_conflict_commit_id=resolved_conflict_commit_id,
            base_branch=base_branch,
            connector_ref=connector_ref,
            last_commit_id=last_commit_id,
            is_new_branch=is_new_branch,
            is_harness_code_repo=is_harness_code_repo,
            if_match=if_match,
        )
    ).parsed
