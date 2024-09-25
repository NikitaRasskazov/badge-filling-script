from PIL import Image, ImageDraw, ImageFont
import os

# Функция для добавления ФИО на шаблон изображения
def add_name_to_template(template_path: str, user_name: str, output_dir: str, output_name: str, text_position=(50, 50), font_size=80):
    # Открываем шаблон изображения
    img = Image.open(template_path)

    # Инициализируем инструмент для рисования
    draw = ImageDraw.Draw(img)

    # Загружаем шрифт (используем стандартный шрифт Pillow)
    try:
        font = ImageFont.truetype("Jura-Bold.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Наносим текст (ФИО) на изображение в заданной позиции
    draw.text(text_position, user_name.upper(), fill=(255, 255, 255), font=font)  # Белый цвет текста

    # Указываем путь для сохранения изображения
    output_path = os.path.join(output_dir, f"{output_name}.png")

    # Сохраняем изображение
    img.save(output_path)
    print(f"Создано изображение для пользователя: {user_name}, сохранено как: {output_path}")

# Основная функция для генерации изображений
def generate_images_with_names(template_path: str, user_names, output_dir="output_images"):
    # Создаем выходную директорию, если она не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Генерация изображений для каждого пользователя
    for user_name in user_names:
        output_name = user_name.replace("\n", "").replace(" ", "_")  # Используем ФИО как имя файла
        # Определяем координаты для размещения ФИО над словом "ГОСТЬ"
        text_position = (97, 800)  # Эти координаты можно подкорректировать
        add_name_to_template(template_path, user_name, output_dir, output_name, text_position=text_position)

# Пример списка пользователей
user_names = ["Иванов \nИван", "Петров \nПетр", "Сидоров \nСидор", "Шаймарданова \nВиктория"]

# Путь к шаблону изображения
template_path = "template/template.png"  # Замените на путь к вашему шаблону

# Генерация изображений
generate_images_with_names(template_path, user_names)
