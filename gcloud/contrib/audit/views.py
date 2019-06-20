# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from django.http import HttpResponseForbidden
from django.shortcuts import render

from gcloud.core.api_adapter import is_user_auditor


def home(request):
    # 只有审计人员可以查看
    is_auditor = is_user_auditor(request)
    if not is_auditor:
        return HttpResponseForbidden()

    return render(request, 'core/base_vue.html', {})
