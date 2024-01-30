import json

# 读取原始JSON文件
with open('/wangjiatai/data/alpaca/alpaca_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 转化为目标格式
converted_data = []
for item in data:
    conversation_item = {
        "conversation": [
            {
                "system": "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n" + item["instruction"] + "\n\n### Response:",
                "input": item["instruction"] + " " + item["input"],
                "output": item["output"]
            }
        ]
    }
    converted_data.append(conversation_item)

# 保存为新的JSON文件
with open('/wangjiatai/data/alpaca/alpaca_data_convert.json', 'w', encoding='utf-8') as output_file:
    json.dump(converted_data, output_file, ensure_ascii=False, indent=4)
