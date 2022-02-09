# flake8: noqa
"""
Copyright 2022 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject
from okta.models import capabilities_object\
    as capabilities_object
from okta.models import enabled_status\
    as enabled_status


class ApplicationFeature(
    OktaObject
):
    """
    A class for ApplicationFeature objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            if "capabilities" in config:
                if isinstance(config["capabilities"],
                              capabilities_object.CapabilitiesObject):
                    self.capabilities = config["capabilities"]
                elif config["capabilities"] is not None:
                    self.capabilities = capabilities_object.CapabilitiesObject(
                        config["capabilities"]
                    )
                else:
                    self.capabilities = None
            else:
                self.capabilities = None
            self.description = config["description"]\
                if "description" in config else None
            self.name = config["name"]\
                if "name" in config else None
            if "status" in config:
                if isinstance(config["status"],
                              enabled_status.EnabledStatus):
                    self.status = config["status"]
                elif config["status"] is not None:
                    self.status = enabled_status.EnabledStatus(
                        config["status"].upper()
                    )
                else:
                    self.status = None
            else:
                self.status = None
        else:
            self.links = None
            self.capabilities = None
            self.description = None
            self.name = None
            self.status = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "capabilities": self.capabilities,
            "description": self.description,
            "name": self.name,
            "status": self.status
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
