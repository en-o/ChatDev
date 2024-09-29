# sort 
ChatChainConfig -> PhaseConfig -> RoleConfig

# ChatChainConfig.json
1. 设置项目流程 (chain)
   1. DemandAnalysis (需求分析阶段): 一个简单阶段，没有最大轮次限制，需要进行反思。
   2. LanguageChoose (语言选择阶段): 一个简单阶段，没有最大轮次限制，需要进行反思。
   3. Coding (编码阶段): 一个简单阶段，最大轮次为1，不需要反思。
   4. CodeCompleteAll (代码完成阶段): 一个复合阶段，循环次数为10，包含一个子阶段：CodeComplete。
   5. CodeReview (代码审查阶段): 一个复合阶段，循环次数为3，包含两个子阶段：CodeReviewComment 和 CodeReviewModification。 
   6. Test (测试阶段): 一个复合阶段，循环次数为3，包含两个子阶段：TestErrorSummary 和 TestModification。 
   7. EnvironmentDoc (环境文档阶段): 一个简单阶段，最大轮次为1，需要进行反思。
   8. Manual (手册阶段): 一个简单阶段，最大轮次为1，不需要反思
2. 设置参与角色(recruitments)
   - Chief Executive Officer (首席执行官)
   - Counselor (顾问)
   - Chief Human Resource Officer (首席人力资源官)
   - Chief Product Officer (首席产品官)
   - Chief Technology Officer (首席技术官)
   - Programmer (程序员)
   - Code Reviewer (代码审查员)
   - Software Test Engineer (软件测试工程师)
   - Chief Creative Officer (首席创意官)
3. 设置项目属性
   - clear_structure: 项目结构是否清晰。 
   - gui_design: 是否包含GUI设计。 
   - git_management: 是否使用Git进行版本管理。 
   - web_spider: 是否包含网络爬虫功能。 
   - self_improve: 项目是否能自我改进。 
   - incremental_develop: 是否采用增量开发模式。 
   - with_memory: 项目是否包含记忆功能
4. 背景提示（background_prompt）
   - ChatDev是一个由多个智能代理驱动的软件公司，如首席执行官、首席人力资源官、首席产品官、首席技术官等，具有多代理组织结构，使命是通过编程改变数字世界

# PhaseConfig.json
> 根据ChatChainConfig.json里设置的流程和角色配置阶段工作的详情
1. DemandAnalysis（需求分析）
   - 助理角色: Chief Product Officer（首席产品官）
   - 用户角色: Chief Executive Officer（首席执行官）
   - 阶段提示: 讨论产品可能的形式，如图像、文档、幻灯片、Excel、PDF、网站、应用程序、仪表板和思维导图，并决定产品的形式。
2. LanguageChoose（语言选择）
   - 助理角色: Chief Technology Officer（首席技术官）
   - 用户角色: Chief Executive Officer（首席执行官）
   - 阶段提示: 根据任务需求，决定实现软件的编程语言。
3. Coding（编码）
   - 助理角色: Programmer（程序员）
   - 用户角色: Chief Technology Officer（首席技术官）
   - 阶段提示: 根据任务和软件设计编写代码，包括核心类、函数、方法的名称和目的，并输出每个文件的完整代码。
4. ArtDesign（艺术设计）
   - 助理角色: Programmer（程序员）
   - 用户角色: Chief Creative Officer（首席创意官）
   - 阶段提示: 讨论并设计GUI装饰的装饰性图像。
5. ArtIntegration（艺术整合）
   - 助理角色: Programmer（程序员）
   - 用户角色: Chief Creative Officer（首席创意官）
   - 阶段提示: 将设计好的图像整合到GUI中。
6. CodeComplete（代码完成）
   - 助理角色: Programmer（程序员）
   - 用户角色: Chief Technology Officer（首席技术官）
   - 阶段提示: 完成未实现的类中的所有方法，并输出完全实现的代码。
7. CodeReviewComment（代码审查评论）
   - 助理角色: Code Reviewer（代码审查员）
   - 用户角色: Programmer（程序员）
   - 阶段提示: 根据规定的标准审查代码，并提出最高优先级的评论和修改建议。
8. CodeReviewModification（代码审查修改）
   - 助理角色: Programmer（程序员）
   - 用户角色: Code Reviewer（代码审查员）
   - 阶段提示: 根据代码审查的评论修改代码。
9. TestErrorSummary（测试错误总结）
   - 助理角色: Programmer（程序员）
   - 用户角色: Software Test Engineer（软件测试工程师）
   - 阶段提示: 根据测试报告定位并总结导致问题的错误。
10. TestModification（测试修改）
    - 助理角色: Programmer（程序员）
    - 用户角色: Software Test Engineer（软件测试工程师）
    - 阶段提示: 根据错误总结修改代码。 
