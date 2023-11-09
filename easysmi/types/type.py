
from dataclasses import dataclass
from typing import Optional



# dataclass를 활용하면 데이터를 담을 수 있는 Class를 쉽게 만들 수 있다. (Type-Safety)

# ParsedSMI 에서 main 항목에 들어갈 데이터 타입
@dataclass
class MainSMIData:
    timeline: str
    text: str

# SMI 파싱 결과로 리턴할 Class 타입 
@dataclass
class ParsedSMI:
    orig: str
    main: list[MainSMIData]
    raw: str
    text: list[str]
    lines: int
    type: Optional[str]