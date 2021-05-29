# on RaspberryPi

変更点とか意見あればガンガン直してって

### files

    RaspberryPi/README.md
      this
    RaspberryPi/main.py
      execute it
    RaspberryPi/modules/
      external modules
    RaspberryPi/functions/
      internal(self-made) modules

### last

開発中は./functions/*はimportして実行するけど、最終的に速度を気にするならmain.pyに埋め込んでもいいかもしれない

### 必要な関数類

- readFileData(filepath)
- await readCardInfo()
- checkLectureData(id, time)
- displayCheckResult(response_of_checkLectureData)
- addAttendance()
- writeAttendanceData()

### 暗号化方式
暗号化zipでいいのでは => だめかもしれない(jsで開けない可能性)