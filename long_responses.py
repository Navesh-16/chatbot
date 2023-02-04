import re
import random
R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
College = "VET Institute of Arts and Science (VETIAS), the youngest member of the Vellalar family is an intellectual community that nurtures student learning, fosters faculty research and creative activity, and provides service to the larger community."
ao = "MR. LOGESH KUMAR S."
aesthetics = "The Aesthetics club will be a place for students to better themselves, network with others and share ideas with other students and members of faculty on campus regarding the world of beauty and fashion. The club aims to branch itself throughout the beauty and fashion community, on and off campus, and its members will gain up to date knowledge out of classes and meetings."
Agri = "The Agri and Environmental Club’s pledge is to raise awareness of different agricultural and environmental trends and issues in and around the community. The club engages the students, members of the faculty and the community in diverse activities and trips that show and promote environmental consciousness, better sustainable practices and instil in them the power to reverse current agricultural and environmental problems."
Arts_Crafts = "The Arts and Crafts club aims to promote and develop young students’ artistic and creative skills. Often with little or no prior experience or access to hands on art and craft activities, the club members gain self-confidence and social skills in their ability to create and express themselves through crafting in a trusting and supportive environment."
rules = "A student shall be allowed to appear for the End Semester Examinations (ESE) only if,they put in at least 75% of attendance.they show satisfactory progress in studies, in all the tests and examinations conducted by the college during the semester and has secured the minimum required marks in them. their conduct in the college during the semester had been satisfactory."
computer_science = "BSC Computer Science, BSC Computer Application, BSC Computer Science AI&DS"
consumer = "The Consumer Club of VETIAS functions with an aim to enhance awareness among the student community about the rights and responsibilities of a consumer and to impart such knowledge and encourage students to stand up against malpractices in the society. The club organises workshops, field visits, awareness camps and competitions to achieve its aim"
Dean ="Dr. Nallaswamy V P"
Departments = "In our college totally Ten Departments we have"
Entrepreneurship = "The Entrepreneurship & Forum for Industry Interaction was established the year 2019 to help its student members educate themselves about the current business world. Through the programmes conducted and the training imparted, the members of the club will learn to recognise the various components needed to understand the markets and excel professionally."
Exam_Shell = "Dr. Radhika C - Controller of Examinations and Mr. Jagadeesan S Assistant Controller of Examinations."
Examination_Hall_rules = "The identity card issued by the institution has to be presented before entering the hall. If, a student forgets their identity card, they shall submit a letter stating reasons and get it signed by the invigilator/ HoD / CoE to enter the hall Students shall be present outside the hall at least 15 minutes prior the commencement of the examination; coming late shall be entertained Students shall not be permitted to undertake ESE when they arrive late by more than 30 minutes from the commencement of the examination Students shall not be permitted to exit the hall before the final bell"
Faculty_List_computer_science = "Dr. Ananth KR, Dr. Selvanayaki K, Dr. Prasath S, Dr. Vijayakumar M, Mr. Praveenkumar G D, Dr. Karthika D, Dr. Sudha L, Dr. Priscillasasi J, Dr. Mohanasathiya K S, and Dr. Panjatcharam VG"
Faculty_List_School_of_Fashion = "Dr. Rajalakshmi M, Ms. Swedha R, Mr. Jeeva S, Ms. Dhurgha Niranjan Kumar, Mr. Ashok Kannan, and Mr. Rajaram T"
Fine_Arts_Club = "The Fine Arts Club is for anyone with a passion towards performance music and dance. The aim of the club is to build a working network of students and professionals seeking education, mentorship, hands-on experience and exposure to further their skills within the community and the arts industry. Whether students learn from each other, or from industry professional guest speakers, the programmes organised will provide and encourage a safe and respectable environment for all to share their craft, insight and opinion connected to the concerned art."
First_Aid = "First Aid & Pharmaceutics was set up in the year 2019 for students and members of faculty to come together to raise awareness of the importance of first aid and learn life-saving skills. Its members also have the opportunity to serve the institution through providing first aid coverage for institutional events. The club has also paved great way for students to develop leadership and team work skills, as they help and learn from each other."
Infrastructure = "Known for its lush green campus, VETIAS is ecologically, intellectually and technically equipped to provide the best environment for learning in an enjoyable manner. Have a look at our state-of-the-art infrastructure.Digital LibraryDigital Classrooms Conference Hall PWD Accessibility Seminar Hall Arena Halls IT LaboratoriesCDF Laboratory "
Library = "Working Hours: 9:00 to 5:30 And Transaction Hours:9:30 to 5:00"
Library_rules = "All members of the faculties and students of the college are members of the library.All members shall scan their ID card at the entrance of the library and once again scan their ID card at the time of leaving the library.ID card is a must for all transactions. Books shall not be issued to a holder with another person’s ID card"
National_service_Scheme = "The NSS Unit of VETIAS, currently functions with two units comprising 100 students each. The club organises various social and community programmes which include awareness rallies, blood donation camps, tree plantation drives and the like."
Photography_MAD_club = "The mission of the Photography & MAD club is to provide a supportive environment for interested photography and film-making students to share their creativity, knowledge and passion for the art. The club will hold regular meetings and discussions and organise events such as photo-walks, field trips, museum and gallery visits, and lectures and workshops by visiting artists. From the basics of photography to editing, from pre-production to post-production, from writing the screenplay to editing the video, the members of the club will be taught everything to start out on their own."
Principal_name = "DR. R. SARAVANAN"
Rotaract_Club = "The Rotaract of VETIAS was established in 2020 with a vision to help students exchange ideas with leaders in the community, develop leadership and professional skills, and have fun through service. The club regularly conducts sessions on skill, personality and employment development programmes for students of VETIAS and the general public too."
School_of_Business_Courses = "BBA - Business Administration"
School_of_Commerce_courses = "BCOM - General BCOM Accounting and Finance, BCOM Computer Application, BCOM Professional Accounting, MCOM, MPHIL(PT/FT) & PHD(PT/FT)"
School_of_Fashion = "BSC Costume Design and Fashion"
School_of_Social_Studies_courses = "BA Sociology"
Secretary_name = "THIRU. CHANDRASEKAR S D,B.A."
Sports_Club = "The Sports teams of VETIAS are open to all the students of the institution possessing any skill set. It offers the opportunity for the students to compete with other colleges at the zone and even nationally. Our Sports teams are competitive and places emphasis on participation, skill development and leadership. Our philosophy is to support the best elements of competition, instruction and recreation by providing the opportunity for all students to participate and excel."
Total_Departments_list = "School of Fashion, School of Literature, School of Social Studies, School of Computer Science, School of Commerce, School of Business, School of Tamil,School of Mathematics, School of Economics"
Transportation = "VETIAS offers air-conditioned commutation to and from the campus with door-step pick up and drop. Our busses cover wider routes for the convenience of the students."
Why_you_choose_AS = "Here are our top five reasons for you to choose us:  Excellent Teaching Fraternity, All that is Needed to Learn, Wholesome Development, Academic and Industry Exposure and World Class Technology"
Youth_Read_Cross_Club = "The YRC of VETIAS, as per the Indian Red Cross Society, was established with an aim to inspire, encourage and initiate students at all times to be innovators, inter-cultural ambassadors, peer educators, community mobilisers, and most importantly, agents of behavioural change and advocates for vulnerable people. Keeping up with the vision, the club regularly organises blood donation camps, awareness programmes and talks and competitions among many others."
who_are_you = "chatbot developed by Navesh "
Computer_science_HOD = "Dr. Karthika D"
Computer_Application_HOD = "Dr. Ananth KR"
Admissions = "SCHOOL OF LITERATURE -MPHIL(PT/FT) & PHD(PT&FT), SCHOOL OF FASHION -    BSC COSTUME DESIGN AND FASHION, SCHOOL OF SOCIAL STUDIES - BA SOCIOLOGY, SCHOOL OF COMPUTER SCIENCES BSC COMPUTER SCIENCE BSC COMPUTER SCIENCE & APPLICATION BSC COMPUTER SCIENCE (ARTIFICIAL INTELLIGENCE AND DATA SCIENCE) BSC INFORMATION TECHNOLOGY, SCHOOL OF COMMERCE - BCOM - GENERAL BCOM ACCOUNTING AND FINANCE BCOM COMPUTER APPLICATIONS BCOM PROFESSIONAL ACCOUNTING MCOM MPHIL(PT/FT) & PHD(PT&FT), SCHOOL OF BUSINESS BBA - BUSINESS ADMINISTRATION"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    #response('VET Institute of Arts and Science College', ['college', 'name'], required_words=['college'])
    # Longer responses
    response(R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(College, ['college', 'us', 'vet', 'name'])
    response(ao, ['ao', 'administrative', 'officer'])
    response(aesthetics, ['aesthetics', 'club'], required_words=['aesthetics'])
    response(Agri, ['agri', 'and', 'environment', 'club'], required_words=['agri'])
    response(Arts_Crafts, [ 'arts', 'and', 'crafts', 'club'], required_words=['arts', 'crafts'])
    response(rules, ['student', 'attendance', 'rules', 'rules', 'for', 'student', 'requirements'])
    response(computer_science, ['school', 'of', 'computer', 'science', 'offered', 'courses'])
    response(consumer, ['consumer', 'club'], required_words=['consumer', 'club'])
    response(Dean, ['who', 'is', 'college', 'dean'], required_words=['dean'])
    response(Departments, ['count', 'of', 'college', 'department', 'number', 'how', 'many', 'total'])
    response(Entrepreneurship, ['entrepreneurship', 'forum', 'for', 'industry', 'interaction', 'club'])
    response(Exam_Shell,['exam', 'shall'])
    response(Examination_Hall_rules, ['examination', 'hall', 'rules', 'exam'])
    response(Faculty_List_computer_science,['total', 'faculty', 'list', 'School', 'computer', 'science'])
    response(Faculty_List_School_of_Fashion, ['total', 'faculty', 'list', 'School', 'fashion'])
    response(Fine_Arts_Club, ['fine', 'arts', 'club'], required_words=['fine', 'arts'])
    response(First_Aid, ['first', 'aid', 'pharmaceutics', 'club'], required_words=['first', 'aid'])
    response(Infrastructure, ['college',  'infrastructure'], required_words=['infrastructure'])
    response(Library, ['opening', 'library', 'time'], required_words=['library', 'time'])
    response(Library_rules, ['rules', 'library'], required_words=['rules', 'library'])
    response(National_service_Scheme, ['national', 'service', 'scheme', 'club', 'nss'])
    response(Photography_MAD_club, ['photography', 'mad', 'club'], required_words=['photography'])
    response(Principal_name, ['who', 'Principal', 'sir'], required_words=[' principal'])
    response(Rotaract_Club, ['rotaract', 'club'], required_words=['rotaract', 'club'])
    response(School_of_Business_Courses, ['list', 'course', 'courses', 'school', 'of', 'business', 'offered'])
    response(School_of_Commerce_courses, ['list', 'course', 'courses', 'school', 'of', 'commerce', 'offered'])
    response(School_of_Fashion, [ 'offered', 'school', 'fashion'])
    response(School_of_Social_Studies_courses, ['list', 'course', 'courses', 'school', 'sociology', 'social', 'studies', 'offered'])
    response(Secretary_name, ['college', 'secretary'], required_words=['secretary'])
    response(Sports_Club, ['sports', 'sport', 'club'], required_words=['sports' or 'sport', 'club'])
    response(Total_Departments_list, ['total' 'college' 'departments', 'list'])
    response(Transportation, ['transportation'], required_words=['transportation'])
    response(Why_you_choose_AS, ['choose', 'as'])
    response(Youth_Read_Cross_Club, ['youth', 'read', 'cross', 'yrc'])
    response(who_are_you, ['who', 'are', 'you'])
    response(Computer_science_HOD, ['hod', 'computer', 'cs', 'science'])
    response(Computer_Application_HOD, ['hod', 'computer', 'csa', 'application'])
    response(Admissions, ['admissions'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response