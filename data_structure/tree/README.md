# Tree 자료구조 

- 트리 자료구조를 정리하고 구체적인 객체로 구현합니다.

## B+Tree

- [Issue #16 B+Tree 구현하기](https://github.com/16-SulGore/Algorithm/issues/16)
- [참고](https://gist.github.com/savarin/69acd246302567395f65ad6b97ee503d)
- [개념정리](https://sulgore.notion.site/B-Tree-5cd11e0d38064c00a3d835d1407c763a)
- 출력 예시
    ```python
    # 출력 형식
    출력1: 전위 순회
    [10, 16], [1,3], [5], [12], [10], [12, 13], [17], [16], [17, 18]

    출력2: 리프노드 선형 탐색
    [1, 3], 5, 10, [12, 13], [16], [17, 18]
    1, 3, 5, 10, 12, 13, 16, 17, 18
    ```
