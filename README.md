# 目覚ましロボ  
## LEGO MindStormEV3をつかって目覚ましロボットを作りました。  
### 使用言語はmicroPython  
## 機能  
### タイマーセットを画面上で行ってから、睡眠。時間が来ると光と音で目覚まし機能を持つが乱数でモーターを駆動して様々な動きをするために移動して止めなければならない。タッチセンサーにより停止を試みるが左タッチを押すと犬の鳴き声がさらになり余計にうるさくなってしまう。右のタッチを押しても止まらず、中央のボタンと右のタッチセンサを同時に押さなければ止まらない仕組みとなっているために、目が覚めるという魂胆である。  
### threadingによりSound()タスクとMotorOn()タスクを並列処理させている。
