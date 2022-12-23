import time, json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

endpoint = 'https://collegedunia.com/usa/college/1090-harvard-university-cambridge'

driver_path = Service('chromedriver.exe')
driver = webdriver.Chrome(service=driver_path)
driver.get(endpoint)

# title and Veda_Burman name scraping
title = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/header/div[2]/div/div[1]/h1').text
Veda_Burman = driver.find_element(By.LINK_TEXT, 'Veda Burman').text

# read more button
read_more = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[2]')
read_more.click()

# Veda_Burman acknowledgement
info_of_veda1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/p[1]').text
info_of_veda2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/p[2]').text
info_of_veda3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/p[3]').text
info_of_veda = info_of_veda1 + "\n" + info_of_veda2 + "\n" + info_of_veda3

# ranking
ranking = driver.find_element(By.ID, 'Harvard_Ranking').text
ranking_description1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/p[1]').text
ranking_description2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/ul').text
ranking_description3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/p[2]').text
ranking_description = ranking_description1 + "\n" + ranking_description2 + "\n" + ranking_description3

# comparisons
comparisons = {}
for h in range(1, 4):
    b = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/table/tbody/tr/td[{h}]/a'
    comparison = driver.find_element(By.XPATH, b)
    comparisons[comparison.text] = comparison.get_attribute('href')

# checkout
checkout_spanish = driver.find_element(By.LINK_TEXT, 'Harvard University (Spanish)').get_attribute('href')
harvard_spanish = {'Harvard University (Spanish)': checkout_spanish}

# ranking comparison subjectwise
ranking_comparison_description = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/p[4]').text
ranking_comparison = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]').text

# courses
course_description = driver.find_element(By.CLASS_NAME, 'cdcms_courses').text

# Top programs
program_title = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[4]/h3').text
top_courses = []
for i in range(1, 13):
    xpath = f'//*[@id="table-body"]/tr[{i}]'
    a = driver.find_element(By.XPATH, xpath)
    top_courses.append(a.text)

# university international students enrollment
enrollment_title = driver.find_element(By.ID, 'Enrollments').text
enrollment = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/p[5]').text
enrollment_img = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[5]/img').get_attribute('data-src')

# Admission
admission_title = driver.find_element(By.ID, 'Admission').text
admission_details = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/p[7]').text
portals = []
for j in range(1, 4):
    x_path = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[6]/p[2]/a[{j}]'
    admission_portal = driver.find_element(By.XPATH, x_path)
    portals.append(admission_portal.get_attribute('href'))
admission_deadlines = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[6]/div[1]/table').text

# Admission Requirements
requirements_title = driver.find_element(By.ID, 'Requirements').text
requirements_data = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[6]/div[2]/table').text

# other links [Also CHeck]
links = {}
for k in range(1, 4):
    a = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[6]/ul/li[{k}]/a'
    link = driver.find_element(By.XPATH, a)
    links[link.text] = link.get_attribute('href')

# campus
campus_title = driver.find_element(By.ID, 'Campus_Accommodation').text
campus_description = ''
for g in range(1, 5):
    xpat_h = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/p[{g}]'
    campus_description += driver.find_element(By.XPATH, xpat_h).text

# accommodation
accommodation_title = driver.find_element(By.ID, 'Housing_Residence').text
accommodation_description = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/p[5]').text
on_campus_residence = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/ul[1]').text
off_campus_residence = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/ul[2]').text

# cost of attendance
attendance_title = driver.find_element(By.ID, 'Cost_Attendance').text
fee_structure1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/div[1]/div[1]/table').text
fee_structure2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/div[1]/div[2]/table').text

# scholarships
scholarship_title = driver.find_element(By.ID, 'Harvard_Scholarship').text
scholarship_description = ''
for i in range(1, 4):
    x = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/div[2]/p[{i}]'
    scholarship_description += driver.find_element(By.XPATH, x).text
scholarship_description += '\n' + driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/div[2]/div').text + '\n' +driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/div[2]/p[5]').text + '\n' +driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/div[2]/ul').text
scholarship_link = driver.find_element(By.LINK_TEXT,'Scholarships in USA')
scholarship_description += f' {scholarship_link.text} in {scholarship_link.get_attribute("href")}.'

# alumni
alumni_title = driver.find_element(By.ID, 'Alumni_Network').text
alumni_description = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/div[3]').text
alumni_description += " in  " + driver.find_element(By.LINK_TEXT, 'Harvard University Student Profile').get_attribute('href')

# placements
placement_title = driver.find_element(By.ID, 'Harvard_Placements').text
placement_description = ''
for i in range(1, 4):
    x = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[7]/div[4]/p[{i}]'
    placement_description += driver.find_element(By.XPATH, x).text


