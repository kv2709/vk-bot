import sys
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from tests.test_const import *

TEMPLATE_PATH = 'files/ticket.png'
FONT_PATH = 'files/liberation-sans.ttf'
FONT_SIZE = 35
BLACK_COLOR = (0, 0, 0, 255)
NAME_OFFSET = (45, 275)
EMAIL_OFFSET = (45, 330)
AVATAR_SIZE = 220
AVATAR_OFFSET = (44, 17)
EMAIL = REG_CONF_SCENARIO_LST_INPUT[4][0]
URL_API_GENERATE_AVATAR = f"https://api.adorable.io/avatars/{AVATAR_SIZE}/"


def generate_ticket(name, email):
    print("Start generate")
    root_dir = sys.path.pop()
    print("root_dir => ", root_dir)
    sys.path.append(root_dir)
    print("sys.path.append(root_dir)")
    abs_path_for_avatar_file = os.path.join(root_dir, 'files/ticket.png')
    print("abs_path_for_avatar_file => ", abs_path_for_avatar_file)
    abs_path_for_font_file = os.path.join(root_dir, 'files/liberation-sans.ttf')
    print("abs_path_for_font_file => ", abs_path_for_font_file)
    base = Image.open(abs_path_for_avatar_file).convert('RGBA')
    print("base = Image.open(abs_path_for_avatar_file).convert('RGBA')")
    font = ImageFont.truetype(abs_path_for_font_file, FONT_SIZE)
    print("font = ImageFont.truetype(abs_path_for_font_file, FONT_SIZE)")
    draw = ImageDraw.Draw(base)
    print("draw = ImageDraw.Draw(base)")
    draw.text(NAME_OFFSET, name, font=font, fill=BLACK_COLOR)
    print("draw.text(NAME_OFFSET, name, font=font, fill=BLACK_COLOR)")
    draw.text(EMAIL_OFFSET, email, font=font, fill=BLACK_COLOR)
    print("draw.text(EMAIL_OFFSET, email, font=font, fill=BLACK_COLOR)")
    url_api_generate_avatar = f"{URL_API_GENERATE_AVATAR}{email}"
    print("url_api_generate_avatar = f'{URL_API_GENERATE_AVATAR}{email}'")
    response = requests.get(url=url_api_generate_avatar)
    print("response = requests.get(url=url_api_generate_avatar)")
    avatar_file_like = BytesIO(response.content)
    print("avatar_file_like = BytesIO(response.content)")
    avatar = Image.open(avatar_file_like)
    print("avatar = Image.open(avatar_file_like)")
    base.paste(avatar, AVATAR_OFFSET)
    print("base.paste(avatar, AVATAR_OFFSET)")
    temp_file = BytesIO()
    print("temp_file = BytesIO()")
    base.save(temp_file, 'png')
    print("base.save(temp_file, 'png')")
    temp_file.seek(0)
    print("temp_file.seek(0) - image ready!!!!!!!!!!!")
    return temp_file
