import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
from datetime import datetime
from typing import List, Dict
import re
from config import AI_COMPANIES, KEYWORDS


class AICompanyCrawler:
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.ua.random
        })
    
    def is_relevant(self, text: str, keywords: List[str]) -> bool:
        text_lower = text.lower()
        for keyword in keywords:
            if keyword.lower() in text_lower:
                return True
        return False
    
    def get_page(self, url: str, timeout: int = 15) -> str:
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"获取页面失败 {url}: {e}")
            return ""
    
    def parse_company_page(self, html: str, company_name: str, base_url: str, models: List[str]) -> List[Dict]:
        soup = BeautifulSoup(html, 'html.parser')
        news = []
        
        # 通用选择器尝试
        selectors = [
            'article', '.post', '.blog-post',
            '.news-item', '.article-item', '.item',
            'li a', '.title a', 'h1 a', 'h2 a', 'h3 a'
        ]
        
        links = set()
        for selector in selectors:
            elements = soup.select(selector)
            for elem in elements:
                link = None
                title = None
                
                if elem.name == 'a':
                    link = elem.get('href', '')
                    title = elem.get_text(strip=True)
                else:
                    a_tag = elem.find('a')
                    if a_tag:
                        link = a_tag.get('href', '')
                        title = a_tag.get_text(strip=True)
                
                if link and title and len(title) > 5:
                    if not link.startswith('http'):
                        if link.startswith('/'):
                            link = base_url.rstrip('/') + link
                        else:
                            link = base_url.rstrip('/') + '/' + link
                    
                    if link not in links:
                        links.add(link)
                        
                        # 检查是否相关
                        all_keywords = KEYWORDS + models
                        if self.is_relevant(title, all_keywords):
                            news.append({
                                'title': title,
                                'link': link,
                                'company': company_name,
                                'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            })
        
        return news[:15]
    
    def crawl_company(self, company: Dict) -> List[Dict]:
        company_name = company['name']
        models = company['models']
        urls = company['urls']
        
        print(f"\n正在爬取 {company_name}...")
        all_news = []
        
        for url in urls:
            if not url:
                continue
                
            print(f"  - URL: {url}")
            
            html = self.get_page(url)
            if html:
                base_url = '/'.join(url.split('/')[:3])
                news = self.parse_company_page(html, company_name, base_url, models)
                all_news.extend(news)
                print(f"    找到 {len(news)} 条相关新闻")
            
            time.sleep(1)
        
        return all_news
    
    def crawl_all_companies(self) -> Dict[str, List[Dict]]:
        results = {
            'foreign': [],
            'domestic': []
        }
        
        print("="*80)
        print("开始爬取AI大厂模型发布动态")
        print("="*80)
        
        print("\n【国外AI公司】")
        for company in AI_COMPANIES['foreign']:
            news = self.crawl_company(company)
            results['foreign'].extend(news)
        
        print("\n【国内AI公司】")
        for company in AI_COMPANIES['domestic']:
            news = self.crawl_company(company)
            results['domestic'].extend(news)
        
        return results
    
    def get_demo_data(self) -> Dict[str, List[Dict]]:
        return {
            'foreign': [
                {
                    'title': 'OpenAI 发布 GPT-5 预览版，多模态能力大幅提升',
                    'link': 'https://openai.com/blog/gpt-5',
                    'company': 'OpenAI',
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                },
                {
                    'title': 'Google Gemini 2.5 正式发布，支持超长上下文',
                    'link': 'https://ai.googleblog.com/',
                    'company': 'Google',
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                },
                {
                    'title': 'OpenAI 发布最新研究论文：Scaling Laws 2.0',
                    'link': 'https://openai.com/research',
                    'company': 'OpenAI',
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
            ],
            'domestic': [
                {
                    'title': 'DeepSeek 发布 V3 版本，性能逼近 GPT-4',
                    'link': 'https://platform.deepseek.com/',
                    'company': 'DeepSeek',
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                },
                {
                    'title': '智谱 GLM-4 大版本更新，推理速度提升 200%',
                    'link': 'https://www.zhipuai.cn/',
                    'company': '智谱',
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                },
                {
                    'title': '月之暗面 Kimi 新功能上线：支持文档问答',
                    'link': 'https://kimi.moonshot.cn/',
                    'company': '月之暗面',
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                },
                {
                    'title': '通义千问 Qwen-3 预发布，开源全新模型系列',
                    'link': 'https://tongyi.aliyun.com/',
                    'company': '通义千问',
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                },
                {
                    'title': 'MiniMax 发布新版本，多模态能力增强',
                    'link': 'https://www.minimax.cn/',
                    'company': 'MiniMax',
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                },
                {
                    'title': '豆包 4.0 更新发布，更加智能的对话体验',
                    'link': 'https://www.doubao.com/',
                    'company': '豆包',
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
            ]
        }
