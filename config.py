AI_COMPANIES = {
    'foreign': [
        {
            'name': 'OpenAI',
            'models': ['GPT', 'ChatGPT'],
            'urls': [
                'https://openai.com/blog',
                'https://openai.com/research'
            ],
            'official_url': 'https://chat.openai.com/',
            'description': 'GPT系列，最知名的大语言模型'
        },
        {
            'name': 'Google',
            'models': ['Gemini', 'PaLM'],
            'urls': [
                'https://ai.googleblog.com/',
                'https://blog.google/technology/ai/'
            ],
            'official_url': 'https://gemini.google.com/',
            'description': 'Gemini多模态模型'
        },
        {
            'name': 'Anthropic',
            'models': ['Claude'],
            'urls': [
                'https://www.anthropic.com/research'
            ],
            'official_url': 'https://claude.ai/',
            'description': 'Claude系列，安全导向AI'
        },
        {
            'name': 'Meta',
            'models': ['Llama'],
            'urls': [
                'https://ai.meta.com/blog/'
            ],
            'official_url': 'https://ai.meta.com/',
            'description': 'Llama开源模型系列'
        },
        {
            'name': 'Mistral',
            'models': ['Mistral'],
            'urls': [
                'https://mistral.ai/news/'
            ],
            'official_url': 'https://chat.mistral.ai/',
            'description': 'Mistral高效模型'
        }
    ],
    'domestic': [
        {
            'name': 'DeepSeek',
            'models': ['DeepSeek'],
            'urls': [
                'https://platform.deepseek.com/',
                'https://github.com/deepseek-ai'
            ],
            'official_url': 'https://chat.deepseek.com/',
            'description': '性价比极高的国产模型'
        },
        {
            'name': '智谱',
            'models': ['GLM'],
            'urls': [
                'https://www.zhipuai.cn/',
                'https://chatglm.cn/'
            ],
            'official_url': 'https://chatglm.cn/',
            'description': 'GLM系列，清华大学背景'
        },
        {
            'name': '月之暗面',
            'models': ['Kimi'],
            'urls': [
                'https://kimi.moonshot.cn/'
            ],
            'official_url': 'https://kimi.moonshot.cn/',
            'description': 'Kimi长文本处理'
        },
        {
            'name': '通义千问',
            'models': ['Qwen'],
            'urls': [
                'https://tongyi.aliyun.com/',
                'https://help.aliyun.com/zh/tongyi/'
            ],
            'official_url': 'https://tongyi.aliyun.com/',
            'description': '阿里通义千问'
        },
        {
            'name': 'MiniMax',
            'models': ['MiniMax'],
            'urls': [
                'https://www.minimax.cn/'
            ],
            'official_url': 'https://api.minimax.chat/',
            'description': 'MiniMax多模态'
        },
        {
            'name': '豆包',
            'models': ['Doubao'],
            'urls': [
                'https://www.doubao.com/'
            ],
            'official_url': 'https://www.doubao.com/',
            'description': '字节跳动豆包'
        },
        {
            'name': '文心一言',
            'models': ['Ernie'],
            'urls': [
                'https://yiyan.baidu.com/'
            ],
            'official_url': 'https://yiyan.baidu.com/',
            'description': '百度文心一言'
        }
    ]
}

KEYWORDS = [
    '发布', 'release', 'announce', 'announcement',
    '新模型', 'new model', 'model release',
    '预发布', 'preview', 'beta',
    '更新', 'update', 'upgrade',
    '论文', 'paper', 'research',
    'GPT', 'Gemini', 'GLM', 'Qwen', 'Kimi', 'DeepSeek', 'Claude', 'Llama', 'Mistral', 'Ernie'
]

AI_PERFORMANCE_DATA = {
    'categories': [
        '代码生成', '数学推理', '文本创作', '多模态', '长文本', '中文理解', '快速响应', '成本效益'
    ],
    'agents': {
        'OpenAI': {
            'name': 'GPT-4o / GPT-4',
            'scores': [95, 95, 95, 98, 90, 88, 90, 70],
            'best_at': ['多模态', '文本创作', '综合能力'],
            'price_range': '$0.01-$0.15/1K tokens'
        },
        'Google': {
            'name': 'Gemini 2.5 Pro',
            'scores': [92, 90, 90, 95, 88, 85, 92, 75],
            'best_at': ['多模态', '快速响应'],
            'price_range': '$0.005-$0.125/1K tokens'
        },
        'Anthropic': {
            'name': 'Claude 3 Opus',
            'scores': [90, 93, 92, 90, 98, 85, 85, 65],
            'best_at': ['长文本', '数学推理'],
            'price_range': '$0.015-$0.15/1K tokens'
        },
        'Meta': {
            'name': 'Llama 3.1',
            'scores': [85, 82, 80, 75, 80, 78, 85, 95],
            'best_at': ['成本效益', '快速响应'],
            'price_range': '免费开源'
        },
        'Mistral': {
            'name': 'Mistral Large 2',
            'scores': [88, 85, 83, 80, 85, 80, 90, 88],
            'best_at': ['快速响应', '成本效益'],
            'price_range': '$0.003-$0.08/1K tokens'
        },
        'DeepSeek': {
            'name': 'DeepSeek V3',
            'scores': [90, 90, 85, 80, 85, 95, 88, 98],
            'best_at': ['中文理解', '成本效益', '代码生成'],
            'price_range': '¥1-¥10/1M tokens'
        },
        '智谱': {
            'name': 'GLM-4',
            'scores': [85, 85, 85, 80, 80, 95, 85, 90],
            'best_at': ['中文理解'],
            'price_range': '¥5-¥50/1M tokens'
        },
        '月之暗面': {
            'name': 'Kimi',
            'scores': [80, 80, 85, 75, 98, 92, 80, 85],
            'best_at': ['长文本', '中文理解'],
            'price_range': '¥10-¥80/1M tokens'
        },
        '通义千问': {
            'name': 'Qwen 2.5',
            'scores': [88, 85, 88, 85, 85, 95, 88, 92],
            'best_at': ['中文理解', '多模态', '文本创作'],
            'price_range': '¥3-¥40/1M tokens'
        },
        'MiniMax': {
            'name': 'MiniMax 4',
            'scores': [80, 78, 82, 90, 75, 90, 85, 80],
            'best_at': ['多模态', '中文理解'],
            'price_range': '¥5-¥60/1M tokens'
        },
        '豆包': {
            'name': 'Doubao 4.0',
            'scores': [82, 80, 88, 85, 80, 95, 90, 88],
            'best_at': ['中文理解', '文本创作', '快速响应'],
            'price_range': '¥2-¥30/1M tokens'
        },
        '文心一言': {
            'name': 'Ernie 4.0',
            'scores': [85, 83, 85, 88, 82, 95, 85, 85],
            'best_at': ['中文理解', '多模态'],
            'price_range': '¥8-¥80/1M tokens'
        }
    }
}
