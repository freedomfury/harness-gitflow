from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_service_list_type import GetServiceListType
from ...models.response_dto_page_response_service_response import ResponseDTOPageResponseServiceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    service_identifiers: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    type_: GetServiceListType | Unset = UNSET,
    git_ops_enabled: bool | Unset = UNSET,
    deployment_template_identifier: str | Unset = UNSET,
    version_label: str | Unset = UNSET,
    include_all_services_accessible_at_scope: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["searchTerm"] = search_term

    json_service_identifiers: list[str] | Unset = UNSET
    if not isinstance(service_identifiers, Unset):
        json_service_identifiers = service_identifiers

    params["serviceIdentifiers"] = json_service_identifiers

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params["gitOpsEnabled"] = git_ops_enabled

    params["deploymentTemplateIdentifier"] = deployment_template_identifier

    params["versionLabel"] = version_label

    params["includeAllServicesAccessibleAtScope"] = include_all_services_accessible_at_scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/servicesV2",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseServiceResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseServiceResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseServiceResponse]:
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
    search_term: str | Unset = UNSET,
    service_identifiers: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    type_: GetServiceListType | Unset = UNSET,
    git_ops_enabled: bool | Unset = UNSET,
    deployment_template_identifier: str | Unset = UNSET,
    version_label: str | Unset = UNSET,
    include_all_services_accessible_at_scope: bool | Unset = False,
) -> Response[Error | Failure | ResponseDTOPageResponseServiceResponse]:
    """Gets Service list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        service_identifiers (list[str] | Unset):
        sort (list[str] | Unset):
        type_ (GetServiceListType | Unset):
        git_ops_enabled (bool | Unset):
        deployment_template_identifier (str | Unset):
        version_label (str | Unset):
        include_all_services_accessible_at_scope (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseServiceResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        service_identifiers=service_identifiers,
        sort=sort,
        type_=type_,
        git_ops_enabled=git_ops_enabled,
        deployment_template_identifier=deployment_template_identifier,
        version_label=version_label,
        include_all_services_accessible_at_scope=include_all_services_accessible_at_scope,
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
    search_term: str | Unset = UNSET,
    service_identifiers: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    type_: GetServiceListType | Unset = UNSET,
    git_ops_enabled: bool | Unset = UNSET,
    deployment_template_identifier: str | Unset = UNSET,
    version_label: str | Unset = UNSET,
    include_all_services_accessible_at_scope: bool | Unset = False,
) -> Error | Failure | ResponseDTOPageResponseServiceResponse | None:
    """Gets Service list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        service_identifiers (list[str] | Unset):
        sort (list[str] | Unset):
        type_ (GetServiceListType | Unset):
        git_ops_enabled (bool | Unset):
        deployment_template_identifier (str | Unset):
        version_label (str | Unset):
        include_all_services_accessible_at_scope (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseServiceResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        service_identifiers=service_identifiers,
        sort=sort,
        type_=type_,
        git_ops_enabled=git_ops_enabled,
        deployment_template_identifier=deployment_template_identifier,
        version_label=version_label,
        include_all_services_accessible_at_scope=include_all_services_accessible_at_scope,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 100,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    search_term: str | Unset = UNSET,
    service_identifiers: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    type_: GetServiceListType | Unset = UNSET,
    git_ops_enabled: bool | Unset = UNSET,
    deployment_template_identifier: str | Unset = UNSET,
    version_label: str | Unset = UNSET,
    include_all_services_accessible_at_scope: bool | Unset = False,
) -> Response[Error | Failure | ResponseDTOPageResponseServiceResponse]:
    """Gets Service list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        service_identifiers (list[str] | Unset):
        sort (list[str] | Unset):
        type_ (GetServiceListType | Unset):
        git_ops_enabled (bool | Unset):
        deployment_template_identifier (str | Unset):
        version_label (str | Unset):
        include_all_services_accessible_at_scope (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseServiceResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        search_term=search_term,
        service_identifiers=service_identifiers,
        sort=sort,
        type_=type_,
        git_ops_enabled=git_ops_enabled,
        deployment_template_identifier=deployment_template_identifier,
        version_label=version_label,
        include_all_services_accessible_at_scope=include_all_services_accessible_at_scope,
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
    search_term: str | Unset = UNSET,
    service_identifiers: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    type_: GetServiceListType | Unset = UNSET,
    git_ops_enabled: bool | Unset = UNSET,
    deployment_template_identifier: str | Unset = UNSET,
    version_label: str | Unset = UNSET,
    include_all_services_accessible_at_scope: bool | Unset = False,
) -> Error | Failure | ResponseDTOPageResponseServiceResponse | None:
    """Gets Service list

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 100.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        search_term (str | Unset):
        service_identifiers (list[str] | Unset):
        sort (list[str] | Unset):
        type_ (GetServiceListType | Unset):
        git_ops_enabled (bool | Unset):
        deployment_template_identifier (str | Unset):
        version_label (str | Unset):
        include_all_services_accessible_at_scope (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseServiceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            search_term=search_term,
            service_identifiers=service_identifiers,
            sort=sort,
            type_=type_,
            git_ops_enabled=git_ops_enabled,
            deployment_template_identifier=deployment_template_identifier,
            version_label=version_label,
            include_all_services_accessible_at_scope=include_all_services_accessible_at_scope,
        )
    ).parsed
