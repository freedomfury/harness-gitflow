from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.failure import Failure
from ...models.response_dto_dashboard_pipeline_execution import ResponseDTODashboardPipelineExecution
from ...types import UNSET, Response


def _get_kwargs(
    *,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    module_info: str,
    start_time: int,
    end_time: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["pipelineIdentifier"] = pipeline_identifier

    params["moduleInfo"] = module_info

    params["startTime"] = start_time

    params["endTime"] = end_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pipelines/pipelineExecution",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Failure | ResponseDTODashboardPipelineExecution:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    response_default = ResponseDTODashboardPipelineExecution.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Failure | ResponseDTODashboardPipelineExecution]:
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
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    module_info: str,
    start_time: int,
    end_time: int,
) -> Response[Failure | ResponseDTODashboardPipelineExecution]:
    """Fetch Execution Details for an Interval

     Returns Pipeline Execution Details for a Given Interval (Presented in Day Wise Format)

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        module_info (str):
        start_time (int):
        end_time (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Failure | ResponseDTODashboardPipelineExecution]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        module_info=module_info,
        start_time=start_time,
        end_time=end_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    module_info: str,
    start_time: int,
    end_time: int,
) -> Failure | ResponseDTODashboardPipelineExecution | None:
    """Fetch Execution Details for an Interval

     Returns Pipeline Execution Details for a Given Interval (Presented in Day Wise Format)

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        module_info (str):
        start_time (int):
        end_time (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Failure | ResponseDTODashboardPipelineExecution
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        module_info=module_info,
        start_time=start_time,
        end_time=end_time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    module_info: str,
    start_time: int,
    end_time: int,
) -> Response[Failure | ResponseDTODashboardPipelineExecution]:
    """Fetch Execution Details for an Interval

     Returns Pipeline Execution Details for a Given Interval (Presented in Day Wise Format)

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        module_info (str):
        start_time (int):
        end_time (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Failure | ResponseDTODashboardPipelineExecution]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        module_info=module_info,
        start_time=start_time,
        end_time=end_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    module_info: str,
    start_time: int,
    end_time: int,
) -> Failure | ResponseDTODashboardPipelineExecution | None:
    """Fetch Execution Details for an Interval

     Returns Pipeline Execution Details for a Given Interval (Presented in Day Wise Format)

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        module_info (str):
        start_time (int):
        end_time (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Failure | ResponseDTODashboardPipelineExecution
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
            module_info=module_info,
            start_time=start_time,
            end_time=end_time,
        )
    ).parsed
