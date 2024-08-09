import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def openai(api_key, user_input):
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': '너는 전기차 뉴스 제목의 감성분석을 하는 챗봇이야, 제목이 긍정, 부정, 중립인지만 표시해줘.'},
            {'role': 'user', 'content': user_input},
        ]
    )

    return completion.choices[0].message.content



# def parse_analysis(analysis):
#     # 키워드와 긍부정 결과를 정규표현식을 통해 추출
#     keyword_match = re.search(r'키워드: (.*?)\n', analysis)
#     result_match = re.search(r'결과: (.*?)\n?', analysis)

#     keywords = keyword_match.group(1) if keyword_match else "None"
#     result = result_match.group(1) if result_match else "Unknown"

#     return keywords, result



df = pd.read_csv('df_24.csv')

results = []

# for title in df['title']:
#     analysis = openai(OPENAI_API_KEY, title)
#     keywords, sentiment_result = parse_analysis(analysis)
#     results.append({
#         'Title': title,
#         'Keywords': keywords,
#         'Sentiment': sentiment_result
#     })


for index, row in df.iterrows():
    headline = row['headline']
    press = row['press']
    result = openai(OPENAI_API_KEY, headline)
    results.append({
        'Press': press,
        'Headline': headline,
        'Analysis': result
    })


# for title in df['title']:
#     result = openai(OPENAI_API_KEY, title)
#     results.append({
#         'Press': press,
#         'Title': title,
#         'Analysis': result
#     })

# 결과를 데이터프레임으로 변환
results_df = pd.DataFrame(results)

# 결과를 CSV 파일로 저장
results_df.to_csv('2024_log.csv', index=False)