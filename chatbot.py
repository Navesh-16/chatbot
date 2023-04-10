from flask import render_template, jsonify, Flask
from flask import request
from flask import Response
import long_responses as long
import json
import requests
from twilio.twiml.messaging_response import MessagingResponse

TOKEN = "5792993344:AAH3h3RWwwyUPZ3G1Lkzd9vze9IzGMojyQc"

app = Flask(__name__)


p = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/03/vet-principal.jpg',
     'caption': long.Principal_name}]
p1 = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/lokesh.jpg',
       'caption': long.ao}]
p2 = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/nallaswamy.jpg',
       'caption': long.Dean}]
p3 = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/Secretary.jpg',
       'caption': long.Secretary_name}]
p4 = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/vellingiri.jpg',
       'caption': long.B_Com_CA_HOD}]
p5 = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/arulraj_vetias.jpg',
       'caption': long.B_Com_HOD}]
p6 = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/vijayanand.jpg',
       'caption': long.BBA_HOD}]
p7 = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/karthika_vetias.jpg',
       'caption': long.Computer_science_HOD}]
p8 = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/ananth_vetias.jpg',
       'caption': long.Computer_Application_HOD}]
p9 = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/yashir.jpg',
       'caption': long.School_of_Social_Studies_HOD}]
p10 = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/rajalakshmi_vetias.jpg',
        'caption': long.School_of_Fashion_HOD}]
p11 = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/mohanasundari_vetias.jpg',
        'caption': long.School_of_Literature_HOD}]
p_af = [{'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/murali_vetias.jpg',
         'caption': long.B_Com_PA_AF_HOD}]
p12 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/02/1-2.jpg', 'caption': 'Library'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/02/digital-library.jpg', 'caption': 'Digital Library'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/02/classroom.jpg', 'caption': 'Classroom'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/02/digital-hall.jpg', 'caption': long.Infrastructure}
]

p13 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/karthika_vetias.jpg',
     'caption': 'Dr. Karthika D \n https://vetias.ac.in/faculty/dr-d-karthika/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/ananth_vetias.jpg',
     'caption': 'Dr. Ananth KR \n https://vetias.ac.in/faculty/dr-k-r-ananth/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/sudha.jpg',
     'caption': 'Dr. Sudha L \n https://vetias.ac.in/faculty/dr-l-sudha/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/pricilla.jpg',
     'caption': 'Dr. Priscillasasi J \n https://vetias.ac.in/faculty/dr-j-priscillasasi/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/mohanasathya.jpg',
     'caption': 'Dr. Mohanasathiya K S \n https://vetias.ac.in/faculty/dr-k-s-mohanasathiya/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/selvanayaki_vetias.jpg',
     'caption': 'Dr. Selvanayaki K \n https://vetias.ac.in/faculty/dr-k-selvanayaki/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/prasath_vetias.jpg',
     'caption': 'Dr. Prasath S \n https://vetias.ac.in/faculty/dr-s-prasath/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/vijaykumar.jpg',
     'caption': 'Dr. Vijayakumar M \n https://vetias.ac.in/faculty/dr-m-vijayakumar/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/praveen.jpg',
     'caption': 'Mr. Praveenkumar G D \n https://vetias.ac.in/faculty/mr-g-d-praveenkumar/'},
    {'photo': 'https://th.bing.com/th/id/OIP.l6nPLCiWuJkhte2Ru60fdQAAAA?pid=ImgDet&rs=1',
     'caption': 'Dr. Arivazhagan B \n https://vetias.ac.in/faculty/dr-b-arivazhagan/'}

]
p14 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/arulraj_vetias.jpg',
     'caption': 'Dr. Arulraj S \n https://vetias.ac.in/faculty/dr-s-arulraj/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/umamaheswari_vetias.jpg',
     'caption': 'Dr. Umamaheswari S \n https://vetias.ac.in/faculty/dr-s-umamaheswari/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/krishnaveni_vetias.jpg',
     'caption': 'Dr. Krishnaveni C \n https://vetias.ac.in/faculty/dr-c-krishnaveni/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/anbupriya_vetias.jpg',
     'caption': 'Dr. Anbupriya D \n https://vetias.ac.in/faculty/dr-d-anbupriya/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/ananthkumar_vetias.jpg',
     'caption': 'Dr. Anantha kumar S \n https://vetias.ac.in/faculty/anantha-kumar-sivananthan/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/7priyadharshini.jpg',
     'caption': 'Ms. Priyadharshini K \n https://vetias.ac.in/faculty/ms-priyadharshini-k/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/8maheswari-mam.jpg',
     'caption': 'Dr. Maheshwari R \n https://vetias.ac.in/faculty/dr-maheshwari-r/'}
]

