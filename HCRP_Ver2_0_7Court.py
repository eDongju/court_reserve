#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from tkinter import *
from datetime import date, timedelta

import schedule
import time
import requests

# 코트 예약 설정을 위한 윈도우 창을 만들기

win = Tk()

win.title("HCRP_Ver2.0 by eDj @2021")
win.geometry("380x890")
win.option_add("*Font", "궁서체 12") # 창 안에 들어가는 폰트 크기

win.configure(bg = '#F7F8E0')

# 윈도우 창에 한울타리 로고 넣기

lab_h = Label(win)
img = PhotoImage(file = "C:\T_booking\한울타리.png", master = win)
img = img.subsample(8)
lab_h.config(image = img)
lab_h.grid(column = 1, row = 0, columnspan = 2)

# 프로그램 이름

lab0 = Label(win)
lab0.config(text = "코트예약\n프로그램\n\nHanultary Court\nReserve Program")
lab0.grid(column = 0, row = 0, padx = 10, pady = 5)


# ID 라벨 삽입

lab1 = Label(win)
lab1.config(text = "ID")
lab1.grid(column = 0, row = 1, padx = 10, pady = 5)

# ID 입력창 : ID를 창에 보여주고 오른쪽 마우스로 클릭하면 없어지게하고 새로 입력 가능

ent1 = Entry(win)

ent1.insert(0, "itkim67")
def clear(event):
    if ent1.get() == "itkim67":
        ent1.delete(0,len(ent1.get()))
ent1.bind("<Button-1>", clear)

ent1.grid(column = 1, row = 1, padx = 10, pady = 5)

# PW 라벨 삽입

lab2 = Label(win)
lab2.config(text = "Password")
lab2.grid(column = 0, row = 2, padx = 10, pady = 5)

# PW 입력창

ent2 = Entry(win)
#ent2.config(show = "*") # 암호를 안보여주게 할 수 있는 함수

ent2.insert(0, "k23367090!")
def clear(event):
    if ent2.get() == "k23367090!":
        ent2.delete(0,len(ent2.get()))
ent2.bind("<Button-1>", clear)

ent2.grid(column = 1, row = 2, padx = 10, pady = 5)

# 날짜 라벨

lab3 = Label(win)
lab3.config(text = "사용 날짜\n(예)date-20210420")
lab3.grid(column = 0, row = 3, padx = 10, pady = 5)

# 사용 날짜 오늘 + 1주일 후로 자동 입력 됩니다.

ent3 = Entry(win)

ent3.insert(0, "자동입력(+1 week)")
def clear(event):
    if ent3.get() == "자동입력(+1 week)":
        ent3.delete(0,len(ent3.get()))
ent3.bind("<Button-1>", clear)
ent3.grid(column = 1, row = 3, padx = 10, pady = 5)

today = date.today()
week = timedelta(weeks=1)

due_day = today + week
input_day = "date-"+due_day.strftime('%Y%m%d')

# 날짜 수동으로 입력할 수 있게 선택 버튼 추가

var40 = IntVar()
check40 = Checkbutton(win, text="수동 입력", variable=var40, onvalue=1, offvalue=0)
check40.grid(column = 0, row = 4, padx = 10, pady = 5)
    
# 코트 라벨
lab4 = Label(win)
lab4.config(text = "★ 사용 코트 ★")
lab4.grid(column = 0, row = 5, padx = 10, pady = 10)

# 코트 선택
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()

check21 = Checkbutton(win, text="1코트", variable=var21, onvalue=1, offvalue=0)
check22 = Checkbutton(win, text="2코트", variable=var22, onvalue=1, offvalue=0)
check23 = Checkbutton(win, text="3코트", variable=var23, onvalue=1, offvalue=0)
check24 = Checkbutton(win, text="4코트", variable=var24, onvalue=1, offvalue=0)
check25 = Checkbutton(win, text="5코트", variable=var25, onvalue=1, offvalue=0)
check26 = Checkbutton(win, text="6코트", variable=var26, onvalue=1, offvalue=0)
check27 = Checkbutton(win, text="7코트", variable=var27, onvalue=1, offvalue=0)
check28 = Checkbutton(win, text="8코트", variable=var28, onvalue=1, offvalue=0)
check29 = Checkbutton(win, text="9코트", variable=var29, onvalue=1, offvalue=0)

