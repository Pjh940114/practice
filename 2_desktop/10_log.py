import logging

# logging.(DEBUG) 레벨 조정가능 (아래 주석 참고)
# logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s [%(levelname)s] %(message)s")

# # debug < info < warning < error < critical
# logging.debug("아 이거 누가 짠거야")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 조금 오래 되었습니다. 실행상에 문제가 있을 수 있습니다.")
# logging.error("에러가 발생하였습니다.")
# logging.critical("복구가 불가능한 심각한 문제가 발생했습니다...")

# 터미널과 파일에 함께 로그 남기기
from datetime import datetime 

# 시간 [로그레벨] 메시지 형태로 로그를 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
#로그 레벨 설정
logger.setLevel(logging.DEBUG)

#스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

#파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log") # mylogfile_20220212193000
fileHandler = logging.FileHandler(filename, encoding="UTF-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트")