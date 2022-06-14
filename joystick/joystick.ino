int VRx = A0;
int VRy = A1;
int SW = 2;

int xPosition = 0;
int yPosition = 0;
int SW_state = 0;
int mapX = 0;
int mapY = 0;

void setup() {
  Serial.begin(9600); 
  
  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);
  pinMode(SW, INPUT_PULLUP); 
  
}

void loop() {
  xPosition = analogRead(VRx);
  yPosition = analogRead(VRy);
  SW_state = digitalRead(SW);
  mapX = map(xPosition, 0, 1023, -512, 512);
  mapY = map(yPosition, 0, 1023, -512, 512);

  if (mapX>400){
    Serial.println("derecha");
  }
  else if (mapX<-400){
    Serial.println("Izquierda");
  }

  if (mapY>400){
    Serial.println("arriba");
  }
  else if (mapY<-400){
    Serial.println("abajo");
  }
  else if (SW_state==LOW){
    Serial.println("ok");
  }
  

  delay(500);
  
}
