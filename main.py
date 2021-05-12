'''
Task 1
A Person class
Make a class called Person. Make the __init__() method take firstname, lastname,
and age as parameters and add them as attributes.
Make another method called talk() which makes prints a greeting from the person containing,
 for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:
    def __init__(self, firstname, lastname, age):
        self.f = firstname
        self.l = lastname
        self.a = age

    def talk(self, f, l, a):
        print(f'Hello my name is {f} {l} and I am {a} years old')


if __name__ == '__main__':
    person = Person(input("enter your firstname"), input("enter your lastname"), input("enter your age"))
    person.talk(person.f, person.l, person.a)
'''


"""
Task 2
Doggy age
Create a class Dog with class attribute `age_factor` equals to 7. 
Make __init__() which takes values for a dog’s age. 
Then create a method `human_age` which returns the dog’s age in human equivalent.
class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        while True:
            try:
                dog_age = int(dog_age)
                break
            except ValueError:
                print("age should be digital")
                dog_age = input("enter dogs age")
        self.d_a = dog_age

    def human_age(self, d_a, age_factor):
        self.h_a = d_a * age_factor
        return self.h_a


if __name__ == '__main__':
    dog = Dog(input("enter dogs age"))
    print(dog.human_age(dog.d_a, dog.age_factor))
"""



"""
Task 3

TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel.
 If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - 
the number N or the string 'name' and returns "Yes", if the channel N or 'name' 
exists in the list, or "No" - in the other case.
 The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.
"""
CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    ch = 0
    def __init__(self, channels):
        self.ch = channels

    def first_channel(self):
        self.ch = CHANNELS[0]
        return self.ch

    def last_channel(self):
        self.ch = CHANNELS[len(CHANNELS) - 1]
        return self.ch

    def turn_channel(self, N):
        while True:
            try:
                N = int(N)
                break
            except ValueError:
                print("number of channel should be digital")
                N = input("enter number of channel")
        N -= 1
        if N < len(CHANNELS) and N >= 0:
            self.ch = CHANNELS[N]
            return self.ch
    def next_channel(self, channel ):
        channel = str(channel)
        n = CHANNELS.index(channel)
        if n == len(CHANNELS) - 1:
            self.ch = CHANNELS[0]
        else:
            self.ch = CHANNELS[n + 1]
        return self.ch
    def previous_channel(self, channel):
        channel = str(channel)
        n = CHANNELS.index(channel)
        if n == 0:
            self.ch = CHANNELS[len(CHANNELS) - 1]
        else:
            self.ch = CHANNELS[n - 1]
        return self.ch
    def current_cannel(self, ch):
        self.ch = ch
        return self.ch
    def is_exist(self, n):
        try:
            n = int(n)
            n -=1
            if n in range(len(CHANNELS)):
                return "Yes"
            else:
                return "No"
        except ValueError:
            if n in CHANNELS:
                return "Yes"
            else:
                return "No"


if __name__ == '__main__':
    controller = TVController(CHANNELS)
    controller.first_channel()
    controller.last_channel()
    print(controller.turn_channel(input("enter number of channel")))
    print(controller.next_channel(controller.ch))
    print(controller.current_cannel(controller.ch))
    print(controller.is_exist(input("enter number or name")))


