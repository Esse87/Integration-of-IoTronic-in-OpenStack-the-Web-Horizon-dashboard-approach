# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.



from django.conf import settings
from horizon.utils.memoized import memoized  # noqa
from openstack_dashboard.api import base
import iotronicclient as iotronic_client
import logging
LOG = logging.getLogger(__name__)


@memoized
def iotronicclient(request):
    """Initialization of Iotronic client."""
    
    endpoint = base.url_for(request, 'iot')
    insecure = getattr(settings, 'OPENSTACK_SSL_NO_VERIFY', False)
    cacert = getattr(settings, 'OPENSTACK_SSL_CACERT', None)
    return iotronic_client.client.Client('1', endpoint)


def node_create(request, context):

    id=str(context['NodeID'])
    type=str(context['DeviceType'])
    name=str(context['DeviceName'])
    latitude=str(context['Latitude'])
    longitude=str(context['Longitude'])
    height=str(context['Height'])

    return iotronicclient(request).node._create(id,type,name,latitude,longitude,height,False)


def node_delete(request, uuid):
    iotronicclient(request).node._delete(uuid)
       
def get_info(request, uuid):
    inf = iotronicclient(request).node.get(uuid)

    return [inf.code, inf.location,inf.session,inf.device,inf.mobile]

    
class Node(base.APIResourceWrapper):
    """Represents one Iotronic node."""
    _attrs = ['code', 'name', 'uuid', 'status']
   
   
def node_list(request):
    """List the info of the nodes."""
    nodes = iotronicclient(request).node.list()
    response = []

    for n in nodes:
        node = Node(n)
        setattr(node, 'id', n.uuid)
        response.append(node)

    return response





