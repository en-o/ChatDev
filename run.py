# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
import argparse
import logging
import os
import sys

from camel.typing import ModelType

# 获取当前执行文件的目录路径
root = os.path.dirname(__file__)
# 将 root 这个路径添加到 sys.path 列表的末尾
sys.path.append(root)

from chatdev.chat_chain import ChatChain

try:
    from openai.types.chat.chat_completion_message_tool_call import ChatCompletionMessageToolCall
    from openai.types.chat.chat_completion_message import FunctionCall

    openai_new_api = True  # new openai api version
except ImportError:
    openai_new_api = False  # old openai api version
    print(
        "Warning: Your OpenAI version is outdated. \n "
        "Please update as specified in requirement.txt. \n "
        "The old API interface is deprecated and will no longer be supported.")

# 基础配置
def get_config(company):
    """
    return configuration json files for ChatChain
    user can customize only parts of configuration json files, other files will be left for default
    Args:
        company: customized configuration name under CompanyConfig/ （./CompanyConfig下了子目录名字就是用户自定义配置文件的名称，目录下面的文件参考default设置）

    Returns:
        path to three configuration jsons: [config_path（主配置）, config_phase_path（阶段配置）, config_role_path（规则配置）]
    """

    # 加载配置文件目录
    config_dir = os.path.join(root, "CompanyConfig", company)
    # 加载默认配置文件目录 - 自定义的查不到就会使用默认的
    default_config_dir = os.path.join(root, "CompanyConfig", "Default")

    # --------------------------------------------------------
    #          配置文件 （只允许如下配置文件，请参考Default的写法）
    # ------------- ChatChainConfig : 作为ChatChain系统的整体配置文件，它规定了整个软件开发流程的结构，
    #   包括各个阶段的顺序、类型、迭代次数以及是否需要反思等
    # ------------- PhaseConfig : 指导ChatChain系统在每个阶段应该如何与用户互动，
    #   包括系统和用户的角色名称、阶段提示（phase_prompt）等。这些提示是对话式指南，用于引导用户和系统之间的对话，以完成特定阶段的任务
    #   包括需求分析、编程语言选择、编码、艺术设计、环境文档和用户手册等
    # ------------- RoleConfig : 为ChatChain系统中的每个角色提供详细的背景和职责描述。
    #   这些描述帮助指导系统和用户在对话中扮演相应的角色，确保任务能够根据角色的专业能力和责任得到适当的解决
    #   这些角色包括首席执行官、产品总监、技术总监、程序员、代码审查员、软件测试工程师和创意总监等
    # --------------------------------------------------------
    config_files = [
        "ChatChainConfig.json",
        "PhaseConfig.json",
        "RoleConfig.json"
    ]

    # 当前运行需要的配置文件
    config_paths = []

    # 获取配置文件 - 对未设置的使用默认填充
    for config_file in config_files:
        # 自定义
        company_config_path = os.path.join(config_dir, config_file)
        # 默认
        default_config_path = os.path.join(default_config_dir, config_file)
        if os.path.exists(company_config_path):
            # 自定义存在就用
            config_paths.append(company_config_path)
        else:
            # 自定义不存在就是用默认
            config_paths.append(default_config_path)
    return tuple(config_paths)


# 命令解析
parser = argparse.ArgumentParser(description='argparse')
# 设置自定义配置[填写CompanyConfig/下的文件夹名]
parser.add_argument('--config', type=str, default="Default",
                    help="Name of config, which is used to load configuration under CompanyConfig/")
# 设置生成software的目录名字（name_你输入的_timestamp）
parser.add_argument('--org', type=str, default="DefaultOrganization",
                    help="Name of organization, your software will be generated in WareHouse/name_org_timestamp")
# software 名字和简单描述
parser.add_argument('--task', type=str, default="Develop a basic Gomoku game.",
                    help="Prompt of software")
# software 名字(同时会被应用到--org 用到的名字的 name_org_timestamp 目录上的name里)
parser.add_argument('--name', type=str, default="Gomoku",
                    help="Name of software, your software will be generated in WareHouse/name_org_timestamp")
# 选择模型
parser.add_argument('--model', type=str, default="GPT_3_5_TURBO",
                    help="GPT Model, choose from {'GPT_3_5_TURBO', 'GPT_4', 'GPT_4_TURBO', 'GPT_4O', 'GPT_4O_MINI'}")
# 增量模式 November 2, 2023: ChatDev is now supported with a new feature: incremental development,
# which allows agents to develop upon existing codes.
# Try --config "incremental" --path "[source_code_directory_path]" to start it.
# https://github.com/OpenBMB/ChatDev/issues/381
parser.add_argument('--path', type=str, default="",
                    help="Your file directory, ChatDev will build upon your software in the Incremental mode")
args = parser.parse_args()

# Start ChatDev

# ----------------------------------------
#          Init ChatChain
# ----------------------------------------
config_path, config_phase_path, config_role_path = get_config(args.config)
args2type = {'GPT_3_5_TURBO': ModelType.GPT_3_5_TURBO,
             'GPT_4': ModelType.GPT_4,
            #  'GPT_4_32K': ModelType.GPT_4_32k,
             'GPT_4_TURBO': ModelType.GPT_4_TURBO,
            #  'GPT_4_TURBO_V': ModelType.GPT_4_TURBO_V
            'GPT_4O': ModelType.GPT_4O,
            'GPT_4O_MINI': ModelType.GPT_4O_MINI,
             }
if openai_new_api:
    args2type['GPT_3_5_TURBO'] = ModelType.GPT_3_5_TURBO_NEW

chat_chain = ChatChain(config_path=config_path,
                       config_phase_path=config_phase_path,
                       config_role_path=config_role_path,
                       task_prompt=args.task,
                       project_name=args.name,
                       org_name=args.org,
                       model_type=args2type[args.model],
                       code_path=args.path)

# ----------------------------------------
#          Init Log（日志）
# ----------------------------------------
logging.basicConfig(filename=chat_chain.log_filepath, level=logging.INFO,
                    format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%Y-%d-%m %H:%M:%S', encoding="utf-8")

# ----------------------------------------
#          Pre Processing（前置处理）
# ----------------------------------------

chat_chain.pre_processing()

# ----------------------------------------
#          Personnel Recruitment（人员招聘）
# ----------------------------------------

chat_chain.make_recruitment()

# ----------------------------------------
#          Chat Chain （聊天）
# ----------------------------------------

chat_chain.execute_chain()

# ----------------------------------------
#          Post Processing（后置处理）
# ----------------------------------------

chat_chain.post_processing()
