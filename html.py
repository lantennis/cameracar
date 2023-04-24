def web_page():
    html_page = """<!doctype html>
                <html>
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,initial-scale=1">
                    <title>控制</title>
                    <style>
                        .button3 {background-color:#30FF30;border: none;border-radius: 4px;color: white;padding: 10px 25px;text-align: center;font-size: 16px;margin: 4px 2px;cursor: pointer;}
                        .button2 {background-color: #b50024;border: none;border-radius: 4px;color: white;padding: 10px 25px;text-align: center;font-size: 16px;margin: 4px 2px;cursor: pointer;}
                        .button {background-color: #0097b5;border: none;border-radius: 4px;color: white;padding: 10px 25px;text-align: center;font-size: 16px;margin: 4px 2px;cursor: pointer;}
                    </style>
                </head>
                <body>
                <form>
                    <div align=center>
                    <img src=  http://192.168.213.37 style='width:300px'></div>
                    <br/>
                    <br/>
                    <div align=center> 
                    <button class="button" type='submit' name="car" value='1'>前進</button>
                    </div>
                    <br/>
                    <div align=center> 
                    <button class="button" type='submit' name="car" value='4'>左轉</button>
                    <button class="button" type='submit' name="car" value='3'>停止</button>
                    <button class="button" type='submit' name="car" value='5'>右轉</button>
                    </div>
                    <br/>
                    <div align=center> 
                    <button class="button" type='submit' name="car" value='2'>後退</button>
                    </div>
                    <br/>
                    <div align=center> 
                    <button class="button" type='submit' name="light" value='6'>開燈</button>
                    <button class="button" type='submit' name="light" value='7'>關燈</button>
                    </div>
                    <br/>
                    <div align=center> 
                    <button class="button2" type='submit' name="angle" value='8'>左轉角度</button>
                    <button class="button2" type='submit' name="angle" value='9'>右轉角度</button>
                    </div>
                    <br/>
                    <div align=center> 
                    <button class="button2" type='submit' name="angle" value='10'>下角度</button>
                    <button class="button2" type='submit' name="angle" value='11'>上角度</button>
                    </div>
                    <br/>
                    <div align=center> 
                    <button class="button3" type='submit' name="fast" value='12'>速度上升</button>
                    <button class="button3" type='submit' name="fast" value='13'>速度下降</button>
                    </div>
                    <br/>
                </form>
                </body>
                </html>"""
    return html_page

   