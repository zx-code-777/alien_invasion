import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                     '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
response = requests.get(url, headers=headers)
print(f'Status code: {response.status_code}')
# 将API响应赋给一个变量
response_dict = response.json()
# 处理结果
# print(response_dict.keys())
print(f'总计仓库: {response_dict["total_count"]}')

# 探索有关仓库的信息
response_dicts = response_dict['items']
print(f'仓库结果:{len(response_dicts)}')

# 研究第一个仓库
response_dict1 = response_dicts[0]
print(f'\nkeys:{len(response_dict1)}')
for key in sorted(response_dict1.keys()):
    print(f"Name: {response_dict1['name']}")
    print(f"Owner: {response_dict1['owner']['login']}")
    print(f"Stars: {response_dict1['stargazers_count']}")
    print(f"Repository: {response_dict1['html_url']}")
    print(f"Created: {response_dict1['created_at']}")
    print(f"Updated: {response_dict1['updated_at']}")
    print(f"Description: {response_dict1['description']}")
