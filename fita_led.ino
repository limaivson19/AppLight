#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif
#define NUM_LEDS 4
int OFFSET;
int incomingByte = 0;

Adafruit_NeoPixel strip(15, 13, NEO_GRB + NEO_KHZ800);

void setup() {
  #if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
  #endif
  strip.begin();
  strip.show();
  Serial.begin(9600); 
}
int a;
int var;
int cont;
void loop() {
  int pivo = Serial.read();
  int c;
  int l;
if(pivo == 'b' || pivo == 'l'){
  c = pivo;
}
if(pivo == 'a' || pivo == 'V'){
  c = pivo;
}
if(pivo == 'v' || pivo == 'r'){
  c = pivo;
}
if(pivo == 'p'){
  c = pivo;
}
if(pivo == '0' || pivo == '2'){
  l = pivo;
}
if(pivo == '5' || pivo == '7'){
  l = pivo;
}
else{
  l = pivo;
}
 
  if(c == 'b' && l == '2'){
    //branco
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color(63.75,63.75,63.75));
    strip.show();
    delay(50);
    cont=cont+1;
  }
  }
  if(c == 'b' && l == '5'){
    //branco
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color(127.5,127.5,127.5));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'b' && l == '7'){
    //branco
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color(191.25,191.25,191.25));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'b' && l == '1'){
    //branco
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color(255,255,255));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'a' && l == '2'){
    //azul
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color(0,0,63.75));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'a' && l == '5'){
    //azul
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color(0,0,127.5));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'a' && l == '7'){
    //azul
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color(0,0,191.25));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'a' && l == '1'){
    //azul
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color(0,0,255));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'p'){
    c = Serial.read();
    //verde
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((0),(63.75),(0)));
    strip.show();
    cont=cont+1;
  }
  delay(300);
  cont = 0;
  while(cont<15){
    strip.setPixelColor((cont),strip.Color((63.75),(63.75),(63.75)));
    strip.show();
    cont=cont+1;
  }
  delay(300);
  }
  
  if(c == 'v' && l == '2'){
    //verde
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((0),(63.75),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'v' && l == '5'){
    //verde
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((0),(127.25),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'v' && l == '7'){
    //verde
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((0),(191.25),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'v' && l == '1'){
    //verde
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((0),(255),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'V' && l == '2'){
    //vermelho
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((63.75),(0),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'V' && l == '5'){
    //vermelho
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((127.5),(0),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'V' && l == '7'){
    //vermelho
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((191.25),(0),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'V' && l == '1'){
    //vermelho
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((255),(0),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'r' && l == '2'){
    //roxo
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((32),(0),(32)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'r' && l == '5'){
    //roxo
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((64),(0),(64)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'r' && l == '7'){
    //roxo
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((96),(0),(96)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'r' && l == '1'){
    //roxo
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((128),(0),(128)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'l' && l == '2'){
    //laranja
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((63.75),(35),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'l' && l == '5'){
    //laranja
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((127.5),(70),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'l' && l == '7'){
    //laranja
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((191.25),(105),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  if(c == 'l' && l == '1'){
    //laranja
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((255),(140),(0)));
    strip.show();
    delay(30);
    cont=cont+1;
  }
  }
  else if (l == '0'){
    int cont1 = 0;
    while(cont1<15){
    strip.setPixelColor((cont1),strip.Color(random(0,0),random(0,0),random(0,0)));
    strip.show();
    delay(30);
    cont1=cont1+1;
  }
  }
  if(l == '8'){
    int p = '8';
    while(p == '8'){
      a = Serial.read();
      if(a==' '){
        p=8;
      }
      else{
        p=a;
      }
      rainbow(10);
      theaterChaseRainbow(50);
      }
  }
  if(pivo == 'm'){
    while(pivo != '0'){
      a = Serial.read();
      int cont = 0;
      while(cont<15){
        strip.setPixelColor((cont),strip.Color((63.75),(35),(0)));
        strip.show();
        delay(60);
        if(cont==14){
          cont=0;
          while(cont<15){
        strip.setPixelColor((cont),strip.Color((0),(0),(0)));
        strip.show();
        delay(60);
        cont=cont+1;
          }
        }
        cont=cont+1;
        pivo = a;
      }
      }
  }  
  if(pivo == 'q'){
    while(pivo != '0'){
      a = Serial.read();
      int cont = 0;
      while(cont<15){
        strip.setPixelColor((cont),strip.Color((63.75),(0),(0)));
        strip.show();
        delay(60);
        if(cont==14){
          cont=0;
          while(cont<15){
        strip.setPixelColor((cont),strip.Color((0),(0),(0)));
        strip.show();
        delay(60);
        cont=cont+1;
          }
        }
        cont=cont+1;
        pivo = a;
      }
      }
  }
  if(pivo == 'f'){
    while(pivo != '0'){
      a = Serial.read();
      int cont = 0;
      while(cont<15){
        strip.setPixelColor((cont),strip.Color((0),(0),(63.75)));
        strip.show();
        delay(60);
        if(cont==14){
          cont=0;
          while(cont<15){
        strip.setPixelColor((cont),strip.Color((0),(0),(0)));
        strip.show();
        delay(60);
        cont=cont+1;
          }
        }
        cont=cont+1;
        pivo = a;
      }
      }
  }
  else if (c == '0'){
    int cont1 = 0;
    while(cont1<15){
    strip.setPixelColor((cont1),strip.Color(random(0,0),random(0,0),random(0,0)));
    strip.show();
    delay(30);
    cont1=cont1+1;
  }
  }
}
  void rainbow(int wait) {
for(long firstPixelHue = 0; firstPixelHue < 5*65536; firstPixelHue += 256) {
    strip.rainbow(firstPixelHue);
    strip.show(); // Update strip with new contents
    delay(wait);  // Pause for a moment
  }
}
void theaterChaseRainbow(int wait) {
  int firstPixelHue = 0;     // First pixel starts at red (hue 0)
  for(int a=0; a<30; a++) {  // Repeat 30 times...
    for(int b=0; b<3; b++) { //  'b' counts from 0 to 2...
      strip.clear();         //   Set all pixels in RAM to 0 (off)
      for(int c=b; c<strip.numPixels(); c += 3) {
        int      hue   = firstPixelHue + c * 65536L / strip.numPixels();
        uint32_t color = strip.gamma32(strip.ColorHSV(hue)); // hue -> RGB
        strip.setPixelColor(c, color); // Set pixel 'c' to value 'color'
      }
      strip.show();                // Update strip with new contents
      delay(wait);                 // Pause for a moment
      firstPixelHue += 65536 / 90; // One cycle of color wheel over 90 frames
    }
  }
}
