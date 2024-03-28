from enum import Enum

# 선언 법
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# 액세스 하는법
print(Color.RED)  # Color.RED
print(Color['RED'])  # Color.RED
print(Color.RED.value)  # 1



# 선언법 2
State = Enum('State', 'new running sleeping restart zombie')
print(State.new)  # State.new
print(State['running'])  # State.running
print(State.restart.value)  # 4


# 쓰는 이유
# 가독성, 유지보수
country_li = ['Korea', 'USA', 'UK', 'China']
Country = Enum('Country', 'Korea, USA, UK, China')


# Key 덮어쓰기 방지
# Country = Enum('Country', 'Korea, USA, UK, China, Korea')
print(Country.USA.value)  # 2
country_dic = {'Korea': 1, 'USA': 2, 'UK': 3, 'China': 4, 'Korea': 5}
print(country_dic)  # {'Korea': 5, 'USA': 2, 'UK': 3, 'China': 4}
