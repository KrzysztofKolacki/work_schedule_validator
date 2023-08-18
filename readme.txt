Instrukcje dotyczące uruchamiania programu walidującego harmonogram czasu pracy:

1. Upewnij się, że masz zainstalowanego Pythona (wersja 3.6 lub nowsza).
2. Umieść plik z danymi (np. work_hours.txt) w tym samym katalogu, co skrypt walidujący.
3. Uruchom skrypt walidujący w konsoli za pomocą komendy: python <nazwa_skryptu>.py
4. Wyniki walidacji zostaną wyświetlone w konsoli.

Uwagi:
- Plik z danymi powinien być w formacie: <dzień miesiąca>, <liczba godzin>. Przykład: 1, 8
- Skrypt zakłada, że miesiąc ma 31 dni, ale można dostosować ilość dni w skrypcie, jeśli to konieczne.


Jeśli uruchomisz skrypt work_schedule_validator.py z przykładowym plikiem work_hours.txt, uzyskasz wymienione wyniki:
- Walidacja całkowitej liczby godzin: Całkowita liczba godzin wynosi 226,5, co przekracza dozwoloną wartość dla standardowego miesiąca o 22 dniach roboczych (czyli 176 godzin).
- Walidacja pracy w niedzielę: Nie jest zaplanowana praca w niedzielę.
- Całkowita liczba nadgodzin: Jest 18 godzin nadgodzin.
- Walidacja przerwy między dniami: Jest co najmniej 11 godzin przerwy między końcem jednego dnia a początkiem następnego.