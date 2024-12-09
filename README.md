
- 调用可以定义检测规则的病毒扫描工具yara，解决了yara无法批量使用yar扫描和python直接调用 yara.compile..match不能有中文路径报错的问题*
需要编辑三个变量方可执行：
1.yara_path：YARA的可执行文件路径
2.rules_directory：YARA规则目录
3.target_directory：待扫描的目录

最后会在yara.exe的目录下生成结果文件yara_output.log