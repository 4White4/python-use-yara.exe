import os
import subprocess

def get_yara_files(rules_directory):
    yara_files = []
    # 递归遍历规则目录
    for root, _, files in os.walk(rules_directory):
        for file in files:
            if file.endswith('.yar') or file.endswith('.yara'):
                yara_files.append(os.path.join(root, file))
    return yara_files

def get_target_files(target_directory):
    target_files = []
    # 递归遍历目标目录，收集所有文件
    for root, _, files in os.walk(target_directory):
        for file in files:
            target_files.append(os.path.join(root, file))
    return target_files

def scan_with_yara(yara_files, target_files, yara_path):
    output_file = os.path.join(os.path.dirname(yara_path), 'yara_output.log')  # 输出文件路径

    total_files = len(target_files)
    print(f"Total files to scan: {total_files}")

    with open(output_file, 'w', encoding='utf-8') as f:
        for index, target_file in enumerate(target_files):
            for yara_file in yara_files:
                cmd = [yara_path, '-r', yara_file, target_file]
                try:
                    #print(f"Scanning: {target_file} (yara rule: {yara_file})")
                    # 执行命令，将输出重定向到文件
                    subprocess.run(cmd, check=True, stdout=f, stderr=subprocess.STDOUT)
                    #print(f"Executed: {cmd}")
                except subprocess.CalledProcessError as e:
                    print(f"Error executing {cmd}: {e}")
                # 实时显示进度
                print(f"Scanned {index + 1}/{total_files} files")

def main():
    yara_path = r'C:\77\ASoft\RmTools-main\yara_scanner\yara64.exe'  # YARA的可执行文件路径
    rules_directory = r'C:\77\ASoft\RmTools-main\yara_scanner'  # YARA规则目录
    target_directory = r'C:\77\ASoft\灵兔宝盒\Rabbit_Treasure_Box_v1.0\toosl\Post-Exploitation\Credential_Access\mimikatz_trunk\x64'  # 目标文件目录

    yaras = get_yara_files(rules_directory)
    target_files = get_target_files(target_directory)
    scan_with_yara(yaras, target_files, yara_path)

if __name__ == "__main__":
    main()
