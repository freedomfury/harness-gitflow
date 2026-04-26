from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.custom_deployment_yaml_request_dto import CustomDeploymentYamlRequestDTO
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_custom_deployment_variable_response_dto import (
    ResponseDTOCustomDeploymentVariableResponseDTO,
)
from ...types import Response


def _get_kwargs(
    *,
    body: CustomDeploymentYamlRequestDTO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/customDeployment/expression-variables",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOCustomDeploymentVariableResponseDTO:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOCustomDeploymentVariableResponseDTO.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOCustomDeploymentVariableResponseDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CustomDeploymentYamlRequestDTO,
) -> Response[Error | Failure | ResponseDTOCustomDeploymentVariableResponseDTO]:
    """Gets Custom Deployment Expression Variables

    Args:
        body (CustomDeploymentYamlRequestDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOCustomDeploymentVariableResponseDTO]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CustomDeploymentYamlRequestDTO,
) -> Error | Failure | ResponseDTOCustomDeploymentVariableResponseDTO | None:
    """Gets Custom Deployment Expression Variables

    Args:
        body (CustomDeploymentYamlRequestDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOCustomDeploymentVariableResponseDTO
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CustomDeploymentYamlRequestDTO,
) -> Response[Error | Failure | ResponseDTOCustomDeploymentVariableResponseDTO]:
    """Gets Custom Deployment Expression Variables

    Args:
        body (CustomDeploymentYamlRequestDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOCustomDeploymentVariableResponseDTO]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CustomDeploymentYamlRequestDTO,
) -> Error | Failure | ResponseDTOCustomDeploymentVariableResponseDTO | None:
    """Gets Custom Deployment Expression Variables

    Args:
        body (CustomDeploymentYamlRequestDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOCustomDeploymentVariableResponseDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
