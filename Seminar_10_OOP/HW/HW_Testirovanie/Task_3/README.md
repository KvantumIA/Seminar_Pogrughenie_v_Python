## Задача 3. Крестики-нолики
Создайте программу, которая реализует игру «Крестики-нолики».
Для этого напишите:

1. Класс, который будет описывать поле игры.
class Board:
 - Класс поля, который создаёт у себя экземпляры клетки.
- Пусть класс хранит информацию о состоянии поля (это может быть список из
девяти элементов).
- Помимо этого, класс должен содержать методы:
  - «Изменить состояние клетки». Метод получает номер клетки и, если клетка не
  занята, меняет её состояние. Если состояние удалось изменить, метод возвращает
  True, иначе возвращается False.
  - «Проверить окончание игры». Метод не получает входящих данных, но
  возвращает True/False. True — если один из игроков победил, False — если
  победителя нет.
2. Класс, который будет описывать одну клетку поля:
class Cell:
- Клетка, у которой есть значения:
- занята она или нет;
- номер клетки;
- символ, который клетка хранит (пустая, крестик, нолик).
3. Класс, который описывает поведение игрока:
class Player:
- У игрока может быть:
- имя,
- количество побед.
- Класс должен содержать метод:
  - «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер
  клетки). Введённый номер нужно обязательно проверить.
4. Класс, который управляет ходом игры:
class Game:
- класс «Игры» содержит атрибуты:
- состояние игры,
- игроки,
- поле.
- А также методы:
  - Метод запуска одного хода игры. Получает одного из игроков, запрашивает у
  игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил,
  возвращает True, иначе False.
  - Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который
  завершается победой одного из игроков или ничьей. Если игра завершена, метод
  возвращает True, иначе False.
  - Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой
  игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт
  игроков.

### Подсказка № 1
Начните с создания класса Cell, который будет хранить номер клетки, символ
(крестик, нолик или пустое значение), и состояние занятости клетки. Это позволит
каждой клетке иметь своё собственное состояние.

### Подсказка № 2
Создайте класс Board, который содержит список из 9 объектов Cell. Этот список
будет представлять игровое поле.

### Подсказка № 3
В классе Board создайте метод display_board, который будет выводить текущее
состояние доски на экран. Используйте простой цикл и форматирование строк для
создания наглядного интерфейса.

### Подсказка № 4
Напишите метод в классе Board, который изменяет символ клетки, если она не занята.
Метод должен проверять состояние клетки перед изменением и возвращать True или
False в зависимости от успеха операции.

### Подсказка № 5.
В классе Board создайте метод check_game_over, который проверяет все возможные
победные комбинации. Если одна из них выполнена, метод должен возвращать True.

### Подсказка № 6.
Создайте класс Player, который будет хранить имя игрока, его символ (X или O), и
количество побед. Также добавьте метод для запроса хода игрока.

### Подсказка № 7.
Создайте класс Game, который будет управлять процессом игры. В этот класс включите
игроков и доску. Добавьте метод, который выполняет ход игрока и проверяет окончание
игры.

### Подсказка № 8.
В классе Game создайте метод play_one_game, который будет запускать одну
партию. Этот метод должен очищать доску, поочередно запрашивать ходы игроков и
завершаться либо победой одного из игроков, либо ничьей.

### Подсказка № 9.
Добавьте метод reset_board в класс Board, который будет сбрасывать состояние
всех клеток. Этот метод понадобится, чтобы начать новую партию с чистого листа.

### Подсказка № 10.
В классе Game создайте основной метод start_games, который будет в цикле
запускать новые игры до тех пор, пока игроки хотят продолжать. Не забудьте добавить
возможность показа текущего счёта и сброса доски перед началом новой игры.