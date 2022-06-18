﻿
# player 
define player = DynamicCharacter('player_name', color="#cc2cdb")

# v = vtuber
define v_chika = Character("Chika")
define v_reira = Character("Reira")
define v_nimone = Character("Nimone")
define v_sylphy = Character("Sylphy") 

# ex = extra character
define ex_player_dad = Character("พ่อ")
define unknown_character = Character("???")

# The game starts here.

label start:
    scene bg room
    show eileen happy

    # Use in case of dev
    $ player_name = "หลีกิมฮวง"
    "{a=jump:dev_portal}DEV PORTAL{/a}"

    # Use in case of production
    # $ player_name = renpy.input("กรุณาใส่ชื่อผู้เล่น", length=20)
    # $ player_name = player_name.strip()
    # if player_name == "":
    #     $ player_name = "หลีกิมฮวง" 
 
    # Episode Prologue
    # Scene 1 - player house; front 
    player "นานแค่ไหนแล้วนะ ที่ไม่ได้กลับมาที่บ้านหลังนี้" 
    "ผมสูดอากาศบริสุทธิ์และกวาดตามองไปรอบ ๆ ช่างเป็นบรรยากาศที่น่าคิดถึงจริง ๆ ผมมองไปยังบ้านชั้นเดียวหลังหนึ่งที่ต้นไม้ใบหญ้าตะไคร่เกาะ ราขึ้นเต็มไปหมด… เหมือนไม่มีใครดูแลมาซักพักนึงแล้ว" 
    "ต้องใช้เวลาซัก 2-3 วันในการจัดการบ้านหลังใหม่ของผมนี้ให้เข้าที่เข้าทางพร้อมอาศัย"
    
    "{size=50} -- 2 สัปดาห์ก่อนหน้านี้ --  {/size}"
    
    # Scene 2 - Japan; Dad car
    "นี่ก็เป็นอีกวันที่ญี่ปุ่น ผมนั่งรถกลับบ้านกับพ่อเหมือนทุกๆวัน ผ่านถนนทางเลียบภูเขาริมทะเล ซึ่งภาพเหล่านี้ก็เป็นสิ่งที่ผมเห็นอยู่ทุกวัน"
    
    ex_player_dad "เออนี่ ไอลูกชาย"
    player "เอ้อ ว่าไง"
    ex_player_dad "พ่อคิดว่า..."
    ex_player_dad "พ่อน่าจะได้บินไปอีกหลายที่น่ะนะ"
    player "อ่าฮะ แล้ว ?"
    ex_player_dad "คือ..."
    ex_player_dad "พ่ออยากจะให้ลูกกลับไปที่ไทยแหละ"
    ex_player_dad "แม่แกขอไว้ตอนพ่อพาลูกไปรอบโลก แกบอกว่าอยากให้ลูกได้มาเริ่มต้นที่นี่ด้วยตัวเองในตอนที่ลูกพร้อมแล้ว"
    player "อายุ 17 เนี่ยนะที่พ่อว่าพร้อม!"

    ex_player_dad "ถ้าสำหรับเด็กบ้านอื่นก็คงเป็นแบบนั้น แต่บ้านเรา.. ก็ไม่แน่"
    player "รู้ดีอย่างกับเป็นพ่อคนมาแล้วเลย"
    ex_player_dad "ก็เป็นพ่อสิวะ!! ไอ้ลูกคนนี้นี่"
    player "เอาเถอะ ที่ไทยเหรอ อืมม น่าคิดถึงเนอะ เธอคนนั้น.. จะยังอยู่รึเปล่านะ"

    "ผมนึกถึงภาพในอดีตขึ้นมา มันเป็นความทรงจำที่หอมหวาน ภาพในวันนั้นเป็นภาพของเด็กผู้หญิงคนหนึ่ง พวกเราเคยเล่นด้วยกันตลอดทุกๆวัน" 
    "มันเป็นช่วงเย็นวันสุดท้ายก่อนที่ผมจะย้ายออกจากไทยตามครอบครัวไปอยู่ที่ญี่ปุ่น ความทรงจำที่ไม่เคยลืมเลือนหายจากใจผมไป ความทรงจำนั้นบอกผมว่า เราเคยสัญญากัน สัญญากับเธอ"

    unknown_character "เธอจะกลับมาอีกใช่ไหม สัญญานะ!"
    player "อื้ม! เราสัญญา"

    "แล้วเราก็เกี่ยวก้อยสัญญากัน ผ่านไป 10 ปี ในใจลึก ๆ ของผมนั้นกลับหวังให้เธอยังอยู่ที่นั่น และนี่ก็เป็นโอกาศอันดีที่ผมจะได้กลับไปหาเธอ"
    player "เอาสิ"
    "ทันใดนั้นเองคุณพ่อก็เหยียบเบรกดังลั่น"
    "{size=50}{b}เอี๊ยดด!! {/b}{/size}"
    "รถไถลมาด้วยความเร็วเกือบจะชนกับขอบราวเหล็กกั้นถนน โชคดีที่พ่อยังมีสติที่เหยียบเบรกไว้ทันก่อนที่จะประสานงา และก็โชคดีอีกขั้นที่ตอนนี้บนถนนเส้นนี้ไม่มีรถอยู่เลย"

    player "พ่อขับรถดี ๆ สิวะ เกือบขิตคู่แล้วมั้ยเห้ย"
    ex_player_dad "โทษที ๆ พอดีพ่อตกใจว่าไอ้ลูกชายหัวแก้วหัวแหวนมันจะยอมอะไรง่ายขนาดนั้น"
    player "เวลาเปลี่ยนคนก็เปลี่ยนแหละน่าพ่อ คิดมาก ระวังแก่ไวนะ"
    ex_player_dad "ถ้าเอ็งจะเล่นมุกว่า เมื่อวานก็คือประวัติศาสตร์ ล่ะก็นะ" 
    ex_player_dad "เออนี่ ก่อนแม่แกเสีย ท่านทำเรื่องเข้าโรงเรียนไว้ให้ก่อนแล้วนะ เหมือนแม่แกจะเป็นเพื่อนเก่าเพื่อนแก่ของผู้อำนวยการที่นี่หรืออะไรสักอย่างนี่แหละ" 
    ex_player_dad "พ่อคิดอยู่เหมือนกันว่าจะคุยกับแกยังไงดี แต่ก็แหม ว่านอนสอนง่ายขนาดนี้เลยคุยกันง่ายหน่อย"
    "ผมหยิบแฟ้มเอกสารซองน้ำตาลที่มีตราประทับลายดอกไม้แปลกประหลาดแปะอยู่ด้านหน้าของซองขึ้นมา"
    player "Flora Academy ? ชื่อแปลกดีแฮะ" 
    "ผมหยิบเอกสารออกมาอ่านดู โรงเรียนเอกชน “Flora Academy” ดูเหมือนเป็นโรงเรียนที่พึ่งเปิดใหม่ไม่นานมานี้ถ้าเทียบกับโรงเรียนเอกชนที่อื่นในไทย"
    player"ไว้เดี๋ยวเราค่อยหาเวลาอ่านที่หลังดีกว่า" 
    "ตอนนี้สิ่งที่ต้องทำเป็นอันดับแรกคือต้องรีบเอารถออกจากถนนก่อนที่จะมีใครมาและก่อนจะตกทะเลด้วย... "
    "ยิ่งถ้ามีใครมาเจอนี่ ไปคุยเรื่องอุบัติเหตุรถที่สน.ของญี่ปุ่นนี่...นาน เดี๋ยวก่อนนะ นั่นสิ! เราอาจจะเจอคนที่เราหวังไว้ที่นี่ก็ได้ เอาเว้ย!! ไป!!"

    ex_player_dad "เออพ่อลืมบอก พ่อไม่ได้ไปกับแกด้วยนะ"
    player "?????????????????????????????????????????"
    ex_player_dad "อย่าทำหน้าแบบนั้นสิ แม่แกอยากให้แกออกไปใช้ชีวิตด้วยตัวเองบ้างไง"
    ex_player_dad "ถึงความจริงพ่อจะอยากไปลั้นลาตามประสาคนวัยทองก็เถอะ"
    player "ถ้าไม่ติดว่าแม่ขอมานะ เราร่วงลงทะเลทั้งคู่ตรงนี้แน่ผมบอกเลย"
    ex_player_dad "ฮ่า ๆ ๆ ขอให้สนุกกับชีวิตวัยเรียนที่แสนหวานปนขมนะ ไอ้ ลูก ชาย"
    "พ่อตบไหล่ผมเบา ๆ หลังจากที่พยายามกลับรถอยู่ซักพักรถก็กลับมาวิ่งบนถนนได้แบบปกติ"
    "เอาล่ะ ถึงเวลาทีเราจะได้ออกไปใช้ชีวิตของตัวเองซักทีสินะ! ไว้เจอกันนะ! ประเทศไทย!"

    return
