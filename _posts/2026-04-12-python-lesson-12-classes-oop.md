---
layout: post
title: "클래스와 객체 지향 프로그래밍"
date: 2026-04-12 05:54:04
categories: [파이썬 강의]
---

# 12강: 클래스와 객체 지향 프로그래밍

안녕하세요! 이번에는 파이썬의 핵심 개념 중 하나인 '클래스와 객체 지향 프로그래밍'에 대해 알아보겠습니다. 이 강좌에서는 기본적인 개념부터 실제 코드 예제까지 구체적으로 다룰 것이며, 초보자분들이 쉽게 이해할 수 있도록 설명하겠습니다.

## 1. 클래스란 무엇인가요?

클래스는 객체를 만드는 틀이라고 생각하시면 됩니다. 클래스 안에는 데이터(속성)와 동작(메서드)이 정의되어 있습니다. 이를 통해 여러 개의 비슷한 객체를 쉽게 만들 수 있게 해줍니다.

## 2. 객체란 무엇인가요?

객체는 클래스의 인스턴스라고도 합니다. 클래스에서 정의된 속성과 메서드를 실제로 사용할 수 있는 구체적인 사례를 말합니다.

## 3. 클래스와 객체 생성하기

클래스를 만들고 객체를 생성하는 과정을 살펴보겠습니다.

### 예제 코드: 기본 클래스 생성

```python
# Person 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"안녕하세요. 제 이름은 {self.name}이고 나이는 {self.age}살입니다.")

# 객체 생성
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 메서드 호출
person1.introduce()
person2.introduce()
```

## 4. 클래스의 특징: 상속과 다형성

### 4-1. 상속(Inheritance)

상속은 이미 정의된 클래스를 기반으로 새로운 클래스를 만드는 것을 말합니다. 이는 코드 재사용성을 높이고 프로그램 구조를 명확하게 하게 도와줍니다.

#### 예제 코드: 상속

```python
# 부모 클래스
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# 자식 클래스
class Dog(Animal):
    def speak(self):
        return f"{self.name}는 멍멍합니다!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}는 мя우릅니다!"

# 객체 생성
dog = Dog("토이")
cat = Cat("나비")

print(dog.speak())
print(cat.speak())
```

### 4-2. 다형성(Polymorphism)

다형성은 같은 이름의 메서드가 다른 동작을 할 수 있게 해주는 개념입니다. 이를 통해 코드의 유연성을 높일 수 있습니다.

#### 예제 코드: 다형성

```python
# 부모 클래스
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# 자식 클래스들
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    import math
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.math.pi * (self.radius ** 2)

# 객체 생성
rect = Rectangle(3, 4)
circle = Circle(5)

print(f"사각형의 넓이: {rect.area()}")
print(f"원의 넓이: {circle.area()}")
```

## 5. 클래스 변수와 인스턴스 변수

클래스 변수는 모든 객체가 공유하는 변수이고, 인스턴스 변수는 각 객체별로 독립적으로 저장되는 변수입니다.

### 예제 코드: 클래스 변수와 인스턴스 변수

```python
# 클래스 변수 예제
class Counter:
    count = 0  # 클래스 변수
    
    def __init__(self):
        Counter.count += 1  # 클래스 변수 접근
    
    @classmethod
    def get_count(cls):
        return cls.count

obj1 = Counter()
obj2 = Counter()

print(Counter.get_count())  # 출력: 2

# 인스턴스 변수 예제
class Car:
    def __init__(self, model):
        self.model = model  # 인스턴스 변수
    
    def display_model(self):
        print(f"차종은 {self.model}입니다.")

car1 = Car("Sedan")
car2 = Car("SUV")

car1.display_model()  # 출력: 차종은 Sedan입니다.
car2.display_model()  # 출력: 차종은 SUV입니다.
```

## 결론

클래스와 객체 지향 프로그래밍은 파이썬에서 매우 중요한 개념입니다. 이를 통해 코드를 더 효율적이고 재사용 가능하게 만들 수 있습니다. 이번 강좌에서는 기본적인 클래스 및 객체 생성부터 상속과 다형성까지 다양한 개념을 살펴보았습니다. 앞으로도 클래스와 객체 지향 프로그래밍에 대해 더 깊이 있게 알아가면서, 더욱 복잡한 프로그램을 구현해 보시기 바랍니다.

만약 이번 강좌에서 이해하지 못한 부분이 있다면 언제든지 질문해 주세요! 기꺼이 도움드리겠습니다.

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
