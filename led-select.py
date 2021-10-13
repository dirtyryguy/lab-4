#!/usr/bin/python37all
import cgi
import json

data = cgi.FieldStorage()
led = data.getvalue('option')
pwm_duty = data.getvalue('slider1')
data = {'led':led, 'value':pwm_duty}

with open('/home/pi/Documents/ENME441/labs/led-select.txt', 'w') as f:
    json.dump(data, f)

# Begin web page generation
print('Content-type:text/html\n\n')
print(
'''
<html>
<head>
  <title>LED Selector</title>
  <style>
    body
    {
      background-color: powderblue;
    }
    .aDiv
    {
      width: 500px;
      margin: 0 auto;
      border: 5px outset black;
      background-color: white;
      text-align: center;
    }
  </style>
</head>

'''
)
print(
'''
<body>
  <br>
  <div class="aDiv">
    <h2>Choose an LED</h2>
    <form>
'''
)
if led == 'a':
    print(
'''
      <input type="radio" name="option" value="a" checked> LED 1 <br>
      <input type="radio" name="option" value="b"> LED 2 <br>
      <input type="radio" name="option" value="c"> LED 3 <br>
'''
)
elif led == 'b':
    print(
'''
      <input type="radio" name="option" value="a"> LED 1 <br>
      <input type="radio" name="option" value="b" checked> LED 2 <br>
      <input type="radio" name="option" value="c"> LED 3 <br>
'''
)
else:
    print(
'''
      <input type="radio" name="option" value="a"> LED 1 <br>
      <input type="radio" name="option" value="b"> LED 2 <br>
      <input type="radio" name="option" value="c" checked> LED 3 <br>
'''
)
print(
f'''
      <h2>Choose the Brightness</h2>
      <input oninput="this.form.submit()" type="range" name="slider1" min="0" max="100" value="{pwm_duty}"> <br><br>
      <input type="submit" value="Submit"> <br>
    </form>
  </div>
</body>
</html>
'''
)
