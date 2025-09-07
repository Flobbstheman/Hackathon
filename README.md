Lista kontrolna testów – bot Discord + google tm

1. Komendy

 ?advice – reaguje na poprawne tematy i podaje poradę.

 ?advice – informuje przy nieznanym temacie.

 ?predict – prosi o obrazek, analizuje go i podaje przewidywaną kategorię + poradę.

2. Interfejs / UX

 Wiadomości bota są czytelne, emoji i formatowanie działają.

 Powitanie wysyłane na właściwy kanał po starcie.

3. Bezpieczeństwo

 Token bota nie jest publiczny.

 Bot nie przyznaje nadmiarowych uprawnień.

 Nie crashuje przy błędnych danych wejściowych.

4. Wydajność

 Działa stabilnie przy kilku użytkownikach jednocześnie.

 5. Biblioteki
 Upewnić się, że wszytkie biblioteki(discord, discord.ext, numpy, PIL, requests, BytesIO, Random, TFSM Layers, difflib) są za instalowane, importowane i funkcjonują sprawnie.

Lista poleceń (commands) i ich działanie:
Preferowany prefiks polecenia "?" zmień w razie potrzeby.
?predict:
Używa załączonego obrazu z modelem TensorFlow do przewidywania i udzielania porad. Prześlij zdjęcie, na przykład wylesiania, a bot udzieli Ci wskazówek, jak temu zapobiec.

?advice:
Używa danych wprowadzanych przez użytkownika (strukturalnie: ?advice x) z 5 kategorii (zanieczyszczenie, energia odnawialna, topniące lodowce, wylesianie, energia), aby udzielać użytkownikowi porad na każdy temat/kategorię.

Zdarzenia, które zawsze mają miejsce po uruchomieniu bota:
- Wysyła wiadomość tekstową na czacie, przedstawiając siebie i swoje zadanie (wkrótce tłumaczenie na angielski)
- Wyświetla konsolę po zalogowaniu i gotowości do użycia (!Nie uruchomi się, jeśli wystąpi błąd związany z kodem lub innymi konfiguracjami!)

Miłej zabawy :) (Kod w języku angielskim do tej pory niedostępny)


/// English

Test Checklist – Discord Bot + Google TM

1. Commands

?advice – responds to valid topics and provides advice.

?advice – provides information about unknown topics.

?predict – requests an image, analyzes it, and provides a predicted category + advice.

2. Interface / UX

The bot's messages are clear, emojis and formatting work.

The greeting is sent to the correct channel upon startup.

3. Security

The bot's token is not public.

The bot does not grant excessive permissions.

Does not crash on invalid input.

4. Performance

Works stably with multiple users simultaneously.

5. Libraries
Make sure all libraries (discord, discord.ext, numpy, PIL, requests, BytesIO, Random, TFSM Layers, difflib) are installed (use pip install x ) and imported.

Command list and what they do:
Preffered command prefix "?" change if needed.
?Predict:
Uses a image attachment with a tensorflow model to predict and give you advice. Upload a pic like for example of deforestation and the bot will give you advice on how to prevent.

?advice:
Uses a user input (structured like this: ?advice x) from 5 categories (Pollution, Renewable Energy, Melting Glaciers, Deforestation, Energy) to give the user advice on each topic/catgory

Events that always happen when bot starts:
- Sends a text message in the chat introducing itself and its purpose (In polish english translation coming soon)
- prints out a logged in console when logged in and ready to use (!Wont start if there is a error related to the code or other configs!)

Enjoy :) (English version not out yet)








