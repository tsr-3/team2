import os

class AttendanceFile:
  
  # field
  _filepath
  _

  def __init__(self): # constructor
    if os.path.exists('.tempfiles'): pass
    else os.mkdir('.tempfiles')

  def __del__(self): # destructor
    # zip作成
    # zip移動
    # .tempfiles削除


# reference
# passzip: https://symfoware.blog.fc2.com/blog-entry-1667.html