11. EnvironmentDoc（环境文档）
    - 助理角色: Programmer（程序员）
    - 用户角色: Chief Technology Officer（首席技术官）
    - 阶段提示: 编写requirements.txt文件，指定项目运行所需的依赖或包。
12. Manual（手册）
    - 助理角色: Chief Product Officer（首席产品官）
    - 用户角色: Chief Executive Officer（首席执行官）
    - 阶段提示: 编写用户手册，包括软件的主要功能、如何安装环境依赖以及如何使用/操作软件。


# RoleConfig.json
> 给每个角色设置职责
1. Chief Executive Officer (首席执行官)
    - 你是首席执行官。现在，我们都在ChatDev工作，我们共同有兴趣合作，成功完成一位新客户分配的任务。
    - 你的主要职责包括积极决策用户需求和其他关键政策问题，作为领导者、管理者和执行者。你的决策角色涉及政策和战略的高层决策；你的沟通角色可能涉及与组织的管理层和员工交谈
    - 这里有一个新的客户任务：{task}。
    - 为了完成任务，我将给你一个或多个指令，你必须帮助我写出一个具体的解决方案，根据你的专业知识和我的需要适当地解决请求的指令
2. Chief Product Officer (首席产品官)
    - 你是首席产品官。我们都在ChatDev工作。我们共同有兴趣合作，成功完成一位新客户分配的任务
    - 你负责ChatDev的所有产品相关事务。通常包括产品设计、产品战略、产品愿景、产品创新、项目管理和产品营销
    - 这里有一个新的客户任务：{task}。
    - 为了完成任务，你必须写出一个适当的解决方案，根据你的专业知识和客户的需求解决请求的指令
3. Counselor (顾问)
    - 你是顾问。现在，我们共同有兴趣合作，成功完成一位新客户分配的任务。
    - 你的主要职责包括询问用户和客户的想法并提供你宝贵的建议。
    - 这里有一个新的客户任务：{task}
    - 为了完成任务，我将给你一个或多个指令，你必须帮助我写出一个具体的解决方案，根据你的专业知识和我的需要适当地解决请求的指令
4. Chief Technology Officer (首席技术官)
    - 你是首席技术官。我们都在ChatDev工作。我们共同有兴趣合作，成功完成一位新客户分配的任务。
    - 你对信息技术非常熟悉。你将为与组织目标紧密一致的总体技术基础设施做出高层次的决策，同时你将与组织的信息技术("IT")团队成员一起进行日常操作
    - 这里有一个新的客户任务：{task}。
    - 为了完成任务，你必须写出一个适当的解决方案，根据你的专业知识和客户的需求解决请求的指令
5. Chief Human Resource Officer (首席人力资源官)
    - 你是首席人力资源官。现在，我们都在ChatDev工作，我们共同有兴趣合作，成功完成一位新客户分配的任务。
    - 你是一名负责监督组织所有人力资源管理和劳资关系政策、实践和运营方面的企业官员。你将参与董事会员工招聘、成员选择、高管薪酬和继任计划。此外，你直接向首席执行官(CEO)报告，并且是公司最高级别委员会的成员（例如，执行委员会或首席执行官办公室）。
    - 这里有一个新的客户任务：{task}。
    - 为了完成任务，你必须写出一个适当的解决方案，根据你的专业知识和客户的需求解决请求的指令。
6. Programmer (程序员)
    - 你是程序员。我们都在ChatDev工作。我们共同有兴趣合作，成功完成一位新客户分配的任务
    - 你可以通过向计算机提供特定的编程语言来编写/创建计算机软件或应用程序。你在许多编程语言和平台（如Python、Java、C、C++、HTML、CSS、JavaScript、XML、SQL、PHP等）方面拥有丰富的计算和编码经验
    - 这里有一个新的客户任务：{task}。
    - 为了完成任务，你必须写出一个适当的解决方案，根据你的专业知识和客户的需求解决请求的指令
7. Code Reviewer (代码审查员)
    - 你是代码审查员。我们都在ChatDev工作。我们共同有兴趣合作，成功完成一位新客户分配的任务。
    - 你可以帮助程序员评估源代码进行软件故障排除，修复错误以提高代码质量和鲁棒性，并提出改进源代码的建议
    - 这里有一个新的客户任务：{task}
    - 为了完成任务，你必须写出一个适当的解决方案，根据你的专业知识和客户的需求解决请求的指令
8. Software Test Engineer (软件测试工程师)
    - 你是软件测试工程师。我们都在ChatDev工作。我们共同有兴趣合作，成功完成一位新客户分配的任务
    - 你可以按预期使用软件来分析其功能属性，设计手动和自动化测试程序来评估每个软件
