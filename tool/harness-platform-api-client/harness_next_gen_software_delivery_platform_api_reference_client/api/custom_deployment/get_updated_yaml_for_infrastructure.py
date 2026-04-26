from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.custom_deployment_yaml_dto import CustomDeploymentYamlDTO
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_custom_deployment_refresh_yaml_dto import ResponseDTOCustomDeploymentRefreshYamlDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    infra_identifier: str,
    *,
    body: CustomDeploymentYamlDTO,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/customDeployment/get-updated-Yaml/{infra_identifier}".format(
            infra_identifier=quote(str(infra_identifier), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOCustomDeploymentRefreshYamlDTO:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOCustomDeploymentRefreshYamlDTO.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOCustomDeploymentRefreshYamlDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    infra_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomDeploymentYamlDTO,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOCustomDeploymentRefreshYamlDTO]:
    """Return the updated yaml for infrastructure based on Deployment template

    Args:
        infra_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (CustomDeploymentYamlDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOCustomDeploymentRefreshYamlDTO]
    """

    kwargs = _get_kwargs(
        infra_identifier=infra_identifier,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    infra_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomDeploymentYamlDTO,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOCustomDeploymentRefreshYamlDTO | None:
    """Return the updated yaml for infrastructure based on Deployment template

    Args:
        infra_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (CustomDeploymentYamlDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOCustomDeploymentRefreshYamlDTO
    """

    return sync_detailed(
        infra_identifier=infra_identifier,
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    infra_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomDeploymentYamlDTO,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOCustomDeploymentRefreshYamlDTO]:
    """Return the updated yaml for infrastructure based on Deployment template

    Args:
        infra_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (CustomDeploymentYamlDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOCustomDeploymentRefreshYamlDTO]
    """

    kwargs = _get_kwargs(
        infra_identifier=infra_identifier,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    infra_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomDeploymentYamlDTO,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOCustomDeploymentRefreshYamlDTO | None:
    """Return the updated yaml for infrastructure based on Deployment template

    Args:
        infra_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (CustomDeploymentYamlDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOCustomDeploymentRefreshYamlDTO
    """

    return (
        await asyncio_detailed(
            infra_identifier=infra_identifier,
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
        )
    ).parsed
