# easysmi

- The following libraries make it easy to handle smi files.
- 다음 라이브러리를 사용하면 간편하게 smi 파일의 싱크를 조절 할 수 있습니다.
- 타입 힌트를 지원합니다. (Type-Safety)

## install

```python
pip install easysmi
```

다음 명령어를 입력하여 라이브러리를 설치합니다.

```python
pip uninstall easysmi
```

설치를 했는데 문제가 발생해서 제거해야 하는 경우는 다음 명령어를 입력 합니다.

## How to Use

```h
<SAMI>
<HEAD>
<Title></Title>
<STYLE TYPE="text/css">
</STYLE>
</HEAD>

<BODY>
<Sync Start=1000><P Class=KRCC>
&nbsp;
<Sync Start=2000><P Class=KRCC>
&nbsp;
<Sync Start=3000><P Class=KRCC>
&nbsp;
<Sync Start=4000><P Class=KRCC>&nbsp;
<Sync Start=5000><P Class=KRCC>&nbsp;
</BODY>
</SAMI>
```

사용법을 알아보기 위해 위와 같은 간단한 smi 파일로 테스트 해보겠습니다.  
BODY 이외의 내용이 비어있으나 본 라이브러리는 BODY 부분을 위주로 파싱하기 때문에 큰 문제가 없습니다.  
파일 명은 `test.smi`로 가정합니다.

```python
from easysmi import *
path = "./test.smi"
p = parse_smi(path)
```

우선 다음과 같이 열 파일의 자막 경로를 parse_smi에 인자값으로 제공하여 smi를 파싱합니다.  
parse_smi 함수는 경로로 제공된 smi 파일을 파싱하고 `ParsedSMI` 라는 객체로 반환합니다.  
우리는 제공된 라이브러리 함수와 `ParsedSMI` 객체를 잘 조작해서 자막을 수정하면 됩니다.

```python
from pprint import pprint
from easysmi import *

path = "./test.smi"
p = parse_smi(path)
pprint(p)

/////////////////////////////////////////////////////////////////////
ParsedSMI(orig='./test.smi',
          main=[MainSMIData(timeline='1000', text='&nbsp;'),
                MainSMIData(timeline='2000', text='&nbsp;'),
                MainSMIData(timeline='3000', text='&nbsp;'),
                MainSMIData(timeline='4000', text='&nbsp;'),
                MainSMIData(timeline='5000', text='&nbsp;')],
          raw='<SAMI>\n'
              '<HEAD>\n'
              '<Title></Title>\n'
              '<STYLE TYPE="text/css">\n'
              '</STYLE>\n'
              '</HEAD>\n'
              '\n'
              '<BODY>\n'
              '<Sync Start=1000><P Class=KRCC>\n'
              '&nbsp;\n'
              '<Sync Start=2000><P Class=KRCC>\n'
              '&nbsp;\n'
              '<Sync Start=3000><P Class=KRCC>\n'
              '&nbsp;\n'
              '<Sync Start=4000><P Class=KRCC>&nbsp;\n'
              '<Sync Start=5000><P Class=KRCC>&nbsp;\n'
              '</BODY>\n'
              '</SAMI>',
          text=['&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;'],
          lines=5,
          type='KRCC')
```

ParsedSMI 객체는 smi의 다양한 정보를 가지고 있습니다.  
`pprint(p)` 로 출력을 해보면 다음과 같이 자막의 내용이 객체 내부에 제대로 파싱된 것을 확인할 수 있습니다.
다음 예제에서는 출력이 잘 보이게 하기 위해 pprint 라이브러리를 사용하겠습니다.  
pprint는 필요한 분들만 사용하시면 됩니다. print로 출력해도 무관합니다. (선택)

```python
# 원본 자막 파일 경로
pprint(p.orig)
>>> './test.smi'
```

```python
# 자막 메인 데이터
pprint(p.main)

>>>
[MainSMIData(timeline='1000', text='&nbsp;'),
 MainSMIData(timeline='2000', text='&nbsp;'),
 MainSMIData(timeline='3000', text='&nbsp;'),
 MainSMIData(timeline='4000', text='&nbsp;'),
 MainSMIData(timeline='5000', text='&nbsp;')]
```

