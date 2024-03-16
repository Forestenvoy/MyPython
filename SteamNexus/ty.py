from steam.api import interface
from steam.enums import EAppInfoSection


def get_system_requirements(app_id):
    # 初始化 Steam API 介面
    api = interface.API(interface.EInterface.Apps)

    # 獲取遊戲的最低和建議系統要求
    system_requirements = api.app(app_id).section(
        EAppInfoSection.Config)['pc_requirements']

    return system_requirements


def main():
    # 請替換為你感興趣的遊戲的 AppID
    app_id = 570  # Dota 2 的 AppID

    # 獲取系統要求
    requirements = get_system_requirements(app_id)

    # 打印最低和建議系統要求
    print("最低系統要求:")
    print(requirements['minimum'])
    print("\n建議系統要求:")
    print(requirements['recommended'])


if __name__ == "__main__":
    main()
