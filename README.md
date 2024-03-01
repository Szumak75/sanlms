# sanlms

Aplikacja służąca do ręcznego importu raportów bankowych `Santander Bank Polska S.A.` do systemu [LMS](https://lms.org.pl/).

W obecnej wersji pokazuje również listę operacji finansowych zaimportowanych do LMS, które mogą być duplikatami.

Serwis zbudowany został w oparciu o framework Flask i wymaga integracji z serwerem WWW jako serwis PROXY.

Instalację najlepiej wykonać w oparciu o venv a dedykowanym sposobem uruchomienia serwisu jest *runit* dla którego został przygotowany przykładowy schemat startowy w katalogu _examples_.