```python
# 자막 파일 내용 (RAW-TEXT)
pprint(p.raw)

>>>
('<SAMI>\n'
 '<HEAD>\n'
 '<Title></Title>\n'
 '<STYLE TYPE="text/css">\n'
 '</STYLE>\n'
 '</HEAD>\n'
 '\n'
 '<BODY>\n'
 '<Sync Start=1000><P Class=KRCC>\n'
 '&nbsp;\n'
 '<Sync Start=2000><P Class=KRCC>\n'
 '&nbsp;\n'
 '<Sync Start=3000><P Class=KRCC>\n'
 '&nbsp;\n'
 '<Sync Start=4000><P Class=KRCC>&nbsp;\n'
 '<Sync Start=5000><P Class=KRCC>&nbsp;\n'
 '</BODY>\n'
 '</SAMI>')
```

```python
# 자막 대사만 추출
pprint(p.text)
>>> ['&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;']
```

```python
# 자막 대사 갯 수(라인 수)
pprint(p.lines)
>>> 5
```

```python
# 자막 타입 (언어)
pprint(p.type)
>>> 'KRCC'
```

**orig**는 원본 자막 파일 경로(parse_smi에 제공한 경로), **main**은 SMI의 싱크, 그 싱크에 표시되는 텍스트를 한번에 추출하고 **raw**는 자막 파일의 내용입니다.
또한 **text**는 자막 파일에서 대사만 추출한 부분, **lines**은 총 줄 갯수,  
**type**은 자막 타입(언어) 입니다.

- 해당 라이브러리에서는 줄 갯수를 대사마다 한줄씩 새는 것이 아닌 한 싱크에 표시되는 항목을 한 줄로 인식합니다.  
  ex) 어떤 영상 1:00에서 5줄, 10줄인 대사가 나와도 1줄(1개의 항목)로 생각합니다.

```python
pprint(p.main)  # 모든 자막의 타임라인, 텍스트 가져오기 (배열)
pprint(p.main[0])  # 첫 번째 자막의 타임라인, 텍스트 가져오기
pprint(p.main[0:3])  # 0번째부터 2번째 줄의 자막의 타임라인, 텍스트 가져오기
```

참고로 본 라이브러리에서 가장 중요한 것은 ParsedSMI 에 담긴 main 이라는 변수(속성) 입니다. 자막 파싱 시 main 이외의 모든 속성들은 수정을 하더라도, 나중에 저장하는 함수를 사용 시 반영되지 않습니다. 따라서 자막에 무언가 수정을 가해야 할 때는 main 변수를 수정해야 합니다.

다만 꼭 main 변수를 직접 수정하지 않고 본 라이브러리에서 제공하는 함수들을 이용해 싱크 정도는 간편하게 조절할 수 있습니다.

<br/>

**sync_shift_after_specific_index()**

```python
# 특정 인덱스 이후로 싱크 일괄 조절
sync_shift_after_specific_index(p, x, y)
```

해당 함수는 자막의 x번째 줄 부터 끝까지 싱크를 y만큼 조정하는 함수입니다.  
참고로 해당 함수는 들어온 p(ParsedSMI) 의 원본을 변경하지 않고, p의 main 속성에서 y만큼 싱크를 조절한 p의 복사본을 반환합니다.

**sync_shift_before_specific_index**

```python
# 특정 인덱스 이전으로 싱크 일괄 조절
sync_shift_before_specific_index(p, x, y)
```

해당 함수는 자막의 0번째 줄부터 x번째 줄 까지 싱크를 y만큼 조정하는 함수입니다.  
참고로 해당 함수는 들어온 p(ParsedSMI) 의 원본을 변경하지 않고, p의 main 속성에서 y만큼 싱크를 조절한 p의 복사본을 반환합니다.

**자막이 10초 늦게 나올때 (-10초 만큼 땡김)**

```python
path = "C:/[SubsPlease] Tokyo Revengers - 01.smi"
p = parse_smi(path)

# 0번째(첫번째)라인부터 끝까지 -10초 조절
s = sync_shift_after_specific_index(p, 0, -10000)
```

**자막이 10초 빨리 나올때 (+10초 만큼 지연)**

```python
path = "C:/[SubsPlease] Tokyo Revengers - 01.smi"
p = parse_smi(path)

# 0번째(첫번째)라인부터 끝까지 +10초 조절
s = sync_shift_after_specific_index(p, 0, 10000)
```

**작업한 자막 파일 저장 방법**

