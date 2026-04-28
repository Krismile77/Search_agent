
import sys
import time
from datetime import datetime
from config import AI_COMPANIES
from ai_company_crawler import AICompanyCrawler
from data_storage import DataStorage
from performance_analyzer import PerformanceAnalyzer

class AINewsAgent:
    def __init__(self, use_demo=False):
        self.crawler = AICompanyCrawler()
        self.storage = DataStorage()
        self.analyzer = PerformanceAnalyzer()
        self.use_demo = use_demo
    
    def run(self):
        if self.use_demo:
            print("\n[演示模式] 使用演示数据展示...")
            news_data = self.crawler.get_demo_data()
        else:
            news_data = self.crawler.crawl_all_companies()
            
            total = len(news_data['foreign']) + len(news_data['domestic'])
            if total == 0:
                print("\n[提示] 未能爬取到任何数据，切换到演示模式...")
                news_data = self.crawler.get_demo_data()
        
        self.storage.save_company_news(news_data)
        self.storage.print_company_news(news_data)
        print(f"\n[完成] 数据已保存到 {self.storage.filename}")

def print_usage():
    print("\nAI 性能对比分析平台 - 多模型集成")
    print("="*70)
    print("\n使用方法:")
    print("  python main.py [命令]")
    print("\n命令:")
    print("  (无参数)       - 尝试爬取真实数据")
    print("  --demo         - 使用演示数据爬取新闻")
    print("  demo           - 使用演示数据爬取新闻")
    print("  --web          - 启动Web界面（推荐）")
    print("  web            - 启动Web界面（推荐）")
    print("  --analysis     - 显示性能分析报告")
    print("  analysis       - 显示性能分析报告")
    print("  --api-test     - 测试API功能")
    print("  api-test       - 测试API功能")
    print("  --help         - 显示帮助信息")
    print("\n功能特性:")
    print("  - AI新闻爬虫 - 跟踪国内外大厂动态")
    print("  - 性能分析 - 各模型功能对比")
    print("  - API接口 - 标准化模型调用")
    print("  - Web界面 - 可视化展示 & 快捷入口")
    print("\n覆盖模型:")
    print("\n国外 (5家):")
    for company in AI_COMPANIES['foreign']:
        print(f"  - {company['name']} ({', '.join(company['models'])})")
    print("\n国内 (7家):")
    for company in AI_COMPANIES['domestic']:
        print(f"  - {company['name']} ({', '.join(company['models'])})")
    print()

def start_web_server():
    try:
        from web_app import run_web_server
        run_web_server()
    except ImportError:
        print("\n[错误] Flask未安装，请运行: pip install Flask\n")

def show_analysis():
    analyzer = PerformanceAnalyzer()
    analyzer.print_analysis_report()

def test_api():
    print("\n" + "="*70)
    print("API 功能测试")
    print("="*70)
    
    try:
        from api_handler import APIHandler
        handler = APIHandler()
        
        print("\n1. 列出所有模型:")
        models = handler.list_models()
        print(f"   共找到 {models['total_count']} 个模型")
        for model in models['models'][:5]:
            print(f"   - {model['name']} - {model['provider']}")
        
        print("\n2. 测试对话 (使用模拟响应):")
        test_message = "Hello, how are you?"
        result = handler.chat_completion(
            'gpt-4o',
            [{'role': 'user', 'content': test_message}]
        )
        
        if result.get('error'):
            print(f"   错误: {result['message']}")
        else:
            print(f"   模型: {result['model']}")
            print(f"   响应时间: {result['latency_ms']}ms")
            print(f"   回复: {result['content'][:100]}...")
        
        print("\n" + "="*70)
        print("API 功能测试完成")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n测试失败: {e}\n")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ['--help', '-h', 'help']:
            print_usage()
            sys.exit(0)
        elif arg in ['--web', 'web']:
            start_web_server()
            sys.exit(0)
        elif arg in ['--analysis', 'analysis']:
            show_analysis()
            sys.exit(0)
        elif arg in ['--api-test', 'api-test', 'api_test']:
            test_api()
            sys.exit(0)
        elif arg in ['--demo', 'demo']:
            agent = AINewsAgent(use_demo=True)
            agent.run()
            sys.exit(0)
    
    agent = AINewsAgent(use_demo=False)
    agent.run()
