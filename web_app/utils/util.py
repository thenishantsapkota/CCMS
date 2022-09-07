from PIL import Image, ImageFont, ImageDraw


def add_newline(string: str, number_of_words: int = 15) -> str:
    new_string = ""
    words = string.split(" ")
    word_count = 0
    for word in words:
        new_string += word + " "
        word_count += 1
        if word_count == number_of_words:
            new_string += "\n"
            word_count = 0

    return new_string


poppins_regular = ImageFont.truetype("fonts/regular.ttf", size=40)
poppins_bold = ImageFont.truetype("fonts/bold.ttf", size=50)


def create_certificate(
    school_name: str,
    school_address: str,
    established_date: str,
    gender: str,
    student_name: str,
    father_name: str,
    student_address: str,
    academic_year: str,
    program: str,
    passed_year: str,
    secured_gpa: str,
    date_of_birth: str,
    symbol_number: str,
    registration_number: str,
    issued_date: str,
):
    image = Image.open("images/certificate.png")
    draw = ImageDraw.Draw(image)

    draw.text(xy=(1000, 500), text=school_name, font=poppins_bold, fill=(0, 0, 0))
    draw.text(xy=(1050, 580), text=school_address, font=poppins_regular, fill=(0, 0, 0))
    draw.text(
        xy=(1150, 630),
        text="Estd: {}".format(established_date),
        font=poppins_regular,
        fill=(0, 0, 0),
    )

    draw.text(
        xy=(350, 830),
        text=add_newline(
            f"This is to cerify that {student_name} is a bonafide student of the Academy from {school_name}. {'She' if gender=='female' else 'He'} passed the conducted by CTEVT in the year and has secured {secured_gpa} on a four point scale. According to the academy,{'her' if gender=='female' else 'his'} date of birth is {date_of_birth} . We certify that the student bears a good moral character."
        ),
        font=poppins_regular,
        fill=(0, 0, 0),
        align="center",
    )

    draw.text(
        xy=(350, 1100),
        text=f"Registration Number: {registration_number}",
        font=poppins_regular,
        fill=(0, 0, 0),
        align="left",
    )
    draw.text(
        xy=(350, 1150),
        text=f"Symbol Number: {symbol_number}",
        font=poppins_regular,
        fill=(0, 0, 0),
        align="left",
    )

    draw.text(
        xy=(350, 1200),
        text=f"Date of Issue: {issued_date}",
        font=poppins_regular,
        fill=(0, 0, 0),
        align="left",
    )

    img = image.save(
        f"media/certificate_{registration_number}.png"
    )  # create_certificate()
