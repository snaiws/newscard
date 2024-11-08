from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")  # 리눅스에서 필수적인 옵션
    chrome_options.add_argument("--disable-dev-shm-usage")  # 공유 메모리 문제 해결
    chrome_options.add_argument("--disable-gpu")  # GPU 비활성화 (옵션)
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver