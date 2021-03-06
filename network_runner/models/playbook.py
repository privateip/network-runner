#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
from network_runner.types.objects import Object
from network_runner.types.attrs import String, Dict, TypedList, Boolean
from network_runner.types.containers import Index

from network_runner.types.attrs import SERIALIZE_WHEN_PRESENT


class Base(object):

    connection = String(
        serialize_when=SERIALIZE_WHEN_PRESENT
    )


class Task(Base, Object):

    name = String(
        serialize_when=SERIALIZE_WHEN_PRESENT
    )

    action = String(
        required=True
    )

    args = Dict()

    vars = Dict(
        serialize_when=SERIALIZE_WHEN_PRESENT
    )

    when = String(
        serialize_when=SERIALIZE_WHEN_PRESENT
    )


class Play(Base, Object):

    name = String(
        serialize_when=SERIALIZE_WHEN_PRESENT
    )

    hosts = String(
        default='all'
    )

    gather_facts = Boolean(
        serialize_when=SERIALIZE_WHEN_PRESENT
    )

    tasks = TypedList(
        item_class=Task
    )


class Playbook(Index):

    def __init__(self):
        super(Playbook, self).__init__(Play)
