- 정규표현식(Regular Expressions)은 복잡한 문자열을 처리할 때 사용하는 기법으로, 파이썬만의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용한다.

1. 문자클래스 []
- [] 사이의 문자들과 매치

ex) 
정규식 [abc]는 문자열 'a'와 일치하는 문자인 'a'가 있으므로 매치된다.
정규식 [abc]는 문자열 'before'과 일치하는 문자인 'b'가 있으므로 매치된다.
정규식 [abc]는 문자열 'dude'와 일치하는 문자가 하나도 없으므로 매치되지 않는다.

[]안의 두 문자 사이에 - 를 넣으면 문자사이의 범위를 의미한다.
[a-c]는 [abc]와 동일하고 
[0-5]는 [012345]와 동일하다





2. 반복 +
- 반복을 나타내는 메타 문자 +는 바로 앞의 문자가 최소 한 번 이상 반복될 때 사용한다.

ex)
정규식 'ca+t'는 문자열 ct와 'a'가 0번 매치되므로 매치되지 않는다.
정규식 'ca+t'는 문자열 cat와 'a'가 1번 매치되므로 매치된다.
정규식 'ca+t'는 문자열 caaaat와 'a'가 3번 매치되므로 매치된다.



3. match 메서드는 문자열의 처음부터 정규식과 매치되는지 조사한다.