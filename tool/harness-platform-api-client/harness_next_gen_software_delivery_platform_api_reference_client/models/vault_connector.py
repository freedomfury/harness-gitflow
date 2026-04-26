from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vault_connector_access_type import VaultConnectorAccessType, check_vault_connector_access_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="VaultConnector")


@_attrs_define
class VaultConnector:
    """This contains the Vault Connector configuration.

    Attributes:
        connector_type (str):
        vault_url (str): URL of the HashiCorp Vault.
        renewal_interval_minutes (int): This is the time interval for token renewal.
        auth_token (str | Unset): This is the authentication token for Vault.
        base_path (str | Unset): This is the location of the Vault directory where Secret will be stored.
        secret_engine_manually_configured (bool | Unset): Manually entered Secret Engine.
        secret_engine_name (str | Unset): Name of the Secret Engine.
        app_role_id (str | Unset): ID of App Role.
        app_role_path (str | Unset): Custom Path to the App Role
        secret_id (str | Unset): ID of the Secret.
        secret_engine_version (int | Unset): Version of Secret Engine.
        delegate_selectors (list[str] | Unset): List of Delegate Selectors that belong to the same Delegate and are used
            to connect to the Secret Manager.
        namespace (str | Unset): This is the Vault namespace where Secret will be created.
        sink_path (str | Unset): This is the location at which auth token is to be read from.
        use_vault_agent (bool | Unset): Boolean value to indicate if Vault Agent is used for authentication.
        use_aws_iam (bool | Unset): Boolean value to indicate if Aws Iam is used for authentication.
        aws_region (str | Unset): This is the Aws region where aws iam auth will happen.
        vault_aws_iam_role (str | Unset): This is the Vault role defined to bind to aws iam account/role being accessed.
        use_k8_s_auth (bool | Unset): Boolean value to indicate if K8s Auth is used for authentication.
        vault_k8_s_auth_role (str | Unset): This is the role where K8s auth will happen.
        service_account_token_path (str | Unset): This is the SA token path where the token is mounted in the K8s Pod.
        k_8_s_auth_endpoint (str | Unset): This is the path where kubernetes auth is enabled in Vault.
        renew_app_role_token (bool | Unset): Boolean value to indicate if appRole token renewal is enabled or not.
        enable_cache (bool | Unset): Boolean value to indicate if cache is enabled for App Role Token.
        ignore_test_connection (bool | Unset):
        use_jwt_auth (bool | Unset): Boolean value to indicate if JWT Auth is used for authentication.
        jwt_auth_role_with_granular_claims (str | Unset): Auth Role
        jwt_auth_role (str | Unset): This is the role name which is created to perform JWT auth method.
        jwt_auth_path (str | Unset): This specifies mount path where JWT auth method is enabled.
        execute_on_delegate (bool | Unset): Should the secret manager execute operations on the delegate, or via Harness
            platform
        proxy (bool | Unset): Whether to use proxy for connecting to Vault server
        access_type (VaultConnectorAccessType | Unset):
        read_only (bool | Unset):
        default (bool | Unset):
        ng_certificate_ref (str | Unset):
        xvault_aws_iam_server_id (str | Unset): This is the Aws Iam Header Server ID that has been configured for this
            Aws Iam instance.
    """

    connector_type: str
    vault_url: str
    renewal_interval_minutes: int
    auth_token: str | Unset = UNSET
    base_path: str | Unset = UNSET
    secret_engine_manually_configured: bool | Unset = UNSET
    secret_engine_name: str | Unset = UNSET
    app_role_id: str | Unset = UNSET
    app_role_path: str | Unset = UNSET
    secret_id: str | Unset = UNSET
    secret_engine_version: int | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    namespace: str | Unset = UNSET
    sink_path: str | Unset = UNSET
    use_vault_agent: bool | Unset = UNSET
    use_aws_iam: bool | Unset = UNSET
    aws_region: str | Unset = UNSET
    vault_aws_iam_role: str | Unset = UNSET
    use_k8_s_auth: bool | Unset = UNSET
    vault_k8_s_auth_role: str | Unset = UNSET
    service_account_token_path: str | Unset = UNSET
    k_8_s_auth_endpoint: str | Unset = UNSET
    renew_app_role_token: bool | Unset = UNSET
    enable_cache: bool | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    use_jwt_auth: bool | Unset = UNSET
    jwt_auth_role_with_granular_claims: str | Unset = UNSET
    jwt_auth_role: str | Unset = UNSET
    jwt_auth_path: str | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    proxy: bool | Unset = UNSET
    access_type: VaultConnectorAccessType | Unset = UNSET
    read_only: bool | Unset = UNSET
    default: bool | Unset = UNSET
    ng_certificate_ref: str | Unset = UNSET
    xvault_aws_iam_server_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        vault_url = self.vault_url

        renewal_interval_minutes = self.renewal_interval_minutes

        auth_token = self.auth_token

        base_path = self.base_path

        secret_engine_manually_configured = self.secret_engine_manually_configured

        secret_engine_name = self.secret_engine_name

        app_role_id = self.app_role_id

        app_role_path = self.app_role_path

        secret_id = self.secret_id

        secret_engine_version = self.secret_engine_version

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        namespace = self.namespace

        sink_path = self.sink_path

        use_vault_agent = self.use_vault_agent

        use_aws_iam = self.use_aws_iam

        aws_region = self.aws_region

        vault_aws_iam_role = self.vault_aws_iam_role

        use_k8_s_auth = self.use_k8_s_auth

        vault_k8_s_auth_role = self.vault_k8_s_auth_role

        service_account_token_path = self.service_account_token_path

        k_8_s_auth_endpoint = self.k_8_s_auth_endpoint

        renew_app_role_token = self.renew_app_role_token

        enable_cache = self.enable_cache

        ignore_test_connection = self.ignore_test_connection

        use_jwt_auth = self.use_jwt_auth

        jwt_auth_role_with_granular_claims = self.jwt_auth_role_with_granular_claims

        jwt_auth_role = self.jwt_auth_role

        jwt_auth_path = self.jwt_auth_path

        execute_on_delegate = self.execute_on_delegate

        proxy = self.proxy

        access_type: str | Unset = UNSET
        if not isinstance(self.access_type, Unset):
            access_type = self.access_type

        read_only = self.read_only

        default = self.default

        ng_certificate_ref = self.ng_certificate_ref

        xvault_aws_iam_server_id = self.xvault_aws_iam_server_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "vaultUrl": vault_url,
                "renewalIntervalMinutes": renewal_interval_minutes,
            }
        )
        if auth_token is not UNSET:
            field_dict["authToken"] = auth_token
        if base_path is not UNSET:
            field_dict["basePath"] = base_path
        if secret_engine_manually_configured is not UNSET:
            field_dict["secretEngineManuallyConfigured"] = secret_engine_manually_configured
        if secret_engine_name is not UNSET:
            field_dict["secretEngineName"] = secret_engine_name
        if app_role_id is not UNSET:
            field_dict["appRoleId"] = app_role_id
        if app_role_path is not UNSET:
            field_dict["appRolePath"] = app_role_path
        if secret_id is not UNSET:
            field_dict["secretId"] = secret_id
        if secret_engine_version is not UNSET:
            field_dict["secretEngineVersion"] = secret_engine_version
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if sink_path is not UNSET:
            field_dict["sinkPath"] = sink_path
        if use_vault_agent is not UNSET:
            field_dict["useVaultAgent"] = use_vault_agent
        if use_aws_iam is not UNSET:
            field_dict["useAwsIam"] = use_aws_iam
        if aws_region is not UNSET:
            field_dict["awsRegion"] = aws_region
        if vault_aws_iam_role is not UNSET:
            field_dict["vaultAwsIamRole"] = vault_aws_iam_role
        if use_k8_s_auth is not UNSET:
            field_dict["useK8sAuth"] = use_k8_s_auth
        if vault_k8_s_auth_role is not UNSET:
            field_dict["vaultK8sAuthRole"] = vault_k8_s_auth_role
        if service_account_token_path is not UNSET:
            field_dict["serviceAccountTokenPath"] = service_account_token_path
        if k_8_s_auth_endpoint is not UNSET:
            field_dict["k8sAuthEndpoint"] = k_8_s_auth_endpoint
        if renew_app_role_token is not UNSET:
            field_dict["renewAppRoleToken"] = renew_app_role_token
        if enable_cache is not UNSET:
            field_dict["enableCache"] = enable_cache
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if use_jwt_auth is not UNSET:
            field_dict["useJwtAuth"] = use_jwt_auth
        if jwt_auth_role_with_granular_claims is not UNSET:
            field_dict["jwtAuthRoleWithGranularClaims"] = jwt_auth_role_with_granular_claims
        if jwt_auth_role is not UNSET:
            field_dict["jwtAuthRole"] = jwt_auth_role
        if jwt_auth_path is not UNSET:
            field_dict["jwtAuthPath"] = jwt_auth_path
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate
        if proxy is not UNSET:
            field_dict["proxy"] = proxy
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if default is not UNSET:
            field_dict["default"] = default
        if ng_certificate_ref is not UNSET:
            field_dict["ngCertificateRef"] = ng_certificate_ref
        if xvault_aws_iam_server_id is not UNSET:
            field_dict["xvaultAwsIamServerId"] = xvault_aws_iam_server_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        vault_url = d.pop("vaultUrl")

        renewal_interval_minutes = d.pop("renewalIntervalMinutes")

        auth_token = d.pop("authToken", UNSET)

        base_path = d.pop("basePath", UNSET)

        secret_engine_manually_configured = d.pop("secretEngineManuallyConfigured", UNSET)

        secret_engine_name = d.pop("secretEngineName", UNSET)

        app_role_id = d.pop("appRoleId", UNSET)

        app_role_path = d.pop("appRolePath", UNSET)

        secret_id = d.pop("secretId", UNSET)

        secret_engine_version = d.pop("secretEngineVersion", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        namespace = d.pop("namespace", UNSET)

        sink_path = d.pop("sinkPath", UNSET)

        use_vault_agent = d.pop("useVaultAgent", UNSET)

        use_aws_iam = d.pop("useAwsIam", UNSET)

        aws_region = d.pop("awsRegion", UNSET)

        vault_aws_iam_role = d.pop("vaultAwsIamRole", UNSET)

        use_k8_s_auth = d.pop("useK8sAuth", UNSET)

        vault_k8_s_auth_role = d.pop("vaultK8sAuthRole", UNSET)

        service_account_token_path = d.pop("serviceAccountTokenPath", UNSET)

        k_8_s_auth_endpoint = d.pop("k8sAuthEndpoint", UNSET)

        renew_app_role_token = d.pop("renewAppRoleToken", UNSET)

        enable_cache = d.pop("enableCache", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        use_jwt_auth = d.pop("useJwtAuth", UNSET)

        jwt_auth_role_with_granular_claims = d.pop("jwtAuthRoleWithGranularClaims", UNSET)

        jwt_auth_role = d.pop("jwtAuthRole", UNSET)

        jwt_auth_path = d.pop("jwtAuthPath", UNSET)

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        proxy = d.pop("proxy", UNSET)

        _access_type = d.pop("accessType", UNSET)
        access_type: VaultConnectorAccessType | Unset
        if isinstance(_access_type, Unset):
            access_type = UNSET
        else:
            access_type = check_vault_connector_access_type(_access_type)

        read_only = d.pop("readOnly", UNSET)

        default = d.pop("default", UNSET)

        ng_certificate_ref = d.pop("ngCertificateRef", UNSET)

        xvault_aws_iam_server_id = d.pop("xvaultAwsIamServerId", UNSET)

        vault_connector = cls(
            connector_type=connector_type,
            vault_url=vault_url,
            renewal_interval_minutes=renewal_interval_minutes,
            auth_token=auth_token,
            base_path=base_path,
            secret_engine_manually_configured=secret_engine_manually_configured,
            secret_engine_name=secret_engine_name,
            app_role_id=app_role_id,
            app_role_path=app_role_path,
            secret_id=secret_id,
            secret_engine_version=secret_engine_version,
            delegate_selectors=delegate_selectors,
            namespace=namespace,
            sink_path=sink_path,
            use_vault_agent=use_vault_agent,
            use_aws_iam=use_aws_iam,
            aws_region=aws_region,
            vault_aws_iam_role=vault_aws_iam_role,
            use_k8_s_auth=use_k8_s_auth,
            vault_k8_s_auth_role=vault_k8_s_auth_role,
            service_account_token_path=service_account_token_path,
            k_8_s_auth_endpoint=k_8_s_auth_endpoint,
            renew_app_role_token=renew_app_role_token,
            enable_cache=enable_cache,
            ignore_test_connection=ignore_test_connection,
            use_jwt_auth=use_jwt_auth,
            jwt_auth_role_with_granular_claims=jwt_auth_role_with_granular_claims,
            jwt_auth_role=jwt_auth_role,
            jwt_auth_path=jwt_auth_path,
            execute_on_delegate=execute_on_delegate,
            proxy=proxy,
            access_type=access_type,
            read_only=read_only,
            default=default,
            ng_certificate_ref=ng_certificate_ref,
            xvault_aws_iam_server_id=xvault_aws_iam_server_id,
        )

        vault_connector.additional_properties = d
        return vault_connector

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
