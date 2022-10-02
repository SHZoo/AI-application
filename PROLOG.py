!sudo apt install swi-prolog
!pip install pyswip
from pyswip import Prolog
prolog=Prolog()
prolog.assertz("father(hyerim, taewoong)")
prolog.assertz("father(hyerim, taeyoung)")
bool(list(prolog.query("father(hyerim, taewoong)")))
bool(list(prolog.query("father(hyerim, taeyeon)")))
for per in prolog.query("father(hyerim, X)"):
  print(per["X"])
from google.colab import drive
#drive.mount('/content/drive') 
# PROLOG로 DFS코드 짜기
