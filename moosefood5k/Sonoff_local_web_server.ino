#include <ESP8266WiFi.h>
//#include <WiFiClient.h>
#include <ESP8266WebServer.h>
//#include <ESP8266mDNS.h>
#include <PolledTimeout.h>

//MDNSResponder mdns;

// Replace with your network credentials
const char* ssid = "SSID";
const char* password = "Password";

int gpio13Led = 13;
int gpio12Relay = 12;

ESP8266WebServer server(80);

using esp8266::polledTimeout::oneShotMs;

class MooseFood5k {
 public:
  MooseFood5k();

  void init();
  void execute();
  void feed(int seconds);
  void stop();

 private:
  void cmdPower(int state);

  enum class State {
    OFF,
    ON
  } state_;

  oneShotMs timeoutOff_;
};

MooseFood5k::MooseFood5k() :
    timeoutOff_(0) {
  // Empty
}

void MooseFood5k::cmdPower(int state) {
  // LED is active low.
  digitalWrite(gpio13Led, (HIGH == state) ? LOW : HIGH);

  // Power is active high.
  digitalWrite(gpio12Relay, state);

  state_ = (HIGH == state) ? State::ON : State::OFF;
}

void MooseFood5k::init() {
  cmdPower(LOW);
}

void MooseFood5k::execute() {
  if (timeoutOff_) {
    cmdPower(LOW); 
  }

void MooseFood5k::feed(int seconds) {
  cmdPower(HIGH);
  timeoutOff_.reset(seconds * 1000);
}

void MooseFood5k::stop() {
  cmdPower(LOW);
  timeoutOff_.resetToNeverExpires();
}

String webPage = 
  "<h1>MooseFood 5000 version 1.0</h1>"
  "<form action='feed'>"
  "    Seconds:<br>"
  "    <input type='text' name='seconds'><br>"
  "    <input type='submit' value='Feed'>"
  "</form>"
  "<br>"
  "<form action='stop'>"
  "    <input type='submit' value='Stop'>"
  "</form>";

MooseFood5k mf5k;

void setup(void){
  pinMode(gpio13Led, OUTPUT);
  pinMode(gpio12Relay, OUTPUT);

  mf5k.init();
 
  Serial.begin(115200); 
  delay(5000);
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  
//  if (mdns.begin("esp8266", WiFi.localIP())) {
//    Serial.println("MDNS responder started");
//  }
  
  server.on("/", [](){
    server.send(200, "text/html", webPage);
  });
  
  server.on("/feed", [](){
    server.send(200, "text/html", webPage);
    String seconds_string = server.arg("seconds");
    Serial.println("Feed: " + seconds_string + " sec.");
    int seconds = seconds_string.toInt();
    mf5k.feed(seconds);
  });

  server.on("/stop", [](){
    server.send(200, "text/html", webPage);
    mf5k.stop();
  });
  
  server.begin();
  Serial.println("HTTP server started");
}
 
void loop(void){
  server.handleClient();
  mf5k.execute();
} 
