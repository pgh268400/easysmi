@REM 기존 업로드된 build, dist, easysmi.egg-info 폴더 삭제
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q easysmi.egg-info

@REM 빌드
python setup.py sdist bdist_wheel