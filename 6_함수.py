#6_함수.py
#%%
#(1) 원의 넓이를 구하는 함수
def getCircleArea(r) : #매개변수 r은 반지름 값
    return r*r*3.14159

area1 = getCircleArea(10)
area2 = getCircleArea(4.2)
print(area1, area2)

#(2) 삼각형의 넓이를 구하는 함수
def getTriangleArea(base, height) :
    return base*height/2
area1 = getTriangleArea(3, 4)
area2 = getTriangleArea(5.1, 6.3)
# area2 = getTriangleArea("3", "5") 
print(area1, area2)

#(3) 출력이 없는 함수
def say_myself(name, age, man) :
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는 {age}입니다.')
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")

say_myself('홍길동', 30, True)
a = say_myself('김하나', 24, False)
print(a)
#%%
#함수의 매개변수 디폴트 값 설정
#디폴트 값을 설정한 매개변수는 함수의 입력 매개변수들 중 끝에 배치
def say_myself(name, age=-1, man=True) :
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는 {age}입니다.')
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")
say_myself("홍길동", 30) #man 매개변수 생략 가능
say_myself("김하나", man=False, age=27) #매개변수 이름으로 값 지정
say_myself("김현수")

def say_myself(name="", age=" ", man=True) :
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는 {age}입니다.')
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")

# %%
# 함수의 호출 방식
# (1) 매개변수에 값이 복사되어 호출 (Call by Value)
# (2) 매개변수에 주소값이 복사되어 호출 (Call by Reference)

# (1) 예제
def testFunc(num) :
    num = 5

num = 10
testFunc(num)
print(num)

# (2) 예제
def testFunc(numList) :
    numList.append(10)
    print(id(numList))
    numList[0] = -100

aList = [1,2,3]
testFunc(aList)
print(id(aList)) #aList의 주소값 1992250365184
print(aList) #[-100, 2, 3, 10]

# (3) 함수 내에서 함수 밖의 변수(기본타입 변수)를 사용하고 싶은 경우
def testFunc(num2) :
    global num 
    num = 100

num = 10
testFunc(num)
print(num)

# %%
# 함수의 가변 인수
# 가변인수 : 매개변수의 개수가 정해져 있지 않고 사용하는 인수
#Ex) print(1,2,3,4,5)
def testFunc(*arg) : 
    print(arg)
    return sum(arg)

print(testFunc(10,20,30,40))

#일반 매개변수와 가변인수가 같이 사용될 경우
#가변인수를 마지막 인수로 넣어줘야한다.
def testFunc(str1, str2, *nums) : 
    print(str1, str2, nums)
    return sum(nums)

print(testFunc("Hi", "Bye", 10,20,30))

# %%
# 재귀 함수 : 자기 함수를 다시 호출하는 함수

def recursive(num=0) :
    print(f"{num} 재귀 함수를 호출합니다.")
    recursive(num+1)
recursive(0)
#재귀함수는 반드시 종료조건을 명시해야한다.
# %%
def recursive(num=0) :
    print(f"{num} 재귀 함수를 호출합니다.")
    if num==100:
        return  #함수는 return 문을 실행하면 종료
    recursive(num+1)
recursive(0)
# %%
# 재귀함수활용
# (1) 팩토리얼
# ex) 5! = 5*4*3*2*1

def factorial(n) :
    result = 1
    for i in range(1, n+1) :
        result *= i
    return result
print(factorial(5))

def factorial2(n) :
    if n <= 1 :
        return 1
    return n*factorial(n-1)
print(factorial2(5))
#5*factorial2(4)
#5*4*factorial2(3)
#5*4*3*factorial2(2)
#5*4*3*2*factorial2(1)
#5*4*3*2*1 종료

# %%
#(2) 피보나치 수열
# 1 1 2 3 5 8 13 ......
fibo = [0,1]
n = 5 
for i in range(2, n+1) :
    fibo.append(fibo[i-1] + fibo[i-2])
print(fibo)
print(fibo[-1])

def fiboFunc(n) :
    if n==1 or n==2 :
        return 1
    else :
        return fiboFunc(n-1) + fiboFunc(n-2)
print(fiboFunc(5))

    #                  fiboFunc(5)
    #             fiboFunc(4)+fiboFunc(3)
    #      fiboFunc(3)+fiboFunc(2) + fiboFunc(2)+fiboFunc(1)
    # fiboFunc(2)+fiboFunc(1)
#%% 리스트의 평균값 구하는 함수
numList = [1,2,3,4]
avg = sum(numList) / len(numList)

def getListAvg(numList) :
    return sum(numList) / len(numList)
print(getListAvg([1,2,3,4,5]))
numList = [2,4,5]
print(getListAvg(numList))
print(getListAvg(num_list))

# %%
# 합성 저항 구하는 함수
def getTotalResis(rList, serial=True) :
    if serial :
        return sum(rList)
    else :
        result = 0
        for r in rList :
            result += 1/r
        return 1/result
    
#serial = True  직렬저항 값 리턴
#serial = False 병렬저항 값 리턴
#직렬저항 = 저항1+저항2+저항3+....
#병렬저항 = 1/(1/저항1 + 1/저항2 + 1/저항3 + ...)

print(getTotalResis([1,2,3,4])) #직렬저항
print(getTotalResis([1,2,3,4], False)) #병렬저항

