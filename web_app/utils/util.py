from nepali_datetime import date, datetime
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
square_dot = ImageFont.truetype("fonts/RepetitionScrolling.ttf", size=40)
poppins_bold = ImageFont.truetype("fonts/bold.ttf", size=40)
patrick = ImageFont.truetype("fonts/patrick.ttf", size=50)
revue = ImageFont.truetype("fonts/RevueBT.ttf", size=80)


def create_certificate(
    user,
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
    exam_board: str,
):
    ad_issue_date = (
        (datetime.strptime(issued_date, "%Y-%m-%d"))
        .to_datetime_date()
        .strftime("%d-%m-%Y")
    )

    ad_dob = (
        (datetime.strptime(str(date_of_birth), "%Y-%m-%d"))
        .to_datetime_date()
        .strftime("%d-%m-%Y")
    )

    dob = str(date_of_birth.strftime("%d-%m-%Y"))
    date = issued_date.split("-")
    issue_date = "-".join(date[::-1])
    image = Image.open("images/certificate.jpg")
    logo = Image.open(f"./media/{user.institute.institute_logo}").resize((216, 231))
    x_coord = image.size[0] / 2
    image.paste(logo, (int(x_coord - 100), 120), logo)
    draw = ImageDraw.Draw(image)

    draw.text(
        xy=(x_coord, 400),
        text=user.institute.institute_name.upper(),
        font=revue,
        fill=0xFFF000,
        anchor="mm",
    )

    draw.text(
        xy=(x_coord, 500),
        text=school_name,
        font=poppins_bold,
        fill=(0, 0, 0),
        align="left",
        anchor="mm",
    )
    draw.text(
        xy=(x_coord, 580),
        text=school_address,
        font=poppins_regular,
        fill=(0, 0, 0),
        align="left",
        anchor="mm",
    )
    draw.text(
        xy=(x_coord, 630),
        text="Estd: {}".format(established_date),
        font=poppins_regular,
        fill=(0, 0, 0),
        align="left",
        anchor="mm",
    )

    line_height = poppins_regular.getbbox("A")[3] + 4
    y = 800
    rows = [
        [
            (poppins_regular, "This is to certify that "),
            (poppins_bold, f"{'Mr.' if gender=='male' else 'Ms.'} {student_name} "),
            (poppins_regular, f"{'daughter' if gender=='female' else 'son'} of"),
            (poppins_bold, f" Mr. {father_name}"),
            (poppins_regular, " is"),
        ],
        [
            (poppins_regular, " an inhabitant of "),
            (poppins_bold, student_address),
        ],
        [
            (poppins_regular, f" and is a bonafide student of the academy. {'She' if gender=='female' else 'He'} passed the "),
        ],
        [
            (
                poppins_regular,
                f"examination of ",
            ),
            (poppins_bold, program),
            (poppins_regular, f" conducted by "),
        ],
        [
            (poppins_bold, exam_board),
            (poppins_regular, f" in the year {passed_year} B.S."),
            (poppins_regular, f" and secured "),
            (poppins_bold, f"{secured_gpa}."),
        ],
        [
            (poppins_regular, " According to the academy, "),
            (
                poppins_regular,
                f"{'her' if gender=='female' else 'his'} date of birth is",
            ),
            (poppins_bold, f" {dob} B.S.({ad_dob} A.D.)."),
        ],
        [
            (
                poppins_regular,
                f"We certify that {'she' if gender=='female' else 'he'} bears a good moral character.",
            )
        ],
    ]
    for row in rows:
        row_length = sum(font.getlength(segment) for font, segment in row)
        x = (image.size[0] - row_length) / 2

        for font, segment in row:
            if font == square_dot:
                draw.text((x, y+10), segment, fill="black", font=font,)
            else:
                draw.text((x, y), segment, fill="black", font=font)
            x += font.getlength(segment)

        y += line_height

    draw.text(
        xy=(350, 1200),
        text=f"Registration Number: {registration_number}",
        font=poppins_regular,
        fill=(0, 0, 0),
        align="left",
    )
    draw.text(
        xy=(350, 1250),
        text=f"Symbol Number: {symbol_number}",
        font=poppins_regular,
        fill=(0, 0, 0),
        align="left",
    )

    draw.text(
        xy=(350, 1300),
        text=f"Date of Issue: {issue_date} B.S.({ad_issue_date} A.D.)",
        font=poppins_regular,
        fill=(0, 0, 0),
        align="left",
    )

    img = image.save(f"media/certificate_{registration_number}.jpg")
