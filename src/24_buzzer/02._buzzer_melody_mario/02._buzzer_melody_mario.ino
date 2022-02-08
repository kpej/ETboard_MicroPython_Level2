/******************************************************************************************
* FileName: 02._buzzer_melody_mario
* Description : 부저를 이용하여 멜로디를 내는 예제(mario)
* Author : 이인정
* Created Date : 2021.06.18
* Reference : 
* modified : 2021.06.18 : LIJ : 헤더 수정
******************************************************************************************/
#include "pitches.h"

#define beepPin D2 // GPIO 4
unsigned long previousButtonMillis = 0;
int melody_note[] = { NOTE_E7, NOTE_E7, 0, NOTE_E7, 0, NOTE_C7, NOTE_E7, 0, NOTE_G7, 0, 0, 0, NOTE_G6, 0, 0, 0, NOTE_C7, 0, 0, NOTE_G6, 0, 0, NOTE_E6, 0, 0, NOTE_A6, 0, NOTE_B6, 0, NOTE_AS6, NOTE_A6, 0, NOTE_G6, NOTE_E7, NOTE_G7, NOTE_A7, 0, NOTE_F7, NOTE_G7, 0, NOTE_E7, 0, NOTE_C7, NOTE_D7, NOTE_B6, 0, 0, NOTE_C7, 0, 0, NOTE_G6, 0, 0, NOTE_E6, 0, 0, NOTE_A6, 0, NOTE_B6, 0, NOTE_AS6, NOTE_A6, 0, NOTE_G6, NOTE_E7, NOTE_G7, NOTE_A7, 0, NOTE_F7, NOTE_G7, 0, NOTE_E7, 0, NOTE_C7, NOTE_D7, NOTE_B6, 0, 0 };
// 마리오 멜로디 입니다.
uint8_t noteDurations[]={ 2000, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, };
uint8_t melody_num = 0;
unsigned long beepTime = 0;

void setup() {
  Serial.begin(115200);
  ledcSetup(0,1E5,12);  
  ledcAttachPin(beepPin,0);  
}

void loop(){
  if (millis() - beepTime >= 2000/noteDurations[melody_num])
  {
    beepTime = millis();
    ledcWrite(0,0); 
    ledcWriteTone(0,melody_note[melody_num]);  
    melody_num++;
    if (melody_num == 50) { 
      ledcWrite(0,0); 
      melody_num = 0; 
      beepTime = 0;
    }
  }
}
//┌────────────────────────────────┐
//│                                                    │
//│     (주)한국공학기술연구원 http://et.ketri.re.kr       │
//│                                                    │ 
//└────────────────────────────────┘
