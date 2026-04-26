from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_boolean import ResponseDTOBoolean
from ...types import UNSET, Response, Unset


def _get_kwargs(
    input_set_identifier: str,
    *,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/inputSets/{input_set_identifier}".format(
            input_set_identifier=quote(str(input_set_identifier), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOBoolean:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOBoolean.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOBoolean]:
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
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOBoolean]:
    """Delete an Input Set

     Deletes the Input Set by Identifier

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
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBoolean]
    """

    kwargs = _get_kwargs(
        input_set_identifier=input_set_identifier,
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
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOBoolean | None:
    """Delete an Input Set

     Deletes the Input Set by Identifier

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
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBoolean
    """

    return sync_detailed(
        input_set_identifier=input_set_identifier,
        client=client,
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
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    input_set_identifier: str,
    *,
    client: AuthenticatedClient | Client,
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
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOBoolean]:
    """Delete an Input Set

     Deletes the Input Set by Identifier

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
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBoolean]
    """

    kwargs = _get_kwargs(
        input_set_identifier=input_set_identifier,
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
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    input_set_identifier: str,
    *,
    client: AuthenticatedClient | Client,
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
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOBoolean | None:
    """Delete an Input Set

     Deletes the Input Set by Identifier

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
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBoolean
    """

    return (
        await asyncio_detailed(
            input_set_identifier=input_set_identifier,
            client=client,
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
            if_match=if_match,
        )
    ).parsed
