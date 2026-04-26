from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.types_label_value import TypesLabelValue
from ...models.update_space_label_value_body import UpdateSpaceLabelValueBody
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key: str,
    value: str,
    *,
    body: UpdateSpaceLabelValueBody | Unset = UNSET,
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
        "method": "patch",
        "url": "/labels/{key}/values/{value}".format(
            key=quote(str(key), safe=""),
            value=quote(str(value), safe=""),
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
) -> TypesLabelValue | UsererrorError | None:
    if response.status_code == 200:
        response_200 = TypesLabelValue.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UsererrorError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsererrorError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsererrorError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsererrorError.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UsererrorError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TypesLabelValue | UsererrorError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    value: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSpaceLabelValueBody | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[TypesLabelValue | UsererrorError]:
    """Update label value at account, org or project level

    Args:
        key (str):
        value (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (UpdateSpaceLabelValueBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesLabelValue | UsererrorError]
    """

    kwargs = _get_kwargs(
        key=key,
        value=value,
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
    key: str,
    value: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSpaceLabelValueBody | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> TypesLabelValue | UsererrorError | None:
    """Update label value at account, org or project level

    Args:
        key (str):
        value (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (UpdateSpaceLabelValueBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesLabelValue | UsererrorError
    """

    return sync_detailed(
        key=key,
        value=value,
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    key: str,
    value: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSpaceLabelValueBody | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[TypesLabelValue | UsererrorError]:
    """Update label value at account, org or project level

    Args:
        key (str):
        value (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (UpdateSpaceLabelValueBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesLabelValue | UsererrorError]
    """

    kwargs = _get_kwargs(
        key=key,
        value=value,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key: str,
    value: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSpaceLabelValueBody | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> TypesLabelValue | UsererrorError | None:
    """Update label value at account, org or project level

    Args:
        key (str):
        value (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (UpdateSpaceLabelValueBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesLabelValue | UsererrorError
    """

    return (
        await asyncio_detailed(
            key=key,
            value=value,
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
        )
    ).parsed
