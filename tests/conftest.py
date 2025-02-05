# Copyright 2020-2022 Cambridge Quantum Computing
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pytest
from pytket.extensions.iqm import IQMBackend


def get_demo_url() -> str:
    return "https://cortex-demo.qc.iqm.fi/"


@pytest.fixture(name="demo_url", scope="session")
def fixture_demo_url() -> str:
    return get_demo_url()


@pytest.fixture(name="authenticated_iqm_backend", scope="session")
def fixture_authenticated_iqm_backend() -> IQMBackend:
    # Authenticated IQMBackend used for the remote tests
    # The credentials are taken from the env variables:
    # - PYTKET_REMOTE_IQM_AUTH_SERVER_URL
    # - PYTKET_REMOTE_IQM_USERNAME
    # - PYTKET_REMOTE_IQM_PASSWORD

    return IQMBackend(
        url=get_demo_url(),
        auth_server_url=os.getenv("PYTKET_REMOTE_IQM_AUTH_SERVER_URL"),
        username=os.getenv("PYTKET_REMOTE_IQM_USERNAME"),
        password=os.getenv("PYTKET_REMOTE_IQM_PASSWORD"),
    )
