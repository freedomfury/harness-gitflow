from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.plan_execution_response import PlanExecutionResponse
from ...models.retry_pipeline_request import RetryPipelineRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    body: RetryPipelineRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    module_type: str | Unset = UNSET,
    plan_execution_id: str,
    retry_stages: list[str],
    run_all_stages: bool | Unset = True,
    notes_for_pipeline_execution: str | Unset = "",
    async_plan_creation: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["moduleType"] = module_type

    params["planExecutionId"] = plan_execution_id

    json_retry_stages = retry_stages

    params["retryStages"] = json_retry_stages

    params["runAllStages"] = run_all_stages

    params["notesForPipelineExecution"] = notes_for_pipeline_execution

    params["asyncPlanCreation"] = async_plan_creation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pipeline/execute/retry/v2/{identifier}".format(
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
) -> Error | Failure | PlanExecutionResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = PlanExecutionResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | PlanExecutionResponse]:
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
    body: RetryPipelineRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    module_type: str | Unset = UNSET,
    plan_execution_id: str,
    retry_stages: list[str],
    run_all_stages: bool | Unset = True,
    notes_for_pipeline_execution: str | Unset = "",
    async_plan_creation: bool | Unset = False,
) -> Response[Error | Failure | PlanExecutionResponse]:
    """Retry a executed pipeline with Runtime Input YAML V2

     Retry a executed pipeline with Runtime Input YAML and Expression Values V2

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        module_type (str | Unset):
        plan_execution_id (str):
        retry_stages (list[str]):
        run_all_stages (bool | Unset):  Default: True.
        notes_for_pipeline_execution (str | Unset):  Default: ''.
        async_plan_creation (bool | Unset):  Default: False.
        body (RetryPipelineRequest | Unset): Request Parameters for retrying a Pipeline execution

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | PlanExecutionResponse]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        module_type=module_type,
        plan_execution_id=plan_execution_id,
        retry_stages=retry_stages,
        run_all_stages=run_all_stages,
        notes_for_pipeline_execution=notes_for_pipeline_execution,
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
    body: RetryPipelineRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    module_type: str | Unset = UNSET,
    plan_execution_id: str,
    retry_stages: list[str],
    run_all_stages: bool | Unset = True,
    notes_for_pipeline_execution: str | Unset = "",
    async_plan_creation: bool | Unset = False,
) -> Error | Failure | PlanExecutionResponse | None:
    """Retry a executed pipeline with Runtime Input YAML V2

     Retry a executed pipeline with Runtime Input YAML and Expression Values V2

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        module_type (str | Unset):
        plan_execution_id (str):
        retry_stages (list[str]):
        run_all_stages (bool | Unset):  Default: True.
        notes_for_pipeline_execution (str | Unset):  Default: ''.
        async_plan_creation (bool | Unset):  Default: False.
        body (RetryPipelineRequest | Unset): Request Parameters for retrying a Pipeline execution

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | PlanExecutionResponse
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        module_type=module_type,
        plan_execution_id=plan_execution_id,
        retry_stages=retry_stages,
        run_all_stages=run_all_stages,
        notes_for_pipeline_execution=notes_for_pipeline_execution,
        async_plan_creation=async_plan_creation,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: RetryPipelineRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    module_type: str | Unset = UNSET,
    plan_execution_id: str,
    retry_stages: list[str],
    run_all_stages: bool | Unset = True,
    notes_for_pipeline_execution: str | Unset = "",
    async_plan_creation: bool | Unset = False,
) -> Response[Error | Failure | PlanExecutionResponse]:
    """Retry a executed pipeline with Runtime Input YAML V2

     Retry a executed pipeline with Runtime Input YAML and Expression Values V2

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        module_type (str | Unset):
        plan_execution_id (str):
        retry_stages (list[str]):
        run_all_stages (bool | Unset):  Default: True.
        notes_for_pipeline_execution (str | Unset):  Default: ''.
        async_plan_creation (bool | Unset):  Default: False.
        body (RetryPipelineRequest | Unset): Request Parameters for retrying a Pipeline execution

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | PlanExecutionResponse]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        module_type=module_type,
        plan_execution_id=plan_execution_id,
        retry_stages=retry_stages,
        run_all_stages=run_all_stages,
        notes_for_pipeline_execution=notes_for_pipeline_execution,
        async_plan_creation=async_plan_creation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: RetryPipelineRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    module_type: str | Unset = UNSET,
    plan_execution_id: str,
    retry_stages: list[str],
    run_all_stages: bool | Unset = True,
    notes_for_pipeline_execution: str | Unset = "",
    async_plan_creation: bool | Unset = False,
) -> Error | Failure | PlanExecutionResponse | None:
    """Retry a executed pipeline with Runtime Input YAML V2

     Retry a executed pipeline with Runtime Input YAML and Expression Values V2

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        module_type (str | Unset):
        plan_execution_id (str):
        retry_stages (list[str]):
        run_all_stages (bool | Unset):  Default: True.
        notes_for_pipeline_execution (str | Unset):  Default: ''.
        async_plan_creation (bool | Unset):  Default: False.
        body (RetryPipelineRequest | Unset): Request Parameters for retrying a Pipeline execution

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | PlanExecutionResponse
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
            plan_execution_id=plan_execution_id,
            retry_stages=retry_stages,
            run_all_stages=run_all_stages,
            notes_for_pipeline_execution=notes_for_pipeline_execution,
            async_plan_creation=async_plan_creation,
        )
    ).parsed
