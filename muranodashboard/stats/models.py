#    Copyright (c) 2014 Mirantis, Inc.
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

from muranodashboard.environments import api


class StatsModel(object):
    def get_api_stats(self, request):
        st_list = api.muranoclient(request).request_statistics.list()
        for srv in st_list:
            srv.max_cpu = srv.cpu_count * 100
        return st_list


class Stats(object):
    def __init__(self, from_dict):
        for k, v in from_dict.items():
            setattr(self, k, v)
