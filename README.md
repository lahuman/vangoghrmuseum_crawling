# vangoghrmuseum_crawling

[고흐의 그림 1,000점을 무료로 다운받을 수 있는 오픈컬처닷컴](https://ppss.kr/archives/170443) 라는 글을 보고 해당 사이트에 가보니 그림이 참 많았다.

하지만 아쉬운 부분은 이미지를 하나씩만 다운로드를 지원하지 않았다.
~~~어쩌면 당연한 걸지도~~~

그래서 간단하게 다운로드 하는 크롤러를 개발했다.


## 언어 및 환경
 - Python 2.7.x
 - Linux 환경에서 동작
 - requirements.txt 설치
 
## 설정
index.py 에서 다른 이미지를 다운로드 하고 싶다면, 9 라인의 URL을 수정 해야 한다.
현재는 반고흐의 모든 이미지를 받도록 설정 되어 있다.

~~~
# 9 LINE
LIST_URL = BASE_URL+'/en/search/collection?q=&artist=Vincent%20van%20Gogh&pagesize=996'
~~~


### 실행
~~~
python index.py
~~~

## 참고 사이트
- [고흐의 그림 1,000점을 무료로 다운받을 수 있는 오픈컬처닷컴](https://ppss.kr/archives/170443)
- [파이썬으로 크롤링 하기
](https://medium.com/@mjhans83/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%98%EA%B8%B0-908e78ee09e0)
- [How do I download a file over HTTP using Python?](https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python)

## License

This project is licensed under the GPL License - see the [WIKI-LICENSE](https://en.wikipedia.org/wiki/GNU_General_Public_License) file for details