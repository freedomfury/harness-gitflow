from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_plan_execution_response import ResponseDTOPlanExecutionResponse
from ...models.run_stage_request import RunStageRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    body: RunStageRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    module_type: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    use_fqn_if_error: bool | Unset = False,
    notes_for_pipeline_execution: str | Unset = "",
    input_set_identifiers: list[str] | Unset = UNSET,
    async_plan_creation: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["moduleType"] = module_type

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["getDefaultFromOtherRepo"] = get_default_from_other_repo

    params["useFQNIfError"] = use_fqn_if_error

    params["notesForPipelineExecution"] = notes_for_pipeline_execution

    json_input_set_identifiers: list[str] | Unset = UNSET
    if not isinstance(input_set_identifiers, Unset):
        json_input_set_identifiers = input_set_identifiers

    params["inputSetIdentifiers"] = json_input_set_identifiers

    params["asyncPlanCreation"] = async_plan_creation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pipeline/execute/{identifier}/stages".format(
            identifier=quote(str(identifier), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPlanExecutionResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPlanExecutionResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPlanExecutionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: RunStageRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    module_type: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    use_fqn_if_error: bool | Unset = False,
    notes_for_pipeline_execution: str | Unset = "",
    input_set_identifiers: list[str] | Unset = UNSET,
    async_plan_creation: bool | Unset = False,
) -> Response[Error | Failure | ResponseDTOPlanExecutionResponse]:
    """Execute given Stages of a Pipeline

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        module_type (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        use_fqn_if_error (bool | Unset):  Default: False.
        notes_for_pipeline_execution (str | Unset):  Default: ''.
        input_set_identifiers (list[str] | Unset):
        async_plan_creation (bool | Unset):  Default: False.
        body (RunStageRequest | Unset): Request Parameters needed to run specific Stages of a
            Pipeline

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPlanExecutionResponse]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        module_type=module_type,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        use_fqn_if_error=use_fqn_if_error,
        notes_for_pipeline_execution=notes_for_pipeline_execution,
        input_set_identifiers=input_set_identifiers,
        async_plan_creation=async_plan_creation,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: RunStageRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    module_type: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    use_fqn_if_error: bool | Unset = False,
    notes_for_pipeline_execution: str | Unset = "",
    input_set_identifiers: list[str] | Unset = UNSET,
    async_plan_creation: bool | Unset = False,
) -> Error | Failure | ResponseDTOPlanExecutionResponse | None:
    """Execute given Stages of a Pipeline

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        module_type (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        use_fqn_if_error (bool | Unset):  Default: False.
        notes_for_pipeline_execution (str | Unset):  Default: ''.
        input_set_identifiers (list[str] | Unset):
        async_plan_creation (bool | Unset):  Default: False.
        body (RunStageRequest | Unset): Request Parameters needed to run specific Stages of a
            Pipeline

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPlanExecutionResponse
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        module_type=module_type,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        use_fqn_if_error=use_fqn_if_error,
        notes_for_pipeline_execution=notes_for_pipeline_execution,
        input_set_identifiers=input_set_identifiers,
        async_plan_creation=async_plan_creation,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: RunStageRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    module_type: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    use_fqn_if_error: bool | Unset = False,
    notes_for_pipeline_execution: str | Unset = "",
    input_set_identifiers: list[str] | Unset = UNSET,
    async_plan_creation: bool | Unset = False,
) -> Response[Error | Failure | ResponseDTOPlanExecutionResponse]:
    """Execute given Stages of a Pipeline

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        module_type (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        use_fqn_if_error (bool | Unset):  Default: False.
        notes_for_pipeline_execution (str | Unset):  Default: ''.
        input_set_identifiers (list[str] | Unset):
        async_plan_creation (bool | Unset):  Default: False.
        body (RunStageRequest | Unset): Request Parameters needed to run specific Stages of a
            Pipeline

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPlanExecutionResponse]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        module_type=module_type,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        use_fqn_if_error=use_fqn_if_error,
        notes_for_pipeline_execution=notes_for_pipeline_execution,
        input_set_identifiers=input_set_identifiers,
        async_plan_creation=async_plan_creation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: RunStageRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    module_type: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    use_fqn_if_error: bool | Unset = False,
    notes_for_pipeline_execution: str | Unset = "",
    input_set_identifiers: list[str] | Unset = UNSET,
    async_plan_creation: bool | Unset = False,
) -> Error | Failure | ResponseDTOPlanExecutionResponse | None:
    """Execute given Stages of a Pipeline

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        module_type (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        use_fqn_if_error (bool | Unset):  Default: False.
        notes_for_pipeline_execution (str | Unset):  Default: ''.
        input_set_identifiers (list[str] | Unset):
        async_plan_creation (bool | Unset):  Default: False.
        body (RunStageRequest | Unset): Request Parameters needed to run specific Stages of a
            Pipeline

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPlanExecutionResponse
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            module_type=module_type,
            branch=branch,
            repo_identifier=repo_identifier,
            get_default_from_other_repo=get_default_from_other_repo,
            use_fqn_if_error=use_fqn_if_error,
            notes_for_pipeline_execution=notes_for_pipeline_execution,
            input_set_identifiers=input_set_identifiers,
            async_plan_creation=async_plan_creation,
        )
    ).parsed
