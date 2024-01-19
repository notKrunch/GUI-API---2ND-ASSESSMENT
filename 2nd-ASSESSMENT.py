import tkinter as tk
import requests

def search_movie():
    movie_name = entry.get()
    if movie_name:
        api_key = 'b638ca6ae4b639d3f388bc33995b4b49'
        url = f'https://api.themoviedb.org/3/search/movie'
        params = {'api_key': api_key, 'query': movie_name}
        response = requests.get(url, params=params)
        data = response.json()

        result_text.delete(1.0, tk.END)

        if 'results' in data:
            for result in data['results']:
                title = result.get('title', 'N/A')
                overview = result.get('overview', 'N/A')
                release_date = result.get('release_date', 'N/A')
                result_text.insert(tk.END, f"Title: {title}\nOverview: {overview}\nRelease Date: {release_date}\n\n")
        else:
            result_text.insert(tk.END, "No results found.")

# GUI setup
app = tk.Tk()
app.title("Movie Database GUI")


# Entry for user to input movie name
entry = tk.Entry(app, width=30)
entry.grid(row=0, column=0, padx=10, pady=10)

# Search button
search_button = tk.Button(app, text="Search", command=search_movie)
search_button.grid(row=0, column=1, padx=10, pady=10)

# Display area for movie details
result_text = tk.Text(app, height=20, width=150, font=("Courier", 9, "bold"))
result_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
