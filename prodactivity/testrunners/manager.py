#! /usr/bin/env python
# Copyright 2015-2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

'''library to create and use containers an environment with a local registry
and a container orchestration environment'''
import sys
import time

from prodactivity.utils.dockerlib import render_dockerfile
from prodactivity.utils.dockerlib import build_and_publish


def main():
    render_dockerfile(test_type=sys.argv[1],
                      project=sys.argv[2],
                      branch=sys.argv[3],
                      registry_project_name=REG_ID,
                      timestamp=TIMESTAMP)
    build_and_publish(test_type=sys.argv[1],
                      project=sys.argv[2],
                      branch=sys.argv[3],
                      subjectcode_id=sys.argv[4],
                      time.time())

if __name__ == '__main__':
    main()
