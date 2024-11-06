from datetime import datetime
import pytz



def korean_now(format_ = '%Y-%m-%d %H:%M:%S'):
    korea_tz = pytz.timezone('Asia/Seoul')
    return datetime.now(korea_tz).strftime(format_)



if __name__ == "__main__":
    now = korean_now()
    print(now)