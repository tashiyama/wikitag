import wikipedia

# キーワードを設定
keyword = "python"

# キーワードで検索
wikipedia.set_lang("ja")
search_response = wikipedia.search(keyword)

#検索結果を表示
print('キーワード:'+ str(keyword) + 'での検索結果は' + str(len(search_response)) + '件です。')
print(search_response)
#検索結果のページ内容を表示
page_data = wikipedia.page(search_response[0])
print(page_data.content)