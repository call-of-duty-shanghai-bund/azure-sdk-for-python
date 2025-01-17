# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AzureAsyncOperationResult
from ._models_py3 import Backend
from ._models_py3 import BackendPool
from ._models_py3 import BackendPoolListResult
from ._models_py3 import BackendPoolProperties
from ._models_py3 import BackendPoolUpdateParameters
from ._models_py3 import BackendPoolsSettings
from ._models_py3 import CacheConfiguration
from ._models_py3 import CheckNameAvailabilityInput
from ._models_py3 import CheckNameAvailabilityOutput
from ._models_py3 import CustomHttpsConfiguration
from ._models_py3 import CustomRule
from ._models_py3 import CustomRuleList
from ._models_py3 import Endpoint
from ._models_py3 import Error
from ._models_py3 import ErrorDetails
from ._models_py3 import ErrorResponse
from ._models_py3 import Experiment
from ._models_py3 import ExperimentList
from ._models_py3 import ExperimentUpdateModel
from ._models_py3 import ForwardingConfiguration
from ._models_py3 import FrontDoor
from ._models_py3 import FrontDoorListResult
from ._models_py3 import FrontDoorProperties
from ._models_py3 import FrontDoorUpdateParameters
from ._models_py3 import FrontendEndpoint
from ._models_py3 import FrontendEndpointLink
from ._models_py3 import FrontendEndpointProperties
from ._models_py3 import FrontendEndpointUpdateParameters
from ._models_py3 import FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLink
from ._models_py3 import FrontendEndpointsListResult
from ._models_py3 import HeaderAction
from ._models_py3 import HealthProbeSettingsListResult
from ._models_py3 import HealthProbeSettingsModel
from ._models_py3 import HealthProbeSettingsProperties
from ._models_py3 import HealthProbeSettingsUpdateParameters
from ._models_py3 import KeyVaultCertificateSourceParametersVault
from ._models_py3 import LatencyMetric
from ._models_py3 import LatencyScorecard
from ._models_py3 import LoadBalancingSettingsListResult
from ._models_py3 import LoadBalancingSettingsModel
from ._models_py3 import LoadBalancingSettingsProperties
from ._models_py3 import LoadBalancingSettingsUpdateParameters
from ._models_py3 import ManagedRuleDefinition
from ._models_py3 import ManagedRuleExclusion
from ._models_py3 import ManagedRuleGroupDefinition
from ._models_py3 import ManagedRuleGroupOverride
from ._models_py3 import ManagedRuleOverride
from ._models_py3 import ManagedRuleSet
from ._models_py3 import ManagedRuleSetDefinition
from ._models_py3 import ManagedRuleSetDefinitionList
from ._models_py3 import ManagedRuleSetList
from ._models_py3 import MatchCondition
from ._models_py3 import PolicySettings
from ._models_py3 import PreconfiguredEndpoint
from ._models_py3 import PreconfiguredEndpointList
from ._models_py3 import Profile
from ._models_py3 import ProfileList
from ._models_py3 import ProfileUpdateModel
from ._models_py3 import PurgeParameters
from ._models_py3 import RedirectConfiguration
from ._models_py3 import Resource
from ._models_py3 import RouteConfiguration
from ._models_py3 import RoutingRule
from ._models_py3 import RoutingRuleLink
from ._models_py3 import RoutingRuleListResult
from ._models_py3 import RoutingRuleProperties
from ._models_py3 import RoutingRuleUpdateParameters
from ._models_py3 import RoutingRuleUpdateParametersWebApplicationFirewallPolicyLink
from ._models_py3 import RulesEngine
from ._models_py3 import RulesEngineAction
from ._models_py3 import RulesEngineListResult
from ._models_py3 import RulesEngineMatchCondition
from ._models_py3 import RulesEngineProperties
from ._models_py3 import RulesEngineRule
from ._models_py3 import RulesEngineUpdateParameters
from ._models_py3 import SecurityPolicyLink
from ._models_py3 import Sku
from ._models_py3 import SubResource
from ._models_py3 import TagsObject
from ._models_py3 import Timeseries
from ._models_py3 import TimeseriesDataPoint
from ._models_py3 import ValidateCustomDomainInput
from ._models_py3 import ValidateCustomDomainOutput
from ._models_py3 import WebApplicationFirewallPolicy
from ._models_py3 import WebApplicationFirewallPolicyList

