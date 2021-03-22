import sys
import pprint

def get_natural_number():
    n=0
    while(n<=100):
        n+=1
        yield n

#return generator
#<generator object get_natural_number at 0x7ffa18930850>
print(get_natural_number())

#next로 추출
g = get_natural_number()
for _ in range(0,10):
    print(next(g))

'''
함수와의 차이점?
함수는 return을 마주치면 값을 리턴하고 실행 종료.
generator은 yield를 만나면 실행 중이던 값을 내보낸다는 의미이다.
즉 실행이 종료되지 않고 맨 끝에 도달할 때까지 계속 실행한다.

generator은 만들어 두고 필요할 때 사용하며, 특히 많은 데이터를 만들어두고 
그 중 일부만 사용할 때 효과적인 프로그래밍 방법이다.
'''

#range a는 생성완료, b는 생성에 대한 조건 -> generator방식을 이용하는 함수.
a_10000 = [n for n in range(10000)]
b_10000 = range(10000)

#a_10000: 87632 , b_10000: 48
print(sys.getsizeof(a_10000))
print(sys.getsizeof(b_10000))

#enumerate: 순서가 있는 자료형(list, set, tuple)을 인덱스를 포함한 enumerate 객체로 리턴한다.

list_a = ['a1', 'b2', 'c3']

for i in range(len(list_a)):
    print(i, list_a[i])
    
for i,v in enumerate(list_a):
    print(i,v)

#divmod: 몫과 나머지를 한 번에 구하는 함수
divmod(5,3)

#print 구분자: "sep="
print(1,2,3,sep=',')
#print list -> join
print(' '.join(list_a))

#format, f-string(upper python version 3.6+)
idx = 1
fruit ="Apple"

print('{0} : {1}'.format(idx+1, fruit))
print('{} : {}'.format(idx+1, fruit))
print(f'{idx+1} : {fruit}')

pprint.pprint(locals())
