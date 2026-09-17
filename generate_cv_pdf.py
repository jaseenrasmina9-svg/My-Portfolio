from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate

pdf_path = 'jaseen-rasmina-cv.pdf'

styles = getSampleStyleSheet()

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4,
    rightMargin=48,
    leftMargin=48,
    topMargin=36,
    bottomMargin=36,
)

header_style = ParagraphStyle(
    'Header',
    parent=styles['Title'],
    fontName='Helvetica-Bold',
    fontSize=26,
    leading=28,
    spaceAfter=4,
)

subhead_style = ParagraphStyle(
    'Subhead',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#5d6573'),
    spaceAfter=14,
)

section_style = ParagraphStyle(
    'Section',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=12,
    textColor=colors.HexColor('#111827'),
    spaceAfter=10,
    spaceBefore=12,
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['BodyText'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
)

label_style = ParagraphStyle(
    'Label',
    parent=styles['BodyText'],
    fontName='Helvetica-Bold',
    fontSize=9,
    leading=12,
    textColor=colors.HexColor('#5d6573'),
    spaceAfter=2,
)

story = []
story.append(Paragraph('Jaseen Rasmina', header_style))
story.append(Paragraph('Software Engineering Student • Aspiring Software Engineer', subhead_style))

story.append(Paragraph('Profile', section_style))
story.append(Paragraph(
    'I am a passionate and detail-oriented Software Engineering student with a strong foundation in programming, problem-solving, and software development. I have knowledge in Java, Python, JavaScript, web application development, and database concepts. I am a quick learner with good teamwork and communication skills, and I am interested in applying my technical knowledge to real-world projects and growing as a software developer.',
    body_style,
))

story.append(Paragraph('Contact', section_style))
contact_items = [
    'Email: jaseenrasmina9@gmail.com',
    'Phone: +94 771 085 861',
    'Location: Pallikudiyirupu, Akkaraipattu, Sri Lanka',
]
story.append(
    ListFlowable(
        [ListItem(Paragraph(item, body_style), leftIndent=18) for item in contact_items],
        bulletType='•',
        leftIndent=0,
        style=body_style,
    )
)

story.append(Paragraph('Skills', section_style))
story.append(Paragraph('Technical', label_style))
story.append(
    ListFlowable(
        [ListItem(Paragraph(item, body_style), leftIndent=18) for item in ['Java', 'Python', 'JavaScript', 'HTML', 'CSS', 'Web Development', 'Database Management', 'SQL / Database Concepts']],
        bulletType='•',
        leftIndent=0,
        style=body_style,
    )
)
story.append(Paragraph('Professional', label_style))
story.append(
    ListFlowable(
        [ListItem(Paragraph(item, body_style), leftIndent=18) for item in ['Communication', 'Attention to Detail', 'Analytical Thinking', 'Team Collaboration', 'Problem Solving', 'Adaptability']],
        bulletType='•',
        leftIndent=0,
        style=body_style,
    )
)

story.append(Paragraph('Experience', section_style))
story.append(Paragraph('Trainee in Computing', label_style))
story.append(Paragraph('Base Hospital Akkaraipattu', body_style))
story.append(Paragraph('August 2023 – December 2023', body_style))
story.append(
    Paragraph(
        'Assisted with IT support and daily technical operations. Gained practical experience with hospital software, patient data systems, networking, and general IT operations.',
        body_style,
    )
)

story.append(Paragraph('Education', section_style))
story.append(
    ListFlowable(
        [ListItem(Paragraph(item, body_style), leftIndent=18) for item in [
            'BSc (Hons) in Software Engineering — International Campus of Science and Technology',
            'Diploma in English — Bright Future E-Learning Education, Punanai, Batticaloa, Sri Lanka',
            'GCE Advanced Level — Completed with 3S qualification',
            'GCE Ordinary Level — Distinction pass in each subject',
        ]],
        bulletType='•',
        leftIndent=0,
        style=body_style,
    )
)

story.append(Paragraph('Professional Development', section_style))
story.append(
    ListFlowable(
        [ListItem(Paragraph(item, body_style), leftIndent=18) for item in [
            'Future Leadership — Eminence College of Science and Technology, June 2023',
            'Management — Axis Academy, December 2024',
        ]],
        bulletType='•',
        leftIndent=0,
        style=body_style,
    )
)

doc.build(story)
print(f'Created: {pdf_path}')
