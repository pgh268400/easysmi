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
**text**는 리스트 형태로 텍스트 만을 추출합니다.
* 해당 라이브러리에서는 줄 갯수를 대사마다 한줄씩 새는 것이 아닌 한 싱크에 표시되는 항목을 한 줄로 인식합니다.  
  ex) 어떤 영상 1:00에서 5줄, 10줄인 대사가 나와도 1줄(1개의 항목)로 생각합니다.

<br/>

**자막이 10초 늦게 나올때 (-10초 만큼 땡김)**

```python
path = "C:/[SubsPlease] Tokyo Revengers - 01.smi"
p = parse_smi(path)
s = sync_shift(p, 0, -10000) #0번째(첫번째)라인부터 끝까지 -10초
```



**자막이 10초 빨리 나올때 (+10초 만큼 지연)**

```python
path = "C:/[SubsPlease] Tokyo Revengers - 01.smi"
p = parse_smi(path)
s = sync_shift(p, 0, 10000) #0번째(첫번째)라인부터 끝까지 +10초
```



**작업한 자막 파일 저장 방법**

```python
path = "C:/test.smi"
p = parse_smi(path)
s = sync_shift(p, 0, 2000)

new_path = "enter_your_save_path_here"
file_save(new_path, s)
```



## S(sponsored) 자막을 NS(non-sponsored) 자막으로 쉽게 바꾸기

애니메이션을 보다 보면 영상 시작전 10초 정도 다음과 같은 화면에서 스폰서(후원자)가 표시되고 영상이 진행되는 경우가 많습니다. 

보통 방영중인 애니메이션이 한참 방영중일때는 릴그룹이 방영중인 TV영상을 파일로 변환해서 배포하기 때문에 자막 작업 하시는 분들도 이 스폰서가 중간에 껴있는걸 기준으로 작업하시는 경우가 많습니다.  

(이렇게 스폰서가 껴있고 빠른 Release로 유명한 그룹이 Ohys-Raws)



그런데 시간이 지나면서 BD판이 뜨고, 편집본이 뜨다보면 중간에 스폰서가 편집상 사라지는 경우가 99%인데 스폰서를 기준으로 작업한 것은 싱크가 10초정도 어긋나게 됩니다. 
