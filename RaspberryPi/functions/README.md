# on functions

実装された関数と実装予定の関数を記述していく

### 実装済み(開発中も含む)
 
- AES256CBC 暗号化?

  - def encode(text:str):

  - def decode(key:str, iv:str, text:str):

- attendance 出席の判定

  - def attendance(now: datetime, lect_time):

- cardreader NFCによるカードの読み取り

  - def on_connect(tag):

  - def read_id():

  - def printidm():

  - def second_warm():

- dummy_cardreader IDmの手入力を可能にする

  cardreaderの関数と同じ

- command 文字コードの統一(?)

  - def command(command):

- comparsion IDmから履修者を識別

  - def comp(IDm:str, students_list:list):

- ValueStorage 他関数と値を取りたいとき使う

- SaveDataFile 

  - class SaveDataFile

    - def read():

    - def write(dat:object, path:str):

  - class DummySaveDataFile:

    - def read():

    - def write(dat: dict, path:str):

- time_attend 出席の判定

  - def time(start_time,late_time,end_time):

- time_setting datetime型の加算

  - def minutes_add(original:datetime, additon:int):

- windowsv3 PiのGUI

- subwindows windowsv3で用いるポップアップ


### 必要な関数類 (実装されてたら消していって下さい)

- readFileData(filepath)
- await readCardInfo()
- checkLectureData(id, time)
- displayCheckResult(response_of_checkLectureData)
- addAttendance()
- writeAttendanceData()

