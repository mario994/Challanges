function solution(A, K) {
    let answer;
    if (A.length == 0 || A.length == K) {
        answer = A;
    } else {
        let arr = A;
        for (let i = 0; i < K; i++) {
            let valueMoved = arr.pop();
            arr.unshift(valueMoved);
        }
        answer = arr;
    }
    return answer;
}