```python
path = "C:/test.smi"
p = parse_smi(path)
s = sync_shift_after_specific_index(p, 0, 2000)

new_path = "enter_your_save_path_here"
smi_file_save(new_path, s)
```

**smi에서 첫번째 항목 제거**

```python
path = "C:/[SubsPlease] Tokyo Revengers - 01.smi"
p = parse_smi(path)
print(p['main'][0:5])
r = remove_line(p, 0) # 0번째 라인을 제거한다.
print(r['main'][0:5])
```

이 함수는 인자로 제공된 p 변수(ParsedSMI 객체)의 원본을 변경합니다. 리턴값은 삭제된 본인 p 변수 입니다.

## S(sponsored) 자막을 NS(non-sponsored) 자막으로 쉽게 바꾸기

![image](https://user-images.githubusercontent.com/31213158/134211650-89ec18d8-ef05-4a99-bdd4-f198b89b58d6.png)

애니메이션을 보다 보면 영상 시작전 10초 정도 다음과 같은 화면에서 스폰서(후원자)가 표시되고 영상이 진행되는 경우가 많습니다.

보통 방영중인 애니메이션이 한참 방영중일때는 릴그룹이 방영중인 TV영상을 파일로 변환해서 배포하기 때문에 자막 작업 하시는 분들도 이 스폰서가 중간에 껴있는걸 기준으로 작업하시는 경우가 많습니다.

(이렇게 스폰서가 껴있고 빠른 Release로 유명한 그룹이 Ohys-Raws)

그런데 시간이 지나면서 BD판이 뜨고, 편집본이 뜨다보면 중간에 스폰서가 편집상 사라지는 경우가 99%인데 스폰서를 기준으로 작업한 것은 싱크가 10초정도 어긋나게 됩니다.

보통 다음팟플레이어 같은 것으로 -10초를 하게 되면 싱크가 대부분 맞게 되는데 전체적으로 -10초 되는 것이기 때문에 앞의 오프닝의 싱크가 맞지 않는 불상사가 생깁니다. 물론 오프닝은 대부분 몇번만 보고 스킵하겠지만 저는 이게 불편해서 해당 라이브러리를 제작 했습니다.

```python
#단일 파일 처리

folder = 'C:/자막/'
filename = '[SubsPlease] Tokyo Revengers - 02 (1080p) [B66CEAA7].smi'

p = parse_smi(folder + filename)
search_line = find_line_by_text(p, "sub by")

if search_line != -1:
    s = sync_shift_after_specific_index(p, search_line, -10000)
    s = sync_shift_after_specific_index(s, 0, 1300)

    make_dirs(folder + 'output') #make output folder
    new_path = folder + "output/" + filename
    file_save(new_path, s)
else:
    print("cannot find item")
```

영상 자막이 (sub by 제작자)가 뜨고 나서 스폰서가 뜨는데 제가 받은 영상엔 스폰서가 없어서 싱크가 맞지 않습니다.

"sub by" 텍스트의 위치부터 자막 끝까지 -10초로 싱크를 조절하고 다시 전체적으로 +1.3초로 조정 한 뒤 output 폴더에 저장하는 예제입니다.

```python
find_line_by_text(p, "sub by")
```

find_line_by_text 함수는 파싱된 자막 데이터 내에서 인자로 들어온 string 값의 포함여부를 확인하고 그 line 위치를 반환합니다.

찾지 못한다면 -1을 반환 합니다.

```python
find_line_by_regex(p, "pattern"):
```

또한 정규식을 통한 검색도 지원 합니다. 단, 정규식에서 처음으로 match 된 string의 위치를 반환 합니다.

찾지 못한다면 -1을 반환 합니다.

지원되는 함수를 이용해 자유롭게 자막 작업을 하시길 바랍니다.

## 사용시 주의 할 점

위와 같이 특정 규칙에 따라 싱크를 조절 하는 방식은 어떤 영상의 경우엔 스폰서가 아예 없어서 이렇게 조절하면 오히려 싱크가 어긋날 수 있습니다.  
영상 시청 중 그런 문제가 발생시 다시 수동으로 조절하시거나 원래 자막으로 복구하시면 됩니다.  
그리고 웬만하면 해당 BD 자막이 존재하면 그걸 받아서 쓰는게 제일 좋습니다.

### Bug Report

버그 발견시 해당 Github 사이트 내의 Issues 탭을 이용해 제보 부탁드립니다.
또한 개선점도 제보 해주시면 좋습니다.
