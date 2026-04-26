from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.count_pull_req_space_review_decision_item import CountPullReqSpaceReviewDecisionItem
from ...models.count_pull_req_space_state_item import CountPullReqSpaceStateItem
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    state: list[CountPullReqSpaceStateItem] | Unset = UNSET,
    source_repo_ref: str | Unset = UNSET,
    source_branch: str | Unset = UNSET,
    target_branch: str | Unset = UNSET,
    query: str | Unset = UNSET,
    created_by: list[int] | Unset = UNSET,
    created_lt: int | Unset = UNSET,
    created_gt: int | Unset = UNSET,
    updated_lt: int | Unset = UNSET,
    include_subspaces: bool | Unset = False,
    label_id: list[int] | Unset = UNSET,
    value_id: list[int] | Unset = UNSET,
    author_id: int | Unset = UNSET,
    commenter_id: int | Unset = UNSET,
    mentioned_id: int | Unset = UNSET,
    reviewer_id: int | Unset = UNSET,
    review_decision: list[CountPullReqSpaceReviewDecisionItem] | Unset = UNSET,
    include_rules: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    params["source_repo_ref"] = source_repo_ref

    params["source_branch"] = source_branch

    params["target_branch"] = target_branch

    params["query"] = query

    json_created_by: list[int] | Unset = UNSET
    if not isinstance(created_by, Unset):
        json_created_by = created_by

    params["created_by"] = json_created_by

    params["created_lt"] = created_lt

    params["created_gt"] = created_gt

    params["updated_lt"] = updated_lt

    params["include_subspaces"] = include_subspaces

    json_label_id: list[int] | Unset = UNSET
    if not isinstance(label_id, Unset):
        json_label_id = label_id

    params["label_id"] = json_label_id

    json_value_id: list[int] | Unset = UNSET
    if not isinstance(value_id, Unset):
        json_value_id = value_id

    params["value_id"] = json_value_id

    params["author_id"] = author_id

    params["commenter_id"] = commenter_id

    params["mentioned_id"] = mentioned_id

    params["reviewer_id"] = reviewer_id

    json_review_decision: list[str] | Unset = UNSET
    if not isinstance(review_decision, Unset):
        json_review_decision = []
        for review_decision_item_data in review_decision:
            review_decision_item = review_decision_item_data.value
            json_review_decision.append(review_decision_item)

    params["review_decision"] = json_review_decision

    params["include_rules"] = include_rules

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pullreq/count",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsererrorError | int | None:
    if response.status_code == 200:
        response_200 = cast(int, response.json())
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
) -> Response[UsererrorError | int]:
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
    state: list[CountPullReqSpaceStateItem] | Unset = UNSET,
    source_repo_ref: str | Unset = UNSET,
    source_branch: str | Unset = UNSET,
    target_branch: str | Unset = UNSET,
    query: str | Unset = UNSET,
    created_by: list[int] | Unset = UNSET,
    created_lt: int | Unset = UNSET,
    created_gt: int | Unset = UNSET,
    updated_lt: int | Unset = UNSET,
    include_subspaces: bool | Unset = False,
    label_id: list[int] | Unset = UNSET,
    value_id: list[int] | Unset = UNSET,
    author_id: int | Unset = UNSET,
    commenter_id: int | Unset = UNSET,
    mentioned_id: int | Unset = UNSET,
    reviewer_id: int | Unset = UNSET,
    review_decision: list[CountPullReqSpaceReviewDecisionItem] | Unset = UNSET,
    include_rules: bool | Unset = False,
) -> Response[UsererrorError | int]:
    """Count pull requests in account/org/project

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        state (list[CountPullReqSpaceStateItem] | Unset):
        source_repo_ref (str | Unset):
        source_branch (str | Unset):
        target_branch (str | Unset):
        query (str | Unset):
        created_by (list[int] | Unset):
        created_lt (int | Unset):
        created_gt (int | Unset):
        updated_lt (int | Unset):
        include_subspaces (bool | Unset):  Default: False.
        label_id (list[int] | Unset):
        value_id (list[int] | Unset):
        author_id (int | Unset):
        commenter_id (int | Unset):
        mentioned_id (int | Unset):
        reviewer_id (int | Unset):
        review_decision (list[CountPullReqSpaceReviewDecisionItem] | Unset):
        include_rules (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | int]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        state=state,
        source_repo_ref=source_repo_ref,
        source_branch=source_branch,
        target_branch=target_branch,
        query=query,
        created_by=created_by,
        created_lt=created_lt,
        created_gt=created_gt,
        updated_lt=updated_lt,
        include_subspaces=include_subspaces,
        label_id=label_id,
        value_id=value_id,
        author_id=author_id,
        commenter_id=commenter_id,
        mentioned_id=mentioned_id,
        reviewer_id=reviewer_id,
        review_decision=review_decision,
        include_rules=include_rules,
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
    state: list[CountPullReqSpaceStateItem] | Unset = UNSET,
    source_repo_ref: str | Unset = UNSET,
    source_branch: str | Unset = UNSET,
    target_branch: str | Unset = UNSET,
    query: str | Unset = UNSET,
    created_by: list[int] | Unset = UNSET,
    created_lt: int | Unset = UNSET,
    created_gt: int | Unset = UNSET,
    updated_lt: int | Unset = UNSET,
    include_subspaces: bool | Unset = False,
    label_id: list[int] | Unset = UNSET,
    value_id: list[int] | Unset = UNSET,
    author_id: int | Unset = UNSET,
    commenter_id: int | Unset = UNSET,
    mentioned_id: int | Unset = UNSET,
    reviewer_id: int | Unset = UNSET,
    review_decision: list[CountPullReqSpaceReviewDecisionItem] | Unset = UNSET,
    include_rules: bool | Unset = False,
) -> UsererrorError | int | None:
    """Count pull requests in account/org/project

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        state (list[CountPullReqSpaceStateItem] | Unset):
        source_repo_ref (str | Unset):
        source_branch (str | Unset):
        target_branch (str | Unset):
        query (str | Unset):
        created_by (list[int] | Unset):
        created_lt (int | Unset):
        created_gt (int | Unset):
        updated_lt (int | Unset):
        include_subspaces (bool | Unset):  Default: False.
        label_id (list[int] | Unset):
        value_id (list[int] | Unset):
        author_id (int | Unset):
        commenter_id (int | Unset):
        mentioned_id (int | Unset):
        reviewer_id (int | Unset):
        review_decision (list[CountPullReqSpaceReviewDecisionItem] | Unset):
        include_rules (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | int
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        state=state,
        source_repo_ref=source_repo_ref,
        source_branch=source_branch,
        target_branch=target_branch,
        query=query,
        created_by=created_by,
        created_lt=created_lt,
        created_gt=created_gt,
        updated_lt=updated_lt,
        include_subspaces=include_subspaces,
        label_id=label_id,
        value_id=value_id,
        author_id=author_id,
        commenter_id=commenter_id,
        mentioned_id=mentioned_id,
        reviewer_id=reviewer_id,
        review_decision=review_decision,
        include_rules=include_rules,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    state: list[CountPullReqSpaceStateItem] | Unset = UNSET,
    source_repo_ref: str | Unset = UNSET,
    source_branch: str | Unset = UNSET,
    target_branch: str | Unset = UNSET,
    query: str | Unset = UNSET,
    created_by: list[int] | Unset = UNSET,
    created_lt: int | Unset = UNSET,
    created_gt: int | Unset = UNSET,
    updated_lt: int | Unset = UNSET,
    include_subspaces: bool | Unset = False,
    label_id: list[int] | Unset = UNSET,
    value_id: list[int] | Unset = UNSET,
    author_id: int | Unset = UNSET,
    commenter_id: int | Unset = UNSET,
    mentioned_id: int | Unset = UNSET,
    reviewer_id: int | Unset = UNSET,
    review_decision: list[CountPullReqSpaceReviewDecisionItem] | Unset = UNSET,
    include_rules: bool | Unset = False,
) -> Response[UsererrorError | int]:
    """Count pull requests in account/org/project

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        state (list[CountPullReqSpaceStateItem] | Unset):
        source_repo_ref (str | Unset):
        source_branch (str | Unset):
        target_branch (str | Unset):
        query (str | Unset):
        created_by (list[int] | Unset):
        created_lt (int | Unset):
        created_gt (int | Unset):
        updated_lt (int | Unset):
        include_subspaces (bool | Unset):  Default: False.
        label_id (list[int] | Unset):
        value_id (list[int] | Unset):
        author_id (int | Unset):
        commenter_id (int | Unset):
        mentioned_id (int | Unset):
        reviewer_id (int | Unset):
        review_decision (list[CountPullReqSpaceReviewDecisionItem] | Unset):
        include_rules (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | int]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        state=state,
        source_repo_ref=source_repo_ref,
        source_branch=source_branch,
        target_branch=target_branch,
        query=query,
        created_by=created_by,
        created_lt=created_lt,
        created_gt=created_gt,
        updated_lt=updated_lt,
        include_subspaces=include_subspaces,
        label_id=label_id,
        value_id=value_id,
        author_id=author_id,
        commenter_id=commenter_id,
        mentioned_id=mentioned_id,
        reviewer_id=reviewer_id,
        review_decision=review_decision,
        include_rules=include_rules,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    state: list[CountPullReqSpaceStateItem] | Unset = UNSET,
    source_repo_ref: str | Unset = UNSET,
    source_branch: str | Unset = UNSET,
    target_branch: str | Unset = UNSET,
    query: str | Unset = UNSET,
    created_by: list[int] | Unset = UNSET,
    created_lt: int | Unset = UNSET,
    created_gt: int | Unset = UNSET,
    updated_lt: int | Unset = UNSET,
    include_subspaces: bool | Unset = False,
    label_id: list[int] | Unset = UNSET,
    value_id: list[int] | Unset = UNSET,
    author_id: int | Unset = UNSET,
    commenter_id: int | Unset = UNSET,
    mentioned_id: int | Unset = UNSET,
    reviewer_id: int | Unset = UNSET,
    review_decision: list[CountPullReqSpaceReviewDecisionItem] | Unset = UNSET,
    include_rules: bool | Unset = False,
) -> UsererrorError | int | None:
    """Count pull requests in account/org/project

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        state (list[CountPullReqSpaceStateItem] | Unset):
        source_repo_ref (str | Unset):
        source_branch (str | Unset):
        target_branch (str | Unset):
        query (str | Unset):
        created_by (list[int] | Unset):
        created_lt (int | Unset):
        created_gt (int | Unset):
        updated_lt (int | Unset):
        include_subspaces (bool | Unset):  Default: False.
        label_id (list[int] | Unset):
        value_id (list[int] | Unset):
        author_id (int | Unset):
        commenter_id (int | Unset):
        mentioned_id (int | Unset):
        reviewer_id (int | Unset):
        review_decision (list[CountPullReqSpaceReviewDecisionItem] | Unset):
        include_rules (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | int
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            state=state,
            source_repo_ref=source_repo_ref,
            source_branch=source_branch,
            target_branch=target_branch,
            query=query,
            created_by=created_by,
            created_lt=created_lt,
            created_gt=created_gt,
            updated_lt=updated_lt,
            include_subspaces=include_subspaces,
            label_id=label_id,
            value_id=value_id,
            author_id=author_id,
            commenter_id=commenter_id,
            mentioned_id=mentioned_id,
            reviewer_id=reviewer_id,
            review_decision=review_decision,
            include_rules=include_rules,
        )
    ).parsed
