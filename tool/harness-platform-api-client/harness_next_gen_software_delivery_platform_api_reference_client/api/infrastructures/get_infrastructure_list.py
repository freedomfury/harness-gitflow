from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_infrastructure_list_deployment_type import (
    GetInfrastructureListDeploymentType,
)
from ...models.response_dto_page_response_infrastructure_response import ResponseDTOPageResponseInfrastructureResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    search_term: str | Unset = UNSET,
    infra_identifiers: list[str] | Unset = UNSET,
    deployment_type: GetInfrastructureListDeploymentType | Unset = UNSET,
    deployment_template_identifier: str | Unset = UNSET,
    version_label: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    service_refs: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["environmentIdentifier"] = environment_identifier

    params["searchTerm"] = search_term

    json_infra_identifiers: list[str] | Unset = UNSET
    if not isinstance(infra_identifiers, Unset):
        json_infra_identifiers = infra_identifiers

    params["infraIdentifiers"] = json_infra_identifiers

    json_deployment_type: str | Unset = UNSET
    if not isinstance(deployment_type, Unset):
        json_deployment_type = deployment_type

    params["deploymentType"] = json_deployment_type

    params["deploymentTemplateIdentifier"] = deployment_template_identifier

    params["versionLabel"] = version_label

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_service_refs: list[str] | Unset = UNSET
    if not isinstance(service_refs, Unset):
        json_service_refs = service_refs

    params["serviceRefs"] = json_service_refs

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/infrastructures",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseInfrastructureResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseInfrastructureResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseInfrastructureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    search_term: str | Unset = UNSET,
    infra_identifiers: list[str] | Unset = UNSET,
    deployment_type: GetInfrastructureListDeploymentType | Unset = UNSET,
    deployment_template_identifier: str | Unset = UNSET,
    version_label: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    service_refs: list[str] | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseInfrastructureResponse]:
    """Gets Infrastructure list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        search_term (str | Unset):
        infra_identifiers (list[str] | Unset):
        deployment_type (GetInfrastructureListDeploymentType | Unset):
        deployment_template_identifier (str | Unset):
        version_label (str | Unset):
        sort (list[str] | Unset):
        service_refs (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseInfrastructureResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        search_term=search_term,
        infra_identifiers=infra_identifiers,
        deployment_type=deployment_type,
        deployment_template_identifier=deployment_template_identifier,
        version_label=version_label,
        sort=sort,
        service_refs=service_refs,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    search_term: str | Unset = UNSET,
    infra_identifiers: list[str] | Unset = UNSET,
    deployment_type: GetInfrastructureListDeploymentType | Unset = UNSET,
    deployment_template_identifier: str | Unset = UNSET,
    version_label: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    service_refs: list[str] | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseInfrastructureResponse | None:
    """Gets Infrastructure list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        search_term (str | Unset):
        infra_identifiers (list[str] | Unset):
        deployment_type (GetInfrastructureListDeploymentType | Unset):
        deployment_template_identifier (str | Unset):
        version_label (str | Unset):
        sort (list[str] | Unset):
        service_refs (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseInfrastructureResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        search_term=search_term,
        infra_identifiers=infra_identifiers,
        deployment_type=deployment_type,
        deployment_template_identifier=deployment_template_identifier,
        version_label=version_label,
        sort=sort,
        service_refs=service_refs,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    search_term: str | Unset = UNSET,
    infra_identifiers: list[str] | Unset = UNSET,
    deployment_type: GetInfrastructureListDeploymentType | Unset = UNSET,
    deployment_template_identifier: str | Unset = UNSET,
    version_label: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    service_refs: list[str] | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPageResponseInfrastructureResponse]:
    """Gets Infrastructure list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        search_term (str | Unset):
        infra_identifiers (list[str] | Unset):
        deployment_type (GetInfrastructureListDeploymentType | Unset):
        deployment_template_identifier (str | Unset):
        version_label (str | Unset):
        sort (list[str] | Unset):
        service_refs (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseInfrastructureResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        environment_identifier=environment_identifier,
        search_term=search_term,
        infra_identifiers=infra_identifiers,
        deployment_type=deployment_type,
        deployment_template_identifier=deployment_template_identifier,
        version_label=version_label,
        sort=sort,
        service_refs=service_refs,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    environment_identifier: str,
    search_term: str | Unset = UNSET,
    infra_identifiers: list[str] | Unset = UNSET,
    deployment_type: GetInfrastructureListDeploymentType | Unset = UNSET,
    deployment_template_identifier: str | Unset = UNSET,
    version_label: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    service_refs: list[str] | Unset = UNSET,
) -> Error | Failure | ResponseDTOPageResponseInfrastructureResponse | None:
    """Gets Infrastructure list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_identifier (str):
        search_term (str | Unset):
        infra_identifiers (list[str] | Unset):
        deployment_type (GetInfrastructureListDeploymentType | Unset):
        deployment_template_identifier (str | Unset):
        version_label (str | Unset):
        sort (list[str] | Unset):
        service_refs (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseInfrastructureResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            environment_identifier=environment_identifier,
            search_term=search_term,
            infra_identifiers=infra_identifiers,
            deployment_type=deployment_type,
            deployment_template_identifier=deployment_template_identifier,
            version_label=version_label,
            sort=sort,
            service_refs=service_refs,
        )
    ).parsed
