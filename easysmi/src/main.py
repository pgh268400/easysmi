import copy
import re
import chardet
from ..types.type import ParsedSMI, MainSMIData


'''
Author: pgh268400 (https://pgh268400.tistory.com/)
Version: 1.0
License: MIT License
'''

# smi 파싱할 정규식
# <Sync Start=(시작 시간)><P Class=(자막 언어)>(자막 내용) 형태를 매칭시킨다.
# 그룹 1 -> 시작 시간
# 그룹 2 -> 자막 언어
# 그룹 3 -> 자막 내용
# 그룹 3의 경우 꺾쇠를 포함하지 않으면서,
# <Sync 나 <\BODY 를 포함하지 않는 모든 문자열을 매칭시켜서, 자막 내용을 추출한다.
# 이유는 정확히 모르겠지만 꺾쇠를 포함시키지 않는 [^<] 문구를 넣지 않으면 자막 내용이 제대로 매칭되지 않는다.
SMI_REGEX = r'<\s*Sync\s*Start\s*=\s*(\d+)\s*>\s*<\s*P\s*Class\s*=\s*(\w+)\s*>\s*([^<](?!<\s*Sync|<\/\s*BODY).*)'

def read_file(path : str) -> str:
    #파일 열어서 인코딩 확인
    rawdata = open(path, 'rb').read()
    result = chardet.detect(rawdata)
    enc = result['encoding']
    
    #인코딩 맞게 열기
    f = open(path, "r", encoding = enc)
    line = f.readline()

    data = ""
    while line:
        data += line
        line = f.readline()
    f.close()
    return data

#raw_data => 자막 파일 텍스트 데이터
def parse_smi(path : str) -> ParsedSMI:
    # 파일을 읽어서 raw_data에 저장한다.
    raw_data = read_file(path)

    main : list[MainSMIData]= []
    texts : list[str] = []

    # 통합된 정규식을 통해 자막 언어, 타임라인, 대사를 일괄 추출한다.
    p = re.compile(SMI_REGEX, re.MULTILINE)
    total = p.findall(raw_data)

    # element : (시작 시간, 자막 언어, 자막 내용) 형태의 튜플
    for element in total:
        timeline, type, text = element
        main.append(MainSMIData(timeline=timeline, text=text))
        # 처리하면서 text에도 저장한다.
        texts.append(text)

    # 자막 언어 추출
    type = total[0][1]

    #데이터 정리
    result = ParsedSMI(orig=path,main=main, raw=raw_data, text=texts, lines=len(main), type = type)
    
    return result


#텍스트로 파싱된 라인 찾기
def find_line_by_text(parsed_data : ParsedSMI, target_text : str) -> int:
    main = parsed_data.main
    for i, element in enumerate(main):
        if target_text in element.text:
            return i
    return -1

#정규식으로 파싱된 라인 찾기
def find_line_by_regex(parsed_data : ParsedSMI, pattern : str) -> int:
    main = parsed_data.main
    for i, element in enumerate(main):
        m = re.search(pattern, element.text)
        if m : return i
    return -1


# 싱크 조절을 위해 실제로 사용하는 함수
def sync_shift(parsed_data: ParsedSMI, start_idx: int, end_idx: int, shift_amount: int, after_start=True, ranged_mode = False) -> ParsedSMI:
    # 참고 : 건드는 것은 main 항목뿐이다. 나머지는 그대로 둔다.

    # parsed_data 는 Class Type 이므로 복사본을 만들어서 건드린다. (깊은 복사 수행)
    copy_parsed_data = copy.deepcopy(parsed_data)

    for i, element in enumerate(copy_parsed_data.main):
        # 범위 모드일 경우 start_idx ~ end_idx 사이의 항목만 건드린다. 
        # [범위 모드일때는 after_start 값에 영향을 받지 않는다.]
        if ranged_mode:
            if (i >= start_idx) and (i <= end_idx):
                element.timeline = str(int(element.timeline) + shift_amount)
        # 범위 모드가 아닐 경우, after_start에 따라서 start_idx 이후, end_idx 이전의 항목만 건드린다.
        else:
            if (after_start and i >= start_idx) or (not after_start and i <= end_idx):
                element.timeline = str(int(element.timeline) + shift_amount)
    
    # 복사본을 리턴한다
    return copy_parsed_data


# 특정 인덱스 이후로 싱크 일괄 조절

# parsed_data => parse_smi 의 output으로 나온 리스트 데이터
# start_line => 몇번째 항목부터 옮길 것인지. (0번째부터 시작)
# shift_amount => 얼마만큼 싱크 조절할 것인지. (-1000 -> 1초 빨리 나오게 하기, 10000 -> 10초 늦게 나오게 하기)
def sync_shift_after_specific_index(parsed_data: ParsedSMI, start_line_idx: int, shift_amount: int) -> ParsedSMI:
    return sync_shift(parsed_data, start_line_idx, 0, shift_amount, after_start=True)

# 특정 인덱스 이전으로 싱크 일괄 조절
def sync_shift_before_specific_index(parsed_data: ParsedSMI, end_line_idx: int, shift_amount: int) -> ParsedSMI:
    return sync_shift(parsed_data, 0, end_line_idx, shift_amount, after_start=False)

# 특정 인덱스 범위에서 싱크 일괄 조절
def sync_shift_in_specific_range(parsed_data: ParsedSMI, start_line_idx: int, end_line_idx: int, shift_amount: int) -> ParsedSMI:
    return sync_shift(parsed_data, start_line_idx, end_line_idx, shift_amount, ranged_mode=True)

# 원본을 바꾸는 함수 (Call by Ref)
def remove_line(parsed_data : ParsedSMI, idx : int) -> ParsedSMI:
    parsed_data.main.pop(idx)
    parsed_data.lines = len(parsed_data.main)
    return parsed_data

#path => 파일 저장 경로
#shifted_data => 덮어 씌울 싱크 작업된 parsed_data
def smi_file_save(path : str, shifted_data : ParsedSMI):
    raw = shifted_data.raw
    try:
        #싱크 작업된 데이터를 SMI 문자열로 변환한다.
        smi_data = "\n"
        for element in shifted_data.main:
            smi_data += f"<Sync Start={element.timeline}><P Class={shifted_data.type}>\n{element.text}\n"

        # 정규표현식을 사용하여 BODY 태그 사이의 내용을 찾고, 그 안에 있는 내용을 작업한 내용으로 대체한다.
        match = re.search(r'<BODY>(.*?)<\/BODY>', raw, re.DOTALL)

        if match:
            body_content = match.group(1)  # BODY 태그 안의 내용
            output = raw.replace(body_content, smi_data)  # BODY 태그 안의 내용을 치환한다.
        else:
            raise Exception('BODY 태그를 찾을 수 없습니다.')
        
        # 수정된 문자열을 파일로 저장한다.
        f = open(path, "w", encoding='utf-8')
        f.write(output)
        f.close()
        return True
    except Exception as e:
        raise e