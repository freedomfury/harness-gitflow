from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_pipeline_execution_count_info import ResponseDTOPipelineExecutionCountInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    artifact_path: str | Unset = UNSET,
    artifact_version: str | Unset = UNSET,
    artifact: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["serviceId"] = service_id

    params["startTime"] = start_time

    params["endTime"] = end_time

    params["artifactPath"] = artifact_path

    params["artifactVersion"] = artifact_version

    params["artifact"] = artifact

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dashboard/getPipelineExecutionCount",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPipelineExecutionCountInfo:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPipelineExecutionCountInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPipelineExecutionCountInfo]:
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
    service_id: str | Unset = UNSET,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    artifact_path: str | Unset = UNSET,
    artifact_version: str | Unset = UNSET,
    artifact: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPipelineExecutionCountInfo]:
    """Get pipeline execution count for a service with grouping support on artifact and deployment status

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        service_id (str | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        artifact_path (str | Unset):
        artifact_version (str | Unset):
        artifact (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPipelineExecutionCountInfo]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        service_id=service_id,
        start_time=start_time,
        end_time=end_time,
        artifact_path=artifact_path,
        artifact_version=artifact_version,
        artifact=artifact,
        status=status,
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
    service_id: str | Unset = UNSET,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    artifact_path: str | Unset = UNSET,
    artifact_version: str | Unset = UNSET,
    artifact: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPipelineExecutionCountInfo | None:
    """Get pipeline execution count for a service with grouping support on artifact and deployment status

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        service_id (str | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        artifact_path (str | Unset):
        artifact_version (str | Unset):
        artifact (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPipelineExecutionCountInfo
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        service_id=service_id,
        start_time=start_time,
        end_time=end_time,
        artifact_path=artifact_path,
        artifact_version=artifact_version,
        artifact=artifact,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    artifact_path: str | Unset = UNSET,
    artifact_version: str | Unset = UNSET,
    artifact: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPipelineExecutionCountInfo]:
    """Get pipeline execution count for a service with grouping support on artifact and deployment status

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        service_id (str | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        artifact_path (str | Unset):
        artifact_version (str | Unset):
        artifact (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPipelineExecutionCountInfo]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        service_id=service_id,
        start_time=start_time,
        end_time=end_time,
        artifact_path=artifact_path,
        artifact_version=artifact_version,
        artifact=artifact,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    artifact_path: str | Unset = UNSET,
    artifact_version: str | Unset = UNSET,
    artifact: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPipelineExecutionCountInfo | None:
    """Get pipeline execution count for a service with grouping support on artifact and deployment status

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        service_id (str | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        artifact_path (str | Unset):
        artifact_version (str | Unset):
        artifact (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPipelineExecutionCountInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            service_id=service_id,
            start_time=start_time,
            end_time=end_time,
            artifact_path=artifact_path,
            artifact_version=artifact_version,
            artifact=artifact,
            status=status,
        )
    ).parsed
