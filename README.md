## Programimi me sockets
Ky projekt përfshin një server dhe klientet për transferim të file-ve  përmes protokollit TCP. Serveri lejon përdoruesit e autorizuar të kryejnë operacione read(), write() dhe execute() në file, ndërsa klienti lidhet me serverin dhe ka interaksion me të.
## Server.py
Përdorimi
- Ekzekutoni skriptën 'Server.py' për të startuar serverin.
- Serveri dëgjon për lidhje nga klientët.
- Përdoruesit e autorizuar (p.sh., Admin) mund të kryejnë operacione read, write dhe execute në file.
- Përdoruesit e tjerë kanë leje vetëm për operacionin read.
  Komandat
  1. 'read:file':Lexo përmbajtjen e skedarit të specifikuar.
  2. 'write:file:përmbajtja': Shkruaj përmbajtjen e specifikuar në file-n e dhënë.
  3. 'execute:file': Ekzekuto një skriptë
   Autorizimi
- Autorizimi bazohet në emrin e pajisjes së përdoruesit.
- Vetëm përdoruesi me emrin "Admin" ka leje të plotë.
- Përdoruesit e tjerë janë të kufizuar në operacionin read.

## Client.py 
Përdorimi 
- Ekzekutoni file-n `Client.py` për të startuar klientin.
- Lidhuni me serverin duke specifikuar adresën IP dhe portin e serverit.
- Jepni emrin e pajisjes kur të pyeset.
- Do të merrni leje bazuar në emrin e pajisjes suaj.
- Jepni komandat për të interaktuar me serverin.






Projekti u punua nga Grupi 5:
Elonita Krasniqi
Elvira Metaj
Endi Rashica
Erblin Kelmendi