# FAQ
all_faqs = {}
q1 = driver.find_element(By.ID, 'docs-internal-guid-b9331917-7fff-c182-f1dc-f9479f8e7879')
q1.click()
all_faqs["Ques. " + q1.text + " ?"] = driver.find_element(By.XPATH, '//*[@id="faq_id"]/div[1]/p').text
for i in range(2, 16):
    q_x = f'//*[@id="faq_id"]/p[{i}]/b'
    q = driver.find_element(By.XPATH, q_x)
    q.click()
    a_x = f'//*[@id="faq_id"]/div[{i}]/p'
    a = driver.find_element(By.XPATH, a_x)
    all_faqs[q.text] = a.text

# Harvard popular courses
view_all_button1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[3]/div/div[2]/div[2]/span').click()
view_all_button2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[3]/div/div[3]/div[2]/span').click()
all_courses = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[3]/div').text

# overview
all_courses_overview = {}
for i in range(1, 7):
    x_1 = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[4]/div[{i}]/div'
    x_2 = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[4]/div[{i}]/div/div[1]/div[1]/div[1]/p/a'
    course_description_overview = driver.find_element(By.XPATH, x_1).text
    course = driver.find_element(By.XPATH, x_2)
    name = course.text
    course_link = course.get_attribute('href')
    all_courses_overview[name] = [course_description_overview.replace('\n', ''), {"course link": course_link}]


# harvard student profiles
all_profiles = {}
for i in range(1, 5):
    x_x = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[6]/div[2]/div/div[2]/div/div[{i}]/div/div/a/div'
    x_x_1 = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[6]/div[2]/div/div[2]/div/div[{i}]/div/div/a/div/div[2]/div/div[1]'
    profile_description = driver.find_element(By.XPATH, x_x).text
    profile_name = driver.find_element(By.XPATH, x_x_1).text
    all_profiles[profile_name] = [profile_description.replace('\n', '')]


# universal ranking
universal_ranking_description = driver.find_element(By.XPATH, '//*[@id="ranking_scroll"]/div[2]/div[1]/div/div[2]').text + '\n' + driver.find_element(By.XPATH, '//*[@id="ranking_scroll"]/div[3]/div/div/div[2]').text


# rating
rating_description = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[8]/div[1]/div/div[2]').text


# reviews
all_reviews = {}
for i in range(3, 5):
    a = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[8]/div[2]/div/div/div[{i}]/div[1]/div/div[1]/div[1]/a'
    b = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[8]/div[2]/div/div/div[{i}]/div[1]/div/div[2]/span'
    c = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[8]/div[2]/div/div/div[{i}]/div[2]/h3/a'
    d = f'//*[@id="__next"]/div[2]/section/div/div[1]/div[3]/div[1]/div/div[8]/div[2]/div/div/div[{i}]/div[3]'
    reviewer_name = driver.find_element(By.XPATH, a)
    rating=driver.find_element(By.XPATH, b)
    comment_head = driver.find_element(By.XPATH, c)
    comment_body = driver.find_element(By.XPATH, d)
    all_reviews[reviewer_name.text] = {'rating': rating.text.replace("\n", ''), comment_head.text: comment_head.get_attribute('href'), 'comment': comment_body.text.replace("\n", '').removesuffix('Read More')}

# json conversion of the entire webpage elements
data = {
    'title': title,
    Veda_Burman: info_of_veda,
    ranking: ranking_description.replace("\n", ''),
    'comparisons': comparisons,
    'Harvard University (Spanish)': checkout_spanish,
    'Harvard University Rankings comparison': ranking_comparison.replace("\n", ''),
    'Harvard University Rankings': ranking_comparison_description,
    'Harvard University Courses': course_description,
    program_title: top_courses,
    enrollment_title: [enrollment, enrollment_img],
    admission_title: [admission_details, {'portals': portals}, admission_deadlines.replace("\n", '')],
    requirements_title: requirements_data.replace("\n", ''),
    'Admission links details': links,
    campus_title: campus_description,
    accommodation_title: [accommodation_description.replace("\n", ''), on_campus_residence.replace("\n", ''), off_campus_residence.replace("\n", '')],
    attendance_title: [fee_structure1.replace("\n", ''), fee_structure2.replace("\n", '')],
    scholarship_title: scholarship_description,
    alumni_title: alumni_description.replace("\n", ''),
    placement_title: placement_description,
    'Harvard FAQs': all_faqs,
    'Harvard University Popular Courses': all_courses,
    'Harvard University Popular Course Overview': all_courses_overview,
    'Harvard University Student Profiles': all_profiles,
    'Harvard University Ranking': universal_ranking_description.replace("\n", ''),
    'Harvard University Ratings': rating_description.replace("\n", ''),
    'Harvard University Reviews': all_reviews
}
with open('myfile.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)

driver.quit()





