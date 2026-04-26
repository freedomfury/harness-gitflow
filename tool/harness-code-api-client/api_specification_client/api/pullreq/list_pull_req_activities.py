from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_pull_req_activities_kind_item import ListPullReqActivitiesKindItem
from ...models.list_pull_req_activities_type_item import ListPullReqActivitiesTypeItem
from ...models.types_pull_req_activity import TypesPullReqActivity
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_identifier: str,
    pullreq_number: int,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    kind: list[ListPullReqActivitiesKindItem] | Unset = UNSET,
    type_: list[ListPullReqActivitiesTypeItem] | Unset = UNSET,
    after: int | Unset = UNSET,
    before: int | Unset = UNSET,
    limit: int | Unset = 30,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item = kind_item_data.value
            json_kind.append(kind_item)

    params["kind"] = json_kind

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)

    params["type"] = json_type_

    params["after"] = after

    params["before"] = before

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repos/{repo_identifier}/pullreq/{pullreq_number}/activities".format(
            repo_identifier=quote(str(repo_identifier), safe=""),
            pullreq_number=quote(str(pullreq_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UsererrorError | list[TypesPullReqActivity] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TypesPullReqActivity.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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

    if response.status_code == 500:
        response_500 = UsererrorError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UsererrorError | list[TypesPullReqActivity]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repo_identifier: str,
    pullreq_number: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    kind: list[ListPullReqActivitiesKindItem] | Unset = UNSET,
    type_: list[ListPullReqActivitiesTypeItem] | Unset = UNSET,
    after: int | Unset = UNSET,
    before: int | Unset = UNSET,
    limit: int | Unset = 30,
) -> Response[UsererrorError | list[TypesPullReqActivity]]:
    """List activities

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        kind (list[ListPullReqActivitiesKindItem] | Unset):
        type_ (list[ListPullReqActivitiesTypeItem] | Unset):
        after (int | Unset):
        before (int | Unset):
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[TypesPullReqActivity]]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        pullreq_number=pullreq_number,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        kind=kind,
        type_=type_,
        after=after,
        before=before,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repo_identifier: str,
    pullreq_number: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    kind: list[ListPullReqActivitiesKindItem] | Unset = UNSET,
    type_: list[ListPullReqActivitiesTypeItem] | Unset = UNSET,
    after: int | Unset = UNSET,
    before: int | Unset = UNSET,
    limit: int | Unset = 30,
) -> UsererrorError | list[TypesPullReqActivity] | None:
    """List activities

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        kind (list[ListPullReqActivitiesKindItem] | Unset):
        type_ (list[ListPullReqActivitiesTypeItem] | Unset):
        after (int | Unset):
        before (int | Unset):
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[TypesPullReqActivity]
    """

    return sync_detailed(
        repo_identifier=repo_identifier,
        pullreq_number=pullreq_number,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        kind=kind,
        type_=type_,
        after=after,
        before=before,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    repo_identifier: str,
    pullreq_number: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    kind: list[ListPullReqActivitiesKindItem] | Unset = UNSET,
    type_: list[ListPullReqActivitiesTypeItem] | Unset = UNSET,
    after: int | Unset = UNSET,
    before: int | Unset = UNSET,
    limit: int | Unset = 30,
) -> Response[UsererrorError | list[TypesPullReqActivity]]:
    """List activities

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        kind (list[ListPullReqActivitiesKindItem] | Unset):
        type_ (list[ListPullReqActivitiesTypeItem] | Unset):
        after (int | Unset):
        before (int | Unset):
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[TypesPullReqActivity]]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        pullreq_number=pullreq_number,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        kind=kind,
        type_=type_,
        after=after,
        before=before,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repo_identifier: str,
    pullreq_number: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    kind: list[ListPullReqActivitiesKindItem] | Unset = UNSET,
    type_: list[ListPullReqActivitiesTypeItem] | Unset = UNSET,
    after: int | Unset = UNSET,
    before: int | Unset = UNSET,
    limit: int | Unset = 30,
) -> UsererrorError | list[TypesPullReqActivity] | None:
    """List activities

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        kind (list[ListPullReqActivitiesKindItem] | Unset):
        type_ (list[ListPullReqActivitiesTypeItem] | Unset):
        after (int | Unset):
        before (int | Unset):
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[TypesPullReqActivity]
    """

    return (
        await asyncio_detailed(
            repo_identifier=repo_identifier,
            pullreq_number=pullreq_number,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            kind=kind,
            type_=type_,
            after=after,
            before=before,
            limit=limit,
        )
    ).parsed
