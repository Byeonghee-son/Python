import requests

# 쿠키 값을 추출합니다 (실제로는 브라우저에서 수동으로 쿠키를 확인하고 복사해야 합니다.)
cookies = {
    'FMCSSESSIONID': '1630F80F22325EB3EAB6FF2F9FF63B37'
}

# 쿠키와 함께 웹사이트에 요청을 보냅니다.
response = requests.get('https://www.osansports.or.kr/fmcs/29?action=read&comcd=OSANSISUL01&classcd=00068&type=R', cookies=cookies)

# 로그인 및 세션 유지
session = requests.Session()

# ... 로그인 과정 생략 ...

# 수강신청 버튼이 POST 요청이라 가정하고, 해당 요청을 보냅니다.
url = 'https://www.osansports.or.kr/fmcs/29?action=read&comcd=OSANSISUL01&classcd=00068&type=R'  # 수강신청 요청 URL로 변경 필요
data = { 'some_key': 'some_value' }  # 필요한 요청 데이터로 변경 필요
response = session.post(url, data=data)

print(response.text)  # 응답 확인
