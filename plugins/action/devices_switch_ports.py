#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.meraki.plugins.plugin_utils.meraki import (
    MERAKI,
    meraki_argument_spec,
    meraki_compare_equality2,
    get_dict_result,
)
from ansible_collections.cisco.meraki.plugins.plugin_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = meraki_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present"]),
    name=dict(type="str"),
    tags=dict(type="list"),
    enabled=dict(type="bool"),
    poeEnabled=dict(type="bool"),
    type=dict(type="str"),
    vlan=dict(type="int"),
    voiceVlan=dict(type="int"),
    allowedVlans=dict(type="str"),
    isolationEnabled=dict(type="bool"),
    rstpEnabled=dict(type="bool"),
    stpGuard=dict(type="str"),
    linkNegotiation=dict(type="str"),
    portScheduleId=dict(type="str"),
    udld=dict(type="str"),
    accessPolicyType=dict(type="str"),
    accessPolicyNumber=dict(type="int"),
    macAllowList=dict(type="list"),
    stickyMacAllowList=dict(type="list"),
    stickyMacAllowListLimit=dict(type="int"),
    stormControlEnabled=dict(type="bool"),
    adaptivePolicyGroupId=dict(type="str"),
    peerSgtCapable=dict(type="bool"),
    flexibleStackingEnabled=dict(type="bool"),
    daiTrusted=dict(type="bool"),
    profile=dict(type="dict"),
    serial=dict(type="str"),
    portId=dict(type="str"),
))

