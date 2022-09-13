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
poppins_bold = ImageFont.truetype("fonts/bold.ttf", size=50)
patrick = ImageFont.truetype("fonts/patrick.ttf", size=50)
revue = ImageFont.truetype("fonts/RevueBT.ttf", size=90)


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
    exam_board: str
):
    ad_issue_date = (datetime.strptime(issued_date, "%Y-%m-%d")).to_datetime_date().strftime("%d-%m-%Y")

    ad_dob = (datetime.strptime(str(date_of_birth),  "%Y-%m-%d")).to_datetime_date().strftime("%d-%m-%Y")
    
    dob = str(date_of_birth.strftime("%d-%m-%Y"))
    date = issued_date.split("-")
    issue_date = "-".join(date[::-1])
    image = Image.open("images/certificate.jpg")
    logo = Image.open(f"./media/{user.institute_logo}").resize((216,231))
    x_coord = image.size[0] / 2
    image.paste(logo, (int(x_coord-100), 120), logo)
    draw = ImageDraw.Draw(image)

    
    draw.text(xy=(x_coord, 400),
        text = user.institute_name,
        font=revue,
        fill=(0,0,0),
        align="left",
        anchor="mm"
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

    draw.text(
        xy=(x_coord, 970),
        text=add_newline(
            f"This is to cerify that {'Mr.' if gender=='male' else 'Ms.'} {student_name}, {'daughter' if gender=='female' else 'son'} of Mr. {father_name} is an inhabitant of {student_address} is a bonafide student of the academy. {'She' if gender=='female' else 'He'} passed the examination of {program} conducted by {exam_board} in the year {passed_year} B.S. and secured {secured_gpa}. According to the academy, {'her' if gender=='female' else 'his'} date of birth is {dob} B.S.({ad_dob} A.D.)."
        )
        + f"\nWe certify {'she' if gender=='female' else 'he'} bears a good moral character.",
        font=poppins_regular,
        spacing=10,
        fill=(0, 0, 0),
        align="center",
        anchor="mm",
    )

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
