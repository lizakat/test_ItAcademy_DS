def search_queries_distribution(search_queries):

    word_count_distribution = []

    for query in search_queries:
        words = query.split()
        word_count_distribution.append(len(words))

    total_queries = len(search_queries)

    for i in range(1, max(word_count_distribution) + 1):
        percentage = (word_count_distribution.count(i) / total_queries) * 100
        if percentage == 0:
            pass
        else:
            if i == 1:
                print(f"{i} word: {percentage:.2f}%")
            else:
                print(f"{i} words: {percentage:.2f}%")


search_queries = ["watch new movies", "coffee near me", "how to find the determinant", "python",
                  "data science jobs in UK", "courses for data science", "taxi", "google", "yandex", "bing",
                  "foreign exchange rates USD/BYN", "Netflix movies watch online free",
                  "Statistics courses online from top universities"]
search_queries_distribution(search_queries)