p15 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/murali_vetias.jpg',
     'caption': 'Dr. Murali P \n https://vetias.ac.in/faculty/p-murali/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/Santhi.jpg',
     'caption': 'Dr. Santhi L \n https://vetias.ac.in/faculty/dr-l-santhi/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/nagalakshmi.jpg',
     'caption': 'Dr. Nagalakshmi Ranganathan \n https://vetias.ac.in/faculty/dr-nagalakshmi-ranganathan/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/hemasri.jpg',
     'caption': 'Ms. Hema Sri S \n https://vetias.ac.in/faculty/ms-hema-sri-s/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/palaniammal.jpg',
     'caption': 'Dr. Palaniammal Kalingarayan S \n https://vetias.ac.in/faculty/dr-s-palaniammal-kalingarayan/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/poonkundran_vetias.jpg',
     'caption': 'Mr. Poonkundran K '},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/6Rajendran.jpg',
     'caption': 'Dr. Rajendran L \n https://vetias.ac.in/faculty/dr-l-rajendran/'}
]

p16 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/vellingiri.jpg',
     'caption': 'Dr. Vellingiri P \n https://vetias.ac.in/faculty/p-murali/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/jayashree.jpg',
     'caption': 'Ms. Jayashree R \n https://vetias.ac.in/faculty/dr-l-santhi/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/santhi_v_n.jpg',
     'caption': 'Dr. Shanthi V N \n https://vetias.ac.in/faculty/dr-nagalakshmi-ranganathan/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/Guruvendran.jpg',
     'caption': 'Mr. Guruvendran S \n https://vetias.ac.in/faculty/ms-hema-sri-s/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/Mohanasundari.jpg',
     'caption': 'Dr. Mohanasundari D \n https://vetias.ac.in/faculty/dr-s-palaniammal-kalingarayan/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/6amuthanandhini.jpg',
     'caption': 'Dr. Amuthanandhini A '}

]

p17 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/yashir.jpg',
     'caption': 'Dr. Yasir Ashraf \n https://vetias.ac.in/faculty/dr-yasir-ashraf/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/03/Mrinialini.jpg',
     'caption': 'Dr. Mrinalini S \n https://vetias.ac.in/faculty/dr-mrinalini-s/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/5.Ayana_.jpg',
     'caption': 'Ms.Ayana Shajan \n https://vetias.ac.in/faculty/ms-ayana-shajan/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/6Ramesh.jpg',
     'caption': 'Mr. Ramesh Babu M \n https://vetias.ac.in/faculty/mr-ramesh-babu-m/'},
    {'photo': 'https://th.bing.com/th/id/OIP.l6nPLCiWuJkhte2Ru60fdQAAAA?pid=ImgDet&rs=1',
     'caption': 'Mr.Kasi Dharan T \n https://vetias.ac.in/faculty/mr-kasi-dharan-t/'}

]

p18 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/rajalakshmi_vetias.jpg',
     'caption': 'Dr. Rajalakshmi M \n https://vetias.ac.in/faculty/dr-yasir-ashraf/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/swetha.jpg',
     'caption': 'Ms. Swedha R \n https://vetias.ac.in/faculty/dr-mrinalini-s/'},
    {'photo': 'https://th.bing.com/th/id/OIP.l6nPLCiWuJkhte2Ru60fdQAAAA?pid=ImgDet&rs=1',
     'caption': 'Mr. Jeeva S \n https://vetias.ac.in/faculty/ms-ayana-shajan/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/dhurgha_niranjankumar_vetias.jpg',
     'caption': 'Ms. Dhurgha Niranjan Kumar \n https://vetias.ac.in/faculty/mr-ramesh-babu-m/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/07/ashok-kannan.jpg',
     'caption': 'Mr. Ashok Kannan \n https://vetias.ac.in/faculty/mr-kasi-dharan-t/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/07/raja-ram.jpg',
     'caption': 'Mr. Rajaram T \n https://vetias.ac.in/faculty/ms-ayana-shajan/'}
]

p19 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/mohanasundari_vetias.jpg',
     'caption': 'Dr. Mohanasundari L \n https://vetias.ac.in/faculty/dr-mohanasundari-l/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/sarikaa-1.png',
     'caption': 'Ms. Sarikaa M \n https://vetias.ac.in/faculty-directory/#'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/manopriya_vetias.jpg',
     'caption': 'Dr. Manopriya M \n https://vetias.ac.in/faculty/dr-manopriya-m/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/revathy_vetias.jpg',
     'caption': 'Ms. Revathy P \n https://vetias.ac.in/faculty/ms-revathy-p/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/puspapriya_vetias.jpg',
     'caption': 'Ms. Pushpapriya D \n https://vetias.ac.in/faculty/ms-pushpapriya-d/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/geetha.jpg',
     'caption': 'Ms. Geetha D \n https://vetias.ac.in/faculty/ms-geetha-d/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/8Ayyeswarya.jpg',
     'caption': 'MS. Ayyeswarya J \n https://vetias.ac.in/faculty/ms-ayyeswarya-j/'},
    {'photo': 'https://th.bing.com/th/id/OIP.l6nPLCiWuJkhte2Ru60fdQAAAA?pid=ImgDet&rs=1',
     'caption': 'Dr.Sathish Kumar C \n https://vetias.ac.in/faculty/dr-sathish-kumar-c/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/10Gayathri.jpg',
     'caption': 'Ms.Gayathri V \n https://vetias.ac.in/faculty/ms-gayathri-v/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/11Agarsana.jpg',
     'caption': 'Ms.Agarsana T K \n https://vetias.ac.in/faculty/ms-agarsana-t-k/'}

]

p20 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/suress_vetias.jpg',
     'caption': 'Dr. Suress CR \n https://vetias.ac.in/faculty/dr-c-r-suress/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/dinesh-1.jpg',
     'caption': 'Dr. Dineshwaran M \n https://vetias.ac.in/faculty/dr-m-dineshwaran/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/dhinesh.jpg',
     'caption': 'Dr. Dhinesh D \n https://vetias.ac.in/faculty/dr-d-dhinesh/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/mahadevi_vetias.jpg',
     'caption': 'Dr. Mahadevi N \n https://vetias.ac.in/faculty/dr-n-mahadevi/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/5Paramasivam.jpg',
     'caption': 'Dr. Paramasivam N \n https://vetias.ac.in/faculty/dr-n-paramasivam/'}
]

p21 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/rathika_1.png',
     'caption': 'Dr. Radhika C \n https://vetias.ac.in/faculty/radhika-c/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/jagadeesan_vetias.jpg',
     'caption': 'Mr. Jagadeesan S \n https://vetias.ac.in/faculty/jagadeesan-s/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/aumdhamalar_vetias.jpg',
     'caption': 'Ms. Amudhamalar V \n https://vetias.ac.in/faculty/amudhamalar-v/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/jayabrindha_vetias.jpg',
     'caption': 'Ms. Jayabrindha D \n https://vetias.ac.in/faculty/jayabrindha-d/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/5kousalya-.jpg',
     'caption': 'Ms. Kousalya P \n https://vetias.ac.in/faculty/ms-kousalya-p/'}
]

p22 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/07/0003_1principal.jpg',
     'caption': 'Dr. Saravanan R \n https://vetias.ac.in/faculty/dr-saravanan-r/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/07/0002_2lokesh.jpg',
     'caption': 'Mr. Logeshkumar S \n https://vetias.ac.in/faculty/mr-logeshkumar-s/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/vijayanand.jpg',
     'caption': 'Dr. Vijayanand S \n https://vetias.ac.in/faculty/dr-s-vijayanand/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/lavanya_vetias.jpg',
     'caption': 'Dr. Lavanya R \n https://vetias.ac.in/faculty/dr-r-lavanya/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/poongulale_vetias.jpg',
     'caption': 'Dr. Poongulale M P \n https://vetias.ac.in/faculty/dr-m-p-poongulale/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/01/srijanani_vetias.jpg',
     'caption': 'Ms. Sri Janani A K \n https://vetias.ac.in/faculty/ms-sri-janani-a-k/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/03/Arulananth.jpg',
     'caption': 'Mr. Arulananth P \n https://vetias.ac.in/faculty/mr-arulananth-p/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/07/0001_8thernika_vetias.jpg',
     'caption': 'Ms. Thernika R \n https://vetias.ac.in/faculty/ms-thernika-r/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/10/9.Sasetharan.jpg',
     'caption': 'Dr. Sasetharan G T \n https://vetias.ac.in/faculty/dr-g-t-sasetharan/'}
]

