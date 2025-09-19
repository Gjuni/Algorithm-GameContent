import feedparser
from openpyxl import Workbook
from datetime import datetime, timezone
import io
## https://www.dailysecu.com/rss/S1N2.xml
## http://www.boannews.com/media/news_rss.xml?skind=6

## 데일리시큐 이슈
def dailySecure():
    rss_url = "https://www.dailysecu.com/rss/S1N2.xml"
    feed = feedparser.parse(rss_url)

    return feed

## 보안 정책
def sercureRule():
    rss_url = "http://www.boannews.com/media/news_rss.xml?skind=6"
    feed = feedparser.parse(rss_url)

    return feed

def create_rss_excel(rss_url, file_base_name):
    feed = feedparser.parse(rss_url)

    wb = Workbook()
    ws = wb.active

    header = ["Index" ,"Title", "Link", "description"]
    ws.append(header)

    for i, entry in enumerate(feed.entries, 1):
        ws.append([i, entry.title, entry.link, entry.description])

    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    filename = f'{today}일자 {file_base_name}.xlsx'

    # 파일을 메모리 버퍼에 저장
    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    return buffer, filename

def downloadDailySecure():
    rss_url = "https://www.dailysecu.com/rss/S1N2.xml"
    return create_rss_excel(rss_url, "데일리시큐 뉴스")

def downloadsercureRule():
    rss_url = "http://www.boannews.com/media/news_rss.xml?skind=6"
    return create_rss_excel(rss_url, "보안뉴스")