check21.grid(column=0, row=6, padx = 2, pady = 5)
check22.grid(column=0, row=7, padx = 10, pady = 5)
check23.grid(column=0, row=8, padx = 10, pady = 5)
check24.grid(column=0, row=9, padx = 10, pady = 5)
check25.grid(column=0, row=10, padx = 10, pady = 5)
check26.grid(column=1, row=6, padx = 10, pady = 5)
check27.grid(column=1, row=7, padx = 10, pady = 5)
check28.grid(column=1, row=8, padx = 10, pady = 5)
check29.grid(column=1, row=9, padx = 10, pady = 5)

# 사용시간 라벨
lab6 = Label(win)
lab6.config(text = "★ 사용 시간 ★")
lab6.grid(column = 0, row = 11, padx = 10, pady = 10)

# 사용시간 라벨
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()

check1 = Checkbutton(win, text="8시", variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(win, text="9시", variable=var2, onvalue=1, offvalue=0)
check3 = Checkbutton(win, text="10시", variable=var3, onvalue=1, offvalue=0)
check4 = Checkbutton(win, text="11시", variable=var4, onvalue=1, offvalue=0)
check5 = Checkbutton(win, text="12시", variable=var5, onvalue=1, offvalue=0)
check6 = Checkbutton(win, text="13시", variable=var6, onvalue=1, offvalue=0)
check7 = Checkbutton(win, text="14시", variable=var7, onvalue=1, offvalue=0)
check8 = Checkbutton(win, text="15시", variable=var8, onvalue=1, offvalue=0)
check9 = Checkbutton(win, text="16시", variable=var9, onvalue=1, offvalue=0)
check10 = Checkbutton(win, text="17시", variable=var10, onvalue=1, offvalue=0)
check11 = Checkbutton(win, text="18시", variable=var11, onvalue=1, offvalue=0)

check1.grid(column=0, row=12, padx = 2, pady = 5)
check2.grid(column=0, row=13, padx = 10, pady = 5)
check3.grid(column=0, row=14, padx = 10, pady = 5)
check4.grid(column=0, row=15, padx = 10, pady = 5)
check5.grid(column=0, row=16, padx = 10, pady = 5)
check6.grid(column=1, row=12, padx = 10, pady = 5)
check7.grid(column=1, row=13, padx = 10, pady = 5)
check8.grid(column=1, row=14, padx = 10, pady = 5)
check9.grid(column=1, row=15, padx = 10, pady = 5)
check10.grid(column=1, row=16, padx = 10, pady = 5)
check11.grid(column=1, row=17, padx = 10, pady = 5)

# ID 라벨
lab17 = Label(win)
lab17.config(text = "★ 시작 시간 ★")
lab17.grid(column = 0, row =18, padx = 10, pady = 5)

# ID 입력창
ent17 = Entry(win)

ent17.insert(0, "08:59")
def clear(event):
    if ent17.get() == "08:59":
        ent17.delete(0,len(ent17.get()))
ent17.bind("<Button-1>", clear)

ent17.grid(column = 1, row = 18, padx = 10, pady = 20)

# 입력 버튼
btn1 = Button(win)
btn1.config(text = "입력")
def data_input():
    user_name = ent1.get()
    user_pw = ent2.get()
    t_operation = ent17.get()

    if var40.get() == 1:
        date = ent3.get()
    else :
        date = input_day
    
    lab3.config(text = "[데이터] 입력 성공!")

    def job_day():
    
        driver = webdriver.Chrome('C:\T_booking\chromedriver.exe')

        url = 'https://www.gunpouc.or.kr/fmcs/160?referer=%2Ffmcs%2F157'
        driver.get(url)
        time.sleep(1)

        xpath1 = "//input[@id='user_id']"
        input_id = driver.find_element_by_xpath(xpath1)
        input_id.send_keys("{}".format(user_name)) # ★★★★★★★
        time.sleep(1)

        xpath2 = "//input[@id='user_password']"
        input_pw = driver.find_element_by_xpath(xpath2)
        input_pw.send_keys("{}".format(user_pw)) # ★★★★★★★
        time.sleep(1)

        xpath3 = "//button[@type='submit']"
        login_btn = driver.find_element_by_xpath(xpath3)
        login_btn.click()
        time.sleep(1)

        xpath4 = "//select[@id='center']"
        select_btn1 = driver.find_element_by_xpath(xpath4).click()
        select_btn1 = driver.find_element_by_xpath(xpath4).send_keys("시민체육광장")
        time.sleep(1)

        xpath5 = "//select[@id='part']"
        select_btn2 = driver.find_element_by_xpath(xpath5).click()
        select_btn2 = driver.find_element_by_xpath(xpath5).send_keys("테니스장")
        time.sleep(1)

        xpath6 = "//select[@id='place']"
               
        if var21.get() == 1 :
            select_btn3 = driver.find_element_by_xpath(xpath6).click()
            select_btn3 = driver.find_element_by_xpath(xpath6).send_keys("1코트")
            court_en1 = 784
        else :
            court_en1 = 0
            
        if var22.get() == 1 :
            select_btn3 = driver.find_element_by_xpath(xpath6).click()
            select_btn3 = driver.find_element_by_xpath(xpath6).send_keys("2코트")
            court_en2 = 800
        else :
            court_en2 = 0

        if var23.get() == 1 :
            select_btn3 = driver.find_element_by_xpath(xpath6).click()
            select_btn3 = driver.find_element_by_xpath(xpath6).send_keys("3코트")
            court_en3 = 816
        else :
            court_en3 = 0
        
        if var24.get() == 1 :
            select_btn3 = driver.find_element_by_xpath(xpath6).click()
            select_btn3 = driver.find_element_by_xpath(xpath6).send_keys("4코트")
            court_en4 = 832
        else :
            court_en4 = 0
        
        if var25.get() == 1 :
            select_btn3 = driver.find_element_by_xpath(xpath6).click()
            select_btn3 = driver.find_element_by_xpath(xpath6).send_keys("5코트")
            court_en5 = 848
        else :
            court_en5 = 0
        
        if var26.get() == 1 :
            select_btn3 = driver.find_element_by_xpath(xpath6).click()
            select_btn3 = driver.find_element_by_xpath(xpath6).send_keys("6코트")
            court_en6 = 864
        else :
            court_en6 = 0
                        
        if var27.get() == 1 :
            select_btn3 = driver.find_element_by_xpath(xpath6).click()
            select_btn3 = driver.find_element_by_xpath(xpath6).send_keys("7코트")
            court_en7 = 880
        else :
            court_en7 = 0
            
        if var28.get() == 1 :
            select_btn3 = driver.find_element_by_xpath(xpath6).click()
            select_btn3 = driver.find_element_by_xpath(xpath6).send_keys("8코트")
            court_en8 = 896
        else :
            court_en8 = 0
            
        if var29.get() == 1 :
            select_btn3 = driver.find_element_by_xpath(xpath6).click()
            select_btn3 = driver.find_element_by_xpath(xpath6).send_keys("9코트")
            court_en9 = 960
        else :
            court_en9 = 0
            
        time.sleep(1)
        
        xpath7 = "//button[@type='submit']"
        search_btn = driver.find_element_by_xpath(xpath7).click()
        time.sleep(1)

    # 신청하는 월이 이번달이 아니고 다음달 인경우 아래 if문에서 확인 한다.
        
        year_month = driver.find_element_by_class_name("title_month")
        get_year_month = year_month.text
        
        get_month_from_web = get_year_month[5:7]
        get_month_from_win = date[9:11]
        time.sleep(2)
        
        if get_month_from_web != get_month_from_win :
            xpath202 = "//a[@id='next_month']"
            select_btn202 = driver.find_element_by_xpath(xpath202).click()
            time.sleep(1)
                   
    # 신청할 날짜 선택

        xpath8 = "//td[@id='{}']".format(date)
        date_btn = driver.find_element_by_xpath(xpath8).click()
        time.sleep(1)

        while True:
            xpath101 = "//tbody/tr[1]/td[1]/input"
            select_en = driver.find_element_by_xpath(xpath101).get_attribute('value')

            if select_en == '{};1부;0600;0700;1'.format(court_en1):
                check_box = "1번 코트"

                break
                
            if select_en == '{};1부;0600;0700;1'.format(court_en2):
                check_box = "2번 코트"

                break

            if select_en == '{};1부;0600;0700;1'.format(court_en3):
                check_box = "3번 코트"

                break
            
            if select_en == '{};1부;0600;0700;1'.format(court_en4):
                check_box = "4번 코트"

                break               
                
            if select_en == '{};1부;0600;0700;1'.format(court_en5):
                check_box = "5번 코트"

                break
            
            if select_en == '{};1부;0600;0700;1'.format(court_en6):
                check_box = "6번 코트"

                break 

            if select_en == '{};1부;0600;0700;1'.format(court_en7):
                check_box = "7번 코트"

                break                

            if select_en == '{};1부;0600;0700;1'.format(court_en8):
                check_box = "8번 코트"

                break                
            
            if select_en == '{};1부;0600;0700;1'.format(court_en9):
                check_box = "9번 코트"

                break
                
            else :
                driver.refresh()
            time.sleep(3)

    # 코트 선택 시간

        xpath9_8 = "//input[@id='checkbox_time_2']"  # 8시
        xpath9_9 = "//input[@id='checkbox_time_3']" # 9시
        xpath9_10 = "//input[@id='checkbox_time_4']" # 10시
        xpath9_11 = "//input[@id='checkbox_time_5']" # 11시
        xpath9_12 = "//input[@id='checkbox_time_6']" # 12시
        xpath9_13 = "//input[@id='checkbox_time_7']" # 13시
        xpath9_14 = "//input[@id='checkbox_time_8']" # 14시
        xpath9_15 = "//input[@id='checkbox_time_9']" # 15시
        xpath9_16 = "//input[@id='checkbox_time_10']" # 16시
        xpath9_17 = "//input[@id='checkbox_time_11']" # 17시
        xpath9_18 = "//input[@id='checkbox_time_12']" # 17시

    # 신청할 시간 선택 "checkbox_time_2(8시) 3~5(9시~11시), 6(12시), 7~10(13시~16시)"

        if var1.get() == 1 :
            driver.find_element_by_xpath(xpath9_8).click()

        if var2.get() == 1 :
            driver.find_element_by_xpath(xpath9_9).click()

        if var3.get() == 1 :
            driver.find_element_by_xpath(xpath9_10).click()

        if var4.get() == 1 :
            driver.find_element_by_xpath(xpath9_11).click()

        if var5.get() == 1 :
            driver.find_element_by_xpath(xpath9_12).click()

        if var6.get() == 1 :
            driver.find_element_by_xpath(xpath9_13).click()

        if var7.get() == 1 :
            driver.find_element_by_xpath(xpath9_14).click()

        if var8.get() == 1 :
            driver.find_element_by_xpath(xpath9_15).click()

        if var9.get() == 1 :
            driver.find_element_by_xpath(xpath9_16).click()

        if var10.get() == 1 :
            driver.find_element_by_xpath(xpath9_17).click()

        if var11.get() == 1 :
            driver.find_element_by_xpath(xpath9_18).click()

    # 대관신청 버튼을 클릭한다.

        xpath10 = "//button[@class='action_application']"
        driver.find_element_by_xpath(xpath10).click()
        time.sleep(1)

    # 한울타리 팀 이름 입력

        xpath11 = "//input[@id='team_nm']"
        driver.find_element_by_xpath(xpath11).click()
        driver.find_element_by_xpath(xpath11).send_keys("한울")
        time.sleep(0.2)

    # 코트 참가 인원 입력

        xpath12 = "//input[@id='users']"
        driver.find_element_by_xpath(xpath12).click()
        driver.find_element_by_xpath(xpath12).send_keys("8")

        time.sleep(0.2)

    # 모임의 목적 입력

        xpath13 = "//input[@id='purpose']"
        driver.find_element_by_xpath(xpath13).click()
        driver.find_element_by_xpath(xpath13).send_keys("운동")
        time.sleep(0.2)

    # 코트 사양 동의서 클릭한다.

        xpath14 = "//input[@id='agree_use1']"
        driver.find_element_by_xpath(xpath14).click()
        time.sleep(0.2)

    # 시설 사용 신청을 한다.

        xpath15 = "//button[@class='button action_write']"
        driver.find_element_by_xpath(xpath15).click()

    # 예약 완료되면 Slack으로 메세지 송부

        def post_message(token, channel, text):
            response = requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer "+token},
            data={"channel": channel,"text": text}
        )

        myToken = "xoxb-1832546090711-1832599956391-fZu9oVOllr326Hy0uxzJrD82"

        post_message(myToken,"#tbooking","'{}' 예약 완료".format(check_box))

    schedule.every().days.at("{}".format(t_operation)).do(job_day)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
btn1.config(command = data_input)
btn1.grid(column = 1, row = 19, columnspan = 2, padx = 10, pady = 10)

# 메세지 라벨
lab3 = Label(win)
lab3.grid(column = 1, row = 20, columnspan = 2)

win.mainloop()


# In[ ]:




