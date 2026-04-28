import json
import os
from datetime import datetime
from typing import List, Dict


class DataStorage:
    def __init__(self, filename='ai_company_news.json'):
        self.filename = filename
    
    def save_company_news(self, news_data: Dict[str, List[Dict]]):
        data = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_foreign': len(news_data['foreign']),
            'total_domestic': len(news_data['domestic']),
            'total': len(news_data['foreign']) + len(news_data['domestic']),
            'news': news_data
        }
        
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_news(self):
        if not os.path.exists(self.filename):
            return None
        
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def print_company_news(self, news_data: Dict[str, List[Dict]]):
        print(f"\n{'='*80}")
        print(f"AI大厂模型发布动态 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*80}")
        
        if news_data['foreign']:
            print("\n【国外AI公司动态】")
            print("-"*80)
            for i, news in enumerate(news_data['foreign'], 1):
                print(f"\n{i}. [{news['company']}] {news['title']}")
                print(f"   链接: {news['link']}")
                print(f"   时间: {news['time']}")
        
        if news_data['domestic']:
            print("\n\n【国内AI公司动态】")
            print("-"*80)
            for i, news in enumerate(news_data['domestic'], 1):
                print(f"\n{i}. [{news['company']}] {news['title']}")
                print(f"   链接: {news['link']}")
                print(f"   时间: {news['time']}")
        
        total = len(news_data['foreign']) + len(news_data['domestic'])
        print(f"\n{'='*80}")
        print(f"总计: 国外 {len(news_data['foreign'])} 条，国内 {len(news_data['domestic'])} 条，共 {total} 条")
        print(f"{'='*80}\n")
    
    def print_news(self, news_list: List[Dict]):
        print(f"\n{'='*80}")
        print(f"AI圈最新动态 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*80}\n")
        
        domestic = [n for n in news_list if n.get('source', '') in ['机器之心', '量子位', '智东西', '36氪AI', '新智元', '36氪', 'InfoQ中文站']]
        international = [n for n in news_list if n.get('source', '') not in ['机器之心', '量子位', '智东西', '36氪AI', '新智元', '36氪', 'InfoQ中文站']]
        
        if domestic:
            print("【国内动态】")
            print("-"*80)
            for i, news in enumerate(domestic, 1):
                print(f"\n{i}. [{news.get('source', 'N/A')}] {news['title']}")
                print(f"   链接: {news['link']}")
                print(f"   时间: {news.get('time', 'N/A')}")
        
        if international:
            print("\n\n【国外动态】")
            print("-"*80)
            for i, news in enumerate(international, 1):
                print(f"\n{i}. [{news.get('source', 'N/A')}] {news['title']}")
                print(f"   链接: {news['link']}")
                print(f"   时间: {news.get('time', 'N/A')}")
        
        print(f"\n{'='*80}")
        print(f"总计: {len(news_list)} 条新闻")
        print(f"{'='*80}\n")
