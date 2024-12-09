import yara
import os
import sys

def load_yara_rules(rule_directory):
    all_rules = {}
    # 递归遍历规则目录
    for root, _, files in os.walk(rule_directory):
        for file in files:
            if file.endswith('.yar') or file.endswith('.yara'):
                rule_path = os.path.join(root, file)
                rule_name = os.path.splitext(file)[0]
                all_rules[rule_name] = rule_path
    
    # 编译所有规则
    return yara.compile(filepaths=all_rules)

def scan_directory(scan_dir, rules):
    # 递归遍历待扫描目录
    for root, _, files in os.walk(scan_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                matches = rules.match(file_path)
                if matches:
                    print(f"Match found in {file_path}: {matches}")
            except Exception as e:
                print(f"Error scanning {file_path}: {e}")

def main():
    rules_directory = 'C:\\77\\ASoft\\RmTools-main\\yara_scanner\\yara_rules'  # 替换为规则文件的实际路径
    scan_directory_path = r'C:\77\ASoft\mimikatz'

    rules = load_yara_rules(rules_directory)
    scan_directory(scan_directory_path, rules)
    
if __name__ == "__main__":
    main()

