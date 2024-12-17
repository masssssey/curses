import requests
import curses

# Функция для получения курса валют
def get_exchange_rate():
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/RUB')
        data = response.json()
        return data['rates']['USD']
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return None

# Основная функция приложения
def main(stdscr):
    # Очистка экрана
    stdscr.clear()
    
    # Получаем курс доллара
    exchange_rate = get_exchange_rate()
    
    if exchange_rate is None:
        stdscr.addstr(0, 0, "Не удалось получить курс валют.")
        stdscr.refresh()
        stdscr.getch()
        return
    
    stdscr.addstr(0, 0, f"Курс RUB к USD: {exchange_rate:.2f}")
    stdscr.addstr(2, 0, "Введите сумму в рублях (или 'q' для выхода): ")

    while True:
        stdscr.addstr(3, 0, " " * 50)  # Очистка строки для ввода
        stdscr.move(3, 0)
        
        # Получаем ввод пользователя
        user_input = stdscr.getstr().decode('utf-8')

        if user_input.lower() == 'q':
            break
        
        try:
            rubles = float(user_input)
            dollars = rubles * exchange_rate
            stdscr.addstr(5, 0, f"{rubles:.2f} RUB = {dollars:.2f} USD")
        except ValueError:
            stdscr.addstr(5, 0, "Некорректный ввод. Пожалуйста, введите число.")

        stdscr.refresh()

# Запуск приложения
if __name__ == "__main__":
    curses.wrapper(main)
