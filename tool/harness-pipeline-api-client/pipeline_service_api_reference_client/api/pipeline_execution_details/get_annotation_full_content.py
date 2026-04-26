from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_annotation_content_response import ResponseDTOAnnotationContentResponse
from ...types import UNSET, Response


def _get_kwargs(
    plan_execution_id: str,
    context_id: str,
    *,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["pipelineIdentifier"] = pipeline_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pipelines/execution/{plan_execution_id}/annotations/{context_id}/content".format(
            plan_execution_id=quote(str(plan_execution_id), safe=""),
            context_id=quote(str(context_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOAnnotationContentResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOAnnotationContentResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOAnnotationContentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plan_execution_id: str,
    context_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
) -> Response[Error | Failure | ResponseDTOAnnotationContentResponse]:
    """Fetch Full Annotation Content

     Returns full annotation content for a specific context from GCS

    Args:
        plan_execution_id (str):
        context_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOAnnotationContentResponse]
    """

    kwargs = _get_kwargs(
        plan_execution_id=plan_execution_id,
        context_id=context_id,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    plan_execution_id: str,
    context_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
) -> Error | Failure | ResponseDTOAnnotationContentResponse | None:
    """Fetch Full Annotation Content

     Returns full annotation content for a specific context from GCS

    Args:
        plan_execution_id (str):
        context_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOAnnotationContentResponse
    """

    return sync_detailed(
        plan_execution_id=plan_execution_id,
        context_id=context_id,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
    ).parsed


async def asyncio_detailed(
    plan_execution_id: str,
    context_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
) -> Response[Error | Failure | ResponseDTOAnnotationContentResponse]:
    """Fetch Full Annotation Content

     Returns full annotation content for a specific context from GCS

    Args:
        plan_execution_id (str):
        context_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOAnnotationContentResponse]
    """

    kwargs = _get_kwargs(
        plan_execution_id=plan_execution_id,
        context_id=context_id,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plan_execution_id: str,
    context_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
) -> Error | Failure | ResponseDTOAnnotationContentResponse | None:
    """Fetch Full Annotation Content

     Returns full annotation content for a specific context from GCS

    Args:
        plan_execution_id (str):
        context_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOAnnotationContentResponse
    """

    return (
        await asyncio_detailed(
            plan_execution_id=plan_execution_id,
            context_id=context_id,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
        )
    ).parsed
