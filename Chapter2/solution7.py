a = "Life is too short, You need Python"
print(a[0:4])
print(a[0:3])
print(a[0:5])
print(a[0:2])
print(a[5:7])
print(a[12:17])
print(a[19:]) # 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지
print(a[:17]) # 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지
print(a[:]) # 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지
print(a[19:-7]) # 슬라이싱에서도 인덱싱과 마찬가지로 마이너스 기호 사용 가능 a[19]부터 a[-7]까지를 의미