import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image

def calculate_dimensions(img_width, img_height, max_width, max_height):
    aspect_ratio = img_width / img_height

    if img_width > max_width:
        img_width = max_width
        img_height = max_width / aspect_ratio

    if img_height > max_height:
        img_height = max_height
        img_width = max_height * aspect_ratio

    return img_width, img_height

def collect_and_merge_files():
    current_path = os.getcwd()
    all_files = os.listdir(current_path)
    image_files = []

    for file in all_files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_files.append(file)

    if image_files:
        print(f'{len(image_files)} images found O_o')
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        merged_file_name = f'sawa4d_imgs2pdf_{current_time}.pdf'
        merged_file_path = os.path.join(current_path, merged_file_name)

        pdf = canvas.Canvas(merged_file_path, pagesize=A4)
        x = 0

        for image_file in image_files:
            image_path = os.path.join(current_path, image_file)
            img = Image.open(image_path)

            # حساب الأبعاد المعدلة مع الحفاظ على نسبة الطول للعرض
            new_width, new_height = calculate_dimensions(img.width, img.height, A4[0], A4[1])

            pdf.setPageSize((new_width, new_height))
            pdf.drawImage(image_path, 0, 0, width=new_width, height=new_height)
            pdf.showPage()

            x += 1
            print(f'{x}/{len(image_files)} image merged.')

        pdf.save()
        print(f'Done ^_^')
    else:
        print('No jpg, png, jpeg images found -_-')

if __name__ == "__main__":
    collect_and_merge_files()