required_if = [
    ("state", "present", ["name", "portId", "serial"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class DevicesSwitchPorts(object):
    def __init__(self, params, meraki):
        self.meraki = meraki
        self.new_object = dict(
            name=params.get("name"),
            tags=params.get("tags"),
            enabled=params.get("enabled"),
            poeEnabled=params.get("poeEnabled"),
            type=params.get("type"),
            vlan=params.get("vlan"),
            voiceVlan=params.get("voiceVlan"),
            allowedVlans=params.get("allowedVlans"),
            isolationEnabled=params.get("isolationEnabled"),
            rstpEnabled=params.get("rstpEnabled"),
            stpGuard=params.get("stpGuard"),
            linkNegotiation=params.get("linkNegotiation"),
            portScheduleId=params.get("portScheduleId"),
            udld=params.get("udld"),
            accessPolicyType=params.get("accessPolicyType"),
            accessPolicyNumber=params.get("accessPolicyNumber"),
            macAllowList=params.get("macAllowList"),
            stickyMacAllowList=params.get("stickyMacAllowList"),
            stickyMacAllowListLimit=params.get("stickyMacAllowListLimit"),
            stormControlEnabled=params.get("stormControlEnabled"),
            adaptivePolicyGroupId=params.get("adaptivePolicyGroupId"),
            peerSgtCapable=params.get("peerSgtCapable"),
            flexibleStackingEnabled=params.get("flexibleStackingEnabled"),
            daiTrusted=params.get("daiTrusted"),
            profile=params.get("profile"),
            serial=params.get("serial"),
            port_id=params.get("portId"),
        )

    def get_all_params(self, name=None, id=None):
        new_object_params = {}
        if self.new_object.get('serial') is not None or self.new_object.get('serial') is not None:
            new_object_params['serial'] = self.new_object.get('serial')
        return new_object_params

    def get_params_by_id(self, name=None, id=None):
        new_object_params = {}
        if self.new_object.get('serial') is not None or self.new_object.get('serial') is not None:
            new_object_params['serial'] = self.new_object.get('serial')
        if self.new_object.get('portId') is not None or self.new_object.get('port_id') is not None:
            new_object_params['portId'] = self.new_object.get('portId') or \
                self.new_object.get('port_id')
        return new_object_params

    def update_by_id_params(self):
        new_object_params = {}
        if self.new_object.get('name') is not None or self.new_object.get('name') is not None:
            new_object_params['name'] = self.new_object.get('name') or \
                self.new_object.get('name')
        if self.new_object.get('tags') is not None or self.new_object.get('tags') is not None:
            new_object_params['tags'] = self.new_object.get('tags') or \
                self.new_object.get('tags')
        if self.new_object.get('enabled') is not None or self.new_object.get('enabled') is not None:
            new_object_params['enabled'] = self.new_object.get('enabled')
        if self.new_object.get('poeEnabled') is not None or self.new_object.get('poe_enabled') is not None:
            new_object_params['poeEnabled'] = self.new_object.get('poeEnabled')
        if self.new_object.get('type') is not None or self.new_object.get('type') is not None:
            new_object_params['type'] = self.new_object.get('type') or \
                self.new_object.get('type')
        if self.new_object.get('vlan') is not None or self.new_object.get('vlan') is not None:
            new_object_params['vlan'] = self.new_object.get('vlan') or \
                self.new_object.get('vlan')
        if self.new_object.get('voiceVlan') is not None or self.new_object.get('voice_vlan') is not None:
            new_object_params['voiceVlan'] = self.new_object.get('voiceVlan') or \
                self.new_object.get('voice_vlan')
        if self.new_object.get('allowedVlans') is not None or self.new_object.get('allowed_vlans') is not None:
            new_object_params['allowedVlans'] = self.new_object.get('allowedVlans') or \
                self.new_object.get('allowed_vlans')
        if self.new_object.get('isolationEnabled') is not None or self.new_object.get('isolation_enabled') is not None:
            new_object_params['isolationEnabled'] = self.new_object.get('isolationEnabled')
        if self.new_object.get('rstpEnabled') is not None or self.new_object.get('rstp_enabled') is not None:
            new_object_params['rstpEnabled'] = self.new_object.get('rstpEnabled')
        if self.new_object.get('stpGuard') is not None or self.new_object.get('stp_guard') is not None:
            new_object_params['stpGuard'] = self.new_object.get('stpGuard') or \
                self.new_object.get('stp_guard')
        if self.new_object.get('linkNegotiation') is not None or self.new_object.get('link_negotiation') is not None:
            new_object_params['linkNegotiation'] = self.new_object.get('linkNegotiation') or \
                self.new_object.get('link_negotiation')
        if self.new_object.get('portScheduleId') is not None or self.new_object.get('port_schedule_id') is not None:
            new_object_params['portScheduleId'] = self.new_object.get('portScheduleId') or \
                self.new_object.get('port_schedule_id')
        if self.new_object.get('udld') is not None or self.new_object.get('udld') is not None:
            new_object_params['udld'] = self.new_object.get('udld') or \
                self.new_object.get('udld')
        if self.new_object.get('accessPolicyType') is not None or self.new_object.get('access_policy_type') is not None:
            new_object_params['accessPolicyType'] = self.new_object.get('accessPolicyType') or \
                self.new_object.get('access_policy_type')
        if self.new_object.get('accessPolicyNumber') is not None or self.new_object.get('access_policy_number') is not None:
            new_object_params['accessPolicyNumber'] = self.new_object.get('accessPolicyNumber') or \
                self.new_object.get('access_policy_number')
        if self.new_object.get('macAllowList') is not None or self.new_object.get('mac_allow_list') is not None:
            new_object_params['macAllowList'] = self.new_object.get('macAllowList') or \
                self.new_object.get('mac_allow_list')
        if self.new_object.get('stickyMacAllowList') is not None or self.new_object.get('sticky_mac_allow_list') is not None:
            new_object_params['stickyMacAllowList'] = self.new_object.get('stickyMacAllowList') or \
                self.new_object.get('sticky_mac_allow_list')
        if self.new_object.get('stickyMacAllowListLimit') is not None or self.new_object.get('sticky_mac_allow_list_limit') is not None:
            new_object_params['stickyMacAllowListLimit'] = self.new_object.get('stickyMacAllowListLimit') or \
                self.new_object.get('sticky_mac_allow_list_limit')
        if self.new_object.get('stormControlEnabled') is not None or self.new_object.get('storm_control_enabled') is not None:
            new_object_params['stormControlEnabled'] = self.new_object.get('stormControlEnabled')
        if self.new_object.get('adaptivePolicyGroupId') is not None or self.new_object.get('adaptive_policy_group_id') is not None:
            new_object_params['adaptivePolicyGroupId'] = self.new_object.get('adaptivePolicyGroupId') or \
                self.new_object.get('adaptive_policy_group_id')
        if self.new_object.get('peerSgtCapable') is not None or self.new_object.get('peer_sgt_capable') is not None:
            new_object_params['peerSgtCapable'] = self.new_object.get('peerSgtCapable')
        if self.new_object.get('flexibleStackingEnabled') is not None or self.new_object.get('flexible_stacking_enabled') is not None:
            new_object_params['flexibleStackingEnabled'] = self.new_object.get('flexibleStackingEnabled')
        if self.new_object.get('daiTrusted') is not None or self.new_object.get('dai_trusted') is not None:
            new_object_params['daiTrusted'] = self.new_object.get('daiTrusted')
        if self.new_object.get('profile') is not None or self.new_object.get('profile') is not None:
            new_object_params['profile'] = self.new_object.get('profile') or \
                self.new_object.get('profile')
        if self.new_object.get('serial') is not None or self.new_object.get('serial') is not None:
            new_object_params['serial'] = self.new_object.get('serial') or \
                self.new_object.get('serial')
        if self.new_object.get('portId') is not None or self.new_object.get('port_id') is not None:
            new_object_params['portId'] = self.new_object.get('portId') or \
                self.new_object.get('port_id')
        return new_object_params

    def get_object_by_name(self, name):
        result = None
        name = self.new_object.get('portId') or self.new_object.get('port_id')
        # NOTE: Does not have a get by name method, using get all
        try:
            items = self.meraki.exec_meraki(
                family="switch",
                function="getDeviceSwitchPorts",
                params=self.get_all_params(name=name),
            )
            if isinstance(items, dict):
                if 'response' in items:
                    items = items.get('response')
            result = get_dict_result(items, 'portId', name)
            if result is None:
                result = items
        except Exception as e:
            print("Error: ", e)
            result = None
        return result

    def get_object_by_id(self, id):
        result = None
        try:
            items = self.meraki.exec_meraki(
                family="switch",
                function="getDeviceSwitchPort",
                params=self.get_params_by_id()
            )
            if isinstance(items, dict):
                if 'response' in items:
                    items = items.get('response')
            result = items
        except Exception as e:
            print("Error: ", e)
            result = None
        return result

    def exists(self):
        prev_obj = None
        id_exists = False
        name_exists = False
        o_id = self.new_object.get("serial")
        o_id = o_id or self.new_object.get(
            "port_id") or self.new_object.get("portId")
        name = self.new_object.get("name")
        if o_id:
            prev_obj = self.get_object_by_id(o_id)
            id_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if not id_exists and name:
            prev_obj = self.get_object_by_name(name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            _id = _id or prev_obj.get("portId")
            if id_exists and name_exists and o_id != _id:
                raise InconsistentParameters(
                    "The 'id' and 'name' params don't refer to the same object")
            if _id:
                self.new_object.update(dict(id=_id))
                self.new_object.update(dict(portId=_id))
            if _id:
                prev_obj = self.get_object_by_id(_id)
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("name", "name"),
            ("tags", "tags"),
            ("enabled", "enabled"),
            ("poeEnabled", "poeEnabled"),
            ("type", "type"),
            ("vlan", "vlan"),
            ("voiceVlan", "voiceVlan"),
            ("allowedVlans", "allowedVlans"),
            ("isolationEnabled", "isolationEnabled"),
            ("rstpEnabled", "rstpEnabled"),
            ("stpGuard", "stpGuard"),
            ("linkNegotiation", "linkNegotiation"),
            ("portScheduleId", "portScheduleId"),
            ("udld", "udld"),
            ("accessPolicyType", "accessPolicyType"),
            ("accessPolicyNumber", "accessPolicyNumber"),
            ("macAllowList", "macAllowList"),
            ("stickyMacAllowList", "stickyMacAllowList"),
            ("stickyMacAllowListLimit", "stickyMacAllowListLimit"),
            ("stormControlEnabled", "stormControlEnabled"),
            ("adaptivePolicyGroupId", "adaptivePolicyGroupId"),
            ("peerSgtCapable", "peerSgtCapable"),
            ("flexibleStackingEnabled", "flexibleStackingEnabled"),
            ("daiTrusted", "daiTrusted"),
            ("profile", "profile"),
            ("serial", "serial"),
            ("portId", "portId"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(not meraki_compare_equality2(current_obj.get(meraki_param),
                                               requested_obj.get(ansible_param))
                   for (meraki_param, ansible_param) in obj_params)

    def update(self):
        id = self.new_object.get("id")
        id = id or self.new_object.get("portId")
        name = self.new_object.get("name")
        result = None
        if not id:
            prev_obj_name = self.get_object_by_name(name)
            id_ = None
            if prev_obj_name:
                id_ = prev_obj_name.get("id")
                id_ = id_ or prev_obj_name.get("portId")
            if id_:
                self.new_object.update(dict(portid=id_))
        result = self.meraki.exec_meraki(
            family="switch",
            function="updateDeviceSwitchPort",
            params=self.update_by_id_params(),
            op_modifies=True,
        )
        return result


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail(
                "ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._supports_check_mode = False
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(
                required_if=required_if,
                required_one_of=required_one_of,
                mutually_exclusive=mutually_exclusive,
                required_together=required_together,
            ),
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            raise AnsibleActionFail(errors)

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        meraki = MERAKI(self._task.args)
        obj = DevicesSwitchPorts(self._task.args, meraki)

        state = self._task.args.get("state")

        response = None
        if state == "present":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                if obj.requires_update(prev_obj):
                    response = obj.update()
                    meraki.object_updated()
                else:
                    response = prev_obj
                    meraki.object_already_present()
            else:
                meraki.fail_json(
                    "Object does not exists, plugin only has update")

        self._result.update(dict(meraki_response=response))
        self._result.update(meraki.exit_json())
        return self._result
