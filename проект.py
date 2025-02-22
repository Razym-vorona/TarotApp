import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random  # Для генерации случайных чисел

# Настройка основного окна приложения
window = tk.Tk()
window.geometry("500x600")  # Размер окна
window.resizable(False, False)  # Запрет изменения размера окна
window.config(bg="#BF3EFF")  # Цвет фона окна
window.title("Раскладики на Таро")  # Заголовок окна
ttk.Style().configure(".",  font="Times 14", foreground="#483D8B"
"", padding=8, background="#EEC900") 
# Класс для хранения информации о картах
class CardInfo:
    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description

class TarotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Раскладики на Таро")
        
        # Главный экран
        self.main_frame = tk.Frame(self.root, width=1600, height=1500)  # Увеличиваем высоту фрейма
        self.main_frame.pack(padx=40, pady=150)  # Устанавливаем отступы слева/справа и снизу

        self.title_label = tk.Label(self.main_frame, text="Раскладики на Таро", font=("Times", 24))
        self.title_label.pack(pady=50)  # Немного увеличиваем отступ сверху

        # Размещаем кнопку "Начать расклад" точно по центру окна
        self.start_button = ttk.Button(self.main_frame, text="Начать расклад", command=self.select_spread)
        self.start_button.place(relx=0.5, rely=0.7, anchor='center')  # Центрирование кнопки

        self.info_button = ttk.Button(self.main_frame, text="Информация о Таро", command=self.show_info)
        self.info_button.pack(pady=5)

    def show_info(self):
        messagebox.showinfo("Информация", "Таро — это система предсказания будущего и анализа текущей ситуации. Не нужно всецело доверять информации из раскладов, так как ваша судьба только в ваших руках.")

    def select_spread(self):
        # Выбор расклада
        self.main_frame.pack_forget()
        self.spread_frame = ttk.Frame(self.root)
        self.spread_frame.pack(pady=20)
        self.spread_label = ttk.Label(self.spread_frame, text="Что хотите узнать?", font=("Times", 18))
        self.spread_label.pack()

        # Список раскладов с четырьмя элементами
        self.spreads = ["Общий расклад", "Любовный расклад", "Финансовый расклад", "Вопросы Да/Нет"]
        for i, spread in enumerate(self.spreads):
            if spread == "Вопросы Да/Нет":
                # Привязываем функцию yes_no_result к кнопке "Вопросы Да/Нет"
                button = ttk.Button(self.spread_frame, text=spread, style="TButton",
                                    command=lambda s=spread: self.yes_no_result(s))
            else:
                # Остальные расклады обрабатываются функцией pick_random_cards
                button = ttk.Button(self.spread_frame, text=spread, style="TButton",
                                    command=lambda s=spread: self.pick_random_cards(s))
            button.pack(pady=5)

    def yes_no_result(self, spread):
        # Функция для расклада "Да/Нет"
        self.spread_frame.pack_forget()

        # Очистка предыдущего содержимого фрейма
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Вывод результата
        result_label = ttk.Label(self.main_frame, text=f"Ответ на ваш вопрос:", font=("Times", 14))
        result_label.pack(pady=10)

        # Случайный выбор между "Да" и "Нет"
        answer = random.choice(["Да", "Нет"])

        # Выводим результат
        answer_label = ttk.Label(self.main_frame, text=answer, font=("Times", 16))
        answer_label.pack(pady=5)

        # Кнопка возврата к раскладам
        back_button = ttk.Button(self.main_frame, text="Вернуться к раскладам", command=self.return_to_spreads)
        back_button.pack(side="bottom", pady=10)

        # Выделяем активный расклад другим цветом
        for child in self.spread_frame.winfo_children():
            if isinstance(child, ttk.Button) and child['text'] == spread:
                child.configure(style="Active.TButton")

        # Возвращаемся к главному фрейму
        self.main_frame.pack(padx=40, pady=150)

    def pick_random_cards(self, spread):
        # Выбор карт: выводим описания карт в случайном порядке
        self.spread_frame.pack_forget()

        # Очистка предыдущего содержимого фрейма
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Доступные карты (только описания)
        available_card_descriptions = [
            CardInfo('Описание первой карты'),
            CardInfo('Описание второй карты'),
            CardInfo('Описание третьей карты'),
            CardInfo('Описание четвертой карты'),
            CardInfo('Описание пятой карты'),
            CardInfo('Описание шестой карты'),
        ]

        # Случайный выбор трех карт
        selected_cards = random.sample(available_card_descriptions, 3)

        # Выводим описания карт
        result_label = ttk.Label(self.main_frame, text=f"Результат {spread}:", font=("Times", 14))
        result_label.pack(pady=10)

        for card in selected_cards:
            label = ttk.Label(self.main_frame, text=card.get_description())
            label.pack(pady=5)

        # Кнопка возврата к раскладам
        back_button = ttk.Button(self.main_frame, text="Вернуться к раскладам", command=self.return_to_spreads)
        back_button.pack(side="bottom", pady=10)

        # Выделяем активный расклад другим цветом
        for child in self.spread_frame.winfo_children():
            if isinstance(child, ttk.Button) and child['text'] == spread:
                child.configure(style="Active.TButton")

        # Возвращаемся к главному фрейму
        self.main_frame.pack(padx=40, pady=150)

    def return_to_spreads(self):
        # Показываем снова фрейм с выбором раскладов
        self.main_frame.pack_forget()
        self.spread_frame.pack(pady=20)

    def show_results(self):
        # Интерпретация карт: выводим сообщение о завершении расклада
        messagebox.showinfo("Расклад завершен", "Ваш расклад завершен. Интерпретация карт уже добавлена!")

# Создание стиля для активного расклада
style = ttk.Style()
style.configure("Active.TButton", foreground="red", background="yellow")

# Создание экземпляра класса и запуск приложения
app = TarotApp(window)
window.mainloop()