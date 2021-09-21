# easysmi
- The following libraries make it easy to handle smi files.
- 다음 라이브러리를 사용하면 간편하게 smi 파일의 싱크를 조절 할 수 있습니다.

## install
```python
pip install git+https://github.com/pgh268400/easysmi
```
다음 명령어를 입력하여 라이브러리를 설치합니다.



```python
pip uninstall easysmi
```

설치를 했는데 문제가 발생해서 제거해야 하는 경우는 다음 명령어를 입력 합니다.

## How to Use
```python
path = "C:/[SubsPlease] Tokyo Revengers - 01.smi"
p = parse_smi(path)
```
우선 다음과 같이 열 파일의 자막 경로를 parse_smi에 인자값으로 제공하여 smi를 파싱합니다.

```python
print(p['line'])
print(p['main'][0:10])
print(p['text'][0:10])
```
해당 명령어로 파싱된 smi의 다양한 정보를 가져올 수 있습니다.  
**line**은 총 줄 갯수, **main**은 리스트 형태로 SMI의 싱크, 그 싱크에 표시되는 텍스트를 한번에 추출하고  
**text**는 SMI의 리스트 형태로 텍스트 만을 추출합니다.
* 해당 라이브러리에서는 줄 갯수를 대사마다 한줄씩 새는 것이 아닌 한 싱크에 표시되는 항목을 한 줄로 인식합니다.  
ex) 어떤 영상 1:00에서 5줄, 10줄인 대사가 나와도 1줄(1개의 항목)로 생각합니다.
