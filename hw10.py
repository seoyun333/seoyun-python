import os
import pickle

filename = "score.bin"
scores = []

if os.path.exists(filename):
    print("[파일 읽기]")
    with open(filename, "rb") as f:
        scores = pickle.load(f)
else:
    print("[점수 입력]")
    i = 1
    while True:
        score = int(input(f"#{i}? "))
        if score >= 0:
            scores.append(score)
            i += 1
        else:
            break
 
    with open(filename, "wb") as f:
        pickle.dump(scores, f)


print("\n[점수 출력]")
total = sum(scores)
avg = total / len(scores) if scores else 0
print("개인 점수:", *scores)
print(f"평균: {avg:.1f}")
