import requests

# Steamworks 统计数据 API 的 URL
api_url = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"

# 游戏的 App ID
app_id = 1245620  # 请替换为你要查询的游戏的 App ID

# 定义请求参数
params = {
    'appid': app_id,
}

try:
    # 发送GET请求
    response = requests.get(api_url, params=params)

    # 检查响应是否成功
    if response.status_code == 200:
        # 处理API响应
        api_response = response.json()
        print(api_response)
        if 'response' in api_response and 'player_count' in api_response['response']:
            peak_players = api_response['response']['player_count']
            print(f"游戏 {app_id} 当日人数高峰：{peak_players} 人")
        else:
            print("未能解析API响应中的数据")
    else:
        print(f"API请求失败，状态码：{response.status_code}")
except Exception as e:
    print(f"发生错误：{e}")