from ._front_door_management_client_enums import ActionType
from ._front_door_management_client_enums import AggregationInterval
from ._front_door_management_client_enums import Availability
from ._front_door_management_client_enums import BackendEnabledState
from ._front_door_management_client_enums import CustomHttpsProvisioningState
from ._front_door_management_client_enums import CustomHttpsProvisioningSubstate
from ._front_door_management_client_enums import CustomRuleEnabledState
from ._front_door_management_client_enums import DynamicCompressionEnabled
from ._front_door_management_client_enums import EndpointType
from ._front_door_management_client_enums import EnforceCertificateNameCheckEnabledState
from ._front_door_management_client_enums import FrontDoorCertificateSource
from ._front_door_management_client_enums import FrontDoorCertificateType
from ._front_door_management_client_enums import FrontDoorEnabledState
from ._front_door_management_client_enums import FrontDoorForwardingProtocol
from ._front_door_management_client_enums import FrontDoorHealthProbeMethod
from ._front_door_management_client_enums import FrontDoorProtocol
from ._front_door_management_client_enums import FrontDoorQuery
from ._front_door_management_client_enums import FrontDoorRedirectProtocol
from ._front_door_management_client_enums import FrontDoorRedirectType
from ._front_door_management_client_enums import FrontDoorResourceState
from ._front_door_management_client_enums import FrontDoorTlsProtocolType
from ._front_door_management_client_enums import HeaderActionType
from ._front_door_management_client_enums import HealthProbeEnabled
from ._front_door_management_client_enums import LatencyScorecardAggregationInterval
from ._front_door_management_client_enums import ManagedRuleEnabledState
from ._front_door_management_client_enums import ManagedRuleExclusionMatchVariable
from ._front_door_management_client_enums import ManagedRuleExclusionSelectorMatchOperator
from ._front_door_management_client_enums import ManagedRuleSetActionType
from ._front_door_management_client_enums import MatchProcessingBehavior
from ._front_door_management_client_enums import MatchVariable
from ._front_door_management_client_enums import MinimumTLSVersion
from ._front_door_management_client_enums import NetworkExperimentResourceState
from ._front_door_management_client_enums import NetworkOperationStatus
from ._front_door_management_client_enums import Operator
from ._front_door_management_client_enums import PolicyEnabledState
from ._front_door_management_client_enums import PolicyMode
from ._front_door_management_client_enums import PolicyRequestBodyCheck
from ._front_door_management_client_enums import PolicyResourceState
from ._front_door_management_client_enums import PrivateEndpointStatus
from ._front_door_management_client_enums import ResourceType
from ._front_door_management_client_enums import RoutingRuleEnabledState
from ._front_door_management_client_enums import RuleType
from ._front_door_management_client_enums import RulesEngineMatchVariable
from ._front_door_management_client_enums import RulesEngineOperator
from ._front_door_management_client_enums import SessionAffinityEnabledState
from ._front_door_management_client_enums import SkuName
from ._front_door_management_client_enums import State
from ._front_door_management_client_enums import TimeseriesAggregationInterval
from ._front_door_management_client_enums import TimeseriesType
from ._front_door_management_client_enums import Transform
from ._front_door_management_client_enums import TransformType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AzureAsyncOperationResult",
    "Backend",
    "BackendPool",
    "BackendPoolListResult",
    "BackendPoolProperties",
    "BackendPoolUpdateParameters",
    "BackendPoolsSettings",
    "CacheConfiguration",
    "CheckNameAvailabilityInput",
    "CheckNameAvailabilityOutput",
    "CustomHttpsConfiguration",
    "CustomRule",
    "CustomRuleList",
    "Endpoint",
    "Error",
    "ErrorDetails",
    "ErrorResponse",
    "Experiment",
    "ExperimentList",
    "ExperimentUpdateModel",
    "ForwardingConfiguration",
    "FrontDoor",
    "FrontDoorListResult",
    "FrontDoorProperties",
    "FrontDoorUpdateParameters",
    "FrontendEndpoint",
    "FrontendEndpointLink",
    "FrontendEndpointProperties",
    "FrontendEndpointUpdateParameters",
    "FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLink",
    "FrontendEndpointsListResult",
    "HeaderAction",
    "HealthProbeSettingsListResult",
    "HealthProbeSettingsModel",
    "HealthProbeSettingsProperties",
    "HealthProbeSettingsUpdateParameters",
    "KeyVaultCertificateSourceParametersVault",
    "LatencyMetric",
    "LatencyScorecard",
    "LoadBalancingSettingsListResult",
    "LoadBalancingSettingsModel",
    "LoadBalancingSettingsProperties",
    "LoadBalancingSettingsUpdateParameters",
    "ManagedRuleDefinition",
    "ManagedRuleExclusion",
    "ManagedRuleGroupDefinition",
    "ManagedRuleGroupOverride",
    "ManagedRuleOverride",
    "ManagedRuleSet",
    "ManagedRuleSetDefinition",
    "ManagedRuleSetDefinitionList",
    "ManagedRuleSetList",
    "MatchCondition",
    "PolicySettings",
    "PreconfiguredEndpoint",
    "PreconfiguredEndpointList",
    "Profile",
    "ProfileList",
    "ProfileUpdateModel",
    "PurgeParameters",
    "RedirectConfiguration",
    "Resource",
    "RouteConfiguration",
    "RoutingRule",
    "RoutingRuleLink",
    "RoutingRuleListResult",
    "RoutingRuleProperties",
    "RoutingRuleUpdateParameters",
    "RoutingRuleUpdateParametersWebApplicationFirewallPolicyLink",
    "RulesEngine",
    "RulesEngineAction",
    "RulesEngineListResult",
    "RulesEngineMatchCondition",
    "RulesEngineProperties",
    "RulesEngineRule",
    "RulesEngineUpdateParameters",
    "SecurityPolicyLink",
    "Sku",
    "SubResource",
    "TagsObject",
    "Timeseries",
    "TimeseriesDataPoint",
    "ValidateCustomDomainInput",
    "ValidateCustomDomainOutput",
    "WebApplicationFirewallPolicy",
    "WebApplicationFirewallPolicyList",
    "ActionType",
    "AggregationInterval",
    "Availability",
    "BackendEnabledState",
    "CustomHttpsProvisioningState",
    "CustomHttpsProvisioningSubstate",
    "CustomRuleEnabledState",
    "DynamicCompressionEnabled",
    "EndpointType",
    "EnforceCertificateNameCheckEnabledState",
    "FrontDoorCertificateSource",
    "FrontDoorCertificateType",
    "FrontDoorEnabledState",
    "FrontDoorForwardingProtocol",
    "FrontDoorHealthProbeMethod",
    "FrontDoorProtocol",
    "FrontDoorQuery",
    "FrontDoorRedirectProtocol",
    "FrontDoorRedirectType",
    "FrontDoorResourceState",
    "FrontDoorTlsProtocolType",
    "HeaderActionType",
    "HealthProbeEnabled",
    "LatencyScorecardAggregationInterval",
    "ManagedRuleEnabledState",
    "ManagedRuleExclusionMatchVariable",
    "ManagedRuleExclusionSelectorMatchOperator",
    "ManagedRuleSetActionType",
    "MatchProcessingBehavior",
    "MatchVariable",
    "MinimumTLSVersion",
    "NetworkExperimentResourceState",
    "NetworkOperationStatus",
    "Operator",
    "PolicyEnabledState",
    "PolicyMode",
    "PolicyRequestBodyCheck",
    "PolicyResourceState",
    "PrivateEndpointStatus",
    "ResourceType",
    "RoutingRuleEnabledState",
    "RuleType",
    "RulesEngineMatchVariable",
    "RulesEngineOperator",
    "SessionAffinityEnabledState",
    "SkuName",
    "State",
    "TimeseriesAggregationInterval",
    "TimeseriesType",
    "Transform",
    "TransformType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
