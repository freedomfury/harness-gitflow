from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_principals_type_item import ListPrincipalsTypeItem
from ...models.types_principal_info_type_0 import TypesPrincipalInfoType0
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    query: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    type_: list[ListPrincipalsTypeItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["query"] = query

    params["page"] = page

    params["limit"] = limit

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/principals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UsererrorError | list[None | TypesPrincipalInfoType0] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(data: object) -> None | TypesPrincipalInfoType0:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_types_principal_info_type_0 = TypesPrincipalInfoType0.from_dict(data)

                    return componentsschemas_types_principal_info_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(None | TypesPrincipalInfoType0, data)

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = UsererrorError.from_dict(response.json())

        return response_400

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
) -> Response[UsererrorError | list[None | TypesPrincipalInfoType0]]:
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
    query: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    type_: list[ListPrincipalsTypeItem] | Unset = UNSET,
) -> Response[UsererrorError | list[None | TypesPrincipalInfoType0]]:
    """
    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        query (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        type_ (list[ListPrincipalsTypeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[None | TypesPrincipalInfoType0]]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        query=query,
        page=page,
        limit=limit,
        type_=type_,
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
    query: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    type_: list[ListPrincipalsTypeItem] | Unset = UNSET,
) -> UsererrorError | list[None | TypesPrincipalInfoType0] | None:
    """
    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        query (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        type_ (list[ListPrincipalsTypeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[None | TypesPrincipalInfoType0]
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        query=query,
        page=page,
        limit=limit,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    query: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    type_: list[ListPrincipalsTypeItem] | Unset = UNSET,
) -> Response[UsererrorError | list[None | TypesPrincipalInfoType0]]:
    """
    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        query (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        type_ (list[ListPrincipalsTypeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[None | TypesPrincipalInfoType0]]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        query=query,
        page=page,
        limit=limit,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    query: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    type_: list[ListPrincipalsTypeItem] | Unset = UNSET,
) -> UsererrorError | list[None | TypesPrincipalInfoType0] | None:
    """
    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        query (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        type_ (list[ListPrincipalsTypeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[None | TypesPrincipalInfoType0]
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            query=query,
            page=page,
            limit=limit,
            type_=type_,
        )
    ).parsed
