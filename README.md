调用yar命令执行扫描.py
- 调用可以定义检测规则的病毒扫描工具yara，解决了yara无法批量使用yar扫描和python直接调用 yara.compile..match不能有中文路径报错的问题*
需要编辑三个变量方可执行：
1.yara_path：YARA的可执行文件路径
2.rules_directory：YARA规则目录
3.target_directory：待扫描的目录

最后会在yara.exe的目录下生成结果文件yara_output.log


scan(扫描路径不能有中文).py
直接调用yara python库，但是扫描路径不能含有中文。
替换两个变量rules_directory（规则目录）、scan_directory_path（扫描目录）
