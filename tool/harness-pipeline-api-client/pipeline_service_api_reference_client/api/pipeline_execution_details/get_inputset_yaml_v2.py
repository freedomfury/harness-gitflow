from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_inputset_yaml_v2_resolve_expressions_type import (
    GetInputsetYamlV2ResolveExpressionsType,
)
from ...models.response_dto_input_set_template_response import ResponseDTOInputSetTemplateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    plan_execution_id: str,
    *,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    resolve_expressions: bool | Unset = False,
    resolve_expressions_type: GetInputsetYamlV2ResolveExpressionsType | Unset = "UNKNOWN",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["resolveExpressions"] = resolve_expressions

    json_resolve_expressions_type: str | Unset = UNSET
    if not isinstance(resolve_expressions_type, Unset):
        json_resolve_expressions_type = resolve_expressions_type

    params["resolveExpressionsType"] = json_resolve_expressions_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pipelines/execution/{plan_execution_id}/inputsetV2".format(
            plan_execution_id=quote(str(plan_execution_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOInputSetTemplateResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOInputSetTemplateResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOInputSetTemplateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plan_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    resolve_expressions: bool | Unset = False,
    resolve_expressions_type: GetInputsetYamlV2ResolveExpressionsType | Unset = "UNKNOWN",
) -> Response[Error | Failure | ResponseDTOInputSetTemplateResponse]:
    """Get the Input Set YAML used for given Plan Execution

    Args:
        plan_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        resolve_expressions (bool | Unset):  Default: False.
        resolve_expressions_type (GetInputsetYamlV2ResolveExpressionsType | Unset):  Default:
            'UNKNOWN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOInputSetTemplateResponse]
    """

    kwargs = _get_kwargs(
        plan_execution_id=plan_execution_id,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        resolve_expressions=resolve_expressions,
        resolve_expressions_type=resolve_expressions_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    plan_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    resolve_expressions: bool | Unset = False,
    resolve_expressions_type: GetInputsetYamlV2ResolveExpressionsType | Unset = "UNKNOWN",
) -> Error | Failure | ResponseDTOInputSetTemplateResponse | None:
    """Get the Input Set YAML used for given Plan Execution

    Args:
        plan_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        resolve_expressions (bool | Unset):  Default: False.
        resolve_expressions_type (GetInputsetYamlV2ResolveExpressionsType | Unset):  Default:
            'UNKNOWN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOInputSetTemplateResponse
    """

    return sync_detailed(
        plan_execution_id=plan_execution_id,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        resolve_expressions=resolve_expressions,
        resolve_expressions_type=resolve_expressions_type,
    ).parsed


async def asyncio_detailed(
    plan_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    resolve_expressions: bool | Unset = False,
    resolve_expressions_type: GetInputsetYamlV2ResolveExpressionsType | Unset = "UNKNOWN",
) -> Response[Error | Failure | ResponseDTOInputSetTemplateResponse]:
    """Get the Input Set YAML used for given Plan Execution

    Args:
        plan_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        resolve_expressions (bool | Unset):  Default: False.
        resolve_expressions_type (GetInputsetYamlV2ResolveExpressionsType | Unset):  Default:
            'UNKNOWN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOInputSetTemplateResponse]
    """

    kwargs = _get_kwargs(
        plan_execution_id=plan_execution_id,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        resolve_expressions=resolve_expressions,
        resolve_expressions_type=resolve_expressions_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plan_execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    resolve_expressions: bool | Unset = False,
    resolve_expressions_type: GetInputsetYamlV2ResolveExpressionsType | Unset = "UNKNOWN",
) -> Error | Failure | ResponseDTOInputSetTemplateResponse | None:
    """Get the Input Set YAML used for given Plan Execution

    Args:
        plan_execution_id (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        resolve_expressions (bool | Unset):  Default: False.
        resolve_expressions_type (GetInputsetYamlV2ResolveExpressionsType | Unset):  Default:
            'UNKNOWN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOInputSetTemplateResponse
    """

    return (
        await asyncio_detailed(
            plan_execution_id=plan_execution_id,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            resolve_expressions=resolve_expressions,
            resolve_expressions_type=resolve_expressions_type,
        )
    ).parsed
