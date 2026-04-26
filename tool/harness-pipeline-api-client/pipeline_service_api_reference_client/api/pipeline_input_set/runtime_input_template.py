from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.input_set_template_request import InputSetTemplateRequest
from ...models.response_dto_input_set_template_with_replaced_expressions_response import (
    ResponseDTOInputSetTemplateWithReplacedExpressionsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: InputSetTemplateRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_cache: str | Unset = "false",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(load_from_cache, Unset):
        headers["Load-From-Cache"] = load_from_cache

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["pipelineIdentifier"] = pipeline_identifier

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["getDefaultFromOtherRepo"] = get_default_from_other_repo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inputSets/template",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOInputSetTemplateWithReplacedExpressionsResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOInputSetTemplateWithReplacedExpressionsResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOInputSetTemplateWithReplacedExpressionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InputSetTemplateRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_cache: str | Unset = "false",
) -> Response[Error | Failure | ResponseDTOInputSetTemplateWithReplacedExpressionsResponse]:
    """Fetch Runtime Input Template

     Returns Runtime Input Template for a Pipeline

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_cache (str | Unset):  Default: 'false'.
        body (InputSetTemplateRequest | Unset): Contains Stage Identifiers to filter Runtime Input
            Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOInputSetTemplateWithReplacedExpressionsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        load_from_cache=load_from_cache,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: InputSetTemplateRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_cache: str | Unset = "false",
) -> Error | Failure | ResponseDTOInputSetTemplateWithReplacedExpressionsResponse | None:
    """Fetch Runtime Input Template

     Returns Runtime Input Template for a Pipeline

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_cache (str | Unset):  Default: 'false'.
        body (InputSetTemplateRequest | Unset): Contains Stage Identifiers to filter Runtime Input
            Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOInputSetTemplateWithReplacedExpressionsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        load_from_cache=load_from_cache,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InputSetTemplateRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_cache: str | Unset = "false",
) -> Response[Error | Failure | ResponseDTOInputSetTemplateWithReplacedExpressionsResponse]:
    """Fetch Runtime Input Template

     Returns Runtime Input Template for a Pipeline

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_cache (str | Unset):  Default: 'false'.
        body (InputSetTemplateRequest | Unset): Contains Stage Identifiers to filter Runtime Input
            Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOInputSetTemplateWithReplacedExpressionsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        pipeline_identifier=pipeline_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        load_from_cache=load_from_cache,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InputSetTemplateRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    pipeline_identifier: str,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    load_from_cache: str | Unset = "false",
) -> Error | Failure | ResponseDTOInputSetTemplateWithReplacedExpressionsResponse | None:
    """Fetch Runtime Input Template

     Returns Runtime Input Template for a Pipeline

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        load_from_cache (str | Unset):  Default: 'false'.
        body (InputSetTemplateRequest | Unset): Contains Stage Identifiers to filter Runtime Input
            Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOInputSetTemplateWithReplacedExpressionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
            branch=branch,
            repo_identifier=repo_identifier,
            get_default_from_other_repo=get_default_from_other_repo,
            load_from_cache=load_from_cache,
        )
    ).parsed
