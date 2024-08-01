import pyupbit

access = "xOq2xnFzH0zvnBtixSz1hPKJaBo84JGjntLj2ryo"          # 본인 값으로 변경
secret = "H3EZsOHt89ELjJvShNe5xA7KN7xHO8QcgMvIjSI7"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-DOGE"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
