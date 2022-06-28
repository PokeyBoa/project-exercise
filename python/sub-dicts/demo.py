# -*- coding: UTF-8 -*-

data = {
    86: "身份编码",
    "姓名": "Ming",
    "学生": True,
    "心情": "😄",
    "年龄": 18,
    "学习": [
        {'小学': {'语文', '数学', '英语'}},
        {'初中': {'品德', '地理', '历史'}},
        {'高中': {'物理', '化学', '生物'}},
        {'大学': {'计算机', '英语', '高数'}}
    ],
    "爱好": {
        '游泳': ['自由泳', '潜水'],
        '滑雪': ['🏂', '🎿'],
        '游戏': ('LOL', 'PUBG', 'Genshin')
    },
    "音乐": {
        '摇滚': {'崔健', '汪峰', '郑钧', '许巍', '朴树'},
        '说唱': {'欧阳靖', 'MC Hotdog', '谢帝', 'GAI', 'JonyJ'},
        '民谣': {'赵雷', '宋冬野', '马頔'},
        '流行': {
            '周杰伦': {
                'Jay': {'星晴', '黑色幽默', '龙卷风'},
                '范特西': {'爱在西元前', '简单爱', '双节棍'},
                '叶惠美': {
                    '以父之名': {
                        "美誉": {"业界天花板", 7.16}
                    },
                },
                '七里香': {'园游会', '止战之殇'},
                '十一月的肖邦': {'夜曲', '枫'},
                '依然范特西': {'夜的第七章'},
                '我很忙': {'阳光宅男', '我不配'},
                '魔杰座': {'龙战骑士', '稻香'}
            },
            '林俊杰': {'江南', '黑武士'},
            '陈奕迅': {'十年', '淘汰', '单车'},
            '薛之谦': {'演员', '绅士'},
            '邓紫棋': {'泡沫', '再见', '光年之外', '倒数'}
        }
    }
}



def assert_dict(data_source=None):
    """
    列出所有的包含的字典
    """
    # 定义序列的数据类型
    data_structures = (list, tuple, set)
    # 如果数据源是序列类型
    if isinstance(data_source, data_structures):
        # 遍历拆解数据源的元素
        for element in data_source:
            # 如果元素是字典类型
            if isinstance(element, dict):
                for k, v in element.items():
                    print(f"key: {k}\tvalue: {v}")
                    assert_dict(data_source=v)
                assert_dict(data_source=element)
    # 如果数据源是字典类型
    elif isinstance(data_source, dict):
        # 遍历拆解字典类型的键与值
        for key, value in data_source.items():
            # 限定key只允许str或int类型
            if isinstance(key, (str, int)):
                # 如果value是序列类型
                if isinstance(value, data_structures):
                    assert_dict(data_source=value)
                # 如果value是字典类型
                elif isinstance(value, dict):
                    print(f"key: {key}\tvalue: {value}")
                    assert_dict(data_source=value)
            else:
                raise TypeError(f"TypeError: unsupported key type: {type(key)}.")
    else:
        pass
        # raise TypeError(f"TypeError: unsupported data source type: {type(data_source)}.")


assert_dict(data)
