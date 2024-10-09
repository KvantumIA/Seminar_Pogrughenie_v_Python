from Seminar_Pogrugenie_v_Python.Seminar_10_OOP.HW.HW_Testirovanie.Task_1.People import \
    People


class Child(People):
    def __init__(self, name, age, calm):
        super().__init__(name, age)
        self.feed = True    # Состояние голода
        self.calm = calm    # Состояние спокойствия

    def __repr__(self):
        return f'Child("{self.name}", "{self.age}", "{self.feed}", "{self.calm}")'

    def __str__(self):
        return f'Ребенок {self.name}, {self.age} в состоянии спокойствия - {self.calm}, голоден - {self.feed}'

    def __setattr__(self, age, value: int):
        if age == 'age':
            if value < 16:
                super().__setattr__(age, value)
            else:
                raise ValueError(f'Возраст ребенка должен быть меньше 16 лет. У вас {value}')
            
