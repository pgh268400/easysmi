from setuptools import setup, find_packages

setup(
    # 배포할 패키지의 이름을 적어줍니다. setup.py파일을 가지는 폴더 이름과 동일하게 합니다.
    name='easysmi',
    # 배포할 패키지의 버전을 적어줍니다. 첫 등록이므로 0.1 또는 0.0.1을 사용합니다.
    version='0.0.7',
    # 배포할 패키지에 대한 설명을 작성합니다.
    description='smi 자막을 파싱하고 간편하게 다룰 수 있는 라이브러리 입니다. 특정 텍스트 위치를 찾아서 그 부분부터 싱크 조절이 가능합니다.',
    # 배포하는 사람의 이름을 작성합니다.
    author='pgh268400',
    # 배포하는 사람의 메일주소를 작성합니다.
    author_email='pgh268400@naver.com',
    # 배포하는 패키지의 url을 적어줍니다. 보통 github 링크를 적습니다.
    url='https://github.com/pgh268400/easysmi',
    # 배포하는 패키지의 다운로드 url을 적어줍니다.
    download_url='https://github.com/pgh268400/easysmi/archive/refs/heads/main.zip',
    # 해당 패키지를 사용하기 위해 필요한 패키지를 적어줍니다. ex. install_requires= ['numpy', 'django']
    # 여기에 적어준 패키지는 현재 패키지를 install할때 함께 install됩니다.
    install_requires=['chardet'],
    # 등록하고자 하는 패키지를 적는 곳입니다.
    # 우리는 find_packages 라이브러리를 이용하기 때문에 아래와 같이 적어줍니다.
    # 만약 제외하고자 하는 파일이 있다면 exclude에 적어줍니다.
    packages=find_packages(exclude=[]),
    # 패키지의 키워드를 적습니다.
    keywords=['smi sync'],
    # 해당 패키지를 사용하기 위해 필요한 파이썬 버전을 적습니다.
    python_requires='>=3',
    # 파이썬 파일이 아닌 다른 파일을 포함시키고 싶다면 package_data에 포함시켜야 합니다.
    package_data={},
    # 위의 package_data에 대한 설정을 하였다면 zip_safe설정도 해주어야 합니다.
    zip_safe=False,
    # PyPI에 등록될 메타 데이터를 설정합니다.
    # 이는 단순히 PyPI에 등록되는 메타 데이터일 뿐이고, 실제 빌드에는 영향을 주지 않습니다.
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