p23 = [
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/06/subha.jpg',
     'caption': 'Dr. Subha S \n https://vetias.ac.in/faculty/dr-s-subha/'},
    {'photo': 'https://vetias.ac.in/wp-content/uploads/2022/07/0000_2.devi-abirami.jpg',
     'caption': 'Ms. Devi Abirami L S \n https://vetias.ac.in/faculty/devi-abirami-ls/'}

]


def tel_parse_message(message):
    print("message-->", message)
    try:
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        print("chat_id-->", chat_id)
        with open('output.txt', 'a') as f:
            try:
                f.write(txt + '\n')
            except:
                f.write('emoji' + '\n')
        return chat_id, txt
    except:
        print("NO text found-->>")


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    k = requests.post(url, json=payload)

    return k


def tel_send_images(chat_id, photos):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    for photo_with_caption in photos:
        caption = photo_with_caption.get('caption', '')
        photo_url = photo_with_caption['photo']
        payload = {
            'chat_id': chat_id,
            'photo': photo_url,
            'caption': caption
        }
        k = requests.post(url, json=payload)
        # do something with the response if needed
    return

def tel_send_poll(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    payload = {
        'chat_id': chat_id,
        "question": "It usefull for you ",
        "options": json.dumps(["YES", "NO"]),
        "is_anonymous": False,
 
    }
    k = requests.post(url, json=payload)
    return k

def tel_send_inlineurl(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
            "chat_id" : chat_id,
            "text" : "Join us",
            "reply_markup" : {
                    "inline_keyboard" : [
                            [
                                {"text" : "website", "url" : "https://vetias.ac.in/"},
                                {"text" : "telegram", "url" : "https://t.me/lkhitech"}
                            ]
                    ]
            }
    }

    k = requests.post(url, json=payload)
    return k


@app.route('/', methods=['GET', 'POST'])
def handle_Telegram():
    if request.method == 'POST':
        msg = request.get_json()

        try:
            chat_id, txt = tel_parse_message(msg)
            txt1 = long.get_response(txt)
            if txt1 == long.Principal_name:
                tel_send_images(chat_id, photos=p)
            elif txt1 == long.ao:
                tel_send_images(chat_id, photos=p1)
            elif txt1 == long.Dean:
                tel_send_images(chat_id, photos=p2)
            elif txt1 == long.Secretary_name:
                tel_send_images(chat_id, photos=p3)
            elif txt1 == long.B_Com_CA_HOD:
                tel_send_images(chat_id, photos=p4)
            elif txt1 == long.B_Com_HOD:
                tel_send_images(chat_id, photos=p5)
            elif txt1 == long.BBA_HOD:
                tel_send_images(chat_id, photos=p6)
            elif txt1 == long.Computer_science_HOD:
                tel_send_images(chat_id, photos=p7)
            elif txt1 == long.Computer_Application_HOD:
                tel_send_images(chat_id, photos=p8)
            elif txt1 == long.School_of_Social_Studies_HOD:
                tel_send_images(chat_id, photos=p9)
            elif txt1 == long.B_Com_PA_AF_HOD:
                tel_send_images(chat_id, photos=p_af)
            elif txt1 == long.School_of_Fashion_HOD:
                tel_send_images(chat_id, photos=p10)
            elif txt1 == long.School_of_Literature_HOD:
                tel_send_images(chat_id, photos=p11)
            elif txt1 == long.Infrastructure:
                tel_send_images(chat_id, photos=p12)
            elif txt1 == long.Faculty_List_computer_science:
                tel_send_images(chat_id, photos=p13)
            elif txt1 == long.Faculty_List_BCOM:
                tel_send_images(chat_id, photos=p14)
            elif txt1 == long.Faculty_List_BCOMPAAF:
                tel_send_images(chat_id, photos=p15)
            elif txt1 == long.Faculty_List_BCOM_CA:
                tel_send_images(chat_id, photos=p16)
            elif txt1 == long.Faculty_List_School_of_Social_Studies:
                tel_send_images(chat_id, photos=p17)
            elif txt == long.Faculty_List_School_of_Fashion:
                tel_send_images(chat_id, photos=p18)
            elif txt == long.Faculty_List_School_of_Literature:
                tel_send_images(chat_id, photos=p19)
            elif txt == long.Faculty_List_School_of_Tamil:
                tel_send_images(chat_id, photos=p20)
            elif txt == long.Faculty_List_School_of_Mathematics:
                tel_send_images(chat_id, photos=p21)
            elif txt == long.Faculty_List_School_of_Business:
                tel_send_images(chat_id, photos=p22)
            elif txt == long.Faculty_List_Library:
                tel_send_images(chat_id, photos=p23)
            elif txt == "poll":
                tel_send_poll(chat_id)
            elif txt == "link":
                tel_send_inlineurl(chat_id)
            else:
                tel_send_message(chat_id, txt1)
        except:
            print("from index-->")

        return Response('ok', status=200)
    else:
        return render_template("navesh.html")
@app.route('/whatsapp', methods=['POST'])
def handle_whatsapp():
    incoming_msg = request.values.get('Body', '')
    client_number = request.form['From']
    #print(f"Client's number: {client_number}")
    resp = MessagingResponse()
    txt2 = incoming_msg.lower()
    txt = long.get_response(txt2)
    with open('output.txt', 'a') as f:
        try:
            f.write(txt2 + '\t' + client_number + '\n')
        except:
            f.write('emoji' + '\n')

    try:
        if txt == long.ao:
            # Create a message with an image
            message = resp.message()
            message.media(p1[0]['photo'])
            message.body(p1[0]['caption'])
        elif txt == long.Principal_name:
            message = resp.message()
            message.media(p[0]['photo'])
            message.body(p[0]['caption'])
        elif txt == long.Dean:
            message = resp.message()
            message.media(p2[0]['photo'])
            message.body(p2[0]['caption'])
        elif txt == long.Secretary_name:
            message = resp.message()
            message.media(p3[0]['photo'])
            message.body(p3[0]['caption'])
        elif txt == long.B_Com_CA_HOD:
            message = resp.message()
            message.media(p4[0]['photo'])
            message.body(p4[0]['caption'])
        elif txt == long.B_Com_HOD:
            message = resp.message()
            message.media(p5[0]['photo'])
            message.body(p5[0]['caption'])
        elif txt == long.BBA_HOD:
            message = resp.message()
            message.media(p6[0]['photo'])
            message.body(p6[0]['caption'])
        elif txt == long.Computer_science_HOD:
            message = resp.message()
            message.media(p7[0]['photo'])
            message.body(p7[0]['caption'])
        elif txt == long.Computer_Application_HOD:
            message = resp.message()
            message.media(p8[0]['photo'])
            message.body(p8[0]['caption'])
        elif txt == long.School_of_Social_Studies_HOD:
            message = resp.message()
            message.media(p9[0]['photo'])
            message.body(p9[0]['caption'])
        elif txt == long.School_of_Fashion_HOD:
            message = resp.message()
            message.media(p10[0]['photo'])
            message.body(p10[0]['caption'])
        elif txt == long.School_of_Literature_HOD:
            message = resp.message()
            message.media(p11[0]['photo'])
            message.body(p11[0]['caption'])
        elif txt == long.Infrastructure:
            for pq in p12:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        elif txt == long.Faculty_List_computer_science:
            for pq in p13:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        elif txt == long.Faculty_List_BCOM:
            for pq in p14:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        elif txt == long.Faculty_List_BCOMPAAF:
            for pq in p15:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        elif txt == long.Faculty_List_BCOM_CA:
            for pq in p16:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        elif txt == long.Faculty_List_School_of_Social_Studies:
            for pq in p17:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        elif txt == long.Faculty_List_School_of_Fashion:
            for pq in p18:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        elif txt == long.Faculty_List_School_of_Literature:
            for pq in p19:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        elif txt == long.Faculty_List_School_of_Tamil:
            for pq in p20:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        elif txt == long.Faculty_List_School_of_Mathematics:
            for pq in p21:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        elif txt == long.Faculty_List_School_of_Business:
            for pq in p22:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        elif txt == long.Faculty_List_Library:
            for pq in p23:
                message = resp.message()
                message.media(pq['photo'])
                message.body(pq['caption'])
        else:
            resp.message(txt)
    except:
        print("from index-->")
    return str(resp)


@app.route("/get", methods=['POST'])
def get_bot_response():
    user_text = request.get_json()['msg']
    bot = long.get_response(user_text)
    return jsonify(response=bot)


if __name__ == '__main__':
    app.run(threaded=True)
