### tolino-notes-translator-transformator 📚

![because reading is what](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExazJiMDF6anJydWpwNzVyM3RtejJoaXFyMmxiMWgxM25leGRiaGc1ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vcshWqhrsOrywNYY9Y/giphy.gif)
<br/>

#### 🚧 working draft 🚧

If you're like me and tag a lot of words you don't know while reading ebooks - this will help you to finally go through your notes. In my case I need it for English - German (as seen in the script). This little project will find synonyms and translations for the words tagged. Some shade on the way: Since the `googletrans` (Google Translate API) library is not performing really well with translations ([see yourself](https://github.com/piavalentin/tolino-notes-translator-transformator/blob/main/tests/files/mock_output.txt)), I also translate their synonyms. This could be adjusted to use DeepL or Google Cloud Translation API (not yet tested).

#### TODO
- implement sentences handling (`extract_words`)
- check for 0 as unlimited synonyms (`find_synonyms`)